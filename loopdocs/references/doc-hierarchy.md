# Document hierarchy

Use when deciding where content belongs, explaining each document, or auditing
ownership. Filenames below are defaults; existing equivalent owners take
precedence. A small repo can keep several short topics in its README.

For directory selection, contents and ownership under `docs/`, use the
[docs layout](docs-layout.md). Root documents give orientation and durable
summaries; detailed documentation links back to those owners.

## README.md: entrypoint and practical orientation

Answer: what is this, who uses it, and how do I get useful results?

Include a short purpose statement, supported usage and status, prerequisites,
installation/setup, a minimal runnable example or local run instructions,
common build/test/validation commands, and a documentation index. Add support,
contribution, license and security-reporting links when the project has them.
For a docs-only repository, explain how to use its content rather than inventing
a local server. For a monorepo, orient readers and link component READMEs.

Verify paths, working directories, dependency versions and commands from
manifests or scripts. Clearly distinguish an example from a verified result.
Keep secret values out of examples. Link detailed product, architecture,
workflow and release material instead of embedding duplicate rulebooks.

## PRODUCT.md: purpose and product decisions

Answer: who are we serving, what problem matters, and what guides scope?

Include the user problem, audience, value proposition, intended outcomes,
product principles, scope/non-goals, important constraints, and decision
ownership when established. Principles should help resolve actual tradeoffs.
Mark goals and hypotheses as intent, not delivered capabilities.

Keep current feature status in the chosen work inventory, technical structure
in architecture docs, UX specifics in DESIGN, and shipped changes in release
history. Existing VISION or MISSION documents may already own this content;
link or consolidate deliberately rather than creating parallel constitutions.
A ROADMAP can remain a roadmap: separate its future work from durable intent.

## DESIGN.md: user experience and visual intent

Answer: how should the interface behave and feel?

Use only when the product has a UI and this content is useful. Cover primary
journeys and outcomes; screen/state transitions; loading, empty, error and
recovery states; navigation/layout and responsive behavior; interaction and
feedback; accessibility; and visual foundations such as semantic colors,
typography, spacing and reusable component behavior.

Link canonical design files, tokens and component documentation rather than
copying their full contents. Identify approved intent versus current
implementation where they differ. Implementation conventions and system
topology belong in code guidance and architecture docs. Existing technical
DESIGN.md files need not be renamed: preserve their meaning and choose an
unambiguous UX owner such as docs/ux.md instead.

## ARCHITECTURE.md and decisions: system structure and rationale

Answer: how does the current system work, and why are its boundaries this way?

Describe components and responsibilities, dependencies, request/data flow,
storage, external interfaces, trust boundaries and material constraints.
Link API/schema specifications, component READMEs and operational runbooks.
Diagrams should name real components and agree with code. Clearly label
proposals and obsolete structures instead of presenting them as current.

Use ADRs for decisions whose context and consequences matter later: decision,
status/date, alternatives, rationale, consequences and superseding links.
Current architecture references active decisions; ADRs preserve history rather
than becoming a second current-system specification.

## AGENTS.md and CLAUDE.md: discoverable working guidance

AGENTS.md routes agents to owning docs and gives concise repo-specific build,
validation and editing constraints. Link the documentation map and installed
LoopDev/LoopShip configs where present. Keep product, UX, API and release
rules with their owners. Local/nested agent guidance may add scoped rules
under the harness's existing precedence model.

CLAUDE.md, when used, routes to shared agent guidance and adds only Claude-only
context. If another harness already owns the auto-read entrypoint, use that
entrypoint; do not multiply files merely to satisfy this layout.

## Component README.md and CONTRIBUTING.md

A component README explains its purpose and place in the repo, independent
setup, working directory, runtime/dependencies, environment variable names and
provisioning instructions, commands, interfaces and operational links. Root
setup and repo-wide policy remain at root. Public API details may belong in
an existing generated spec or dedicated API guide.

CONTRIBUTING is the human contributor path: development prerequisites, how to
validate a change, review expectations and links to the actual work/release
process. Shared human/agent commands should have one owner and be referenced
from the other entrypoint.

## Changelog and release documents

CHANGELOG is concise user/operator-facing history grouped by the project's
actual release identity (version, date or deployed revision). Pending changes,
if used, are visibly separate from published releases. Link producing PRs or
release evidence where useful; implementation logs and plans stay in LoopDev's
chosen inventory. Do not label merged code as released without evidence.

Release process docs explain or link to the owning LoopShip config/runbook:
channels, version source, environment/promotion rules, verification and rollback.
Do not duplicate executable settings already owned there. Optional per-release
records contain scope, exclusions, acceptance, candidate identity, evidence and
remaining checks. They are useful only when the project needs that contract;
LoopDocs does not impose a file per version or choose lifecycle/version policy.

## Navigation and ownership rules

- README links the relevant entry documents and component guides; large doc
  sets can use a docs index rather than an exhaustive root list.
- AGENTS links applicable owners and workflow configs. CLAUDE links shared
  agent guidance. Neither requires the global skills to be present to read it.
- Architecture links component/API/decision owners; DESIGN links UX assets;
  release history links available release records and evidence.
- After moves, update inbound links, scripts and doc generators. Avoid links
  to absent optional files and hard-coded machine-local paths in public docs.
- Do not maintain two editable copies of the same rule. If docs and code
  disagree, determine whether the doc expresses approved intent or claims
  current behavior before correcting either.
