# Buildcast operations

Day-to-day procedures. `<content>/` means the project's content directory (default
`docs/content/`). All hard rules from SKILL.md apply — especially: drafts only, never
publish anywhere.

## Post lifecycle

**Create.** Copy `<content>/TEMPLATE.md` to `posts/YYYY-MM-DD-<platform>-<slug>.md`
(date = publish date, or planned date while drafting) and add a row to INDEX.md. A
thread is one file — number the tweets/posts inside `## Content`. A reply worth
tracking (one that carries real content) gets a file with `type: reply`.

**Status flow.** `idea` (a captured hook, content optional) → `draft` (full text being
iterated) → `posted` (final text frozen, `post_url` filled). Update the INDEX.md row on
every transition. Never edit the `## Content` of a `posted` entry — it is a record of
what was published, not a living document.

**Follow-up chains.** If a post continues an earlier one, set `follow_up_of` to the
earlier file's relative path AND append this file to the earlier file's `follow_ups`
list. Both directions, always — the chain is how future drafting sessions reconstruct
the arc ("where did the last post leave off?").

**Drafting.** Before writing a word, read PLAYBOOK.md and the chain the post belongs to.
Draft in the entry file, not in chat — chat drafts evaporate. Present the draft with a
one-line rationale per playbook rule it leans on. If a platform-specific optimizer skill
is available (e.g. `xpost` for X), run the draft through it. Keep material in reserve:
one milestone per post, and end where the next post begins.

**Assets.** Images and clips live in `<content>/assets/<post-slug>/`, referenced from the
entry's `assets:` frontmatter. Screenshots are content: a post that shows the thing
outperforms a post that describes it.

## Ideation

Triggered by the AGENTS.md binding ("agent finished milestone-worthy work") or by the
user asking "what should I post?".

**Mine two sources:**

1. *What happened* — recent git log, CHANGELOG "Unreleased", sprint/backlog docs, closed
   issues. Look for moments, not tasks: the first time something worked end-to-end, a
   number that changed (build time, users, cost), a decision with real trade-offs, a bug
   with a story, a visual before/after, anything that surprised the builder.
2. *What the arc needs* — INDEX.md and the follow-up chains: what was promised
   ("real code starts now"), what's overdue for a payoff, what's sitting in reserve,
   how long since the last post (1–2 day spacing is healthy; a gap over a week wants a
   "here's what happened" post).

**Post-worthiness filter.** An idea passes if a stranger could care in the first line
AND the builder has a receipt (screenshot, number, diff, decision) — not just an
intention. "We refactored the config loader" fails; "the build went from 40s to 3s and
here's the one-line reason" passes.

**Capture.** One entry file per idea with `status: idea`, a working title, and 2–3 lines
in `## Content`: the hook, the receipt, which chain it belongs to. Add the INDEX.md row.
Do NOT draft the full post at capture time unless asked — capture must stay cheap enough
that agents actually do it mid-task. It parallels backlog idea capture: one minute, then
back to work.

## Metrics

**Cadence.** Snapshot every posted entry at **~24h** and **~7d** (add more if the post
keeps moving). Each snapshot is a new dated row in the entry's `## Metrics` table —
never overwrite an old row; the trajectory is the data.

**Columns** (adapt to what the platform exposes): views, likes, replies, reposts,
bookmarks, profile visits, new follows. Unknown = `—`, never a guess.

**Sources.** Platform analytics pages are the ground truth and usually need the human
(screenshot or read-off). Some platforms expose partial public per-post data without
login (e.g. X's per-tweet syndication endpoint yields like/reply counts; timelines and
full analytics do not work headlessly) — use whatever public endpoint exists for
automated partial rows, marked `(auto)`, and flag entries due for a manual snapshot.

## Retros

Write the retro once ~7d metrics exist (earlier if the result is already clear).

- **What worked** — tie each point to evidence in the metrics or replies, not vibes.
- **What went wrong** — same standard. "0 profile visits on 83 views" is a finding;
  "engagement was low" is not.
- **Lesson** — exactly one line, phrased as advice to a future drafting session.

**Promote** a lesson to PLAYBOOK.md only when it is durable (would apply to most future
posts) — link back to the source entry. When a new retro contradicts a playbook rule,
update the rule and note what changed its status; the playbook is falsifiable or it is
folklore.

## Reply engine

Why: with a small following, the in-network launch pool is too small to push posts
out-of-network. Substantive replies to established accounts in the niche put your
thinking in front of their audience — good replies drive profile clicks → follows →
a bigger launch pool for every future post.

**Discovery (weekly, semi-manual).** Run `<content>/prompts/find-builders.md` in a
logged-in browser-agent session (timelines and search require login — this step cannot
be headless). Paste results into WATCHLIST.md: a "start here" top-5 with reply angles,
the full table, and a Pruned section for accounts that stop qualifying.

**Queueing (human, ~zero cost).** During normal scrolling, the human drops post URLs
worth replying to into `replies/QUEUE.md`, optionally with an angle note.

**Drafting (agent work, automatable).** For each queued URL: fetch the post text (public
per-post endpoints where available), then write **two** alternative replies into
`replies/YYYY-MM-DD.md`, each 1–3 sentences in the user's voice, with a recommendation
of which to send. Move processed URLs to the queue's Processed section. Quality bar per
reply: it must be impossible to paste under a different post; no generic praise; never
pitch the user's own project; no links; end with a real question when one genuinely
exists. Skipping a post ("nothing substantive to add") beats forcing a draft.

**Posting — always the human.** Never send replies. Ever.

## Automations (optional)

If the environment supports scheduled agent tasks (e.g. Claude Code scheduled tasks),
offer two, and document them in `<content>/README.md` under an Automations section:

1. **Metrics capture** (daily, evening) — for every `status: posted` entry with a
   `post_url`, fetch public per-post counts where an endpoint exists, append an
   `(auto)` metrics row (skip if today's row exists, never overwrite), and flag entries
   hitting the 24h/7d marks for a manual analytics snapshot. Scope the task to editing
   `## Metrics` tables only.
2. **Reply drafting** (daily, morning) — process `replies/QUEUE.md` exactly as in
   "Reply engine → Drafting". Bake the hard rule into the task prompt: *it only ever
   writes draft files in the repo; it never posts, publishes, or sends anything.*

Timezone note: schedule in the user's local time and prefer a morning slot for reply
drafts (fresh queue → same-morning replies) and an evening slot for metrics.
