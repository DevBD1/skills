# Document Hierarchy

Use this reference when installing, auditing, or explaining the repo's document hierarchy. Every file has one job. When content could live in two places, the boundary rules below decide.

## Root Files

### `README.md`
- **Role:** Project overview, setup/install, local run guide, common commands, and the doc index.
- **Cadence:** Updated whenever setup, commands, or the doc set changes.
- **Boundary:** Not a process doc, not a product vision doc. It points to those.
- **Rule:** Never overwrite an existing README. Audit it against the checklist below and propose patches.

Root README audit checklist:

- [ ] One-paragraph project overview.
- [ ] Setup/install instructions that work from a fresh clone.
- [ ] Local run guide.
- [ ] Common commands (build, test, validation).
- [ ] Doc index linking `PRODUCT.md`, `AGENTS.md`, `DESIGN.md` (if present), `CHANGELOG.md`, `docs/development-cycle.md`, `docs/sprints/`, `docs/releases/`, and service READMEs.

### `PRODUCT.md`
- **Role:** Long-term product constitution: vision, principles, identity, governance.
- **Cadence:** Rarely changes; edits are deliberate, governance-level decisions.
- **Boundary:** Does not reflect the current implementation. Feature status, API shapes, and screenshots do not belong here — they rot. If existing ROADMAP/VISION/MISSION docs exist, fold their durable content here and leave execution detail to `docs/sprints/` and `docs/releases/`.

### `CHANGELOG.md`
- **Role:** Shipped release history: versions, shipped features/fixes, rare deployment/operator notes.
- **Cadence:** `Unreleased` entries land with release-relevant PRs; sections finalize during release prep.
- **Boundary:** Not a work log. Delivery details, decisions, and verification live in sprint docs; forward-looking scope lives in release contracts.

### `AGENTS.md`
- **Role:** AI-agent router and repo guidelines: where each kind of truth lives, plus the behavioral contract (claim work before implementing, prove work in docs before finishing).
- **Cadence:** Changes when the workflow or hierarchy changes.
- **Boundary:** Must not become a product/API/UI/database rulebook. It routes to `PRODUCT.md`, `DESIGN.md`, service READMEs, and process docs; it does not restate them.

### `CLAUDE.md`
- **Role:** Claude-specific adapter: route to `AGENTS.md`, plus any Claude-only prompt/context.
- **Cadence:** Rarely changes.
- **Boundary:** Keep thin. Any guideline that applies to every agent belongs in `AGENTS.md`, not here.

### `DESIGN.md`
- **Role:** Product UI/UX source of truth: flows, layout, interaction, visual system.
- **When:** Only if the product has a UI. Do not install otherwise.
- **Boundary:** Design intent, not implementation notes. Component code conventions belong in service READMEs or code.

## Service/Module `README.md`
- **Role:** Service-specific setup, runtime, env vars, commands, endpoints, operational notes.
- **When:** Any service, package, or module that a developer or agent operates independently.
- **Boundary:** Local truth only; repo-wide process stays at root.

## `docs/` Layer

### `docs/development-cycle.md`
- **Role:** The full idea-to-release workflow for this repo, with the placeholders resolved.

### `docs/sprints/`
- **Role:** Execution layer: `backlog.md`, weekly sprint files, reviews, retros, historical records. See `workflow-model.md`.

### `docs/releases/`
- **Role:** `README.md` holds the release process, versioning rules, and a contract index. `vX.Y.Z.md` files are version scope contracts: what a version includes/excludes, acceptance criteria, lifecycle status, launch gate. See `release-models.md`.
- **Boundary:** Contracts are not milestone stubs. A contract that only names a date and a title has failed its job.

## Cross-Linking Rules

Links make the hierarchy navigable for agents; keep them current:

- `README.md` indexes every other top-level doc and `docs/` area.
- `AGENTS.md` routes to everything; `CLAUDE.md` routes to `AGENTS.md`.
- Sprint items name their release target as a contract file (`docs/releases/vX.Y.Z.md`) or `Not release-relevant`.
- Release contracts link the sprint docs that produced their scope.
- Finalized `CHANGELOG.md` sections link the release contract they shipped.

During Repair/Audit mode, verify every link resolves; a pointer to a missing file is drift.
