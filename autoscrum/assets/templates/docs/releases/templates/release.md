# Release vX.Y.Z

- **Status:** Draft <!-- Draft | Committed | Shipped | Cancelled -->
- **Target channel:** tag / GitHub Release / package publish / deployment / platform changelog / internal notes
- **Target date:** YYYY-MM-DD or "when scope completes"

## Scope: Includes

What this version ships. Each entry should trace to backlog/sprint items.

- Feature or fix — `docs/sprints/YYYY-MM-DD-sprint-N.md`

## Scope: Excludes

Explicit non-goals for this version, so scope creep is visible.

- Deferred item and where it went (backlog, later contract).

## Acceptance Criteria

Observable outcomes that must hold before this version ships.

- [ ] Criterion tied to an includes entry.
- [ ] Compatibility, migration, or operational expectation.

## Launch Gate

All boxes checked before publishing:

- [ ] All acceptance criteria verified, with results in sprint docs.
- [ ] `<validation-command>` green.
- [ ] `CHANGELOG.md` section finalized from `Unreleased` and linked here.
- [ ] `<version-source>` bumped to `X.Y.Z` in a release prep PR.
- [ ] Config, permission, and migration impacts documented.
- [ ] Publish channel ready (tag/artifact/deploy/external notes).

## Lifecycle Log

- YYYY-MM-DD — Created as Draft.
