---
name: continuous-dev-cycle
description: Establish, operate, or repair a repository's continuous AI-assisted development workflow and document hierarchy. Use when asked to set up or standardize lightweight Scrum, backlog and sprint docs, changelog and release history, release scope contracts, PRODUCT.md, AGENTS.md, CLAUDE.md, DESIGN.md, Conventional Commits, pull request templates, CI validation, versioning, release prep, release channels, tags, GitHub Actions releases, platform changelogs, doc hierarchy audits, or an end-to-end idea-to-release development cycle across one or more repositories.
---

# Continuous Dev Cycle

Use this skill to make a repo's development loop explicit, traceable, and provable through docs: idea capture, sprint planning, implementation, validation, changelog and release contracts, PR or review, merge, release prep, publish.

## Mode Dispatch

Classify the request first, then route:

- **Establish**: the repo lacks the workflow or doc hierarchy, or the user asks to set up/standardize it. Follow the Planning-First Gate and First Pass below, then install adapted templates.
- **Operate**: the workflow exists and the user asks to run a step of it (capture an idea, plan a sprint, log work, update the changelog or a release contract, prep a release). Read `references/operations.md` and run only that step.
- **Repair/Audit**: the workflow exists but has drifted (stale docs, missing entries, version mismatches) or the user asks for a health check. Run the drift audit in `references/operations.md` and propose fixes before applying them.

## Document Hierarchy

The workflow is anchored to a canonical doc hierarchy. Each file has a role and a boundary:

| File | Role | Must not become |
| --- | --- | --- |
| root `README.md` | Overview, setup/install, local run, common commands, doc index | — |
| root `PRODUCT.md` | Product constitution: vision, principles, identity, governance; rarely changes | A mirror of current implementation |
| root `CHANGELOG.md` | Shipped release history | A work log |
| root `AGENTS.md` | AI-agent router and repo guidelines | A product/API/UI/database rulebook |
| root `CLAUDE.md` | Thin Claude adapter that routes to `AGENTS.md` | A duplicate rulebook |
| root `DESIGN.md` | UI/UX source of truth (only if the product has UI) | — |
| service/module `README.md` | Service-specific setup, runtime, env, commands, endpoints, ops notes | — |
| `docs/releases/` | Per-version scope contracts plus release process and index | A bare milestone list |
| `docs/sprints/` | Execution layer: backlog, sprint commitments, reviews, history | — |

Read `references/doc-hierarchy.md` for the full spec, cross-linking rules, and the root README audit checklist. Never overwrite an existing root README, AGENTS.md, or CLAUDE.md wholesale — audit and patch.

## Planning-First Gate

Start in a planning-first posture for workflow setup or substantial workflow changes. Inspect the repo, ask release-profile questions that cannot be answered locally, propose the workflow, and wait for explicit user direction before mutating files. If the current environment has a formal plan mode, use it. If not, still behave planning-first in chat.

Ask only questions that affect the workflow design. Cover these choices when they are not discoverable:

- Project visibility: public, private, internal, local-only, or mixed.
- Delivery type: GitHub artifact release, package registry, deployed app/SaaS, platform changelog, blog or social announcement, PR merge only, or custom.
- Release audience: developers, admins/operators, end users, internal team, customers, or mixed.
- Version source: manifest, version file, deployment version, calendar/date release, changelog-only, or none yet.
- Exit artifact: tag, GitHub Release, package publish, deployment, external changelog post, PR merge, or a combination.

## First Pass

1. Inspect before changing anything:
   - `git rev-parse --show-toplevel`
   - `git status --short --branch`
   - top-level docs, manifests, CI files, PR templates, changelog, release docs, tags, deployment files, and version sources.
2. Preserve repo truth:
   - Do not overwrite meaningful existing workflow docs or unrelated dirty files.
   - Adapt existing conventions before introducing new ones.
   - Map existing docs into the hierarchy (e.g. ROADMAP/VISION content belongs in `PRODUCT.md`) instead of duplicating them.
   - Ask only for preferences that cannot be discovered locally.
3. Classify the repo:
   - Single package, app, service, monorepo, docs repo, local-only repo, or mixed.
   - Public, private, internal, or mixed audience.
   - GitHub, other forge, local-only, or deployed platform workflow.
   - Existing version source, release channel, release notes channel, and automation.

Read `references/repo-adaptation.md` when the repo shape is not obvious or when existing process docs conflict.

## Standard Workflow

Default to this chain unless the repo already has a stronger convention:

```text
idea -> backlog -> sprint -> implementation -> validation -> changelog + release contract -> PR/review -> merge -> release prep -> tag/release/publish
```

Use lightweight Scrum with concise artifacts:

- `docs/sprints/backlog.md` for ideas and groomed work.
- `docs/sprints/YYYY-MM-DD-sprint-N.md` for committed work and delivery notes.
- `docs/releases/vX.Y.Z.md` scope contracts for what each version includes, excludes, and requires to launch.
- `CHANGELOG.md` for final release history or internal release notes.
- `docs/releases/README.md` for versioning, release channels, tags, publishing rules, and the contract index.
- `.github/pull_request_template.md` or forge equivalent for PR/review exit checks when the repo uses PRs.

Read `references/workflow-model.md` before bootstrapping these files or updating the process. Read `references/release-models.md` before changing versioning, release contracts, tags, changelog movement, release notes, deployment records, or CI release workflows.

## Exit Workflow

Prefer a PR-first exit path when the repo uses hosted review:

- Tie non-trivial work to a backlog or sprint item before implementation.
- Record meaningful progress and verification in the sprint work log.
- Update `CHANGELOG.md` under `Unreleased` and the target release contract for release-relevant changes.
- Use Conventional Commits by default: `type(scope): summary`.
- Use release prep PRs for version bumps, changelog finalization, contract status flips, deployment notes, and external release copy.
- Publish from the repo's chosen release channel: tag/artifact, package registry, deployment, platform changelog, blog/social announcement, or internal notes.

## Applying Templates

Use templates in `assets/templates/` as adaptable starting points, not as rigid files:

- Replace placeholders such as `<module-or-package>`, `<validation-command>`, `<release-build-command>`, `<version-source>`, `<version-read-command>`, `<tag-format>`, `<release-branch>`, and `<artifact-glob>`.
- Install `DESIGN.md` only when the product has a UI. Install CI workflow templates only for repos hosted where they can run.
- Remove sections that do not apply. Preserve stronger existing repo-specific process. Keep generated docs short and implementation-ready.

Common templates:

- `assets/templates/PRODUCT.md`, `assets/templates/DESIGN.md`, `assets/templates/CLAUDE.md`
- `assets/templates/snippets/AGENTS.md`, `assets/templates/snippets/CHANGELOG.md`, `assets/templates/snippets/service-README.md`
- `assets/templates/docs/development-cycle.md`
- `assets/templates/docs/sprints/README.md`, `.../backlog.md`, `.../templates/sprint.md`
- `assets/templates/docs/releases/README.md`, `.../templates/release.md`
- `assets/templates/.github/pull_request_template.md`
- `assets/templates/.github/workflows/validate.yml`, `.../workflows/release.yml`

## Validation

After workflow changes:

- Run `git diff --check` on changed docs and workflow files.
- Parse YAML workflow files when possible.
- Run the repo's smallest relevant validation command if CI or release commands changed.
- Confirm `git status --short` contains only intended changes plus pre-existing user changes.
- Confirm no unresolved `<placeholders>` remain in installed files.

When creating or updating this skill itself, run the environment's skill validator if one exists.
