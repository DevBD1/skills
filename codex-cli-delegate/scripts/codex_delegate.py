#!/usr/bin/env python3
"""Safe wrapper for bounded Codex CLI delegation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

TASK_CLASSES = ("heavy", "medium", "simple")
MODES = ("plan", "auto_edit")
FORBIDDEN_TEXT = "--dangerously-" "bypass-approvals-and-sandbox"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Codex CLI with safe defaults for agent delegation."
    )
    parser.add_argument(
        "-p",
        "--prompt",
        default="",
        help="Prompt to send to Codex. Stdin is passed through as additional context.",
    )
    parser.add_argument(
        "--task-class",
        choices=TASK_CLASSES,
        default="medium",
        help="Task metadata for orchestrator routing.",
    )
    parser.add_argument(
        "--mode",
        choices=MODES,
        default="plan",
        help="Delegation mode. plan is read-only; auto_edit allows workspace writes.",
    )
    parser.add_argument(
        "--worktree",
        help="Required task/worktree name for --mode auto_edit.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Timeout in seconds. Defaults to 300.",
    )
    parser.add_argument(
        "--cwd",
        default=os.getcwd(),
        help="Working directory for Codex. Defaults to the current directory.",
    )
    parser.add_argument(
        "--model",
        help="Optional Codex model override. Defaults to local Codex config.",
    )
    return parser.parse_args()


def print_json(value: Any, *, stream: object = sys.stdout) -> None:
    print(json.dumps(value, indent=2, sort_keys=True), file=stream)


def fail(message: str, code: int = 2, **extra: Any) -> int:
    payload: dict[str, Any] = {"error": {"message": message}}
    if extra:
        payload["error"].update(extra)
    print_json(payload, stream=sys.stderr)
    return code


def find_codex() -> str | None:
    return shutil.which("codex")


def command_for_output(command: list[str]) -> list[str]:
    return [Path(command[0]).name, *command[1:]]


def validate_args(args: argparse.Namespace, *, prompt: str) -> int | None:
    if args.timeout <= 0:
        return fail("--timeout must be greater than zero.")
    if not prompt.strip():
        return fail("Provide --prompt and/or stdin context.")
    if FORBIDDEN_TEXT in prompt or (args.model and FORBIDDEN_TEXT in args.model):
        return fail(f"Forbidden unsafe Codex flag: {FORBIDDEN_TEXT}")
    if args.mode == "auto_edit":
        if not args.worktree or not args.worktree.strip():
            return fail("--worktree is required when --mode auto_edit.")
        if FORBIDDEN_TEXT in args.worktree:
            return fail(f"Forbidden unsafe Codex flag: {FORBIDDEN_TEXT}")
    return None


def build_command(
    *,
    codex: str,
    args: argparse.Namespace,
    prompt: str,
    output_file: Path,
) -> list[str]:
    sandbox = "read-only" if args.mode == "plan" else "workspace-write"
    command = [
        codex,
        "--ask-for-approval",
        "never",
        "exec",
        "--sandbox",
        sandbox,
        "--output-last-message",
        str(output_file),
        "--color",
        "never",
        "--cd",
        str(Path(args.cwd).expanduser().resolve()),
    ]
    if args.model:
        command.extend(["--model", args.model])
    command.append(prompt)
    return command


def run_captured(
    command: list[str],
    *,
    cwd: Path,
    timeout: int,
) -> subprocess.CompletedProcess[str] | subprocess.TimeoutExpired[str]:
    try:
        return subprocess.run(
            command,
            cwd=str(cwd),
            stdin=subprocess.DEVNULL,
            text=True,
            capture_output=True,
            timeout=timeout + 10,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return exc


def read_output_file(path: Path, stdout: str) -> str:
    try:
        text = path.read_text(encoding="utf-8").strip()
    except OSError:
        text = ""
    return text or stdout.strip()


def main() -> int:
    args = parse_args()
    stdin_text = "" if sys.stdin.isatty() else sys.stdin.read()
    prompt = args.prompt.strip()
    if stdin_text.strip():
        prompt = f"{prompt}\n\n{stdin_text.strip()}".strip()

    validation_error = validate_args(args, prompt=prompt)
    if validation_error is not None:
        return validation_error

    codex = find_codex()
    if not codex:
        return fail("Codex CLI was not found on PATH.", 127)

    cwd = Path(args.cwd).expanduser().resolve()
    if not cwd.exists() or not cwd.is_dir():
        return fail(f"--cwd does not exist or is not a directory: {cwd}")

    output_handle = tempfile.NamedTemporaryFile(
        prefix="codex-delegate-",
        suffix=".txt",
        delete=False,
    )
    output_file = Path(output_handle.name)
    output_handle.close()

    command = build_command(
        codex=codex,
        args=args,
        prompt=prompt,
        output_file=output_file,
    )

    result = run_captured(command, cwd=cwd, timeout=args.timeout)
    if isinstance(result, subprocess.TimeoutExpired):
        return fail(
            f"Codex timed out after {args.timeout} seconds.",
            124,
            stdout=result.stdout or "",
            stderr=result.stderr or "",
            command=command_for_output(command),
            output_file=str(output_file),
        )

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    response = read_output_file(output_file, stdout)

    if result.returncode != 0:
        return fail(
            "Codex CLI failed.",
            result.returncode or 1,
            response=response,
            stdout=stdout,
            stderr=stderr,
            command=command_for_output(command),
            output_file=str(output_file),
        )

    payload: dict[str, Any] = {
        "response": response,
        "task_class": args.task_class,
        "mode": args.mode,
        "cwd": str(cwd),
        "command": command_for_output(command),
        "output_file": str(output_file),
    }
    if args.worktree:
        payload["worktree"] = args.worktree
    if stderr:
        payload["stderr"] = stderr
    print_json(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
