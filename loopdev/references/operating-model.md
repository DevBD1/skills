# Operating Model

Use this reference for migration, project configuration, durable state, and
delivery. The project chooses its tools; LoopDev supplies the connection
between recorded work, optional plans, implementation, and user review.

## Discovery and choice

Inspect actual repository instructions and automation before assuming how the
team works. Follow references to connected issue trackers and project boards
when accessible. Existing labels, status fields, priorities, branch targets,
and CI/release rules are stronger evidence than conventional filenames.

Summarize the findings in terms the user can choose between:

| Work inventory | Useful when | Configure |
| --- | --- | --- |
| GitHub Issues + GitHub Project | Issues and project views already live with the code | Repository, project URL/ID, field/status mapping, selection/view rules |
| Linear | The team manages work in Linear | Workspace/team/project, status mapping, repository linkage |
| Repository Markdown | Work should travel with the checkout | `docs/issues.md`, `docs/backlog.md`, or chosen files; stable IDs and statuses |
| Existing/custom system | Another tool or format already fits | Exact location, lookup/update mechanism, ownership, status mapping |

These are examples, not an allowlist. GitHub Issues alone or another tracker
can be sufficient. Keep a working provider if the user chooses it. Ask for
selection only if it has not already been made; do not assume migration
authorization from a request to inspect or recommend a workflow.

If both local issues and backlog files are used, define their distinct roles
(for example triage inbox and accepted work) and move items by stable ID.
Avoid two independently editable copies of the same item. A project board
should be a view over issues, not a competing inventory.

## Migration and archival

Once the user has selected the target:

1. Inventory active items, unfinished plans, historical process files, agent
   instructions, templates, scripts, and CI jobs tied to the old system.
2. Map open work into the selected inventory. Preserve scope, acceptance,
   dependencies, priorities, ownership, and history links. Reuse items already
   present; record source IDs and URLs so interrupted migrations are resumable.
3. Move still-useful plans to `docs/plan/` (or the configured path) and link
   them to their items. Archive obsolete plans with the superseded process.
4. Move replaced local artifacts into a unique directory such as
   `docs/archive/loopdev/2026-10-22-scrum-migration/`. Preserve relative paths
   where helpful and add an `index.md` with the old system, migration date,
   old-to-new item/file mapping, target inventory, and any unresolved work.
   Mark the archive historical and inactive; never load archived instructions
   as current agent rules.
5. Replace live references throughout the repository: root/nested agent
   instructions, contributor docs, README links, templates, scripts, CI, and
   scheduled process jobs. Extract still-valid product and release rules from
   mixed documents into active docs before archiving the old process content.
6. Replace or retire process-specific consumers in the same migration and
   verify remaining consumers use the new source. Preserve meaningful product
   checks. Do not retain sprint-shaped stubs, duplicate queues, or compatibility
   parsers unless explicitly requested. If a necessary consumer cannot yet be
   migrated, record the blocker and incomplete migration instead of claiming a
   clean cutover or silently dropping the check.
7. Verify the selected inventory contains the active work, live links resolve,
   and searches for old paths/process commands find only intentional historical
   references. Check that a cold-starting agent reaches config and current work.

For remote history, put an export or source inventory with stable links in the
archive where access permits; leave original history accessible. A local
migration is not permission to delete shared remote projects or bulk-close
unrelated issues. Retire obsolete remote views/automation only within the
authorized scope and identify any remaining external cleanup explicitly.

Do not move unrelated documentation just because it mentions a sprint. The
archive is for superseded workflow material, not still-current product history
or release contracts.

## Project configuration and discovery

Adapt [../assets/config.md](../assets/config.md) into the project's
`.agents/skills/loopdev/config.md`. Replace example values with observed or
selected values; remove unused alternatives. Keep it readable Markdown so
agents from different harnesses can use it without a parser. If local tooling
parses it, document and honor that project's schema.

Record choices once. When a preference is `ask`, ask only when that decision
arises and has not already been answered for this task. Save durable preferences
when requested; do not convert a one-time speed request into project policy.
If an older LoopDev installation has no config, derive candidate values from
its live rules and confirm only unresolved choices. Do not restart setup on
every invocation.

Add a binding like this to the existing auto-read repository instructions,
substituting actual paths and preserving unrelated rules:

