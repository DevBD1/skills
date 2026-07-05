# Workflow Model

Use this reference when creating or operating the planning side of a continuous development cycle.

## Core Cycle

```text
idea -> backlog -> sprint -> implementation -> validation -> changelog + release contract -> PR/review -> merge -> release prep -> tag/release/publish
```

Keep the process lightweight. The artifacts exist to preserve intent, decisions, validation, and release traceability.

## Backlog

Use `docs/sprints/backlog.md` as the idea pool and grooming surface.

Recommended states:

- `Candidate`: fresh ideas, bugs, refactors, docs requests.
- `Ready`: clear enough to implement.
- `Blocked`: waiting on decision, dependency, or external input.
- `Done`: completed items kept for traceability.

Each item should include module/area, user value, acceptance criteria, and validation. Keep items concise enough to groom quickly.

## Sprints

Use one-week sprints by default unless the repo already states a cadence.

Recommended filename:

```text
docs/sprints/YYYY-MM-DD-sprint-N.md
```

Each non-trivial task should be tied to a sprint item before implementation. Sprint items should include status, module/area, user value, release target, changelog impact, acceptance criteria, and validation. The release target should name a release contract file (`docs/releases/vX.Y.Z.md`) or state `Not release-relevant`.

Keep the work log as dated bullets per item — bullets append cleanly across many sessions, tables do not. Log meaningful changes only:

- Progress that changes status.
- Blockers.
- Scope changes.
- Decisions future maintainers or agents need.
- Verification results.

## Review And Retro

At completion, update review notes with completed items, validation, changelog status, and incomplete items. Keep retro short: what to keep, what to change, and follow-up/carryover.

## Proportionality

Tiny one-off changes can use a lighter path. Anything non-trivial, user-visible, release-relevant, risky, or cross-module should stay traceable through backlog/sprint/changelog.
