# Pre-publish checklist & scoring rubric

Use this to critique a draft. Each check maps to the predicted-action head(s) it influences (see
`algorithm-signals.md` for the code). `[general practice]` marks tips not directly provable from the
repo.

---

## Part A — Penalty & filter scan (pass/fail — do this FIRST)

If any of these fire, fix them before optimizing; they subtract from score or drop the post
entirely.

- [ ] **No safety-policy risk** — none of: violent media, adult content, spam, illegal/regulated,
      hate/abuse, violent speech, self-harm. → avoids `VFFilter` drop.
- [ ] **Not engagement-bait / outrage-farm** — no "RT if…", "like if…", rage-baiting, or misleading
      hooks. → avoids raising `report` / `block` / `mute` / `not_interested`.
- [ ] **Not generic reply-spam** — if it's a reply, it adds real value (not a low-effort reply from
      a small account into a small thread). → avoids `low_blast_radius` / spam bucketing.
- [ ] **Account is public** — protected accounts are excluded from For-You ranking.
- [ ] **Not one of a rapid burst** — you're not posting many originals back-to-back.
      → avoids author-diversity decay eating your own reach.
- [ ] **Fresh / well-timed** — posting when the audience is active, not resurfacing something old.
      → passes the age filter, benefits recency features.

---

## Part B — Signal optimization checklist

### Hook & dwell → `not_dwelled` (neg), `dwell`, `cont_dwell_time`, `click`
- [ ] **First line stops the scroll** — the opening earns the stop on its own (the strongest single
      lever; a weak first line triggers the *negative* `not_dwelled` head).
- [ ] **Substance is front-loaded** — no slow wind-up; reward the dwell immediately.
- [ ] **Length fits the payload** — long enough to hold attention, not padded. Threads for depth.

### Conversation → `reply`
- [ ] **Invites a response** — a genuine question, a clear stance to agree/disagree with, or a gap
      readers want to fill. (Not manufactured "comment below 👇" bait.)

### Redistribution → `retweet`, `quote`
- [ ] **Worth reposting** — a clean, self-contained idea someone would put on their own timeline.
- [ ] **Quotable** — a sharp, addable take that invites people to quote with their own comment.

### Off-platform spread → `share`, `share_via_dm`, `share_via_copy_link`
- [ ] **"Send to a friend" test** — is this something someone DMs to one specific person? Useful,
      funny, or striking enough to leave the platform.

### Author value → `profile_click`, `follow_author`
- [ ] **Demonstrates why to follow** — signals there's more where this came from (expertise, voice,
      series), not just a one-off. → drives profile-click → follow.
- [ ] **Consistent topic/voice** *[general practice]* — sharpens your Phoenix embedding so you're
      retrieved to the right out-of-network audiences.

### Media → `photo_expand`, `vqv`, `quoted_vqv`
- [ ] **Media where it helps** *[general practice]* — native image/video tends to hold attention
      better than a bare link-out.
- [ ] **Video meets minimum duration** — if using video, it's long enough to register a quality view
      (very short clips may not qualify).

### Distribution launchpad → in-network / OON
- [ ] **Core audience will engage early** *[general practice]* — early in-network engagement is what
      lets the post overcome the out-of-network penalty and reach strangers.

---

## Part C — Qualitative scoring rubric

Do **not** produce a fake numeric "algorithm score" (exact weights aren't public). Instead:

1. **Penalty gate:** any Part A failure → lead with it; reach is capped until fixed.
2. **Count high-value signals earned** (reply, repost/quote, share, follow, strong dwell) from
   Part B:
   - 0–1 strong signals → **Weak** reach potential
   - 2–3 → **Solid**
   - 4+ with a strong hook and no penalties → **Strong**
3. **Report:** the ordinal rating + the **1–2 highest-leverage fixes** (usually the hook and the
   reply/quote hook). Restate the honest caveat if asked for a hard number.

> Reminder: this rubric models the *open-sourced* algorithm; production weights differ and change.
> It's a strong compass, not a guarantee.
