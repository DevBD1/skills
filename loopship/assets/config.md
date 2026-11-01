# LoopShip project contract

Template only. Adapt into the target repo at `.agents/skills/loopship/config.md`; replace unresolved values with verified facts or mark them `unresolved` / `not applicable`. Do not execute template values. Keep this file concise and link detailed owning contracts. Never include secret values.

## Identity and authority

- Profile: mobile / web / mixed
- Repository and component paths:
- Product/application identity (bundle/package/store IDs where relevant):
- Owning release, development and acceptance documents:
- Last verified date and evidence links:
- Installation state: draft / implemented / qualified; list outstanding activation prerequisites

## Development integration and discovery

- Auto-read binding: root `AGENTS.md` or the existing harness entrypoint:
- Development owner: `.agents/skills/loopdev/config.md` if installed, otherwise
  existing work/review instructions; reference instead of copying the backlog:
- Feature target/review rules: link to development owner:
- Release handoff and receipts location: existing issue/PR or release log:
- Required handoff: exact candidate SHA, item/PR, version/build if applicable,
  checks, remaining acceptance, target/action and existing authorization:
- Completion mapping: implementation merge vs distribution/publication/acceptance:
- Reconfiguration: record durable preferences here; per-task overrides expire
  unless explicitly persisted. Repeat setup reuses existing resources/workflows.

## Branches and promotion

- Development, staging and production branches:
- Forward edges and merge strategies:
- Descending reconciliation/back-sync policy:
- Required checks and source freshness rules:
- Release/version bump owner and authoritative version source(s):

## Environments

Repeat this block per environment and independently deployable component.

### Environment / component

- Source branch and deployable revision policy:
- Frontend target or mobile runtime/distribution channel:
- Backend API/Worker target, provider account and resource identity:
- App/build profile, environment selector and update channel if applicable:
- Existing artifact discovery, exact selection/reuse and retry procedure:
- Commands with working directories (verify, run, build, deploy/upload, smoke check):
- Trigger for each command; path/version gates:
- Execution policy: automatic workflow actions vs actions requiring task authorization
- Required secret names, environment scopes and secure provisioning route:
- Required checks and human/device acceptance:
- Rollback/recovery command or runbook and data compatibility limits:
- Evidence location and current qualification state:

## Version and source publication

- Release trigger (for example a marketing-version increase reaching main):
- Version comparison source and allowed version semantics:
- Tag pattern, immutable source SHA rule and release title:
- GitHub Release workflow, artifact files and manifest format:
- Latest/prerelease policy and concurrency handling:
- Retry and explicit historical backfill entrypoints:
- Binary/deployment version association (web may use commit identity):

## Release content

- Previous/current source range resolution:
- Authoring location and reviewer/approval process:
- GitHub notes, What's New and What to Test sources/outputs:
- Locales, channel limits and preview/validation commands:
- Metadata target selection and dry-run/apply entrypoints:
- Store upload, review submission and public publication policy:

## Activation and evidence

- Implemented local/CI checks and results:
- Live-qualified integrations and exact receipts:
- Unresolved prerequisites and affected operations:
- Deliberately manual steps and acceptance owner:
