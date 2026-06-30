# Development Cycle

This repository uses a lightweight, traceable development cycle. The goal is not ceremony; the goal is making every meaningful idea, implementation, validation step, PR, and release easy to follow later.

## Full Cycle

```text
idea -> backlog -> sprint -> implementation -> validation -> changelog -> PR -> merge -> release prep -> release
```

## 1. Capture The Idea

Drop new ideas, bugs, refactors, or documentation work into `docs/sprints/backlog.md`.

- `Candidate`: fresh ideas.
- `Ready`: clear enough to implement.
- `Blocked`: waiting on a decision or dependency.
- `Done`: completed records.

## 2. Commit Work To A Sprint

Before implementing non-trivial work, create or update the current sprint file under `docs/sprints/`.

Use `docs/sprints/templates/sprint.md` and files named:

```text
docs/sprints/YYYY-MM-DD-sprint-N.md
```

## 3. Implement And Log Meaningful Progress

Make the changes in the relevant module, package, app, or repo area. Update the sprint work log for status changes, blockers, scope changes, decisions, and validation results.

## 4. Validate

Run the smallest relevant validation command, such as:

```sh
<validation-command>
git diff --check
```

Record the result in the sprint item and PR.

## 5. Update Release Records

If the work is user-visible or release-relevant, update `CHANGELOG.md` under `Unreleased` and link the sprint doc.

## 6. Open The PR

Use Conventional Commit style:

```text
type(scope): summary
```

Use the PR template and include changed areas, sprint/backlog link, validation, changelog impact, release/version impact, and risks.

## 7. Merge And Release

After review and CI pass, merge to main/trunk. When ready to ship, open a release prep PR, finalize changelog entries, update `<version-source>`, validate, merge, then publish the release using the repo's release process.
