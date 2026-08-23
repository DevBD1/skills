# Operating Model

Use this reference when setting up, adapting, or running a LoopScrum
workflow. Keep the local repository's names and commands; the shapes below are
portable patterns distilled from WickdAlgo's `wickd-ops` loop.

## The control loop

```text
repository truth
      ↓
read durable state → assert environment → reconcile proofs and drift
      ↓
resume active slice ───────────────┐
      │                            │
      └ if none: derive eligible work from authored priority + dependencies
                                   ↓
                         decide → implement → prove → commit
                                   ↓
                   review/CI/land → harvest durable state
                                   ↓
                         checkpoint → next wake or next row
```

The loop is continuous. A backlog is an inventory and a priority surface, not
a sprint commitment. The active slice is the only work selected at a time.

### Mapping from sprint workflows

| Sprint-oriented artifact | Loop-engineering replacement | Preserve |
| --- | --- | --- |
| Backlog | Work ledger plus authored priority | Item history and acceptance |
| Sprint commitment | One active slice | Scope and ownership, without a calendar boundary |
| Sprint work log | Ledger row, project record, PR, and commit | Decisions and actual verification |
| Sprint review/retro | Harvest and checkpoint | What shipped, what failed, and the next action |
| Sprint planning ceremony | Reconciliation plus dependency-derived selector | Human priority decisions and explicit blockers |

Keep release contracts and changelogs when they are part of the product's
delivery model. They describe what ships and what shipped; they do not need to
become a second execution queue.

The same applies to process tooling. If a selector, trace checker, or release
script still reads sprint-shaped files, that is a migration dependency. Keep a
small compatibility shape or replace the parser in a separate, verified slice;
do not remove the files or skip the check merely because the new operating
model has no calendar sprint.

## Minimum state model

Adapt existing files before creating new ones. A useful mapping is:

| Concern | Durable shape | What belongs there |
| --- | --- | --- |
| Inventory | `goal.md`, roadmap, issue ledger, or equivalent | Deliverable ID, scope, repo, lifecycle status, dependencies, blockers, acceptance, proof, PRs, review state |
| Current work | `active-task.md` or equivalent | One row, slice boundary, branch/worktree, remaining criteria, decisions, blockers, verification, next action |
| Why | `project-record.md`, ADRs, or equivalent | Invariants, maintainer decisions, architectural boundaries, drift resolutions |
| Machine facts | `local-state.md` or equivalent | Environment variables, service/container state, ports, scratch locations; untracked and secret-free |
| Boot contract | `prompt.md`, runbook, or equivalent | Read order, environment assertions, reconciliation, selection, verification, handoff, stop conditions |
| Repository rules | `AGENTS.md` or equivalent | Ownership, local commands, protected actions, contribution and release boundaries |

Do not make the active file a chat transcript. If a fact matters after the
slice, harvest it into the ledger, project record, backlog item, changelog, or
release contract before resetting the checkpoint.

### Ledger rows

The exact schema is repository-specific, but the row must answer:

- What deliverable is being claimed, and where does it live?
- What status vocabulary is allowed?
- What must be complete first (`Deps`)?
- What external decision or resource blocks it (`Blockers`)?
- What observable acceptance makes it complete?
- Which command re-establishes the claim (`Proof`)?
- Which branch, commit, PR, release contract, and review facts support it?

Keep authored priority separate from derived eligibility. A selector may use
the first eligible item in an ordered list, but it should refuse when the
authored order contradicts the dependency graph. Do not solve that refusal by
silently editing the order or selecting a less convenient row.

Prefer a single row per deliverable. Split a row when implementation, API
serving, client adoption, deployment, or human review have different finish
lines; otherwise `built` can hide an unserved or unverified boundary.

### Active-task checkpoint

Keep the checkpoint bounded and machine-readable. At minimum record:

1. the ledger row and slice;
2. repository, branch/worktree, and ownership;
3. remaining acceptance criteria;
4. completed verification and its actual counts/results;
5. blockers and manual actions;
6. the next action, including the exact external condition to wait for;
7. forbidden actions that would violate the current boundary.

