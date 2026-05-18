#!/usr/bin/env python3
"""Safe wrapper for bounded Gemini CLI delegation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Gemini CLI with safe defaults for Codex delegation."
    )
    parser.add_argument(
        "-p",
        "--prompt",
        default="",
        help="Prompt to send to Gemini. Stdin is passed through as additional context.",
    )
    parser.add_argument("-m", "--model", help="Optional Gemini model name.")
    parser.add_argument(
        "--mode",
        choices=("plan", "auto_edit"),
        default="plan",
        help="Gemini approval mode. yolo is intentionally unsupported.",
    )
    parser.add_argument(
        "--worktree",
        help="Required for auto_edit mode. Passed to gemini --worktree.",
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
        help="Working directory for Gemini. Defaults to the current directory.",
    )
    return parser.parse_args()


def fail(message: str, code: int = 2) -> int:
    print(json.dumps({"error": {"message": message}}), file=sys.stderr)
    return code


def write_partial_output(value: str | bytes | None, *, stream: object) -> None:
    if not value:
        return
    text = value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value
    print(text, file=stream, end="" if text.endswith("\n") else "\n")


def main() -> int:
    args = parse_args()
    stdin_text = "" if sys.stdin.isatty() else sys.stdin.read()
    prompt = args.prompt.strip()

    if not prompt and not stdin_text.strip():
        return fail("Provide --prompt and/or stdin context.")
    if args.timeout <= 0:
        return fail("--timeout must be greater than zero.")
    if args.mode == "auto_edit" and not args.worktree:
        return fail("--mode auto_edit requires --worktree <name>.")

    gemini = shutil.which("gemini")
    if not gemini:
        return fail("gemini CLI was not found on PATH.", 127)

    cwd = Path(args.cwd).expanduser()
    if not cwd.exists() or not cwd.is_dir():
        return fail(f"--cwd does not exist or is not a directory: {cwd}")

    command = [
        gemini,
        "--approval-mode",
        args.mode,
        "--output-format",
        "json",
        "--skip-trust",
    ]
    if args.model:
        command.extend(["--model", args.model])
    if args.worktree:
        command.extend(["--worktree", args.worktree])
    command.extend(["--prompt", prompt or "Use the stdin context to answer the task."])

    try:
        result = subprocess.run(
            command,
            cwd=str(cwd),
            input=stdin_text or None,
            text=True,
            capture_output=True,
            timeout=args.timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        write_partial_output(exc.stdout, stream=sys.stdout)
        write_partial_output(exc.stderr, stream=sys.stderr)
        return fail(f"Gemini timed out after {args.timeout} seconds.", 124)

    if result.stdout:
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.stderr:
        print(result.stderr, file=sys.stderr, end="" if result.stderr.endswith("\n") else "\n")

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
