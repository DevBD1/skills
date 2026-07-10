# AGENTS.md binding

*How to bind a repo's agent contract to the content system. Patch, don't replace: if the
repo has an `AGENTS.md` (or equivalent agent-contract file), add the pieces below to the
matching sections. If none exists, create a minimal `AGENTS.md` containing just these.*

*The binding has two halves: a **router row** so agents can find the content system, and
a **capture contract** so milestone-worthy work becomes post ideas as a side effect of
normal development.*

---

## 1. Router row

If the file has a "where truth lives" / routing table, add:

```markdown
| Build-in-public content process? | `{{CONTENT_DIR}}/` |
```

Otherwise add an equivalent one-liner wherever the file points agents at docs.

## 2. Capture contract

Add to the workflow/contract section:

```markdown
- **Content signals.** This repo builds in public. When your work produces a
  post-worthy moment — the first time something works end-to-end, a number that
  changed meaningfully, a decision with real trade-offs, a bug with a story, a visual
  before/after — capture it as a post idea: copy `{{CONTENT_DIR}}/TEMPLATE.md` to
  `{{CONTENT_DIR}}/posts/YYYY-MM-DD-<platform>-<slug>.md` with `status: idea`, fill the
  title and 2–3 lines (hook + receipt), add the row to `{{CONTENT_DIR}}/INDEX.md`, then
  get back to work. Capture only — do not draft the full post, and never post or
  publish anything anywhere; drafting and posting are separate, human-gated steps.
  The bar: a stranger could care in the first line, and there is a receipt
  (screenshot, number, diff), not just an intention.
```

## Why this works

The contract mirrors the "capture, don't implement" pattern repos use for backlog ideas:
it costs an agent one minute mid-task, so it actually happens, and it feeds the Ideate
mode a stream of grounded material instead of forcing content sessions to reconstruct
milestones from git archaeology. The human-gate line is load-bearing — keep it verbatim
in spirit: agents capture and draft; only humans publish.
