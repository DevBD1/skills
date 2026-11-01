---
name: loopship
description: Set up, audit and operate project-specific mobile and web release workflows, including dev/stage/main promotion, release notes, GitHub Releases and delivery checks. Use when establishing a release pipeline or preparing, promoting or shipping a version.
---

# LoopShip

Make releases repeatable while keeping the project's actual environment, branching and delivery contracts explicit. Support mobile, web and repositories containing both. Reuse existing infrastructure; do not assume Expo, Cloudflare or a particular hosting provider.

## Project contract

Read repository instructions and existing release/development documentation first. Read `.agents/skills/loopship/config.md` if present. The skill's [assets/config.md](assets/config.md) is a template: on installation, adapt it into the target repository as `.agents/skills/loopship/config.md`. Never store project decisions in this shared skill installation. Link existing owning documents instead of copying competing rules. Install a short binding in root `AGENTS.md` or the harness's existing auto-read instructions, pointing to this config and the owning release rules. Update existing active entrypoints instead of multiplying instruction files. The binding must let a cold-starting agent discover the release workflow even when the global skill is unavailable.

Treat the project config as reviewed intent, not proof of live state or permission. Compare consequential settings with actual workflows, manifests and provider configuration. Reconcile drift explicitly. Keep secret values outside tracked files; record only names, scopes and provisioning instructions.

## Development and release boundary

LoopShip owns release preparation, environment topology, promotion, build and distribution, source publication, channel metadata, rollback and delivery evidence. LoopDev owns work lookup, plans, feature implementation/validation, the feature PR and its authorized integration merge. Read the companion config at `.agents/skills/loopdev/config.md` when present; neither skill requires the other to be installed.

Keep promotion methods, environment gates and version/publication policy here or in linked release contracts. LoopDev should reference those owners rather than copy them. Release preparation may update version/changelog/notes in a single prep PR; reuse an existing work item, branch and PR when that scope already exists. Do not open a second PR merely because control passes between skills. Implementing new release infrastructure is development work that can use LoopDev's configured review flow; executing that infrastructure follows LoopShip's release contract.

A handoff records the work item/PR if any, exact candidate source SHA, version/build where relevant, completed checks, outstanding acceptance, requested target/action and existing authorization. Validate the candidate after any change. Do not infer release permission from the handoff or feature merge. Existing authorized CI may run on that merge; inspect its receipts before scheduling duplicate work. Record delivery separately from implementation completion. Route discovered product defects through the existing work inventory according to its mutation policy; do not create a parallel release backlog.

## Choose the operation

### Set up or repair

For an existing installation, read the saved config first and repair only demonstrated drift or requested changes. For a rename migration, use [migration](references/migration.md). Do not restart setup or ask resolved preferences on every run.

1. Inspect current branch/status, remotes, release history, version sources, workflow triggers, package scripts, backend resources and frontend/build profiles. Preserve unrelated work. Detect monorepo components independently.
2. Map `dev`, `stage`, `main` and their real equivalents. Discover environment URLs and resource identities from owning sources without printing credentials. Record confirmed facts, intentional omissions and unresolved prerequisites separately. Do not invent domains, app IDs or executable commands.
3. Read each applicable profile: [web](references/web.md), [mobile](references/mobile.md), or both for mixed repositories, plus [automation](references/automation.md) when wiring CI. The profile is a starting proposal, not authority to replace an established project convention.
4. Populate `.agents/skills/loopship/config.md` from the template, removing irrelevant sections. Infer established technical conventions; ask only for consequential unresolved choices before dependent work. A one-task override stays temporary unless the user asks to persist it. Capture exact commands, working directories, triggers, source identity, verification, rollback, notes ownership and activation state. Unresolved deploy targets or credentials block only dependent activation; continue independent setup.
5. Implement the scoped scripts/workflows and documentation in the repository. Prefer existing commands and provider integrations. Avoid copying project-specific Gyrolog scripts, IDs or assumptions into another app. Installation does not itself authorize a live deployment, billable build, merge, publication or secret provisioning. Honor authorization already given for those actions.
6. Validate config-to-code consistency, workflow syntax, cold-start discovery and meaningful failure paths. Repeat setup should reuse the same config and workflows without duplicates. Use dry-runs or local previews when available. Report what is installed, what was executed and what still needs activation. Do not label an unexercised live integration verified.

### Prepare a release

Read [notes](references/notes.md). Resolve explicit previous/current source SHAs and release scope. Draft user-facing changes and actionable testing instructions from actual changes; commit them with the release preparation/version bump where the project requires it. Check version consistency and show rendered previews. Keep unresolved claims visible for review.

### Promote or ship

Read every applicable web/mobile profile (both for mixed repositories); also read [automation](references/automation.md) before source publication, retry or backfill. Use the configured environment, component and exact source revision. Check working-tree state, upstream freshness, required checks and environment-specific gates. Execute only actions covered by the current request or existing authorization; ask only when an additional action actually needs it. Promotion, binary build, store upload, metadata update and public-store submission are distinct actions.

Follow configured merge strategy and release triggers. Verify each requested outcome using provider receipts and source/build identity. A GitHub Release proves source publication; a successful build proves artifact creation; neither proves deployment health or device acceptance. Record remaining human checks without fabricating success.

### Audit or close out

Compare desired triggers with recent runs and provider state. Distinguish missing trigger, skipped gate, failed job, credential gap and publication gap. A missing historical release should be recovered only through an explicit version/SHA backfill, without bumping the version to retrigger unrelated work. Persist decisions in the config and receipts in the project's issue/PR or existing release log. Report source publication, deployment, store delivery and acceptance separately.
