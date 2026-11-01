# LoopDev project configuration

Use this template during setup. Save the adapted file as
`.agents/skills/loopdev/config.md` in the target repository, replace example
values with actual choices, and remove unused alternatives and these setup
instructions. Paths below are relative to the repository root. Defaults govern
only unresolved choices; current user instructions can override preferences
for one task without changing this file.

## Work inventory

- Provider: repository Markdown (alternatives include GitHub Issues + Project,
  Linear, or a custom system).
- Authoritative location: `docs/issues.md`.
- Lookup: search open and relevant closed items by ID, title, and meaning;
  check linked PRs before deciding whether work is already covered.
- Selection: resume matching in-flight work; otherwise choose the highest
  priority unblocked item whose dependencies are complete and which is not
  owned by another active worker.
- Missing requested item: `ask` (`create` when preauthorized; `direct` to
  proceed without an item). Always search first. Under `ask`, offer creation
  before implementation and let the user choose creation or direct work.
- Remote access failure: report the unavailable lookup/update; do not assume
  the item is missing or switch inventories. Use explicit user direction for
  proceeding without access and record pending synchronization.
- Field/status mapping: local item ID, priority, dependencies, blockers,
  acceptance, status, plan link, and PR link. Adapt to existing provider fields.

For remote providers, record exact repository/team/project identifiers, URLs,
views, and supported lookup/update tools here. Do not include credentials.
When using both issues and backlog files, define each role and how items move
between them without duplication.

## Plans and speed

- Plan directory: `docs/plan/`.
- Plan filename: `<item-id-or-request-slug>.md`.
- Existing relevant plan: reuse unless the user requests direct implementation
  or the plan is no longer applicable.
- No usable plan: `ask` (alternatives: `plan` or `direct`).
- Planning method and approvals: governed by the current model/harness.
- Fast mode trigger: an explicit per-task request such as "go fast".
- Fast mode without a plan: `direct`.
- Fast mode missing item: inherit the inventory preference above.
- Fast mode still requires repository validation and user approval to merge.
- Task overrides expire with the task; persist changes only when requested.

## Durable progress

- Ledger/handoff location: the authoritative item's fields/activity or local
  item section; no separate ledger required.
- Untracked task handoff: feature PR description, or the repository's existing
  checkpoint before a PR is available.
- Record: scope/acceptance, branch/worktree, PR, plan or direct choice,
  verification results, blockers, review state, and next action.
- Completion rule: merged to the configured feature target with required
  acceptance and checks satisfied. Adapt if delivery requires a later release.
- Local post-merge evidence: conditional completion entry in the feature PR
  plus its live merge state; reconcile literal merge facts on the next normal
  work branch or through existing authorized automation.

## Release integration

- Release contract owner: `.agents/skills/loopship/config.md` when installed,
  otherwise the repository's existing release rulebook; link the actual owner.
- Boundary: LoopDev owns feature work and integration review/merge; the release
  owner governs promotion, builds, distribution, publication and acceptance.
- Handoff location: existing item/PR/progress record, not a separate backlog.
- Handoff fields: candidate SHA, version/build where applicable, item/PR,
  verification, remaining acceptance, requested release action/target and
  already granted authorization.
- Completion/status mapping: distinguish implemented/merged from
  deployed/distributed/accepted when the work item's acceptance requires it.

## Repository delivery rules

Resolve these entries from repository evidence during setup; replace the
descriptions with concrete paths, branches, methods, and commands. Ask only
when a consequential rule cannot be established.

- Rules: link to the applicable `AGENTS.md`, contribution, CI, and release docs.
- Feature branch convention: use the repository's existing naming convention.
- Feature PR target: the repository's integration branch (`main`, `dev`, or
  another established target).
- Required validation: the repository's commands and CI checks for the change.
- Required version/changelog changes: include in the feature PR when applicable.
- User review/testing: PR description includes results and concrete test steps;
  provide a preview when the repository supports one.
- Merge authorization: user's green light for the delivered PR, with required
  checks/reviews satisfied; CI success or fast mode alone is insufficient.
- Merge method: the repository's permitted/preferred merge, squash, or rebase.
- Promotion/release flow: link the owning release contract and summarize only
  the feature handoff obligation; do not duplicate its mutable release policy.
  Without a separate owner, record the existing repo flow; use `none` if absent.
- PR scope: one feature PR includes tracking, plan, implementation, required
  version changes, and ledger updates; no administrative follow-up PRs.

## Discovery and migration

- Auto-read entrypoint: root `AGENTS.md` or the harness's existing equivalent,
  pointing here and to the authoritative inventory/progress record.
- Archive directory: `docs/archive/loopdev/<migration-id>/`.
- Migration index: archive `index.md` with sources, destinations, and status.
- Compatibility: none unless explicitly requested by the user.
- Migration status: record completed cutover or specific unresolved consumers
  and external cleanup; archive superseded instructions and update live links.
