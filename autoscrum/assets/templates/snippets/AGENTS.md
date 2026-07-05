# AGENTS.md

This file routes AI agents to where each kind of truth lives and states the workflow contract. It is a router, not a rulebook — do not accumulate product, API, UI, or database rules here; put them in the file that owns them. `CLAUDE.md` is a thin adapter that points here.

## Where Truth Lives

| Question | File |
| --- | --- |
| What is this project, how do I set it up and run it? | `README.md` |
| What is the product, its principles, its non-goals? | `PRODUCT.md` |
| How should the UI look and behave? | `DESIGN.md` |
| How does service X run — env, commands, endpoints? | `<service>/README.md` |
| What is the development workflow? | `docs/development-cycle.md` |
| What work is planned or in flight? | `docs/sprints/` |
| What does version X include, and when can it ship? | `docs/releases/` |
| What has already shipped? | `CHANGELOG.md` |

## Workflow Contract

- **Before implementing non-trivial work:** check `docs/sprints/backlog.md` and the current sprint; claim an existing item or create one. Do not start unplanned release-relevant work.
- **While working:** append dated bullets to the sprint work log for status changes, blockers, scope changes, decisions, and verification results.
- **Before finishing a change:** update `CHANGELOG.md` under `Unreleased` and the target release contract in `docs/releases/`, or mark the change not release-relevant in the PR (label: `not-release-relevant`).
- **Commits:** Conventional Commits — `type(scope): summary`, scopes from real repo areas.
- **PRs:** use the PR template; include sprint/backlog link, validation results, and changelog/release impact.
- **Releases:** never tag, publish, or deploy outside the release prep flow in `docs/releases/README.md`.
- **Doc boundaries:** keep `PRODUCT.md` implementation-free, `CHANGELOG.md` a release history (not a work log), and this file a router.
