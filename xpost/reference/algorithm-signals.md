# Algorithm Signals — deep reference

Everything here is grounded in X's open-sourced 2026 recommendation algorithm (`x-algorithm` repo).
File paths are relative to the repo root. **Exact numeric weights are not in the repo** — they load
from `xai_feature_switches::Params` at runtime — so importance below is *ordinal/structural*, not
numeric.

---

## 1. The predicted actions (the scoring heads)

The Phoenix transformer outputs a probability for each action; the ranking scorer multiplies each by
its weight and sums them (`home-mixer/scorers/ranking_scorer.rs:43-64` defines the weights;
`:146-170` combines them). Positive heads add to score; the five negative heads subtract
(`:83`, `:166-170`).

### Positive heads — maximize these

| Action (code field) | What earns it | Notes for creators |
|---|---|---|
| `favorite` (like) | A like | Cheapest signal; necessary but not sufficient. One of ~17 heads. |
| `reply` | A reply | High-intent. Take a stance, ask a real question, leave a gap people want to fill. |
| `retweet` (repost) | A repost | Redistribution → more impressions. Make it worth re-sharing. |
| `quote` | A quote post | Its own head *and* adds the quoter's commentary + their audience. Post "quotable" takes. |
| `share` | Tapping share | "Worth passing on." |
| `share_via_dm` | Sending via DM | Separate head — private "you have to see this" sharing is rewarded. |
| `share_via_copy_link` | Copying the link | Separate head — off-platform spread. |
| `click` | Opening the post | Curiosity/hook. |
| `profile_click` | Tapping the author | Step toward a follow. Give a reason to want more of you. |
| `follow_author` | Following you | Highest long-term value — converts a viewer into in-network. |
| `photo_expand` | Expanding an image | Rewards compelling images. |
| `vqv` (video quality view) | A qualifying video view | Gated by a **minimum video duration** (`util::candidates_util::vqv_weight`, `params::MinVideoDurationMs`). Very short clips may not count. |
| `dwell` | Stopping on the post | Binary "did they linger." |
| `cont_dwell_time` | *How long* they dwell | Continuous head — longer holds score more. Front-load substance. |
| `cont_click_dwell_time` | Dwell after clicking in | Rewards content that holds attention after the tap. |
| `quoted_click` | Click on the quoted post | For quote posts. |
| `quoted_vqv` | Video view on quoted post | Gated by duration check (`params::EnableQuotedVqvDurationCheck`). |

### Negative heads — these subtract from your score

| Action (code field) | Triggered by | Avoid by |
|---|---|---|
| `not_interested` | "Not interested in this post" | Don't bait; be relevant to your actual audience. |
| `block_author` | Viewer blocks you | Don't harass / outrage-farm. |
| `mute_author` | Viewer mutes you | Don't spam or over-post one theme. |
| `report` | Viewer reports the post | Stay inside policy (see §3). |
| `not_dwelled` | Viewer scrolls straight past | Strong first line; earn the stop. |

`negative_sum = -(not_interested + block + mute + report + not_dwelled)` and the final score is
normalized via `offset_score` (`ranking_scorer.rs:83, 175+`). The takeaway: **provoking a block,
mute, report, or instant scroll-past actively lowers your rank**, it isn't neutral.

---

## 2. Score adjustments after the weighted sum

| Adjustment | File | Effect |
|---|---|---|
| **Out-of-network penalty** | `scorers/oon_scorer.rs:20-23` | If `in_network == false`, `score *= OON_WEIGHT_FACTOR` (< 1.0). In-network is prioritized; OON reach must be *earned* by strong predicted engagement. |
| **Author diversity decay** | `scorers/author_diversity_scorer.rs:29-31` | For repeated authors in one feed build, `multiplier(position) = (1 - floor) * decay^position + floor`. Your 2nd/3rd post in one feed is attenuated. |
| **OON offset / normalization** | `scorers/ranking_scorer.rs:175+` (`offset_score`) | Normalizes combined score; handles negative totals. |
| **VM ranker (optional)** | `scorers/vm_ranker.rs` | Secondary ranking pass, toggled by `EnableVMRanker`. |

---

## 3. Penalties & hard filters (things that reduce or kill reach)

### Hard filters — content removed entirely

**Pre-scoring** (`home-mixer/filters/`):

| Filter | File | Removes |
|---|---|---|
| Duplicates | `drop_duplicates_filter.rs` | Duplicate post IDs |
| Core-data hydration | `core_data_hydration_filter.rs` | Posts missing core metadata (`author_id == 0`) |
| Age | `age_filter.rs` | Posts older than the max-age threshold |
| Self-post | `self_tweet_filter.rs` | The viewer's own posts (from their feed) |
| Repost dedup | `retweet_deduplication_filter.rs` | Duplicate reposts of the same content |
| Ineligible subscription | `ineligible_subscription_filter.rs` | Paywalled content the viewer can't access |
| Previously seen | `previously_seen_posts_filter.rs` | Posts already viewed (bloom-filter tracked) |
| Previously served | `previously_served_posts_filter.rs` | Posts already served this session |
| Muted keyword | `muted_keyword_filter.rs` | Posts containing the viewer's muted keywords |
| Author socialgraph | `author_socialgraph_filter.rs` | Blocked/muted authors (either direction), incl. quoted/retweeted authors |
| New-user topic | `new_user_topic_ids_filter.rs` | For new users, OON posts outside recommended topics |

**Post-selection** (`README.md`, `filters/vf_filter.rs`):

| Filter | Removes |
|---|---|
| `VFFilter` (visibility filtering) | Posts flagged unsafe/deleted/spam/violence/gore, etc. |
| `DedupConversationFilter` | Extra branches of the same conversation thread |

