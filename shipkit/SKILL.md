---
name: shipkit
description: Set up, audit and operate project-specific mobile and web release workflows, including dev/stage/main promotion, release notes, GitHub Releases and delivery checks. Use when establishing a release pipeline or preparing, promoting or shipping a version.
---

# Shipkit

Make releases repeatable while keeping the project's actual environment, branching and delivery contracts explicit. Support mobile, web and repositories containing both. Reuse existing infrastructure; do not assume Expo, Cloudflare or a particular hosting provider.

## Project contract

Read repository instructions and existing release/development documentation first. Read `.shipkit/config.md` if present. The skill's [config.md](config.md) is a template: on installation, adapt it into the target repository as `.shipkit/config.md`. Never store project decisions in this shared skill installation. Link existing owning documents instead of copying competing rules. Add a short pointer to the project contract in its agent instructions or documentation index when appropriate.

Treat the project config as reviewed intent, not proof of live state or permission. Compare consequential settings with actual workflows, manifests and provider configuration. Reconcile drift explicitly. Keep secret values outside tracked files; record only names, scopes and provisioning instructions.

## Choose the operation

### Set up or repair

1. Inspect current branch/status, remotes, release history, version sources, workflow triggers, package scripts, backend resources and frontend/build profiles. Preserve unrelated work. Detect monorepo components independently.
2. Map `dev`, `stage`, `main` and their real equivalents. Discover environment URLs and resource identities from owning sources without printing credentials. Record confirmed facts, intentional omissions and unresolved prerequisites separately. Do not invent domains, app IDs or executable commands.
3. Read the applicable [web](references/web.md) or [mobile](references/mobile.md) profile, plus [automation](references/automation.md) when wiring CI. The profile is a starting proposal, not authority to replace an established project convention.
4. Populate `.shipkit/config.md` from the template, removing irrelevant sections. Capture exact commands, working directories, triggers, source identity, verification, rollback, notes ownership and activation state. Unresolved deploy targets or credentials block only dependent activation; continue independent setup.
5. Implement the scoped scripts/workflows and documentation in the repository. Prefer existing commands and provider integrations. Avoid copying project-specific Gyrolog scripts, IDs or assumptions into another app. Installation does not itself authorize a live deployment, billable build, merge, publication or secret provisioning. Honor authorization already given for those actions.
6. Validate config-to-code consistency, workflow syntax and meaningful failure paths. Use dry-runs or local previews when available. Report what is installed, what was executed and what still needs activation. Do not label an unexercised live integration verified.

### Prepare a release

Read [notes](references/notes.md). Resolve explicit previous/current source SHAs and release scope. Draft user-facing changes and actionable testing instructions from actual changes; commit them with the release preparation/version bump where the project requires it. Check version consistency and show rendered previews. Keep unresolved claims visible for review.

### Promote or ship

Read the applicable web/mobile profile; also read [automation](references/automation.md) before source publication, retry or backfill. Use the configured environment, component and exact source revision. Check working-tree state, upstream freshness, required checks and environment-specific gates. Execute only actions covered by the current request or existing authorization; ask only when an additional action actually needs it. Promotion, binary build, store upload, metadata update and public-store submission are distinct actions.

Follow configured merge strategy and release triggers. Verify each requested outcome using provider receipts and source/build identity. A GitHub Release proves source publication; a successful build proves artifact creation; neither proves deployment health or device acceptance. Record remaining human checks without fabricating success.

### Audit or close out

Compare desired triggers with recent runs and provider state. Distinguish missing trigger, skipped gate, failed job, credential gap and publication gap. A missing historical release should be recovered only through an explicit version/SHA backfill, without bumping the version to retrigger unrelated work. Persist decisions in the config and receipts in the project's issue/PR or existing release log. Report source publication, deployment, store delivery and acceptance separately.
