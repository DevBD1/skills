#!/usr/bin/env python3
"""Safe wrapper for bounded Gemini CLI delegation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MODEL_BY_TASK_CLASS = {
    "heavy": "gemini-3.1-pro-preview",
    "medium": "gemini-3.1-flash-lite",
    "simple": "flash-lite",
}
ALLOWED_MODELS = set(MODEL_BY_TASK_CLASS.values())
SESSION_STORE = Path.home() / ".codex" / "gemini-delegate" / "sessions.json"


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
    parser.add_argument(
        "--task-class",
        choices=tuple(MODEL_BY_TASK_CLASS),
        default="medium",
        help="Task route used to select a strict approved Gemini model.",
    )
    parser.add_argument(
        "-m",
        "--model",
        choices=tuple(sorted(ALLOWED_MODELS)),
        help="Optional approved Gemini model override.",
    )
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
    parser.add_argument(
        "--chat",
        help="Create or resume a named local chat alias backed by a Gemini session UUID.",
    )
    parser.add_argument(
        "--resume",
        help='Pass through Gemini resume selector: "latest", a UUID, or an index number.',
    )
    parser.add_argument(
        "--session-id",
        help="Start or use an explicit Gemini session UUID.",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run a live Gemini CLI chat. Uses --prompt-interactive when a prompt is provided.",
    )
    parser.add_argument(
        "--list-chats",
        action="store_true",
        help="Print local named chat aliases as JSON and exit.",
    )
    parser.add_argument(
        "--forget-chat",
        help="Remove a local named chat alias without deleting Gemini's native session.",
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


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_sessions() -> dict[str, Any]:
    if not SESSION_STORE.exists():
        return {"chats": {}}
    try:
        with SESSION_STORE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Could not read session store {SESSION_STORE}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"Session store must be a JSON object: {SESSION_STORE}")
    chats = data.setdefault("chats", {})
    if not isinstance(chats, dict):
        raise ValueError(f"Session store field 'chats' must be an object: {SESSION_STORE}")
    return data


def save_sessions(data: dict[str, Any]) -> None:
    SESSION_STORE.parent.mkdir(parents=True, exist_ok=True)
    temp_path = SESSION_STORE.with_suffix(".json.tmp")
    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, sort_keys=True)
        file.write("\n")
    temp_path.replace(SESSION_STORE)


def print_json(value: Any) -> None:
    print(json.dumps(value, indent=2, sort_keys=True))


def validate_chat_name(value: str) -> str:
    name = value.strip()
    if not name:
        raise ValueError("--chat name cannot be empty.")
    if any(char.isspace() for char in name):
        raise ValueError("--chat name cannot contain whitespace.")
    return name


def validate_args(args: argparse.Namespace, *, needs_prompt: bool) -> int | None:
    session_flags = [bool(args.chat), bool(args.resume), bool(args.session_id)]
    if sum(session_flags) > 1:
        return fail("Use only one of --chat, --resume, or --session-id.")
    if args.timeout <= 0:
        return fail("--timeout must be greater than zero.")
    if args.mode == "auto_edit" and not args.worktree:
        return fail("--mode auto_edit requires --worktree <name>.")
    if args.worktree and args.interactive:
        return fail("--interactive cannot be combined with --worktree.")
    if needs_prompt and not args.interactive:
        return fail("Provide --prompt and/or stdin context.")
    return None


def resolve_chat_session(
    *,
    args: argparse.Namespace,
    cwd: Path,
    selected_model: str,
) -> tuple[str | None, dict[str, Any] | None, str | None, bool]:
    if not args.chat:
        return None, None, None, False

    name = validate_chat_name(args.chat)
    sessions = load_sessions()
    chats = sessions["chats"]
    existing = chats.get(name)
    now = utc_now()

    if existing:
        session_id = existing.get("session_id")
        if not isinstance(session_id, str) or not session_id.strip():
            raise ValueError(f"Chat alias '{name}' has an invalid session_id.")
        existing.update(
            {
                "updated_at": now,
                "cwd": str(cwd),
                "last_model": selected_model,
                "last_mode": args.mode,
            }
        )
        return session_id, sessions, name, False

    session_id = str(uuid.uuid4())
    chats[name] = {
        "name": name,
        "session_id": session_id,
        "created_at": now,
        "updated_at": now,
        "cwd": str(cwd),
        "last_model": selected_model,
        "last_mode": args.mode,
    }
    return session_id, sessions, name, True


def run_interactive(command: list[str], *, cwd: Path, stdin_text: str) -> int:
    result = subprocess.run(
        command,
        cwd=str(cwd),
        input=stdin_text or None,
        text=True,
        check=False,
    )
    return result.returncode


def run_captured(command: list[str], *, cwd: Path, stdin_text: str, timeout: int) -> int:
    try:
        result = subprocess.run(
            command,
            cwd=str(cwd),
            input=stdin_text or None,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        write_partial_output(exc.stdout, stream=sys.stdout)
        write_partial_output(exc.stderr, stream=sys.stderr)
        return fail(f"Gemini timed out after {timeout} seconds.", 124)

    if result.stdout:
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.stderr:
        print(result.stderr, file=sys.stderr, end="" if result.stderr.endswith("\n") else "\n")

    return result.returncode


def main() -> int:
    args = parse_args()
    stdin_text = "" if sys.stdin.isatty() else sys.stdin.read()
    prompt = args.prompt.strip()

    if args.list_chats:
        try:
            print_json(load_sessions())
        except ValueError as exc:
            return fail(str(exc), 1)
        return 0

    if args.forget_chat:
        try:
            name = validate_chat_name(args.forget_chat)
            sessions = load_sessions()
            removed = sessions["chats"].pop(name, None)
            if removed is not None:
                save_sessions(sessions)
            print_json({"forgotten": bool(removed), "name": name})
        except (OSError, ValueError) as exc:
            return fail(str(exc), 1)
        return 0

    validation_error = validate_args(args, needs_prompt=not (prompt or stdin_text.strip()))
    if validation_error is not None:
        return validation_error

    selected_model = args.model or MODEL_BY_TASK_CLASS[args.task_class]
    if selected_model not in ALLOWED_MODELS:
        return fail(
            "Unsupported model. Use one of: " + ", ".join(sorted(ALLOWED_MODELS))
        )

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
        "--skip-trust",
    ]
    if not args.interactive:
        command.extend(["--output-format", "json"])
    command.extend(["--model", selected_model])
    sessions = None
    chat_name = None
    created_chat = False
    try:
        chat_session_id, sessions, chat_name, created_chat = resolve_chat_session(
            args=args,
            cwd=cwd,
            selected_model=selected_model,
        )
    except ValueError as exc:
        return fail(str(exc), 1)

    if args.worktree:
        command.extend(["--worktree", args.worktree])
    if args.resume:
        command.extend(["--resume", args.resume])
    elif args.session_id:
        command.extend(["--session-id", args.session_id])
    elif chat_session_id:
        command.extend(["--session-id" if created_chat else "--resume", chat_session_id])

    prompt_arg = prompt or "Use the stdin context to answer the task."
    if args.interactive:
        if prompt or stdin_text.strip():
            command.extend(["--prompt-interactive", prompt_arg])
    else:
        command.extend(["--prompt", prompt_arg])

    if args.interactive:
        return_code = run_interactive(command, cwd=cwd, stdin_text=stdin_text)
    else:
        return_code = run_captured(
            command,
            cwd=cwd,
            stdin_text=stdin_text,
            timeout=args.timeout,
        )

    if return_code == 0 and sessions is not None and chat_name is not None:
        try:
            sessions["chats"][chat_name]["updated_at"] = utc_now()
            save_sessions(sessions)
        except OSError as exc:
            return fail(f"Gemini succeeded but session alias could not be saved: {exc}", 1)

    return return_code


if __name__ == "__main__":
    raise SystemExit(main())
