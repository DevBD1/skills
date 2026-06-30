# Skills

[![skills.sh](https://skills.sh/b/DevBD1/openclaw-skill-scrapling-mcp)](https://skills.sh/DevBD1/openclaw-skill-scrapling-mcp)

Curated AI agent skills I maintain and publish.

This repository is the DevBD1-owned skills collection. The local checkout lives
under `~/.agents/skills/devbd1/openclaw-skill-scrapling-mcp`; generic
third-party skills stay installed as sibling folders under `~/.agents/skills`.
That keeps the published repo limited to maintained source while still allowing
the local skills bank to contain generic installed skills.

## Rules

- Keep DevBD1-owned reusable skills in this repository.
- Keep generic third-party skills outside this checkout, under `~/.agents/skills`.
- Keep repo-specific workflow, product, style, and design rules inside that repo.
- Preserve source, author, and license notes for third-party skills.
- Do not publish third-party skill contents unless redistribution is intentional
  and the license/source is clear.

## Repository Layout

```text
.
├── README.md
├── skills.yml
├── .gitignore
├── openclaw-skill-scrapling-mcp/
├── antigravity-cli-delegate/
├── codex-cli-delegate/
├── continuous-dev-cycle/
└── hytale-modder/
```

## Published Source

These skills are currently published as full folders in this repo.

| Skill | Status | Notes |
| --- | --- | --- |
| `openclaw-skill-scrapling-mcp` | owned | Scrapling MCP guidance, recipes, and helper scripts for web scraping workflows. |
| `antigravity-cli-delegate` | owned / MIT | Local delegate wrapper for bounded Antigravity CLI work. |
| `codex-cli-delegate` | owned / MIT | Local delegate wrapper for bounded Codex CLI work by other agents. |
| `continuous-dev-cycle` | owned | Continuous development workflow templates and release planning guidance. |
| `hytale-modder` | owned | Local Hytale modding guidance and references. |

Owned published skill folders may include their own license files. The root
repository intentionally has no blanket license because the collection also
documents mixed-origin, pointer-only skills.

## Pointer-Only Skills

These skills may be installed locally as generic sibling folders under
`~/.agents/skills`, but they are not published as copied source in this repo.
They are listed in `skills.yml` so the collection remains visible without
claiming ownership.

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
- public git index contains only owned skill folders plus repo docs
