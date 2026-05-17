# Skills

Reusable global AI agent skills I use across workspaces.

This repository is the live contents of `~/.agents/skills`. Each top-level
folder is an active global skill with its own `SKILL.md`.

## Rules

- Keep reusable skills here.
- Keep repo-specific workflow, product, style, and design rules inside that repo.
- Keep the installed layout flat: one skill folder per top-level directory.
- Use README sections and tags for grouping instead of moving active skills into nested folders.
- Preserve source and license notes for third-party skills.
- Mark modified third-party skills as modified forks when documenting them.

## Skills

### Development and Reviews

- `antivibe` - learning-focused explanations for AI-written code.
- `grill-me` - plan and design stress testing through focused questions.
- `repo-bootstrap-pipeline` - bootstrap repo docs, routing rules, and local agent skills.
- `vercel-react-best-practices` - focused React and Next.js performance review guidance.
- `web-design-guidelines` - UI, UX, accessibility, and design review guidance.

### Data and Platforms

- `crawl4ai` - web crawling and structured extraction workflows.
- `supabase` - Supabase implementation guidance.
- `supabase-postgres-best-practices` - Postgres performance guidance from Supabase.

### Design and Domain Skills

- `design-md` - synthesize Stitch design systems into `DESIGN.md`.
- `stitch-design` - Stitch MCP design generation and prompt workflow.
- `hytale-modder` - Hytale modding guidance for ECS, threading, and KuksoHyLib.

### Skill Discovery

- `find-skills` - skill discovery helper.

## Source Notes

Some skills are original or locally adapted. Some are copied or derived from
third-party sources. Check each skill folder for its own metadata, README, and
license files. A root license is intentionally not used because this collection
contains mixed-origin material.

## Before Publishing Changes

Run:

```bash
find . -name ".DS_Store" -o -name ".git"
rg -n "token|secret|password|api[_-]?key|/Users/burak|localhost|127\\.0\\.0\\.1|sk-|ghp_" .
find . -maxdepth 2 -name SKILL.md -print | sort
```

Expected:

- no nested `.git`
- no `.DS_Store`
- no real secrets
- every active skill has a `SKILL.md`
