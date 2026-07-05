# Operations: Operate And Repair

Use this reference when the workflow already exists and the request is to run a step of it (Operate) or check and fix its health (Repair/Audit). Do not re-run Establish setup for these requests.

## Operate

Run only the step asked for. Each recipe assumes the doc hierarchy is installed.

### Capture an idea
Add it to `docs/sprints/backlog.md` under `Candidate` with module/area, user value, acceptance criteria, and validation. Promote to `Ready` once implementable without rediscovery.

### Start a sprint
Create `docs/sprints/YYYY-MM-DD-sprint-N.md` from the sprint template. Pull `Ready` backlog items, set the sprint goal, dates, release targets (contract files or `Not release-relevant`), and changelog impact. Move pulled items out of the backlog or mark them committed.

### Claim and implement an item
Before non-trivial implementation, confirm the work maps to a sprint item (create one if missing). Set its status, implement, and append dated bullets to the work log for status changes, blockers, scope changes, decisions, and verification results — not every edit.

### Record delivery
When an item completes: check acceptance criteria, run its validation, log the result, and update `CHANGELOG.md` under `Unreleased` (linking the sprint doc) plus the target release contract's scope/acceptance if release-relevant.

### Close a sprint
Fill the Review section (completed, verification, changelog status, release channel, not completed) and a short Retro (keep, change, follow up). Move carryover to the backlog or next sprint.

### Draft or update a release contract
Create `docs/releases/vX.Y.Z.md` from the release template. Define includes/excludes, acceptance criteria, and launch gate. Set lifecycle status (`Draft` → `Committed` → `Shipped`; `Cancelled` if abandoned) and update the index in `docs/releases/README.md`.

### Release prep
Follow the release prep steps in `docs/releases/README.md`: confirm sprint coverage, finalize changelog entries, bump the version source, run validation, satisfy the contract's launch gate, merge the release prep PR, publish, then flip the contract to `Shipped`.

## Repair / Audit

Run this checklist read-only first; report findings and proposed fixes before mutating anything.

### Drift checklist

- **Stale Unreleased:** `CHANGELOG.md` has `Unreleased` entries older than the latest tag/deploy — either a release was published without changelog finalization, or entries were never moved.
- **Unproven work:** backlog or sprint items marked `Done` with no changelog entry and no `Not release-relevant` rationale.
- **Version mismatch:** version source (manifest/version file) disagrees with the latest tag or deployed version.
- **Stuck contracts:** release contracts in `Committed` whose version has already shipped, or `Draft` contracts for versions already tagged.
- **Missing sprint closure:** sprint files past their end date without Review/Retro sections filled.
- **Broken routing:** `AGENTS.md`, `CLAUDE.md`, README doc index, or contract/sprint cross-links pointing at missing files.
- **Placeholder leaks:** unresolved `<placeholders>` in installed docs, PR templates, or workflow files.
- **Boundary violations:** implementation status creeping into `PRODUCT.md`, work-log detail in `CHANGELOG.md`, product/API rules accumulating in `AGENTS.md`, repo-wide rules duplicated in `CLAUDE.md`.
- **CI gate health:** `validate.yml`/`release.yml` present but failing, disabled, or referencing commands that no longer exist.

### Fix order

1. Restore truth (version, tags, contract statuses) before restoring process docs.
2. Backfill missing changelog entries from sprint docs and merged PRs — keep them terse.
3. Repair links and boundaries.
4. Only then tighten process (templates, CI gates) so drift does not recur.

Record what was repaired in the current sprint work log.
