---
name: loopdocs
description: Define, establish, update or audit repository documentation roles, content and links. Use for README.md, PRODUCT.md, DESIGN.md, ARCHITECTURE.md, AGENTS.md, CLAUDE.md, contribution guides, service READMEs, docs/ organization and documentation hierarchy. Complements LoopDev development and LoopShip releases without managing their workflows.
---

# LoopDocs

Make it clear which document answers each question, what it contains, and
when it needs updating. Adapt the documentation to the repository and its
readers. Keep each rule or fact in one owning source and link to it elsewhere.

## Route the request

- **Establish:** inspect existing docs and code, map document ownership, and
  fill the gaps that matter to readers. Reuse established filenames.
- **Update:** change the owning document for the requested behavior or
  decision and repair affected indexes and links in the same change.
- **Audit:** compare documentation against owning evidence; report stale,
  missing, contradictory or unverified content. Fix it when the request
  authorizes repairs; an audit-only request stays read-only.
- **Migrate from Autoscrum:** use [migration](references/migration.md) to
  separate documentation from superseded workflow instructions while
  preserving useful content and history.

For detailed content requirements and boundaries, read
[document hierarchy](references/doc-hierarchy.md). For update and audit
procedures, read [operations](references/operations.md).
For organizing `docs/`, choosing subdirectories or separating plans from
durable documentation, read [docs layout](references/docs-layout.md).

## Family responsibilities

LoopDocs owns document roles, content structure, navigation and consistency.
LoopDev owns work inventory, optional plans, implementation, validation and
the feature PR/review/merge flow. LoopShip owns release policy, versioning,
environments, promotion, publication, rollback and delivery evidence.
LoopCast owns build-in-public content ideas, drafts, post history, metrics and
lessons. When installed, its content hub (default `docs/content/README.md`)
owns that workflow; LoopDocs indexes it without duplicating it.

Each skill can work independently. When companion configs exist at
`.agents/skills/loopdev/config.md` or `.agents/skills/loopship/config.md`,
read the relevant parts and link to their owning rules. Do not copy their
mutable settings into a second process document. LoopDocs does not introduce
sprint records, a backlog, release automation or additional approval gates.
Documentation updates belong with the change that makes them necessary,
following the repository's existing review and release rules.

## Document map

These are default roles, not a mandatory set of files. Preserve equivalent
existing names and split documents only when their size, audience or
independent ownership warrants it.

| Document | Contains | Update trigger |
| --- | --- | --- |
| Root `README.md` | Project purpose, audience, supported use, prerequisites, install/setup, quick start, common commands and documentation index | Setup, supported behavior, commands or doc locations change |
| `docs/README.md`, when useful | Reader-oriented index of detailed documentation, its owners and status | Documentation areas, owners or entry paths change |
| `docs/content/` or existing content area, when used | LoopCast content hub, post ledger, ideas/drafts, metrics, retros and playbook | Content changes under the owning content workflow |
| `PRODUCT.md` | User problem, audience, intended outcomes, product principles, scope, non-goals and product decision ownership | A product decision changes the intended direction |
| `DESIGN.md` | UI/UX intent: journeys, states, interaction, accessibility, layout and visual rules; link canonical design assets | User experience or design system changes; create only for a UI |
| `ARCHITECTURE.md` or existing architecture docs | Current system boundaries, components, dependencies, data flow, interfaces and technical constraints; link decisions | Structure, data flow or technical contracts change |
| `AGENTS.md` | Agent entrypoint, repo-specific commands and working constraints, document routing and companion workflow bindings | Agent guidance or its owning sources change |
| `CLAUDE.md` | Thin adapter to shared agent guidance plus Claude-only context, when used | Harness-specific guidance changes |
| Service/package `README.md` | Local purpose, setup, environment variable names, runtime, commands, interfaces and operational links | That component's setup or contracts change |
| `CONTRIBUTING.md` | Human contribution setup, validation, review expectations and links to the development workflow | Contribution rules change |
| `CHANGELOG.md` | User/operator-facing release history; optional pending changes clearly separated from shipped releases | Verified release-relevant changes under the release policy |
| Existing release docs or `docs/releases/` | Release policy/runbook links and optional version scope, acceptance and delivery records | LoopShip's release contract or observed delivery changes |
| `docs/decisions/` or existing ADRs | Significant technical decisions, context, alternatives, consequences and supersession | A lasting decision needs rationale beyond current architecture |

## Establish or change documentation

1. Inspect repository instructions, Git status, existing documents, manifests,
   scripts and relevant code. Identify audiences and authoritative sources
   before writing. Preserve unrelated work and meaningful existing content.
2. Map reader questions to current owners. Distinguish product intent,
   technical implementation, UX intent, work status and shipped history.
   A roadmap is future work, not evidence of implemented features.
3. Patch gaps in place. Create only documents with useful content and a real
   reader need. Do not turn a short repository into an empty template tree.
   Explain unresolved product choices rather than inventing them; continue
   independent edits while only the dependent content remains unresolved.
4. Link new or moved owners from the README index and applicable agent
   entrypoint. When the repo uses agent guidance, add a short documentation
   binding there so a fresh agent can discover the map without this skill.
   Do not create a separate LoopDocs config just to repeat the document index.
5. Verify claims, examples, links and boundaries using
   [operations](references/operations.md). Report actual checks and any
   unverified claims or decisions still needed.

## Use templates selectively

Adapt [README](assets/templates/README.md),
[PRODUCT](assets/templates/PRODUCT.md),
[DESIGN](assets/templates/DESIGN.md) and
[ARCHITECTURE](assets/templates/ARCHITECTURE.md) when starting those documents.
Use the [agent routing snippet](assets/templates/snippets/AGENTS.md),
[Claude adapter](assets/templates/CLAUDE.md),
[service README](assets/templates/snippets/service-README.md) and
[changelog snippet](assets/templates/snippets/CHANGELOG.md) only where relevant.
The [release index](assets/templates/docs/releases/README.md) and
[release record](assets/templates/docs/releases/templates/release.md) describe
content; LoopShip or existing release rules decide policy and lifecycle.
Use the [docs index](assets/templates/docs/README.md) when detailed documentation
needs a separate entrypoint; root README links to it.

Patch existing docs instead of replacing them wholesale. Resolve placeholders,
remove unused sections, and include links only to owners that actually exist.
When modifying this skill, run the environment's skill validator if available.
