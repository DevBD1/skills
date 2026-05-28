# Skills

[![skills.sh](https://skills.sh/b/DevBD1/skills)](https://skills.sh/DevBD1/skills)

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
| `antigravity-cli-delegate` | owned / MIT | Local delegate wrapper for bounded Antigravity CLI work. Install with `npx skills add DevBD1/skills --skill antigravity-cli-delegate`. |
| `hytale-modder` | owned | Local Hytale modding guidance and references. |
| `repo-bootstrap-pipeline` | owned | Local repo bootstrap workflow and starter skill templates. |

Owned published skill folders may include their own license files. The root
repository intentionally has no blanket license because the collection also
documents mixed-origin, pointer-only skills.

## Pointer-Only Skills

These skills are installed locally but are not published as copied source in
this repo. They are listed in `skills.yml` so the collection remains visible
without claiming ownership.

| Skill | Status | Author / Source | Notes |
| --- | --- | --- | --- |
| `antivibe` | third-party | [mohi-devhub](https://github.com/mohi-devhub/antivibe) | Installed framework; source pointer only. |
| `crawl4ai` | third-party | [brettdavies](https://github.com/brettdavies/crawl4ai-skill) | Installed Crawl4AI skill; source pointer only. |
| `design-md` | third-party | [google-labs-code](https://github.com/google-labs-code/stitch-skills) | Installed from Google Labs Stitch skills; source pointer only. |
| `docker-expert` | third-party | [sickn33](https://github.com/sickn33/antigravity-awesome-skills/blob/main/skills/docker-expert/SKILL.md) | Installed Docker expert skill; source pointer only. |
| `find-skills` | unknown-third-party | [skills.sh](https://skills.sh/) | Skill discovery helper; source pointer only. |
| `grill-me` | third-party | [mattpocock](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) | Installed productivity skill; source pointer only. |
| `stitch-design` | third-party | [google-labs-code](https://github.com/google-labs-code/stitch-skills) | Installed from Google Labs Stitch skills; source pointer only. |
| `supabase` | third-party | [Supabase](https://github.com/supabase/agent-skills/tree/main/skills) | Installed Supabase skill; source pointer only. |
| `supabase-postgres-best-practices` | third-party | [Supabase](https://github.com/supabase/agent-skills/tree/main/skills) / MIT | Installed Supabase Postgres guidance; source pointer only. |
| `vercel-react-best-practices` | third-party | [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) / MIT | Installed Vercel React performance guidance; source pointer only. |
| `view-pdf` | third-party | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/blob/main/pdf-viewer/skills/view-pdf/SKILL.md) | Installed PDF viewer skill; source pointer only. |
| `web-design-guidelines` | third-party | [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | Installed Vercel Labs web design review guidance; source pointer only. |

## Manifest

`skills.yml` is the source of truth for ownership metadata. Each entry records
the skill name, ownership status, author/source, install command when known,
license, whether source is published in this repo, and notes.

## Before Publishing Changes

Run:

```bash
find . -name ".DS_Store" -o -name ".git"
rg -n "token|secret|password|api[_-]?key|\\$HOME|localhost|127\\.0\\.0\\.1|sk-|ghp_" .
find . -maxdepth 2 -name SKILL.md -print | sort
git status --short --branch
```

Expected:

- no nested `.git`
- no `.DS_Store`
- no real secrets
- local installed skills still have `SKILL.md`
- public git index contains only owned skill folders plus repo docs
