---
name: xpost
description: >-
  Algorithm Edge — a code-grounded guide and draft optimizer for writing high-performing
  X (Twitter) posts. Use when the user wants to write, improve, critique, or score an X/Twitter
  post, tweet, thread, or reply; asks how to "go viral", get more reach/impressions, or beat the
  "For You" feed algorithm; or pastes a draft and wants it optimized. Grounded in X's open-sourced
  2026 recommendation algorithm (home-mixer / Phoenix / Thunder / grox).
---

# Algorithm Edge

A content guide for X's "For You" feed, reverse-engineered from X's **open-sourced 2026
recommendation algorithm** (the `x-algorithm` repo: `home-mixer`, `phoenix`, `thunder`, `grox`).
Every recommendation here is traceable to how the actual ranking code works. Where a tip is
general practice rather than something provable from the code, it is labeled
**`[general practice]`**.

## How to use this skill

- **If the user pasted a draft** (a tweet/thread/reply they want to improve) → run the
  **Draft Optimizer** workflow below.
- **If the user is asking how X ranking works / what drives reach** → explain from "The mental
  model" and "The levers that matter," pulling depth from `reference/algorithm-signals.md`.
- **If the user wants a checklist or a score** → use `reference/checklist.md`.

Read the reference files on demand; don't dump them wholesale.

---

## The mental model (how a post gets distributed)

X assembles the For You feed in this order (`README.md`, `home-mixer/`):

1. **Retrieval — two sources.**
   - **In-network** (`thunder`): recent posts from accounts the viewer follows.
   - **Out-of-network** (`phoenix` two-tower retrieval): posts from people they *don't* follow,
     pulled from a global corpus by embedding-similarity to what the viewer has engaged with.
2. **Hydrate & filter:** enrich candidates (media, engagement counts, author info…) and drop
   ineligible ones (blocked/muted, muted keywords, too old, already seen, safety violations).
3. **Score:** the **Phoenix** Grok-based transformer predicts a *probability for each of ~17
   positive and ~5 negative actions* the viewer might take on the post. Those probabilities are
   combined into one number:

   ```
   Score = Σ ( weightᵢ × P(actionᵢ) )
   ```
   (`home-mixer/scorers/ranking_scorer.rs:146-170`)

4. **Adjust:** out-of-network posts are multiplied down by a penalty factor
   (`scorers/oon_scorer.rs`); repeated authors in one feed are decayed for diversity
   (`scorers/author_diversity_scorer.rs`).
5. **Select & safety-filter:** sort by score, take top K, then drop anything flagged unsafe
   (`filters/vf_filter.rs`).

**The single most important consequence:** your post is not scored on "quality" in the abstract.
It's scored on the *predicted probability that this specific viewer will take valuable actions on
it*. You win by maximizing those action probabilities — and by not tripping the penalties.

> **Honest caveat — read this before quoting numbers.** The *action set*, the *formula*, the
> *penalties*, and the *filters* are all visible in the open-source code. The **exact numeric
> weights are NOT** — they load at runtime from an external config
> (`xai_feature_switches::Params`). So this skill talks about **relative / ordinal** importance
> and never invents precise weight values. It's a well-informed model of the algorithm, not the
> live production config.

---

## The levers that matter (ranked, code-grounded)

### 1. Earn "expensive" engagements, not cheap likes
The model predicts *each* action separately and each has its own weight
(`ranking_scorer.rs:43-64`). Likes are just one of ~17 positive heads. The heavier, intent-revealing
actions are the ones that separate viral posts from wallpaper:

- **Reply** — the strongest conversation signal. Posts that make people *need to respond* win.
- **Repost / Quote** — redistribution; quote is its own predicted head (adds commentary + reach).
- **Share** — including **share-via-DM** and **share-via-copy-link** (off-platform sharing are
  *separate* predicted heads — "worth sending to a friend" is heavily rewarded).
- **Follow-author** — a post that converts a viewer into a follower is maximally valuable
  (long-term signal). Profile-click is a step on this path.
- **Dwell / dwell-time** — how long they stop on it. Both a binary "dwelled" and a *continuous*
  dwell-time head exist. The opposite, **`not_dwelled`** (scrolled straight past), is a *negative*
  signal.
- **Video quality view (VQV)** — rewarded for video, but gated by a minimum duration
  (`util::candidates_util::vqv_weight`); ultra-short clips may not qualify.

**Implication for writing:** design the post to provoke a reply, be worth quoting, be worth DMing,
and hold the eye for a beat. A post optimized only for likes is leaving most of the score on the
table.