One writer owns a tree. If a delegated agent writes product code, the
orchestrator still verifies the diff, gates, review, CI, and durable state. Do
not let two agents share a worktree or let a delegated self-report become a
ledger fact.

## Cold start and reconciliation

Use the repository's declared read order. If it has none, establish one before
operating:

1. inventory/goal;
2. active checkpoint in full;
3. durable invariants and maintainer decisions;
4. machine-local state;
5. the target repository's `AGENTS.md`.

Then, before selecting or resuming work:

1. assert required services, environment variables, credentials' presence
   (never print secret values), ports, and clean ownership;
2. run the proof for the active row, its dependencies, and recently touched
   rows;
3. run self-tests for the orchestration scripts and state checks for proof,
   PR, trace, and floor health;
4. compare live repository evidence with the ledger and record drift;
5. run the handoff/checkpoint validator;
6. resume the active row, or run the selector.

In the WickdAlgo model, the corresponding checks are:

```text
python3 scripts/selftest.py
python3 scripts/trace.py --all --gaps-only
python3 scripts/status.py --proofs
python3 scripts/status.py --prs
python3 scripts/check_floors.py --audit
python3 scripts/handoff.py
python3 scripts/select_task.py
```

Use those only when operating `wickd-ops` or a repository with the same
scripts. For another repository, map each check to its local equivalent.

Do not close every audit gap at boot. Close gaps on rows in play; record the
rest for a deliberate audit slice. If the environment cannot prove that a
green result is meaningful, stop rather than treating a smaller suite or stale
host as success.

## Slice boundaries and proof integrity

Choose a boundary that can be understood and reverted independently. A good
slice normally has one decision, the implementation and tests for that
decision, the smallest relevant gate, and a commit. Cross-repository slices
are sequential when one repository publishes an artifact consumed by another.

Before claiming a proof:

- resolve the tree and command it names;
- verify the test filter matched and ran the intended cases;
- run with every required service/variable and report what actually ran;
- prefer a gate that turns red when the claimed behavior is broken;
- perturb the gate after committing when the repository has a perturbation
  harness; investigate and fix any perturbation that remains green;
- update floors or test-count baselines with the test change, including why.

A proof is not made stronger by a larger unfiltered suite. A proof that can
pass when its test disappears, its filter is swallowed, or its environment
silently skips is not a proof.

## Landing and harvesting

Use the repository's normal PR and release path. For an implementation slice,
the usual order is:

1. commit the product slice on its feature branch;
2. run the final local gates from a clean tree;
3. obtain the required independent review and CI;
4. address findings that identify real defects;
5. merge only where the local contract authorizes it;
6. record the durable facts: work item, PR/merge SHA, tests and counts,
   changelog/release contract, and any new invariant or decision;
7. regenerate derived roll-ups and validate the checkpoint;
8. commit the orchestration-state checkpoint.

Documentation-only work may have a different review rule if the repository
explicitly says so. Never let a review verdict override a failing gate.

When a row is complete, record the proof and remove it from the authored
priority queue only after the repository and ledger agree. When it is not
complete, leave the exact next action and do not start a second slice in the
same checkpoint.

## Stop and continue rules

Record a blocker on the row and active checkpoint, then continue to another
eligible row when possible for:

- a product or maintainer decision not yet made;
- a credential or external review only the maintainer can supply;
- a dependency that is not yet published;
- three consecutive failures of the same gate, after recording literal output.

Halt the entire loop for an unknown writer or unowned dirty tree, an
unverifiable environment, an unresolved contradiction between repository truth
and the durable model, or an irreversible/billable action that lacks explicit
authorization. A stop condition should be proportional to the risk; do not
turn a normal waiting state into a global halt.

## What to carry forward from WickdAlgo

The most valuable patterns are boundaries, not filenames:

- the repository wins over stale status prose;
- a dataset/cache identity is not the same as a run or a local alias;
- producer implementation, API serving, client adoption, deployment, and
  maintainer eyeball are separate claims;
- `agent-checked` and maintainer `signed-off` are different states;
- a durable decision belongs in the project record, while a volatile next
  action belongs in the active checkpoint;
- a blocked item does not starve independent work;
- every durable claim needs a re-establishing command.
