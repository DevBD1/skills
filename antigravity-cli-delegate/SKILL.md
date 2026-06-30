---
name: antigravity-cli-delegate
description: Delegate bounded work from Codex to the local Antigravity CLI. Use when the user asks to split workload across Antigravity and Codex subscriptions, run Antigravity CLI for planning, brainstorming, second opinions, code review, web research, large-context analysis, or explicit interactive Antigravity sessions. Default to bounded print-mode delegation; use interactive mode only when requested.
license: MIT
---

# Antigravity CLI Delegate

Use Antigravity CLI as a secondary worker. Codex remains the orchestrator and must inspect Antigravity's output before acting on it.

## Install

```bash
npx skills add DevBD1/skills --skill antigravity-cli-delegate
```

## Default Rules

- Prefer bounded headless delegation through `agy --print`.
- Use the wrapper's JSON output so Codex can parse response and conversation metadata.
- Resolve the wrapper relative to the installed skill directory, then run `scripts/antigravity_delegate.py`. If the host agent sandboxes network, auth, local callbacks, or long-running commands, request the narrow approval needed for that wrapper command.
- Do not use `agy --dangerously-skip-permissions`.
- Do not treat Antigravity output as source of truth. Verify claims against files, commands, docs, or tests.
- Do not let Antigravity make changes unless the user explicitly asks for implementation delegation or an interactive Antigravity session.
- For deterministic crawling or scraping, prefer existing Codex/web/crawl4ai paths unless the user asks Antigravity to handle the research.

## Task Routing

The wrapper accepts `--task-class heavy|medium|simple` for Codex-side metadata only. Current `agy --help` exposes no model-selection flag, so task class is not passed to Antigravity.

| Task class | Use for |
| --- | --- |
| `heavy` | hard planning, architecture, complex coding strategy, deep debugging, difficult reviews |
| `medium` | coding tasks, medium analysis, web scraping/research tasks, normal reviews |
| `simple` | smallest summarization, quick checks, simple rewrites, trivial second opinions |

Prefer `medium` when unsure.

## Helper Script

Use the bundled wrapper for repeatable calls:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --task-class medium \
  --prompt "Review this plan for missing risks."
```

Pipe context through stdin when useful:

```bash
git diff --staged | python3 <skill-dir>/scripts/antigravity_delegate.py \
  --task-class medium \
  --prompt "Review this diff. Return findings with file, line, risk, and fix."
```

The wrapper calls Antigravity roughly as:

```bash
agy --print "<prompt>" --print-timeout 300s
```

For Codex, the wrapper returns JSON:

```json
{
  "conversation_id": "conversation-id",
  "response": "Antigravity response text",
  "task_class": "medium",
  "cwd": "/path/to/workspace",
  "command": ["agy", "--print", "..."]
}
```

## Long Chat Sessions

Use named chats when the user wants a long Antigravity conversation or follow-up turns over time. Named chats are local aliases stored in `~/.antigravity-cli-delegate/sessions.json` by default. Override with `--state-dir` or `ANTIGRAVITY_DELEGATE_STATE_DIR`.

Start or resume a named chat:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --chat ai-coding-trends \
  --task-class medium \
  --prompt "Start a thread about recent AI-assisted coding trends."
```

Continue the same named chat:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --chat ai-coding-trends \
  --prompt "Go deeper on IDE agent workflows."
```

Continue the latest Antigravity conversation:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --continue-latest \
  --prompt "Continue from the latest Antigravity session."
```

Use an explicit Antigravity conversation ID:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --conversation 00000000-0000-0000-0000-000000000000 \
  --prompt "Continue this exact Antigravity conversation."
```

List local named chats:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --list-chats
```

Forget a local alias without deleting Antigravity's native conversation:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --forget-chat ai-coding-trends
```

Use live interactive Antigravity only when the user wants a human-style CLI chat:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --chat ai-coding-trends \
  --interactive \
  --prompt "Open this thread interactively."
```

Interactive mode uses `agy --prompt-interactive`, does not return wrapper JSON, and lets Antigravity own stdout/stderr.

## Delegation Patterns

For planning, brainstorming, reviews, research, and large-context analysis:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --cwd /path/to/repo \
  --task-class heavy \
  --timeout 300 \
  --prompt "Analyze this codebase read-only and identify the highest-risk implementation path."
```

For additional workspace directories:

```bash
python3 <skill-dir>/scripts/antigravity_delegate.py \
  --cwd /path/to/repo \
  --add-dir /path/to/extra/context \
  --prompt "Review the repo with the extra context directory."
```

For plugin status checks:

```bash
agy plugin list
```

Expected imported plugins after the Gemini migration include `postgres` and `snitch`.

## Smoke Tests

```bash
agy --version
PYTHONPYCACHEPREFIX=/private/tmp/antigravity-delegate-pycache python3 -m py_compile <skill-dir>/scripts/antigravity_delegate.py
python3 <skill-dir>/scripts/antigravity_delegate.py --list-chats --state-dir /private/tmp/antigravity-delegate-smoke
python3 <skill-dir>/scripts/antigravity_delegate.py --task-class simple --prompt "Reply exactly: AGY_PRINT_OK"
python3 <skill-dir>/scripts/antigravity_delegate.py --chat smoke-antigravity --prompt "Reply exactly: AGY_CHAT_START_OK"
python3 <skill-dir>/scripts/antigravity_delegate.py --chat smoke-antigravity --prompt "Reply exactly: AGY_CHAT_CONTINUE_OK"
python3 <skill-dir>/scripts/antigravity_delegate.py --forget-chat smoke-antigravity
agy plugin list
```