### 2. Win in-network first — it's the launchpad
Out-of-network candidates get their score **multiplied by a factor < 1.0** before ranking
(`oon_scorer.rs:20-23`). Meanwhile, Phoenix retrieval surfaces your post to strangers based on
embedding-similarity to people who already engage with content like yours. So: **early engagement
from your own followers is what powers out-of-network reach.** The first ~30–60 minutes matter
(there's a freshness/age filter — see below). *[general practice]* Prompt your core audience early;
a post that dies in-network rarely escapes to strangers.

### 3. Respect freshness
An **age filter** removes posts older than a threshold from candidate pools
(`filters/age_filter.rs`), and post-age is bucketed as a model feature down to fine granularity
(`phoenix/recsys_model.py` `compute_post_age_bucket`). Recency is structurally favored. Post when
your audience is active; don't expect old posts to resurface.

### 4. Don't flood — author diversity decay
Within a single feed build, the **2nd, 3rd, … post from the same author is multiplied down**
by `decay^position` (`author_diversity_scorer.rs:29-31`). Rapid-fire posting cannibalizes your own
reach in any one feed. Space posts out; make each one count. Threads are one unit and are fine.

### 5. Avoid the penalties and hard filters (see full list in the reference)
Negative predicted actions carry **negative weight** and subtract from your score
(`ranking_scorer.rs:83, 166-170`): **not-interested, block, mute, report**, and **not-dwelled**.
Separately, content can be **hard-dropped** by safety/visibility filtering. Bait, outrage-farming,
and spammy patterns are double-losing: they raise block/mute/report probability *and* risk a safety
drop. See `reference/algorithm-signals.md` for the complete penalty & filter catalog (safety
categories, low-follower reply "spam"/low-blast-radius handling, private-account exclusion, muted
keywords, dedup, etc.).

### 6. Content features the pipeline actually reads
These get hydrated as candidate features, so they carry signal (see reference for files):
media/video presence + duration, engagement counts, language, quote-post expansion, mutual-follow
social proof, and a "friends who replied" facepile gated by a 1000-follower threshold
(`following_replied_users_hydrator.rs`). *[general practice]* Native media generally outperforms a
bare link-out; write in the language your target audience engages in.

---

## Draft Optimizer workflow

When the user shares a draft post, produce a structured critique in **this exact shape**:

### 1. Read intent
Restate in one line what the post is trying to do and who it's for. If the goal is ambiguous
(awareness? replies? clicks? follows?), ask one quick clarifying question — the "best" rewrite
differs by goal.

### 2. Penalty & filter scan (do this first — it's pass/fail)
Check the draft against `reference/checklist.md`'s penalty section. Flag anything that could:
- raise **block / mute / report / not-interested** probability (outrage bait, engagement-bait
  phrasing like "RT if…", misleading claims, pile-on framing), or
- trip a **safety drop** (the 7 categories: violent media, adult content, spam, illegal/regulated,
  hate/abuse, violent speech, suicide/self-harm), or
- read as **low-blast-radius reply spam** (generic reply from/to low-follower accounts).

Call these out plainly. A post that trips these can't be "optimized" into reach.

### 3. Signal-by-signal read
Go through the high-value action heads and say, for each, whether the draft is likely to **earn**
or **miss** it, with a one-line reason:

| Signal | Earns it? | Why |
|---|---|---|
| Reply | … | does it invite a response / take a stance / ask something real? |
| Repost / Quote | … | is it worth redistributing? quotable? |
| Share (DM / copy-link) | … | would someone send this to a friend? |
| Dwell / not-dwelled | … | strong first line? does it hold the eye or is it skippable? |
| Follow-author | … | does it demonstrate why to follow, not just this one post? |
| Video/VQV (if media) | … | is media present and long enough to count? |

### 4. Rewrite
Provide 1–2 rewrites that improve the weak signals — **without** resorting to bait (bait raises the
negative heads). Improve the **hook (first line)**, tighten for dwell, and give a genuine reason to
reply/quote/share. If it fits, propose a thread structure or a media suggestion. Keep the user's
voice.

### 5. Qualitative score
Give a short verdict: an **ordinal** rating (e.g. Weak / Solid / Strong on reach potential) plus
the 1–2 highest-leverage changes. **Do not fabricate a numeric algorithm score** — restate the
honest caveat if the user asks for a hard number.

---

## Honesty guardrails (what this skill will and won't claim)

- ✅ **Will** describe the action set, the scoring formula, the penalties, the filters, and the
  pipeline order — all directly from the open-source code, with file citations.
- ✅ **Will** distinguish code-derived facts from `[general practice]` tips.
- ❌ **Won't** state exact weight numbers, "the algorithm gives likes 0.5," etc. — those aren't in
  the repo.
- ❌ **Won't** claim mechanisms the code doesn't show (e.g. there is **no** TweepCred / verification
  reach-boost visible in this codebase; external links are **not** shown to be explicitly penalized
  here — see "Myths vs. code" in the reference).
- ⚠️ This is the *open-sourced* algorithm as of the repo's 2026 release. Production may differ and
  weights change continuously. Treat it as a strong model, not gospel.

---

## Reference files
- **`reference/algorithm-signals.md`** — full table of the ~22 predicted actions, the complete
  penalty/filter catalog, sourcing & content-feature notes, and "Myths vs. code," all with repo
  citations.
- **`reference/checklist.md`** — the pre-publish checklist and the scoring rubric that maps each
  check to the predicted-action head it influences.
