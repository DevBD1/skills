---
name: continuous-dev-cycle
description: Establish, repair, or operate a repository's continuous development workflow. Use when Codex is asked to set up or standardize lightweight Scrum, backlog and sprint docs, changelog and release history, Conventional Commits, pull request templates, CI validation, versioning, release prep, tags, GitHub Actions releases, or an end-to-end idea-to-release development cycle across one or more repositories.
---

# Continuous Dev Cycle

Use this skill to make a repo's development loop explicit and repeatable: idea capture, sprint planning, implementation, validation, PR, merge, release prep, tag, and release.

## First Pass

1. Inspect before changing anything:
   - `git rev-parse --show-toplevel`
   - `git status --short --branch`
   - top-level docs, manifests, CI files, PR templates, changelog, release docs, tags, and version sources.
2. Preserve repo truth:
   - Do not overwrite meaningful existing workflow docs or unrelated dirty files.
   - Adapt existing conventions before introducing new ones.
   - Ask only for preferences that cannot be discovered locally.
3. Classify the repo:
   - Single package or monorepo.
   - App, library, CLI, service, plugin, docs repo, or mixed.
   - GitHub, other forge, or local-only.
   - Existing version source and release mechanism.

Read `references/repo-adaptation.md` when the repo shape is not obvious or when existing process docs conflict.

## Standard Workflow

Default to this chain unless the repo already has a stronger convention:

```text
idea -> backlog -> sprint -> implementation -> validation -> changelog -> PR -> merge -> release prep -> tag/release
```

Use lightweight Scrum with concise artifacts:

- `docs/sprints/backlog.md` for ideas and groomed work.
- `docs/sprints/YYYY-MM-DD-sprint-N.md` for committed work and delivery notes.
- `CHANGELOG.md` for final release history.
- `docs/releases/` for versioning, tag, artifact, and publishing rules.
- `.github/pull_request_template.md` or forge equivalent for PR exit checks.

Read `references/workflow-model.md` before bootstrapping these files or updating the process.

## Exit Workflow

Prefer a PR-first exit path:

- Tie non-trivial work to a backlog or sprint item before implementation.
- Record meaningful progress and verification in the sprint work log.
- Update `CHANGELOG.md` for user-visible or release-relevant changes.
- Use Conventional Commits by default: `type(scope): summary`.
- Use release prep PRs for version bumps and changelog finalization.
- Publish releases from the main/trunk branch using the repo's CI or release tooling.

Read `references/release-models.md` before changing versioning, release tags, changelog movement, or CI release workflows.

## Applying Templates

Use templates in `assets/templates/` as adaptable starting points, not as rigid files:

- Replace placeholders such as `<repo-name>`, `<module-or-package>`, `<validation-command>`, `<version-source>`, and `<tag-format>`.
- Remove sections that do not apply.
- Preserve stronger existing repo-specific process.
- Keep generated docs short and implementation-ready.

Common templates:

- `assets/templates/docs/development-cycle.md`
- `assets/templates/docs/sprints/README.md`
- `assets/templates/docs/sprints/backlog.md`
- `assets/templates/docs/sprints/templates/sprint.md`
- `assets/templates/docs/releases/README.md`
- `assets/templates/.github/pull_request_template.md`
- `assets/templates/.github/workflows/release.yml`
- `assets/templates/snippets/AGENTS.md`
- `assets/templates/snippets/CHANGELOG.md`

## Validation

After workflow changes:

- Run `git diff --check` on changed docs and workflow files.
- Parse YAML workflow files when possible.
- Run the repo's smallest relevant validation command if CI or release commands changed.
- Confirm `git status --short` contains only intended changes plus pre-existing user changes.

When creating or updating this skill itself, run:

```sh
python3 /Users/burak/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>
```
