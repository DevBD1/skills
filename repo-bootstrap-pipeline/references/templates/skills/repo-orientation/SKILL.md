---
name: repo-orientation
description: Orient work in this repo before making changes. Use when starting a task, deciding where code belongs, finding commands, reading repo docs, or checking how this repo is organized.
---

# Repo Orientation

Use this skill before non-trivial work in this repo.

## Workflow

1. Read root docs in this order:
   - README.md
   - PRODUCT.md
   - PLAN.md
   - AGENTS.md
   - DESIGN.md, only for UI work
2. Run `git status --short` and do not overwrite unrelated user changes.
3. Inspect the relevant app/package/module before planning edits.
4. Use the repo router in AGENTS.md to choose the right path.
5. Use real commands from README.md, AGENTS.md, package files, or config. Do not invent commands.
6. If repo structure, commands, or docs are stale, update the matching doc as part of the work.

## Repo Notes

- Product type: [PRODUCT_TYPE]
- Main app/package paths: [PATHS]
- Primary validation commands: [COMMANDS]
