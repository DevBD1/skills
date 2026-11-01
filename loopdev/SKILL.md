---
name: loopdev
description: Set up, migrate, or operate a repository-specific issue/backlog workflow with saved preferences, optional plans, and one feature PR per work item. Use when asked to establish or run LoopDev, or when repository instructions select it for development work.
---

# LoopDev

Make the project's work easy to find, carry out, and review. The user chooses
where issues/backlog live and how much planning a task needs. Save those
choices in the repository so future agents can work without repeating setup
questions. LoopDev coordinates development through the feature merge; planning methods belong
to the model and harness.

## Route the request

- **Set up or migrate:** inspect the current workflow, help the user choose a
  work inventory, migrate it, archive the replaced process, and install a
  discoverable repository configuration.
- **Operate or resume:** read repository instructions and configuration, find
  the requested or next work item, resolve whether to use a plan, implement,
  and deliver one feature PR for user review.
- **Repair:** reconcile configuration, tracker state, links, and actual PR
  state. Fix the affected workflow without adopting a new system by surprise.

For rename migrations, read [references/migration.md](references/migration.md).
For setup/migration or state and delivery details, read
[references/operating-model.md](references/operating-model.md). For a new
configuration, adapt [assets/config.md](assets/config.md) into
`.agents/skills/loopdev/config.md` in the target repository. This is project
configuration, not a second installed copy of the skill.

## Development and release boundary

LoopDocs is the companion documentation layer: it defines the roles, contents
and links of README, PRODUCT, DESIGN, agent instructions and supporting docs.
When documentation structure needs setup or repair, use its guidance if
available; existing repository document owners remain authoritative. Keep
documentation updates caused by a work item in that item's feature PR. LoopDocs
does not select work, add sprint records or introduce a second backlog. A routine
documentation edit does not require a separate skill handoff or installation.

When an existing content binding selects LoopCast, a noteworthy verified
development result can supply a linked content idea within the current task/PR.
LoopCast owns that capture and the content ledger. Do not require content for
every task, install a content system implicitly or block feature review/merge
on drafting a post. Keep work status in the configured inventory.

LoopDev owns the work inventory, selection, optional plans, implementation,
feature validation, user review and the authorized feature merge. LoopShip
owns release preparation, environment topology, promotion, build/distribution,
source publication, store metadata, rollback and delivery evidence. Either
skill can operate independently using the repository's owning rules.

When `.agents/skills/loopship/config.md` exists, read its relevant release
obligations and link it from the development config. Do not duplicate its
environment commands, promotion methods or publication policy. LoopDev still
includes required changelog/version inputs in the feature PR; it does not
invent a version bump for every task or publish as a side effect of completion.
Release-prep tasks can use the same inventory and PR discipline; the release
contract governs their content and execution. Changes to release automation
can be developed through LoopDev without activating it.

At release handoff, retain the item/PR, exact candidate SHA, applicable
version/build, verification, remaining acceptance, target action and existing
authorization. LoopShip checks existing CI receipts before repeating actions.
Keep merged implementation distinct from released/accepted delivery; close
work according to configured acceptance, without a second editable backlog.
A feature merge may trigger already configured CI, including deployments in a
direct-to-main project; follow those gates and report their actual results.

## Establish the workflow

1. **Inspect before proposing.** Read repository instructions, contributor
   and workflow docs, active plans, sprint records, issue/backlog files,
   automation, branch/release rules, and connected trackers where available.
   The current process may be Scrum, plan-and-implement, GitHub Issues and
   Projects, Linear, another service, a custom system, or a mixture. Identify
   active work, authoritative sources, and what depends on the old process.
2. **Offer a simple choice.** Explain the current arrangement briefly, then
   present suitable places to record problems: GitHub Issues with a GitHub
   Project, Linear, repository Markdown such as `docs/issues.md` and/or
   `docs/backlog.md`, or the user's preferred alternative. Recommend based on
   the repository; do not force a provider. The user chooses before migration.
   An explicit choice already given is sufficient; do not ask again.
3. **Save project preferences.** Record the chosen source, lookup/selection
   rules, missing-item behavior, plan preference, fast-mode behavior, durable
   progress location, validation, feature branch target, release obligations,
   and merge method. Infer established technical conventions from evidence;
   ask only for consequential choices that are still unresolved.
4. **Migrate and archive completely.** Transfer open work and useful plans to
   the chosen system. Move superseded local process material into a dedicated
   `docs/archive/loopdev/<migration-id>/` directory, preserving provenance
   and old-to-new mappings. Update active instructions, links, scripts, and CI
   consumers together. Do not leave competing workflow instructions scattered
   around the repository. Do not retain compatibility layers unless the user
   explicitly requests them. Preserve product/release rules that remain valid.
