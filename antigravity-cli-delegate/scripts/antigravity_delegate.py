#!/usr/bin/env python3
"""Safe wrapper for bounded Antigravity CLI delegation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TASK_CLASSES = ("heavy", "medium", "simple")
DEFAULT_STATE_DIR = Path.home() / ".antigravity-cli-delegate"
CONVERSATION_CACHE = (
    Path.home()
    / ".gemini"
    / "antigravity-cli"
    / "cache"
    / "last_conversations.json"
)
DEFAULT_AGY = Path.home() / ".local" / "bin" / "agy"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Antigravity CLI with safe defaults for Codex delegation."
    )
    parser.add_argument(
        "-p",
        "--prompt",
        default="",
        help="Prompt to send to Antigravity. Stdin is passed through as additional context.",
    )
    parser.add_argument(
        "--task-class",
        choices=TASK_CLASSES,
        default="medium",
        help="Task metadata for Codex routing. Antigravity CLI does not expose model routing.",
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
        help="Working directory for Antigravity. Defaults to the current directory.",
    )
    parser.add_argument(
        "--state-dir",
        default=os.environ.get("ANTIGRAVITY_DELEGATE_STATE_DIR"),
        help=(
            "Directory for local wrapper state. Defaults to "
            "$ANTIGRAVITY_DELEGATE_STATE_DIR or ~/.antigravity-cli-delegate."
        ),
    )
    parser.add_argument(
        "--chat",
        help="Create or resume a named local chat alias backed by an Antigravity conversation ID.",
    )
    parser.add_argument(
        "--continue-latest",
        action="store_true",
        help="Continue the most recent Antigravity conversation.",
    )
    parser.add_argument(
        "--conversation",
        help="Resume an Antigravity conversation by ID.",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run a live Antigravity CLI chat. Uses --prompt-interactive when a prompt is provided.",
    )
    parser.add_argument(
        "--add-dir",
        action="append",
        default=[],
        help="Add a directory to the Antigravity workspace. Repeatable.",
    )
    parser.add_argument(
        "--sandbox",
        action="store_true",
        help="Opt in to Antigravity CLI sandbox mode.",
    )
    parser.add_argument(
        "--list-chats",
        action="store_true",
        help="Print local named chat aliases as JSON and exit.",
    )
    parser.add_argument(
        "--forget-chat",
        help="Remove a local named chat alias without deleting Antigravity's native conversation.",
    )
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def print_json(value: Any, *, stream: object = sys.stdout) -> None:
    print(json.dumps(value, indent=2, sort_keys=True), file=stream)


def fail(message: str, code: int = 2, **extra: Any) -> int:
    payload: dict[str, Any] = {"error": {"message": message}}
    if extra:
        payload["error"].update(extra)
    print_json(payload, stream=sys.stderr)
    return code


def load_json_file(path: Path, *, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Could not read JSON file {path}: {exc}") from exc


def session_store_path(args: argparse.Namespace) -> Path:
    state_dir = Path(args.state_dir).expanduser() if args.state_dir else DEFAULT_STATE_DIR
    return state_dir / "sessions.json"


def load_sessions(path: Path) -> dict[str, Any]:
    data = load_json_file(path, default={"chats": {}})
    if not isinstance(data, dict):
        raise ValueError(f"Session store must be a JSON object: {path}")
    chats = data.setdefault("chats", {})
    if not isinstance(chats, dict):
        raise ValueError(f"Session store field 'chats' must be an object: {path}")
    return data


def save_sessions(data: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(".json.tmp")
    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, sort_keys=True)
        file.write("\n")
    temp_path.replace(path)


def read_conversation_for_cwd(cwd: Path) -> str | None:
    data = load_json_file(CONVERSATION_CACHE, default={})
    if not isinstance(data, dict):
        raise ValueError(f"Conversation cache must be a JSON object: {CONVERSATION_CACHE}")
    value = data.get(str(cwd))
    return value if isinstance(value, str) and value.strip() else None


def validate_chat_name(value: str) -> str:
    name = value.strip()
    if not name:
        raise ValueError("--chat name cannot be empty.")
    if any(char.isspace() for char in name):
        raise ValueError("--chat name cannot contain whitespace.")
    return name


def validate_args(args: argparse.Namespace, *, has_prompt: bool) -> int | None:
    conversation_flags = [bool(args.chat), bool(args.conversation), args.continue_latest]
    if sum(conversation_flags) > 1:
        return fail("Use only one of --chat, --conversation, or --continue-latest.")
    if args.timeout <= 0:
        return fail("--timeout must be greater than zero.")
    if not args.interactive and not has_prompt:
        return fail("Provide --prompt and/or stdin context.")
    if args.interactive and args.continue_latest and has_prompt:
        return fail("--interactive with --continue-latest cannot also send an initial prompt.")
    return None


def resolve_chat(
    *,
    args: argparse.Namespace,
    cwd: Path,
    session_store: Path,
) -> tuple[str | None, dict[str, Any] | None, str | None, bool]:
    if not args.chat:
        return None, None, None, False

    name = validate_chat_name(args.chat)
    sessions = load_sessions(session_store)
    chats = sessions["chats"]
    existing = chats.get(name)

    if existing:
        conversation_id = existing.get("conversation_id")
        if not isinstance(conversation_id, str) or not conversation_id.strip():
            raise ValueError(f"Chat alias '{name}' has an invalid conversation_id.")
        return conversation_id, sessions, name, False

    now = utc_now()
    chats[name] = {
        "name": name,
        "conversation_id": None,
        "created_at": now,
        "updated_at": now,
        "cwd": str(cwd),
        "task_class": args.task_class,
    }
    return None, sessions, name, True


def find_agy() -> str | None:
    if DEFAULT_AGY.exists() and os.access(DEFAULT_AGY, os.X_OK):
        return str(DEFAULT_AGY)
    return shutil.which("agy")


def build_command(
    *,
    agy: str,
    args: argparse.Namespace,
    prompt: str,
    chat_conversation_id: str | None,
) -> list[str]:
    command = [agy]
    for directory in args.add_dir:
        command.extend(["--add-dir", directory])
    if args.sandbox:
        command.append("--sandbox")

    conversation_id = args.conversation or chat_conversation_id
    if conversation_id:
        command.extend(["--conversation", conversation_id])
    elif args.continue_latest:
        command.append("--continue")

    if args.interactive:
        if prompt:
            command.extend(["--prompt-interactive", prompt])
    else:
        command.extend(["--print", prompt])
        command.extend(["--print-timeout", f"{args.timeout}s"])

    return command


def run_interactive(command: list[str], *, cwd: Path, stdin_text: str) -> int:
    result = subprocess.run(
        command,
        cwd=str(cwd),
        input=stdin_text or None,
        text=True,
        check=False,
    )
    return result.returncode


def run_captured(
    command: list[str],
    *,
    cwd: Path,
    stdin_text: str,
    timeout: int,
) -> subprocess.CompletedProcess[str] | subprocess.TimeoutExpired[str]:
    try:
        return subprocess.run(
            command,
            cwd=str(cwd),
            input=stdin_text or None,
            text=True,
            capture_output=True,
            timeout=timeout + 10,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return exc


def command_for_output(command: list[str]) -> list[str]:
    return [Path(command[0]).name, *command[1:]]


def main() -> int:
    args = parse_args()
    session_store = session_store_path(args)
    stdin_text = "" if sys.stdin.isatty() else sys.stdin.read()
    prompt = args.prompt.strip()
    if stdin_text.strip():
        prompt = f"{prompt}\n\n{stdin_text.strip()}".strip()

    if args.list_chats:
        try:
            print_json(load_sessions(session_store))
        except ValueError as exc:
            return fail(str(exc), 1)
        return 0

    if args.forget_chat:
        try:
            name = validate_chat_name(args.forget_chat)
            sessions = load_sessions(session_store)
            removed = sessions["chats"].pop(name, None)
            if removed is not None:
                save_sessions(sessions, session_store)
            print_json({"forgotten": bool(removed), "name": name})
        except (OSError, ValueError) as exc:
            return fail(str(exc), 1)
        return 0

    validation_error = validate_args(args, has_prompt=bool(prompt))
    if validation_error is not None:
        return validation_error

    agy = find_agy()
    if not agy:
        return fail("Antigravity CLI was not found on PATH or at ~/.local/bin/agy.", 127)

    cwd = Path(args.cwd).expanduser().resolve()
    if not cwd.exists() or not cwd.is_dir():
        return fail(f"--cwd does not exist or is not a directory: {cwd}")

    try:
        chat_conversation_id, sessions, chat_name, created_chat = resolve_chat(
            args=args,
            cwd=cwd,
            session_store=session_store,
        )
    except ValueError as exc:
        return fail(str(exc), 1)

    command = build_command(
        agy=agy,
        args=args,
        prompt=prompt,
        chat_conversation_id=chat_conversation_id,
    )

    if args.interactive:
        return_code = run_interactive(command, cwd=cwd, stdin_text="")
        if return_code != 0:
            return return_code
        if sessions is not None and chat_name is not None:
            try:
                conversation_id = (
                    args.conversation
                    or chat_conversation_id
                    or read_conversation_for_cwd(cwd)
                )
            except ValueError as exc:
                return fail(str(exc), 1, command=command_for_output(command))
            if not conversation_id:
                return fail(
                    "Antigravity succeeded but no conversation ID was found for the named chat.",
                    1,
                    command=command_for_output(command),
                )
            chat = sessions["chats"][chat_name]
            chat.update(
                {
                    "conversation_id": conversation_id,
                    "updated_at": utc_now(),
                    "cwd": str(cwd),
                    "task_class": args.task_class,
                }
            )
            try:
                save_sessions(sessions, session_store)
            except OSError as exc:
                return fail(
                    f"Antigravity succeeded but session alias could not be saved: {exc}",
                    1,
                    command=command_for_output(command),
                )
        return 0

    result = run_captured(command, cwd=cwd, stdin_text="", timeout=args.timeout)
    if isinstance(result, subprocess.TimeoutExpired):
        return fail(
            f"Antigravity timed out after {args.timeout} seconds.",
            124,
            stdout=result.stdout or "",
            stderr=result.stderr or "",
            command=command_for_output(command),
        )

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    if result.returncode != 0:
        return fail(
            "Antigravity CLI failed.",
            result.returncode or 1,
            stdout=stdout,
            stderr=stderr,
            command=command_for_output(command),
        )

    try:
        detected_conversation_id = read_conversation_for_cwd(cwd)
    except ValueError as exc:
        return fail(str(exc), 1, response=stdout, command=command_for_output(command))

    conversation_id = args.conversation or chat_conversation_id or detected_conversation_id

    if sessions is not None and chat_name is not None:
        if not conversation_id:
            return fail(
                "Antigravity succeeded but no conversation ID was found for the named chat.",
                1,
                response=stdout,
                command=command_for_output(command),
            )
        now = utc_now()
        chat = sessions["chats"][chat_name]
        chat.update(
            {
                "conversation_id": conversation_id,
                "updated_at": now,
                "cwd": str(cwd),
                "task_class": args.task_class,
            }
        )
        try:
            save_sessions(sessions, session_store)
        except OSError as exc:
            return fail(
                f"Antigravity succeeded but session alias could not be saved: {exc}",
                1,
                response=stdout,
                command=command_for_output(command),
            )

    payload: dict[str, Any] = {
        "conversation_id": conversation_id,
        "response": stdout,
        "task_class": args.task_class,
        "cwd": str(cwd),
        "command": command_for_output(command),
    }
    if stderr:
        payload["stderr"] = stderr
    print_json(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
