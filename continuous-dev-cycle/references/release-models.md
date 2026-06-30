# Release Models

Use this reference before standardizing commits, PRs, versioning, changelog movement, tags, or release automation.

## Commits And PRs

Default commit format:

```text
type(scope): summary
```

Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `ci`, `chore`, `release`.

Scopes should come from real modules, packages, apps, or repo areas. Do not invent scopes that do not map to repo structure.

PRs should include summary, changed areas, sprint/backlog link, validation, changelog impact, release/version impact, config/permission or migration impact, and risks/follow-ups.

## Versioning

Choose the smallest model that matches repo reality:

- Repo-wide version: one app/package release stream.
- Per-package or per-module version: monorepos and independent artifacts.
- Hybrid: independent package versions with coordinated releases documented as separate release entries.

Prefer SemVer when there is no stronger existing convention:

- Stable: `X.Y.Z`
- Prerelease: `X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, `X.Y.Z-rc.N`

## Changelog

Use `Unreleased` for work not shipped yet. During release prep, move relevant entries into a final release section and link producing sprint docs.

Keep changelog as release history, not an implementation diary. Sprint docs hold delivery details.

## Release Prep

Use a release prep PR by default:

1. Confirm release-relevant work is represented in sprint docs.
2. Finalize changelog entries.
3. Update version source.
4. Run relevant validation.
5. Merge to main/trunk.

## Tags And Automation

Use existing tag formats if present. If none exist, choose a clear format:

- Repo-wide: `v<version>` or `<repo-name>-v<version>`.
- Per-module: `<repo-name>-<module-slug>-v<version>`.

Release automation should validate the version source, fail if a tag exists, build only the intended artifacts, and publish from main/trunk.