5. **Make cold starts discoverable.** Add a short binding to root `AGENTS.md`
   or the harness's existing auto-read instruction file. It must point to the
   config and describe issue lookup, plan choice, and the PR approval boundary.
   Update existing alternate entrypoints that would otherwise teach the old
   process. A config file alone is not sufficient discovery.

## Resolve preferences once

Read `.agents/skills/loopdev/config.md` at the start of work. Resolve routine
choices from the current user instruction, then saved project preferences,
then the defaults below. Follow applicable repository validation, contribution,
and release rules; clarify a real conflict instead of silently bypassing them.

Do not ask about a choice already settled by the user or config. A per-task
override, including "go fast", applies to that task; persist it only when the
user asks for a lasting change. Fast mode can skip optional planning and
ceremonies according to config, but does not imply merge approval or waive
repository gates. If fast mode is not configured, resolve only the choices
the user's wording actually settles.

## Run a work item

1. **Read and resume.** Load repository rules, config, and the configured
   progress record. Check the branch, working tree ownership, and linked
   issue/PR state. Resume a matching in-flight item when appropriate. If the
   user requests different work, preserve the existing handoff before switching.
2. **Find the problem.** For a user request, search the authoritative
   issues/backlog by meaning as well as title/ID before starting implementation.
   Reuse a matching item; avoid duplicates. If none exists, default to offering
   to create one before proceeding. The user may choose creation or direct
   implementation without an item; honor that choice. Saved authorization to
   create or proceed directly also resolves this decision. Without a specific
   request, select eligible work using saved priority, dependencies, blockers,
   and ownership. Do not invent work when the inventory is empty.
3. **Resolve the plan.** Look for a relevant plan linked from the item,
   progress record, or `docs/plan/`. Reuse an applicable plan and implement it.
   If the user explicitly requests direct implementation, proceed without a
   plan. If no usable plan exists, apply the saved preference (`plan`, `direct`,
   or `ask`); ask the user only when that decision remains unresolved. When
   planning is chosen, let the model/harness govern its process and approvals,
   and save the resulting Markdown plan at `docs/plan/<item-id-or-slug>.md`
   unless the config specifies another location. LoopDev neither prescribes
   a planning technique nor adds its own plan approval ceremony. A plan-only
   request ends with the plan and resumable state, not automatic implementation.
4. **Implement and verify.** Follow the item scope and applicable plan, using
   the repository's feature branch and validation conventions. Keep the plan,
   implementation, tests, any required version/changelog changes, and ledger
   updates on the same branch and in the same feature PR. Multiple commits or
   sessions do not require multiple PRs. Record actual verification and any
   blockers; do not claim checks that were skipped or could not run.
5. **Deliver for review.** Open or update that feature PR against the target
   established by the repo, whether `main`, `dev`, or another branch. Link the
   work item and plan, summarize behavior, provide test/review instructions,
   and update progress to awaiting review. Give the user the PR and a practical
   way to review/test it. Wait for the user's approval/green light for this PR.
6. **Finish after approval.** Apply review changes to the same PR. Once the
   user has approved and repository gates are satisfied, merge or squash using
   the repository's policy. Verify the result, update linked tracker/ledger
   state according to its completion rules, and report the merge and remaining
   release steps. Do not treat CI success as user approval or conflate merging
   to `dev` with release to production.

## Keep state small and truthful

The chosen issues/backlog system is the authoritative work inventory. Its
fields or activity can also serve as the ledger and handoff; separate ledger,
active-task, project-record, and machine-state files are not mandatory. If a
local ledger is useful, store references and delivery evidence rather than
maintaining another editable backlog. Retain enough durable state to identify
the item (or explicitly untracked task), branch/PR, plan or direct choice,
verification, blocker, review state, and next action.

Prepare repository ledger updates inside the feature PR. Describe completion
as conditional on merge while it is pending; never pre-record approval or a
merge SHA. Actual merge facts can live in the PR/tracker, approved automation,
or be reconciled on the next normal work branch. Do not open a bookkeeping PR
just to record that the feature PR merged.

One feature PR covers one coherent task, including tracking, planning,
implementation, required version changes, and ledger updates. Do not create
sequential administrative PRs for those stages. Mandatory repository promotion
or release PRs remain part of that repository's delivery flow; explain the
requirement and follow existing authorization rather than inventing extra PRs.

Preserve unrelated dirty work and other writers' ownership. If a tracker is
unavailable, report the lookup/update limitation and keep a resumable record;
do not claim a search succeeded or silently create a replacement source of
truth. Continue to another item only within the user's requested scope.
