# {{PROJECT}} — Content Log

*Social media content history and creation guide. Every post — across platforms and
accounts — gets one file in `posts/`, a row in [INDEX.md](INDEX.md), and its lessons
distilled into [PLAYBOOK.md](PLAYBOOK.md). The log exists so past posts teach future ones.*

*Owner: {{OWNER}}*

---

## What lives here

```
{{CONTENT_DIR}}/
├── README.md      ← you are here
├── TEMPLATE.md    ← copy this to start a new post entry
├── INDEX.md       ← ledger of all posts, newest first
├── PLAYBOOK.md    ← aggregated do's / don'ts distilled from post retros
├── WATCHLIST.md   ← accounts worth engaging with (refreshed via prompts/)
├── posts/         ← one .md file per post
├── replies/       ← QUEUE.md (drop post URLs) + dated reply-draft files
├── prompts/       ← reusable agent prompts (e.g. niche account discovery)
└── assets/        ← images per post, in a folder named after the post slug
```

## Conventions

- **File naming:** `posts/YYYY-MM-DD-<platform>-<slug>.md` — date is the publish date
  (or planned date for drafts); platform is `x` / `reddit` / `tiktok` / etc.
- **Accounts:** `personal-build-in-public` ({{OWNER}}'s account) or `brand` (future
  {{PROJECT}} profile).
- **Threads are one entry** — number the posts inside `## Content`.
- **Follow-ups:** if a post continues an earlier one, set `follow_up_of` to the earlier
  file's relative path, and add this post to the earlier file's `follow_ups` list. This
  keeps the chain walkable in both directions.
- **Assets:** put images in `assets/<post-slug>/` and list their paths in the frontmatter.
- **Drafts and posting:** agents draft; a human always posts. Nothing in this directory
  is ever auto-published.

## Workflow for a new post

1. Copy [TEMPLATE.md](TEMPLATE.md) to `posts/<date>-<platform>-<slug>.md` with
   `status: draft` (or `idea`).
2. Write/iterate the content there. Drop attached images into `assets/<slug>/`.
3. On publish: set `status: posted`, fill `post_url` and the final text.
4. Capture metrics at least twice: **~24h** and **~7d** after posting (add more
   snapshots if the post keeps moving).
5. Write the **Retro** — what worked, what went wrong, and the lesson.
6. Promote durable lessons to [PLAYBOOK.md](PLAYBOOK.md) and add the post's row to
   [INDEX.md](INDEX.md).
