---
name: loopscrum
description: Build, operate, or repair a LoopScrum workflow that replaces sprint-planning overhead with durable repository state, dependency-derived work selection, resumable slices, and proof-backed checkpoints. Use for continuous AI development, cold-start/handoff workflows, ledger and active-task design, process setup, or drift reconciliation; do not invoke for ordinary feature implementation unless the user asks to run or adapt the loop.
---

# LoopScrum

Treat the repository as the workflow's control plane. The unit of progress is a
small accepted slice that is implemented, verified, committed, and recorded so
a fresh agent can resume without relying on conversation memory. Do not add
calendar sprints or sprint-planning ceremonies unless the repository or user
explicitly requires them.

## Route the request

- **Establish or adapt**: inspect the repository's existing process, preserve
  its stronger conventions, and propose the smallest durable state model. Add
  or change workflow files only within the user's scope.
- **Resume or operate**: follow the repository's declared cold-start order,
  assert the environment, reconcile claims against live repositories, then
  advance the existing active slice before selecting another one.
- **Audit or repair**: run read-only drift checks first. Repair repository
  truth, broken proofs, and stale links before tightening process. Do not close
  unrelated audit gaps while an active slice is in flight.

Read [references/operating-model.md](references/operating-model.md) when
designing the state files, adapting the loop to a new repository, or operating
an iteration. Use the repository's own `AGENTS.md`, scripts, gates, and
approval boundaries as authoritative; the reference is a pattern, not a reason
to replace local rules.

When replacing a sprint-oriented workflow, keep the useful history and release
discipline: map the backlog to the work ledger, map the current sprint item to
the active checkpoint, move durable decisions and verification into the project
record and row, and keep changelogs/release contracts as landing artifacts.
Do not delete old sprint files until their links, historical purpose, and any
tooling that parses them are understood. If a selector or trace harness still
depends on sprint-shaped input, retain a compatibility layer or make replacing
that dependency its own verified slice; never bypass the harness to make the
workflow appear sprint-free.

## Non-negotiable shape

Keep these concerns separate and durable:

1. **Work ledger** — one row per deliverable, with status, dependencies,
   blockers, acceptance, implementation location, and a proof command. Keep
   priority authored in one place and eligibility derived from the row data.
2. **Active-task checkpoint** — one current slice, its branch/repository,
   acceptance still open, blockers, verification already performed, and the
   exact next action. Keep it short and resumable; it is not a session diary.
3. **Project record** — durable invariants, maintainer decisions, boundaries,
   and lessons learned. Do not bury reasoning in volatile task notes.
4. **Local-state record** — untracked machine facts such as ports, containers,
   credentials, and environment setup. Never commit secrets.
5. **Repository contract** — `AGENTS.md` or the local equivalent describing
   ownership, validation, and forbidden actions.

Use closed vocabularies where a script parses a field. Make derived roll-ups
and summaries reproducible from the ledger; never hand-count them.

## Run the loop

1. **Read the declared sources in order.** Find the repository's boot prompt or
   runbook, then read its ledger, active checkpoint, durable record, local
   state, and the target repository contract. Do not start with arbitrary
   source files.
2. **Inspect ownership and environment.** Check branches and dirty trees,
   required services and variables, and any stale process that can answer a
   request from an old build. A dirty tree owned by another writer is a
   coordination boundary, not an invitation to clean it up.
3. **Reconcile before choosing.** Run proofs for the active row, its
   dependencies, and anything touched by the previous slice. Run the
   repository's self-tests, trace/status checks, and floor/audit checks. Where
   a ledger claim disagrees with a proof against the live repository, the
   repository wins: correct the durable record and log the drift.
4. **Resume before selecting.** If the active checkpoint names work with a
   phase other than `not-started`, continue that work. Otherwise select the
   highest authored-priority row whose dependencies are complete and whose
   blockers are clear. Refuse contradictory priority/dependency data; do not
   silently choose between them.
5. **Do one slice.** Decide the smallest coherent boundary, implement it, add
   the narrowest meaningful proof, and commit the product change. Do not turn a
   row into a hidden mini-sprint.
6. **Verify from repository truth.** Run the smallest relevant gates in a clean
   tree with their required environment. Confirm that filtered commands really
   execute the intended tests, that a missing test cannot produce a false
   green, and that every new or claimed gate is perturbed when the local
   process supports perturbation. A perturbation that stays green is a finding.
7. **Land and harvest.** Follow the repository's review, CI, branch, release,
   and promotion rules. Keep merge and other durable fact-making actions with
   the orchestrator when the local contract requires it. After the slice is
   durable, update the work ledger, changelog/release contract if applicable,
   durable record, and active checkpoint; then prove the checkpoint is
   resumable.
8. **Continue or schedule.** If the row is incomplete, leave an exact next
   action. If it is complete, clear the active checkpoint and let the selector
   choose the next eligible row. If waiting on CI or another external event,
   record what is being watched and use an appropriately paced wake-up.

## Boundaries

- Keep one writer per working tree. Read-only analysis may run concurrently;
  delegated agents may produce bounded diffs or analyses, but only the
  authorized orchestrator records verified facts, runs final gates, merges,
  or changes ledger state.
- Preserve unrelated dirty work. Never reset, discard, prune, overwrite, or
  migrate data without explicit scope and a recoverable target.
- Treat maintainer decisions, credentials, production data admission, stable
  releases, `stage → main` promotion, deletion, spending, and other
  irreversible or billable acts as stop points. Prepare the work and hand it
  back rather than guessing.
- A blocked row must not block the whole loop when another eligible row exists.
  Record the blocker durably and continue. Halt the loop only for an unsafe or
  unverifiable environment, an unknown writer, an unresolved repository
  contradiction, or the local policy's explicit halt condition.
- Do not promote `agent-checked` to maintainer sign-off. Only the maintainer's
  explicit words can create a signed-off claim.

The goal is not a more elaborate planning system. It is a development process
whose state survives compaction, sleep, handoff, and model changes.
