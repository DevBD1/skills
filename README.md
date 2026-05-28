# Skills

Curated global AI agent skills I use across workspaces.

This repository is backed by the live `~/.agents/skills` directory, but it is
not a claim of authorship over every skill I use. Only folders marked as
`owned` are published here as source I maintain. Third-party and unclear-origin
skills are documented as install/reference pointers instead of being published
as copied source.

## Rules

- Keep reusable global skills here.
- Keep repo-specific workflow, product, style, and design rules inside that repo.
- Keep the live installed layout flat: one skill folder per top-level directory.
- Group skills by README sections and manifest tags, not folder nesting.
- Preserve source, author, and license notes for third-party skills.
- Do not publish third-party skill contents unless redistribution is intentional
  and the license/source is clear.

## Published Source

These skills are currently published as full folders in this repo.

| Skill | Status | Notes |
| --- | --- | --- |
| `antigravity-cli-delegate` | owned | Local delegate wrapper for bounded Antigravity CLI work. |
| `hytale-modder` | owned | Local Hytale modding guidance and references. |
| `repo-bootstrap-pipeline` | owned | Local repo bootstrap workflow and starter skill templates. |

## Pointer-Only Skills

These skills are installed locally but are not published as copied source in
this repo. They are listed in `skills.yml` so the collection remains visible
without claiming ownership.

| Skill | Status | Author / Source | Notes |
| --- | --- | --- | --- |
| `antivibe` | third-party | mohi-devhub / GitHub | Installed framework; source pointer only. |
| `crawl4ai` | unknown-third-party | unknown | Keep pointer-only until source/license is confirmed. |
| `design-md` | unknown-third-party | unknown | Keep pointer-only until source/license is confirmed. |
| `docker-expert` | unknown-third-party | community | Local metadata marks this as community/unknown. |
| `find-skills` | unknown-third-party | skills.sh | Skill discovery helper; source pointer only. |
| `grill-me` | unknown-third-party | unknown | Keep pointer-only until source/license is confirmed. |
| `stitch-design` | unknown-third-party | unknown | Keep pointer-only until source/license is confirmed. |
| `supabase` | third-party | Supabase | Installed Supabase skill; source pointer only. |
| `supabase-postgres-best-practices` | third-party | Supabase / MIT | Installed Supabase Postgres guidance; source pointer only. |
| `vercel-react-best-practices` | third-party | Vercel / MIT | Installed Vercel React performance guidance; source pointer only. |
| `view-pdf` | unknown-third-party | unknown | Keep pointer-only until source/license is confirmed. |
| `web-design-guidelines` | third-party | Vercel | Installed from Vercel Labs agent skills; source pointer only. |

## Manifest

`skills.yml` is the source of truth for ownership metadata. Each entry records
the skill name, ownership status, author/source, install command when known,
license, whether source is published in this repo, and notes.

## Before Publishing Changes

Run:

```bash
find . -name ".DS_Store" -o -name ".git"
rg -n "token|secret|password|api[_-]?key|/Users/burak|localhost|127\\.0\\.0\\.1|sk-|ghp_" .
find . -maxdepth 2 -name SKILL.md -print | sort
git status --short --branch
```

Expected:

- no nested `.git`
- no `.DS_Store`
- no real secrets
- local installed skills still have `SKILL.md`
- public git index contains only owned skill folders plus repo docs
