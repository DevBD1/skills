# Release Workflow

This repository releases from main/trunk through release prep, versioning, tags, artifacts, and release notes.

For the full idea-to-release flow, see `../development-cycle.md`.

## Versioning

- Version source: `<version-source>`.
- Stable versions use `X.Y.Z` unless the repo already uses another convention.
- Prereleases use `X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, or `X.Y.Z-rc.N`.
- Change versions in release prep PRs, not ordinary feature or fix PRs.

## Release Prep PR

1. Confirm release-relevant work is represented in `docs/sprints/`.
2. Move relevant `CHANGELOG.md` entries from `Unreleased` into the final release section.
3. Update `<version-source>`.
4. Run `<validation-command>`.
5. Merge the release prep PR to main/trunk.

## Tags And Releases

Tag format:

```text
<tag-format>
```

Publish releases using this repo's CI/CD or release tooling. Release automation should validate the version source, fail if the tag exists, build intended artifacts, and publish from main/trunk.
