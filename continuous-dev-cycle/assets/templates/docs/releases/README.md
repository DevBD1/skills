# Release Workflow

This repository releases through the selected release profile: tags, artifacts, package publishing, deployments, external changelog posts, or internal release notes.

For the full idea-to-release flow, see `../development-cycle.md`.

## Release Profile

- Visibility: public, private, internal, local-only, or mixed.
- Audience: developers, admins/operators, end users, customers, internal team, or mixed.
- Release channel: GitHub Release, package registry, deployment, platform changelog, blog/social/customer announcement, PR merge only, or custom.
- Release branch: `<release-branch>`.

## Versioning

- Version source: `<version-source>`.
- Version read command: `<version-read-command>`.
- Stable versions use `X.Y.Z` unless the repo already uses another convention.
- Prereleases use `X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, or `X.Y.Z-rc.N` when versioned artifacts are published.
- Change versions in release prep PRs, not ordinary feature or fix PRs.

## Release Prep PR

1. Confirm release-relevant work is represented in `docs/sprints/`.
2. Move relevant `CHANGELOG.md` entries from `Unreleased` into the final release section or external release-note draft.
3. Update `<version-source>` when this release profile has a version source.
4. Run `<validation-command>`.
5. Merge the release prep PR to `<release-branch>`.
6. Publish through the selected release channel.

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
