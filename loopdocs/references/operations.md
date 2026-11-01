# Documentation updates and audits

Read only the sections needed for the requested documentation work.

## Update the owning document

Inspect the changed behavior or decision and find its existing owner using
the document map. Update that owner and affected entrypoints in the same work
item/PR as the change when possible. For documentation-only tasks, follow the
repository's normal contribution rules; do not invent a separate tracker or
bookkeeping PR.

Match evidence to the claim:

| Claim | Evidence |
| --- | --- |
| Setup, runtime, commands | Manifests, scripts, config names, safe local smoke check |
| Product direction or non-goals | Established product decisions or explicit user direction |
| Current architecture, API or data flow | Code, schema/specification and relevant tests |
| Intended UX or visual rules | Approved design source, tokens or recorded decisions |
| Work status | LoopDev's configured work inventory and actual PR state |
| Release/deployment status | LoopShip's provider/CI receipts and source/build identity |

Do not derive a product policy from an implementation accident, invent missing
release facts, or replace design intent with current behavior by assumption.
Keep unknown claims visibly unresolved and ask only when the distinction
changes the requested result.

## Audit scope

Start with the reader paths affected by the request; broaden only when the
user asks for a repository-wide audit or evidence shows wider drift.

Check:

- A fresh reader can find the overview, setup, common commands and owning docs.
- Commands, paths, environment names and examples agree with current sources.
- Product intent, current architecture and UX intent are labeled accurately.
- Rules have one owner; indexes and adapters route there without duplication.
- `docs/` areas follow the [docs layout](docs-layout.md) or an established
  equivalent: reader guides, reference material, architecture, operations and
  temporary plans have clear boundaries. Active entrypoints distinguish
  current guidance from proposals and historical material.
- Local links and heading anchors resolve, including inbound links after moves.
- Optional documents are useful rather than empty scaffolding; generated docs
  are updated through their source/generator instead of patched by hand.
- Release claims distinguish pending, merged, published and accepted delivery.
- No credentials, machine-specific paths, stale placeholders or broken images
  leaked into public documentation.

Report actionable findings with file locations, evidence and reader impact.
An audit-only request ends with findings; when repairs are requested, apply
evidence-backed fixes and report unresolved decisions separately.

## Validate changes

Run `git diff --check`, validate local relative links/anchors using existing
tooling or targeted inspection, and review the final diff/status for unrelated
changes. For new setup or command examples, use the smallest safe local smoke
check justified by the change. Never execute a deployment, publication, secret
provisioning or other external mutation just to verify documentation without
existing authorization.

Check that README and agent entrypoints discover new owners and that obsolete
active instructions are removed after a migration. Resolve template placeholders
in installed output; placeholders intentionally remain in this skill's reusable
templates. Report commands actually run and unverified examples plainly.
