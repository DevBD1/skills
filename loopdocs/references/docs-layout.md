# Organizing docs/

Use this reference when establishing or auditing the detailed documentation
tree. These paths are defaults, not required scaffolding. Reuse equivalent
existing locations, including documentation-site conventions. Create a directory
only when there is useful content for it; a small project can use a few files.

## Suggested layout

```text
docs/
  README.md
  guides/
  reference/
  architecture/
  decisions/
  runbooks/
  plan/
  releases/
  content/
  archive/
  assets/
```

Every area above is conditional. Do not install empty directories or index-only
sections for topics the project does not have.

## Contents and boundaries

| Area | When useful and what it contains | Boundary and maintenance |
| --- | --- | --- |
| `docs/README.md` | A growing doc set needs navigation: group links by reader question, identify owning entrypoints, and distinguish current docs, proposals and history | Root README links here and keeps its own quick start. Link existing documents only; do not duplicate their rules |
| `guides/` | Readers need tutorials or task-oriented instructions: prerequisites, steps, examples, expected outcomes and troubleshooting | Explain how to achieve a goal. Link exact API/config details in reference material; verify steps when supported behavior changes |
| `reference/` | Readers need precise lookup: API/CLI contracts, configuration keys, schemas, formats, supported values and compatibility | Describe current supported interfaces. Identify generated specs and update their source/generator; link rather than hand-copy generated content |
| `architecture/` | System explanations outgrow the root overview: component responsibilities, integration boundaries, data flow, storage and technical constraints | `ARCHITECTURE.md` remains an overview/router if present. Identify one owner per detail; distinguish current systems from proposals and link relevant decisions |
| `decisions/` | Lasting technical choices need rationale: ADRs with context, decision, alternatives, consequences, status and superseding links | Preserve past decisions as history; architecture states what is current. Do not rewrite a superseded decision as if it were newly made |
| `runbooks/` | Operators need repeatable procedures: diagnosis, prerequisites/access, commands and working directories, expected signals, failure handling, recovery and verification | Describe established operations. Link LoopShip's release/environment owners for promotion and rollback; do not create competing executable policy or infer execution permission |
| `plan/` | LoopDev or existing repo rules save an implementation plan: problem, scope, approach, execution steps and acceptance/verification expectations | Follow the configured location and plan choice. This is task intent, not current architecture or another editable backlog; reference the owning item/PR for status and evidence |
| `releases/` | Release documentation warrants an index/runbook pointer or per-release scope, exclusions, acceptance and delivery evidence | LoopShip or existing release rules own lifecycle, versions and execution. Keep published facts distinct from pending scope; CHANGELOG remains the user-facing history |
| `content/` | The project builds in public: LoopCast content hub, per-post ideas/drafts and published records, index, metrics, retros, playbook, reply drafts and content assets | Link the content hub; LoopCast owns its internal structure. This is a content ledger, not a development backlog or release record. Social publication remains manual |
| `archive/` | Superseded guidance or migrated process material must remain discoverable for provenance | Mark it historical, link replacements and retain old-to-new mappings after moves. Do not move active work or still-valid runbooks here merely because they are old |
| `assets/` | Docs need local diagrams, screenshots or other supporting media | Use descriptive names, keep editable sources when useful, and link from the owning page. Keep generated builds, logs, credentials and application runtime data outside this area |

Guides and runbooks can both contain steps: guides help users/developers complete
a product or development task; runbooks support operating and recovering a
system. Keep one procedure owner and cross-link when both audiences need it.

## Root documents and family ownership

Keep root README, PRODUCT, DESIGN, ARCHITECTURE and contribution documents in
their established roles. Split detailed content into `docs/` when size or
audience warrants it, leaving a summary and links in the original entrypoint.
Existing owners under `docs/` need not be moved to root to match a template.

LoopDocs defines this organization and maintains documentation consistency.
LoopDev owns work inventory, plan preferences and implementation/review state;
its default plan path is `docs/plan/`, but saved project configuration takes
precedence. A configured Markdown inventory such as `docs/issues.md` or
`docs/backlog.md` can remain at its existing path. Do not introduce one when
the project uses GitHub Issues, Linear or another authoritative inventory.

LoopShip owns release and environment rules and observed delivery facts.
Documentation indexes and runbooks reference those owners instead of copying
commands, gates or version rules into multiple editable locations. Neither
plans nor release records replace the authoritative work inventory.

LoopCast owns `docs/content/` or the existing content location when installed.
Its posts link product/technical owners and development/delivery evidence;
their claims must distinguish proposed, implemented, merged and shipped work.
Keep post media with its content entries (normally `content/assets/`); general
documentation diagrams can remain in `docs/assets/`. Do not duplicate either
solely to match this tree.

## Naming, navigation and lifecycle

- Preserve established naming. For new pages, prefer descriptive lowercase
  kebab-case names; follow existing ADR numbering and release identity formats.
- Use relative links that work from the file's actual directory. Root README
  links to the docs index when present; it routes to the useful reader paths.
  Add subdirectory indexes only when navigation warrants them.
- Identify an owner through existing component ownership, contribution rules
  or the page/index when responsibility would otherwise be unclear. State
  proposal or historical status where it could be mistaken for current guidance.
- Update affected documentation with the code, product, design or release
  change. Verify claims against owning sources; a recent edit date alone does
  not prove freshness.
- On plan completion, move enduring explanations into their documentation
  owners as needed and link them from the plan. Keep task status in the owning
  inventory/PR. Follow existing retention rules for the plan and its evidence.
- Before archiving or moving material, resolve active consumers and inbound
  links. Keep history navigable without presenting obsolete instructions as
  current. Published release records and ADRs can remain in their own history
  areas; they do not need relocation solely due to age.
