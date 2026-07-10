---
name: buildcast
description: >-
  Buildcast — turn a repository into a build-in-public content engine: a versioned content
  log (one file per post, metrics, retros), an aggregated playbook of what works, a reply
  engine for niche engagement, and an AGENTS.md binding so every agent working in the repo
  proposes post ideas from real milestones. Use whenever the user wants to build in public,
  set up or maintain a social content log / content history, log a post they published,
  draft or plan the next post in a series, capture post metrics or write a post retro,
  find builders to reply to, or asks "what should I post about?" — even if they never say
  "buildcast". Also use when an agent finishes milestone-worthy work in a repo that has a
  content log and should capture a post idea.
---

# Buildcast

Building in public fails quietly in two ways: posts that vanish without a trace of what
was learned, and milestones that pass unposted because nobody was watching for them.
Buildcast fixes both by making content a first-class, versioned artifact of the repo —
every post gets a file, every file gets a retro, every retro feeds a playbook, and the
repo's agent contract (`AGENTS.md`) makes idea capture part of normal development work.

The system is content-first and platform-second: it works for X, Reddit, TikTok, or any
platform, and for a personal account today and a brand account later.

## Hard rules (apply in every mode)

- **Drafts only. Never post, publish, schedule, or send anything to a social platform or
  any external service.** The human reviews and posts manually — this is a safety rule and
  a quality rule: automated posting is against most platforms' rules and produces exactly
  the low-effort pattern rankers penalize.
- **Never fabricate metrics.** A metrics cell you don't know stays empty or `—`. Wrong
  numbers poison every retro built on them.
- **Audit and patch, never overwrite.** If a content directory or `AGENTS.md` already
  exists, extend it; wholesale rewrites destroy history the system exists to keep.
- **Real lessons come from the project's own retros.** The seeded playbook is a starting
  point, not doctrine — when a retro contradicts it, the retro wins and the playbook gets
  updated.

## Mode dispatch

Classify the request, then route:

| Request looks like | Mode |
| --- | --- |
| "Set up a content log / let's build in public / install buildcast" | **Establish** |
| "Log this post / draft the next post / I published something" | **Log & draft** |
| "What should I post? / any post ideas? / agent finished a milestone" | **Ideate** |
| "Capture metrics / write the retro / what have we learned?" | **Measure & learn** |
| "Who should I reply to / grow the account / engagement" | **Engage** |

### Establish

1. **Gather the project profile.** Discover from the repo first (README, product docs,
   git remotes), ask only for what's missing: project name, one-line pitch a stranger
   understands, platform handle(s), niche (who should find this content), account types
   in play (`personal-build-in-public` now, `brand` later?), and the content directory
   (default `docs/content/`; honor an existing one).
2. **Install the structure** from `assets/templates/`, replacing every `{{PLACEHOLDER}}`
   with profile values:
   - `README.md` ← `content-readme.md` (hub: conventions + workflow)
   - `TEMPLATE.md` ← `post-template.md` (one post = one file: frontmatter, content,
     metrics table, retro)
   - `INDEX.md` ← `index.md` (ledger of all posts, newest first)
   - `PLAYBOOK.md` ← seed from `references/playbook-seed.md` (keep the grounding labels)
   - `WATCHLIST.md`, `replies/QUEUE.md`, `prompts/find-builders.md`, `assets/.gitkeep`
3. **Bind AGENTS.md** using `assets/templates/agents-md-binding.md`: add the router row
   and the "Content signals" contract to the repo's `AGENTS.md` (create a minimal one if
   none exists — but if the repo has a different agent-contract file, bind that instead).
   This is what turns every future agent session into a source of post ideas.
4. **Backfill** any posts the user can identify (published text, URLs, metrics they
   remember) — history is where the first playbook lessons come from. Write retros only
   for backfilled posts old enough to have real data (~7d); for younger ones, leave the
   retro pending rather than forcing a lesson from partial numbers.
5. Offer (don't push) the automations described in `references/operations.md`
   ("Automations" section): scheduled metrics capture and reply drafting. At install
   time, document them in the content README's Automations section as *available, not
   enabled*; update that section with the schedule once one is actually set up.

### Log & draft

Read `references/operations.md` → "Post lifecycle". In short: one file per post from
TEMPLATE.md (`posts/YYYY-MM-DD-<platform>-<slug>.md`), statuses `idea → draft → posted`,
follow-up chains linked in both directions, thread = one file. When drafting, read
PLAYBOOK.md first and write to it; if an X-specific draft optimizer skill (e.g. `xpost`)
is available, run drafts through it before presenting.

### Ideate

This is the mode the AGENTS.md binding triggers. Read `references/operations.md` →
"Ideation". In short: mine what actually happened (git log, changelog, sprint docs,
closed items) plus what the content arc needs next (INDEX.md — what's posted, what's in
reserve, where the last post left off), filter through the post-worthiness criteria, and
capture ideas as `status: idea` entries. Capture is cheap and non-blocking — an idea file
takes one minute; judging and drafting happen later.

### Measure & learn

Read `references/operations.md` → "Metrics" and "Retros". In short: snapshot metrics at
~24h and ~7d minimum, judge by heavy signals per view (replies, reposts, bookmarks,
follows — not likes), write What worked / What went wrong / one Lesson, and promote
durable lessons to PLAYBOOK.md with a link back to the source post.

### Engage

Read `references/operations.md` → "Reply engine". In short: at small follower counts,
substantive replies to the right accounts outperform posting. Weekly semi-manual
discovery (the `prompts/find-builders.md` prompt, adapted to the niche) fills
WATCHLIST.md; the human drops post URLs into `replies/QUEUE.md`; drafting replies from
the queue is agent work — posting them is not.

## Files in this skill

- `references/operations.md` — day-to-day procedures for every mode + optional automations
- `references/playbook-seed.md` — the starting playbook (labeled by grounding)
- `assets/templates/` — install-ready files; replace `{{PLACEHOLDER}}`s, keep structure