### Safety / visibility categories (`grox/tasks/task_safety_ptos_policy.py`)

Content classified into any of these policy categories can be dropped by visibility filtering:

- **Violent media**
- **Adult content**
- **Spam**
- **Illegal and regulated behaviors**
- **Hate or abuse**
- **Violent speech**
- **Suicide or self-harm**

### Reply / low-reach handling (`grox/tasks/`)

- **Low-follower reply spam** (`task_spam_detection.py`): replies are bucketed by the follower
  counts of the reply author and the thread root — `lte_100`, `lte_500`, `lte_1000`, `gt_1000`
  (`:17-29`) — and a classifier flags spammy replies in the low-follower buckets
  (`SpamEapiLowFollowerClassifier`, `:38-47`).
- **Low blast radius** (`task_filters.py`): replies where participants have too few followers may be
  skipped from ranking ("low_blast_radius"). Generic replies from small accounts to small accounts
  get little distribution.
- **Private / protected accounts** (`task_filters.py`): posts from protected accounts — or reply
  chains that include one — are excluded from ranking / content-understanding
  ("private_account"). A public account is a prerequisite for For-You distribution.
- Other pipeline skips: system accounts, self-replies (`same_user_reply`), missing user/ancestor
  data.

---

## 4. Candidate sourcing & content features

### Where candidates come from (`home-mixer/sources/`)

| Source | File | Type |
|---|---|---|
| Thunder | `thunder_source.rs` | In-network (accounts you follow), sub-ms in-memory lookup |
| Phoenix retrieval | `phoenix_source.rs` | Out-of-network via two-tower embedding similarity |
| Phoenix MoE | `phoenix_moe_source.rs` | OON, mixture-of-experts retrieval |
| Phoenix topics | `phoenix_topics_source.rs` | Topic-based retrieval |
| Cached posts | `cached_posts_source.rs` | Cached results |
| Who-to-follow / ads / prompts | `who_to_follow_source.rs`, `ads_source.rs`, `prompts_source.rs` | Non-organic-post units |

**Out-of-network reach mechanism:** Phoenix encodes the viewer's engagement history into an
embedding and retrieves posts whose embeddings are similar. Practically, your post reaches strangers
who resemble the people *already* engaging with content like yours. Consistency in topic/voice
sharpens your embedding and improves who you're matched to.

### Content features that get hydrated (so they carry signal)

| Feature | File |
|---|---|
| Has media | `candidate_hydrators/has_media_hydrator.rs` |
| Video duration + buckets (`≤10s`, `10–60s`, `>60s`) | `video_duration_candidate_hydrator.rs`, `tweet_type_metrics_hydrator.rs` |
| Engagement counts (fav/reply/repost/quote) | `engagement_counts_hydrator.rs` |
| Language code | `language_code_hydrator.rs` |
| Quote-post expansion | `quote_hydrator.rs` |
| Tweet-type flags (reply/repost/quote/subscription/video/has-ancestors/in-network) | `tweet_type_metrics_hydrator.rs` |
| Tweet-age buckets (`≤30m`, `≤1h`, `≤6h`, `≤12h`, `≥24h`) | `tweet_type_metrics_hydrator.rs`; model side `phoenix/recsys_model.py` |
| Author follower buckets (0–100 … 1M+) | `tweet_type_metrics_hydrator.rs`, `gizmoduck_hydrator.rs` |

### Social-proof / graph signals

| Signal | File | Meaning |
|---|---|---|
| In-network flag | `in_network_candidate_hydrator.rs` | `is_self || followed_ids.contains(author_id)` |
| Mutual-follow Jaccard | `mutual_follow_jaccard_hydrator.rs` | MinHash similarity of the two users' following sets — closeness signal |
| "Friends who replied" facepile | `following_replied_users_hydrator.rs` | Annotates posts with followed users who replied; gated by a 1000-follower threshold (`VIEWER_FOLLOWERS_THRESHOLD`) and min-users param |

---

## 5. Myths vs. code

Claims people make about "the algorithm," checked against *this* repo:

| Claim | Verdict in this codebase |
|---|---|
| "Verified/blue accounts get a reach multiplier." | **Not evidenced here.** No TweepCred, verification tier, or blue-boost scorer appears. Author quality is learned implicitly by the transformer; follower count is only *bucketed as a feature*, not a gate. |
| "External links get suppressed." | **Not evidenced here.** No explicit link/URL penalty in the hydrators/filters. Links aren't a tracked penalty feature in this repo. *(General practice still favors native media for dwell — that's a `[general practice]` claim, not a code fact.)* |
| "Likes are the main thing." | **False by design.** Like is one of ~17 positive heads; replies, reposts, quotes, shares, follows, and dwell are all separately predicted and weighted (`ranking_scorer.rs`). |
| "More posting = more reach." | **Counterproductive within a feed:** author-diversity decay attenuates your repeated posts in one build (`author_diversity_scorer.rs`). |
| "Out-of-network is free reach." | **No — it's penalized by default** (`oon_scorer.rs`) and must be earned via predicted engagement + embedding similarity. |
| "Old posts can resurface if good." | **Structurally disfavored:** age filter + recency features (`age_filter.rs`). |
| "Hashtags/keywords boost reach." | **Not evidenced as a boost.** Muted *keywords* are a filter against you; there's no hashtag reach-multiplier in the ranking code. |

**Bottom line:** the modern system leans almost entirely on a learned transformer over the viewer's
engagement history (`README.md` "No Hand-Engineered Features"). You don't game features — you make
content that a *specific audience* predictably replies to, reposts, shares, and follows you for,
fast, without tripping the negative heads or safety filters.
