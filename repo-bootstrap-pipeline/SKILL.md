---
name: repo-bootstrap-pipeline
description: Standardize a git repository's product docs, repo router, implementation history, and repo-local starter agent skills. Use when bootstrapping a new project repo, cleaning up an existing repo, creating or repairing README.md, PRODUCT.md, PLAN.md, AGENTS.md, optional DESIGN.md, docs/implementation-history, or .agents/skills workflows for repo orientation, implementation history, and git release flow.
---

# Repo Bootstrap Pipeline

Use this skill to make a repo easy for humans and coding agents to understand, modify, validate, and continue later. Keep the output true to the repo. Do not create fake commands, guessed architecture, empty boilerplate, or TODO-heavy docs.

## Hard Stops

Stop before editing when any of these are true:

- The target is not inside a git repo. Explain that bootstrap requires git history/change tracking and ask for the correct repo path.
- The cwd or git root looks like a system, home, cache, or accidental location. Examples: `/`, `/Users/burak`, Desktop, Downloads, `/tmp`, `.codex`, `.agents`, `node_modules`, package caches, or tool cache folders.
- The target looks like a mistake even if it is a git repo. Ask the user to confirm the repo path before continuing.

The current working directory is the default target. If cwd is inside a repo, use the git root as the repo root after the safety check.

## Workflow

1. Inspect first.
   - Run `git rev-parse --show-toplevel` and `git status --short`.
   - List top-level files and important manifests with `rg --files`.
   - Read existing `README.md`, `PRODUCT.md`, `PLAN.md`, `AGENTS.md`, `DESIGN.md`, package/app READMEs, and relevant config files if present.
   - Detect product type and repo capabilities from files before asking.

2. Classify the repo.
   - Use `references/product-types.md` to infer product type.
   - Recognize: `web-app`, `mobile-app`, `desktop-app`, `cli`, `api`, `library-sdk`, `ai-assistant`, `coding-agent`, `automation-script`, and `monorepo`.
   - Ask only when product type or optional capabilities are unclear.

3. Choose write policy.
   - Create missing or obviously incomplete standard files directly.
   - Preserve meaningful existing docs.
   - Before rewriting meaningful docs, show a proposed change list and wait for approval.
   - Dirty working trees are allowed. Do not revert unrelated user changes.

4. Create or update the standard repo surface.
   - Root docs: `README.md`, `PRODUCT.md`, `PLAN.md`, `AGENTS.md`.
   - Create `DESIGN.md` only for UI products.
   - Create `docs/implementation-history/`.
   - If files are written, create an implementation-history entry for the bootstrap itself.
   - Create repo-local starter skills under `.agents/skills/`.

5. Detect optional capabilities.
   - i18n/localization.
   - Generated code/API docs: JavaDoc, XML docs, TypeDoc, DocFX, OpenAPI, or similar.
   - CI/CD, pull request templates, lint, format, tests, typecheck, schema validation, ORM/migrations, deployment, env/config, and monorepo app/package README needs.
   - Document current truth in the right docs.
   - Add missing important standards to `PLAN.md` as `Recommended next standards` with `P0`, `P1`, or `P2` priority. Also mention them in the final response.

6. Validate.
   - Check expected files exist.
   - Run markdown formatting/lint only if the repo already has a markdown tool.
   - Validate starter skill frontmatter and relative paths.
   - Run `git status --short`.
   - Final response must list created/updated files, skipped files, validation run, and recommended next standards.

## Standard Files

- `README.md`: what it is, setup/install, usage when repo-facing, env docs, dev commands, validation, light contribution basics.
- `PRODUCT.md`: lightweight product spec: problem, users, use cases, requirements, non-goals, success criteria.
- `PLAN.md`: vision and roadmap. Include prioritized `Recommended next standards` when gaps are found.
- `AGENTS.md`: thin repo router. Point to docs, commands, repo areas, and local skills. Tell agents to update docs/router when repo truth changes.
- `DESIGN.md`: UI/UX standards only when UI exists.
- `docs/implementation-history/YYYY-MM-DD-short-title.md`: one entry per meaningful planned change.

Keep `PRODUCT.md` and `PLAN.md` at repo root. Put deeper docs under `docs/`.

Do not create `TASKS.md`, `TODO.md`, `.gitignore`, or external skill installs by default.

## Starter Skills

Create these repo-local folders when bootstrapping:

- `.agents/skills/repo-orientation/SKILL.md`
- `.agents/skills/implementation-history/SKILL.md`
- `.agents/skills/git-release-flow/SKILL.md`

Use `references/starter-skills.md` as the index for embedded templates, then adapt each skill to real repo paths, commands, docs, and product type.

Do not install skills from GitHub, `skills.sh`, or `npx` in v1. If these starter skills prove stable across several repos, they can later become shared/global skills. Until then, prefer repo-local templates.

## References

- Read `references/product-types.md` when classifying product type or deciding which docs are required.
- Read `references/doc-templates.md` when choosing standard doc templates.
- Read only the needed files under `references/templates/docs/` when writing standard docs or implementation-history entries.
- Read `references/starter-skills.md` when choosing repo-local starter skill templates.
- Read only the needed files under `references/templates/skills/` when creating repo-local starter skills.
