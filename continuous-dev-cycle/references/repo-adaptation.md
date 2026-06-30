# Repo Adaptation

Use this reference when applying the workflow to a repo that is not already shaped like the source example.

## Inspect First

Before proposing changes, inspect:

- Git status and branch.
- Existing `README`, `AGENTS`, product/roadmap docs, changelog, release docs, and contribution docs.
- Package manifests, build files, CI workflows, deployment files, and PR templates.
- Version sources: package manifests, `version.txt`, Gradle/Maven files, Cargo manifests, tags, or release workflows.
- Existing tag format and recent commit messages.

Do not ask where these files are until targeted inspection fails.

## Preserve Existing Truth

Adapt to existing names and conventions unless they are missing or clearly incomplete. Do not replace meaningful docs without showing the intended change. Never revert unrelated user changes.

## Common Repo Shapes

- Single app/service: one product version, one release stream, app-specific validation.
- Library/SDK: API compatibility, changelog discipline, package publishing, docs generation.
- Monorepo: module/package-specific backlog items, versions, validation commands, release targets.
- Local-only repo: keep release workflow documentation, but omit hosted PR/CI pieces unless requested.
- Non-GitHub repo: adapt PR template and release automation to the host; keep the same concepts.

## Defaults To Offer

When preferences are unknown and not discoverable, recommend:

- Backlog under `docs/sprints/backlog.md`.
- One-week lightweight Scrum.
- `CHANGELOG.md` as release history.
- Conventional Commits: `type(scope): summary`.
- PR-first delivery.
- Release prep PR before tags.
- Versioning source already used by the repo.

Record chosen defaults in docs and sprint assumptions.
