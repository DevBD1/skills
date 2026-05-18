---
name: gemini-cli-delegate
description: Delegate bounded work from Codex to the local Gemini CLI. Use when the user asks to split workload across Gemini and Codex subscriptions, run Gemini CLI for planning, brainstorming, second opinions, code review, web research, web crawling analysis, large-context analysis, or explicit worktree-based coding tasks. Default to read-only Gemini plan mode; allow Gemini edits only when the user explicitly asks for implementation delegation.
---

# Gemini CLI Delegate

Use Gemini CLI as a secondary worker. Codex remains the orchestrator and must inspect Gemini's output before acting on it.

## Default Rules

- Prefer read-only delegation with `--approval-mode plan`.
- Use `--output-format json` so Codex can parse response and usage metadata.
- Use `--skip-trust` for headless runs so Gemini does not block on workspace trust prompts.
- Do not use `--approval-mode yolo`.
- Do not treat Gemini output as source of truth. Verify claims against files, commands, docs, or tests.
- Do not let Gemini edit files unless the user explicitly asks for implementation delegation.
- For deterministic crawling or scraping, prefer existing Codex/web/crawl4ai paths unless the user asks Gemini to handle the research.

## Strict Model Routing

Use only these models:

| Task class | Model | Use for |
| --- | --- | --- |
| `heavy` | `gemini-3.1-pro-preview` | hard planning, architecture, complex coding strategy, deep debugging, difficult reviews |
| `medium` | `gemini-3.1-flash-lite` | coding tasks, medium analysis, web scraping/research tasks, normal reviews |
| `simple` | `flash-lite` | smallest summarization, quick checks, simple rewrites, trivial second opinions |

Route the task yourself before calling Gemini. Prefer `medium` when unsure. Do not pass any other model name.

## Helper Script

Use the bundled wrapper for repeatable calls:

```bash
python3 /Users/burak/.agents/skills/gemini-cli-delegate/scripts/gemini_delegate.py \
  --task-class medium \
  --prompt "Review this plan for missing risks."
```

Pipe context through stdin when useful:

```bash
git diff --staged | python3 /Users/burak/.agents/skills/gemini-cli-delegate/scripts/gemini_delegate.py \
  --task-class medium \
  --prompt "Review this diff. Return findings with file, line, risk, and fix."
```

The wrapper defaults to:

```bash
gemini --approval-mode plan --output-format json --skip-trust --model gemini-3.1-flash-lite -p "<prompt>"
```

If Gemini reports model capacity errors, retry with an explicit model:

```bash
python3 /Users/burak/.agents/skills/gemini-cli-delegate/scripts/gemini_delegate.py \
  --model gemini-3.1-pro-preview \
  --prompt "Review this plan for missing risks."
```

## Delegation Patterns

For planning, brainstorming, reviews, research, and large-context analysis:

```bash
python3 /Users/burak/.agents/skills/gemini-cli-delegate/scripts/gemini_delegate.py \
  --cwd /path/to/repo \
  --task-class heavy \
  --timeout 300 \
  --prompt "Analyze this codebase read-only and identify the highest-risk implementation path."
```

For implementation delegation, only when the user explicitly requests it:

```bash
python3 /Users/burak/.agents/skills/gemini-cli-delegate/scripts/gemini_delegate.py \
  --cwd /path/to/repo \
  --task-class medium \
  --mode auto_edit \
  --worktree gemini-task-name \
  --timeout 900 \
  --prompt "Implement only X. Allowed files: A, B. Run validation command Y. Report changed files and results."
```

Implementation prompts must include:

- exact task scope
- allowed files or modules
- expected output
- validation commands
- instruction to avoid unrelated edits

After Gemini edits code, Codex must review the diff and run validation locally before reporting success.
