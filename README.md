# Skills

[![skills.sh](https://skills.sh/b/DevBD1/openclaw-skill-scrapling-mcp)](https://skills.sh/DevBD1/openclaw-skill-scrapling-mcp)

Curated AI agent skills I maintain and publish.

This repository is the DevBD1-owned skills collection. The local checkout lives
under `~/.agents/skills/devbd1`; generic skills are managed outside this
repository as sibling folders under `~/.agents/skills`.

## Rules

- Keep DevBD1-owned reusable skills in this repository.
- Keep generic skills outside this checkout, under `~/.agents/skills`.
- Keep repo-specific workflow, product, style, and design rules inside that repo.

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
repository intentionally has no blanket license; use each skill folder's own
license and notes.

## Manifest

`skills.yml` is the source of truth for ownership metadata. Each entry records
the skill name, ownership status, author/source, install command when known,
license, and notes.

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
