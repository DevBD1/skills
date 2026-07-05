# Release Models

Use this reference before standardizing commits, PRs, versioning, release contracts, changelog movement, tags, release notes, deployment records, or release automation.

## Release Scope Contracts

Each planned version gets a contract file, `docs/releases/vX.Y.Z.md`, created from `assets/templates/docs/releases/templates/release.md`. A contract defines:

- **Includes / excludes:** the scoped feature set and explicit non-goals for the version.
- **Acceptance criteria:** observable outcomes that must hold before the version can ship.
- **Lifecycle status:** `Draft` (scope forming) → `Committed` (scope locked, work underway) → `Shipped` (published); `Cancelled` if abandoned.
- **Launch gate:** the checklist that must pass during release prep — validation green, changelog finalized, version source bumped, publish channel ready.

Contracts are forward-looking scope; `CHANGELOG.md` is backward-looking shipped history. During release prep the changelog section is finalized from `Unreleased`, the contract's launch gate is satisfied, and after publishing the contract flips to `Shipped`. Keep the contract index in `docs/releases/README.md` current.

## Commits And PRs

Default commit format:

```text
type(scope): summary
```

Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `ci`, `chore`, `release`.

Scopes should come from real modules, packages, apps, or repo areas. Do not invent scopes that do not map to repo structure.

PRs should include summary, changed areas, sprint/backlog link, validation, changelog impact, release/version impact, config/permission or migration impact, release channel impact, and risks/follow-ups.

## Release Profiles

Choose the smallest model that matches repo reality:

- Public library or package: SemVer source, compatibility notes, package publish, tag, and optional GitHub Release.
- Public plugin or downloadable artifact: artifact build, tag, release notes, and per-module or per-artifact versions when needed.
- Private app or SaaS: deployment record, operator notes, platform changelog, blog/social/customer-facing copy, and optional internal tag.
- Internal tool: sprint record, internal changelog, deployment or handoff notes, and optional tag.
- Local-only repo: planning and changelog docs only unless the user asks for hosted PRs or releases.
- Monorepo or mixed repo: per-package release channels when artifacts ship independently; coordinated release notes when users experience one product.

Ask the user before choosing between GitHub Releases, package publishing, deployment-only release records, and external changelog channels when the repo does not make this obvious.

## Versioning

Choose the smallest model that matches the release profile:

- Repo-wide version: one app/package release stream.
- Per-package or per-module version: monorepos and independent artifacts.
- Deployment version: SaaS/private apps that track deployed revisions.
- Date or changelog-only release: products without user-visible binary/package versions.
- Hybrid: independent package versions with coordinated platform release notes.

Prefer SemVer when there is no stronger existing convention and a versioned artifact is published:

- Stable: `X.Y.Z`
- Prerelease: `X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, `X.Y.Z-rc.N`

## Changelog And Release Notes

Use `Unreleased` for work not shipped yet. During release prep, move relevant entries into a final release section or external release-note draft and link producing sprint docs.

Keep changelog as release history, not an implementation diary. Sprint docs hold delivery details.

For SaaS or private apps, record both internal changes and external publication channels when applicable: platform changelog, blog, customer email, docs update, social post, or internal announcement.

## Release Prep

Use a release prep PR by default when the repo uses PRs:

1. Confirm release-relevant work is represented in sprint docs and the version's release contract.
2. Finalize changelog entries or external release-note draft; link the contract.
3. Update the version source if the release profile has one.
4. Run relevant validation and satisfy the contract's launch gate.
5. Merge to the release branch.
6. Publish through the chosen release channel, then set the contract status to `Shipped`.

## Tags And Automation

Use existing tag formats if present. If none exist and tags are part of the release profile, choose a clear format:

- Repo-wide: `v<version>` or `<repo-name>-v<version>`.
- Per-module: `<repo-name>-<module-slug>-v<version>`.
- Deployment/internal: use tags only when they help rollback, audit, or external traceability.

Release automation should validate the version source when one exists, fail if a tag exists, build only intended artifacts, and publish from the configured release branch. Do not add GitHub Release automation for deployment-only, changelog-only, or local-only repos unless the user explicitly chooses it.
