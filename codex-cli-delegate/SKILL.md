---
name: codex-cli-delegate
description: Delegate bounded work from another agent to the local Codex CLI. Use when the user or orchestrating agent asks to delegate work to Codex CLI, split workload across AI subscriptions, get a Codex second opinion, run Codex for planning, code review, research, large-context analysis, or explicit worktree-based implementation delegation.
license: MIT
---

# Codex CLI Delegate

Use Codex CLI as a secondary worker for another local agent. The orchestrating agent remains responsible for reviewing Codex output before acting on it.

## Install

```bash
npx skills add DevBD1/skills --skill codex-cli-delegate
```

## Default Rules

- Prefer bounded non-interactive delegation through `codex exec`.
- Default to read-only mode: `codex --ask-for-approval never exec --sandbox read-only`.
- Resolve the wrapper relative to the installed skill directory, then run `scripts/codex_delegate.py`.
- Do not use or pass through Codex's dangerous approval and sandbox bypass flag.
- Do not treat Codex output as source of truth. Verify claims against files, commands, docs, or tests.
- Do not let Codex make changes unless the user explicitly asks for implementation delegation.
- For implementation delegation, require an isolated worktree and exact scope, allowed files, expected output, and validation commands in the prompt.

## Task Routing

The wrapper accepts `--task-class heavy|medium|simple` as routing metadata. Pass `--model` only when the orchestrator has a specific Codex model preference; otherwise Codex uses its local config.

| Task class | Use for |
| --- | --- |
| `heavy` | hard planning, architecture, complex debugging, difficult reviews, large-context analysis |
| `medium` | normal coding tasks, medium analysis, web research, routine reviews |
| `simple` | quick checks, small rewrites, simple summaries, trivial second opinions |

Prefer `medium` when unsure.

## Helper Script

Use the bundled wrapper for repeatable read-only calls:

```bash
python3 <skill-dir>/scripts/codex_delegate.py \
  --task-class medium \
  --prompt "Review this plan for missing risks."
```

Pipe context through stdin when useful:

```bash
git diff --staged | python3 <skill-dir>/scripts/codex_delegate.py \
  --task-class medium \
  --prompt "Review this diff. Return findings with file, line, risk, and fix."
```

The wrapper calls Codex roughly as:

```bash
codex --ask-for-approval never exec --sandbox read-only --output-last-message <tmp> "<prompt>"
```

For orchestrators, the wrapper returns JSON:

```json
{
  "response": "Codex response text",
  "task_class": "medium",
  "mode": "plan",
  "cwd": "/path/to/workspace",
  "command": ["codex", "exec", "..."],
  "output_file": "/tmp/codex-delegate-..."
}
```

## Implementation Delegation

Use implementation mode only when the user explicitly asks another agent to delegate code changes to Codex. The orchestrator should create or choose the isolated worktree before calling the wrapper.

```bash
python3 <skill-dir>/scripts/codex_delegate.py \
  --mode auto_edit \
  --worktree task-name \
  --cwd /path/to/worktree \
  --prompt "Implement only X in files A and B. Then run command Y and report the result."
```

In `auto_edit` mode, the wrapper uses:

```bash
codex --ask-for-approval never exec --sandbox workspace-write --output-last-message <tmp>
```

The orchestrator must inspect the diff and run validation after Codex completes.

## Smoke Tests

```bash
codex --version
PYTHONPYCACHEPREFIX=/private/tmp/codex-delegate-pycache python3 -m py_compile <skill-dir>/scripts/codex_delegate.py
python3 <skill-dir>/scripts/codex_delegate.py --prompt "Return OK only." --timeout 120
```
