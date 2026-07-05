# Repo Adaptation

Use this reference when applying the workflow to a repo that is not already shaped like the source example.

## Inspect First

Before proposing changes, inspect:

- Git status and branch.
- Existing `README`, `AGENTS`, product/roadmap docs, changelog, release docs, contribution docs, and public-facing release notes.
- Package manifests, build files, CI workflows, deployment files, hosting config, and PR templates.
- Version sources: package manifests, `version.txt`, Gradle/Maven files, Cargo manifests, deployment versions, tags, or release workflows.
- Existing tag format, release channels, recent commit messages, and deployment/release cadence.

Do not ask where these files are until targeted inspection fails.

## Preserve Existing Truth

Adapt to existing names and conventions unless they are missing or clearly incomplete. Do not replace meaningful docs without showing the intended change. Never revert unrelated user changes.

## Map Existing Docs Into The Hierarchy

Before creating any hierarchy file, check whether its content already lives somewhere and fold it in rather than duplicating:

- `ROADMAP`, `VISION`, `MISSION`, or strategy docs → durable content into `PRODUCT.md`; execution detail into `docs/sprints/` and `docs/releases/`.
- Style guides, design docs, UX notes → `DESIGN.md` (only if the product has UI).
- Existing `CONTRIBUTING`, `AGENT`, or bot-instruction files → route from `AGENTS.md`; keep `CLAUDE.md` a thin pointer.
- Existing release/deploy runbooks → `docs/releases/README.md`.
- Never overwrite an existing root `README.md`, `AGENTS.md`, or `CLAUDE.md` — audit against `doc-hierarchy.md` and patch the gaps.

## Common Repo Shapes

- Single app/service: one product stream, deployment-focused validation, optional versioning.
- Library/SDK: API compatibility, changelog discipline, package publishing, docs generation.
- Public plugin/artifact repo: artifact builds, admin/operator notes, tags, and GitHub or registry release channels.
- Private SaaS/platform: deployment records, customer-facing changelog/blog/social copy, internal rollback/audit trail.
- Monorepo: module/package-specific backlog items, versions, validation commands, release targets, and mixed release channels.
- Local-only repo: keep release workflow documentation, but omit hosted PR/CI pieces unless requested.
- Non-GitHub repo: adapt PR template and release automation to the host; keep the same concepts.

## Defaults To Offer

When preferences are unknown and not discoverable, recommend:

- Backlog under `docs/sprints/backlog.md`.
- One-week lightweight Scrum.
- `CHANGELOG.md` as release history or internal release notes.
- Per-version scope contracts under `docs/releases/vX.Y.Z.md`.
- Conventional Commits: `type(scope): summary`.
- PR-first delivery when the repo already uses hosted review.
- Release prep PR before tags, deploys, package publishes, or public changelog posts.
- Versioning source already used by the repo.
- No GitHub Release automation unless the release profile includes downloadable artifacts or GitHub-hosted releases.

Record chosen defaults in docs and sprint assumptions.
