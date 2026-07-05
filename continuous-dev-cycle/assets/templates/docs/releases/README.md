# Release Workflow

This repository releases through the selected release profile: tags, artifacts, package publishing, deployments, external changelog posts, or internal release notes. Each planned version gets a scope contract file in this directory.

For the full idea-to-release flow, see `../development-cycle.md`.

## Release Profile

- Visibility: public, private, internal, local-only, or mixed.
- Audience: developers, admins/operators, end users, customers, internal team, or mixed.
- Release channel: GitHub Release, package registry, deployment, platform changelog, blog/social/customer announcement, PR merge only, or custom.
- Release branch: `<release-branch>`.

## Version Contracts

Every planned version has a contract, `docs/releases/vX.Y.Z.md`, created from `templates/release.md`. A contract defines what the version includes and excludes, its acceptance criteria, and its launch gate.

Lifecycle: `Draft` (scope forming) → `Committed` (scope locked, work underway) → `Shipped` (published). Use `Cancelled` for abandoned versions. Scope changes after `Committed` are recorded in the contract's lifecycle log.

### Contract Index

| Version | Status | Target |
| --- | --- | --- |
| _No contracts yet._ | | |

## Changelog Tracking Rules

- Use `## [Unreleased]` in `CHANGELOG.md` for release-relevant work that has not shipped yet.
- Use repo-specific module, package, app, or area labels in entries.
- Link entries to the sprint docs that produced the work; link finalized release sections to their version contract.
- Keep sprint work logs in `docs/sprints/`; keep final release history in `CHANGELOG.md`.
- For SaaS or private platforms, also track external release-note channels: product changelog, blog, docs, customer email, social post, or internal announcement.

## Versioning

- Version source: `<version-source>`.
- Version read command: `<version-read-command>`.
- Stable versions use `X.Y.Z` unless the repo already uses another convention.
- Prereleases use `X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, or `X.Y.Z-rc.N` when versioned artifacts are published.
- Change versions in release prep PRs, not ordinary feature or fix PRs.

## Release Prep PR

1. Confirm release-relevant work is represented in `docs/sprints/` and the version contract.
2. Move relevant `CHANGELOG.md` entries from `Unreleased` into the final release section or external release-note draft; link the contract.
3. Update `<version-source>` when this release profile has a version source.
4. Run `<validation-command>` and satisfy the contract's launch gate.
5. Merge the release prep PR to `<release-branch>`.
6. Publish through the selected release channel, then set the contract status to `Shipped` and update the index above.

## Tags, Releases, And Publishing

Tag format, when tags are part of this release profile:

```text
<tag-format>
```

Release build command, when artifacts are published:

```sh
<release-build-command>
```

Artifact glob, when GitHub Releases or artifact uploads are used:

```text
<artifact-glob>
```

Release automation should validate the version source when one exists, fail if the tag exists, build intended artifacts, and publish from the selected release branch. Omit GitHub Release automation for deployment-only, changelog-only, or local-only repos unless explicitly chosen.

## External Release Notes

If this is a SaaS, private platform, or customer-facing app, record where release notes are published: product changelog, docs site, blog, customer email, social post, or internal announcement.
