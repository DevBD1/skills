# Repository Guidelines

## Project Structure & Module Organization

This repository is the DevBD1-owned agent skills collection. Keep the checkout at `~/.agents/skills/devbd1`; generic third-party or pointer-only skills belong as sibling folders under `~/.agents/skills`, not inside this repo.

Root files:

- `README.md`: public skill catalog, install example, and usage-facing metadata.
- `skills.yml`: source of truth for published skill metadata.
- `.gitignore`: repository-level ignore rules.

Each skill lives in a top-level directory named after the skill, for example `openclaw-skill-scrapling-mcp/` or `continuous-dev-cycle/`. A skill should include `SKILL.md`; optional supporting content belongs in `references/`, `scripts/`, `assets/`, or `agents/` inside that skill folder.

## Build, Test, and Development Commands

There is no repository-wide build system. Use targeted validation:

```bash
find . -maxdepth 2 -name SKILL.md -print | sort
```

Confirms every published skill has an entrypoint.

```bash
rg -n "token|secret|password|api[_-]?key|sk-|ghp_" .
```

Checks for accidental secrets before publishing.

```bash
find . -name ".DS_Store" -o -name ".git"
git status --short --branch
```

Verifies there are no nested Git repositories, macOS metadata files, or unexpected worktree changes.

Run script-specific smoke checks only when changing scripts, such as `python openclaw-skill-scrapling-mcp/scripts/scrapling_smoke_test.py`.

## Coding Style & Naming Conventions

Use Markdown for skill instructions and YAML for metadata. Keep prose direct, public-safe, and reusable. Name skill directories in lowercase kebab-case, and keep `skills.yml` names aligned with directory names. Prefer ASCII unless a skill’s source material requires otherwise. Python helper scripts should follow standard Python style with clear function names and minimal dependencies.

## Testing Guidelines

Add or run the smallest relevant validation for the changed skill. For documentation-only edits, check links, headings, and manifest consistency manually. For script edits, add a smoke path or example command near the script or in the related `SKILL.md`.

## Commit & Pull Request Guidelines

Recent history uses concise imperative messages, sometimes scoped, for example `Remove pointer-only skills metadata` or `fix(continuous-dev-cycle): harden release workflow planning`. Keep commits focused on one skill or one repository-level concern. Pull requests should describe the changed skill, mention validation commands run, and call out any publishing or install-command changes.

## Agent-Specific Instructions

Do not add generic skills to this repository. Do not create nested Git repositories inside skill folders. When adding, removing, or renaming a skill, update both `README.md` and `skills.yml` in the same change.