```markdown
## Work management

This repository uses LoopDev. Before development work, read
`.agents/skills/loopdev/config.md` and its linked progress/work inventory.
Search that inventory for user-requested work; otherwise resume or select an
eligible item. If a requested item is missing, follow the saved preference or
offer to create it, allowing the user to proceed without tracking. Reuse a
relevant plan; if none exists, follow the saved plan preference or ask. Keep
planning, implementation, required version changes, and ledger updates in one
feature PR. Deliver it for user review/testing and merge only after the user's
green light and the repository's required checks.
```

Use the harness's established entrypoint rather than generating many duplicate
instruction files. Where existing entrypoints coexist, make them point to the
same config. The binding should work even if the global skill is unavailable.

## Progress and plans

Use native issue fields/activity, one local item section, or an existing
ledger/checkpoint. The configured record should let a new agent answer:

- What item/request is in progress, and what is its acceptance scope?
- Which branch/worktree and PR contain it, and who is working there?
- Is there a linked plan, a direct-implementation choice, or a pending choice?
- What verification actually ran, and what is still blocked or untested?
- Is user review pending, approved, or requesting changes?
- What exact action resumes the task?

A useful lifecycle is `queued -> in progress -> awaiting review -> merged`,
with blockers recorded alongside it. Map to existing provider statuses; do not
force those labels or a new schema. When release or deployment is a separate
finish line, record it separately and close the item only when its configured
completion criteria are met.

Search existing plans before creating one. Check that its scope still matches
the current item and code; an obsolete or unrelated plan is not a usable plan.
When no usable plan exists, `plan` delegates planning to the current harness,
`direct` proceeds to implementation, and `ask` presents that choice. The user's
explicit direction settles it for the task. Save an obtained plan as Markdown
and link it to the item/progress record. LoopDev does not prescribe phases,
subagents, reasoning budgets, plan templates, or planning approvals.

Untracked implementation is a valid user choice. Use a short request slug for
the branch/plan/progress reference and do not create an issue after the user
declines one. Reuse the PR as the durable handoff if that is the configured
record. If tracker access fails, distinguish "lookup unavailable" from "no
matching item" and resolve any tracking decision before dependent mutations.

## One feature PR and the merge boundary

Use a feature branch targeting the repository's actual integration branch.
For `feature -> dev -> stage -> main`, the feature PR normally targets `dev`;
for a direct integration model it may target `main`. Inspect the rules instead
of inventing a branch topology. Do not fold unrelated work into the same PR.

Open a draft early if useful, then update it through planning, implementation,
verification, version/changelog changes, and ledger updates. Do not create
separate tracking, plan, implementation, version, and ledger PRs for one task.
An existing plan-only draft can become the implementation PR on a later
request; never implement beyond the user's authorized scope just to fill it.

Before review, include relevant code/docs, the plan if used, required release
metadata, and a truthful progress entry in the feature branch. A pending entry
can say "implementation verified; awaiting review; complete when this PR is
merged". Link the PR and use its live status as merge evidence. Do not predict
an approval, merge date, or merge SHA in committed records.

The handoff must include the PR URL, issue/plan links when present, behavior
changes, verification results, and concrete review/test steps or an available
preview. Set the tracker to its review state, not complete. If pushing or
opening a PR is unavailable, preserve the branch and describe the blocker;
do not fabricate a PR or call delivery complete.

Wait for the user's green light for the delivered PR. Previously given
approval for that same reviewed work is sufficient; do not repeatedly ask.
Address review feedback in the same PR and follow repository re-review rules
for later changes. CI passing, a configured merge method, a speed preference,
or approval of a different PR does not authorize this merge.

After approval and successful required gates, merge using the permitted method
(merge commit, squash, or rebase), then verify live PR state. Synchronize the
remote issue/project or configured ledger with actual results. For a local
ledger, its pre-merge conditional entry plus live PR state can be authoritative;
use existing authorized automation or the next normal work branch for literal
post-merge facts. Do not push an extra bookkeeping commit to a protected branch
or open a follow-up ledger PR just to record the merge.

Include version changes in the feature PR when required. Hand off tagging,
publishing, and promotion to LoopShip when installed, otherwise follow the
repository's existing release procedure. Use the owning release contract and
the user's authorization; merging the feature PR is not blanket release
authorization. Required promotion/release PRs are legitimate repository steps,
not an excuse to split one task into administrative PRs. Report which delivery
stage is complete and any remaining promotion, release, or tracker-sync work.
