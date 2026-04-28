import os
import re
import shutil


class Colors:
    Color_Off = "\033[0m"

    Red = "\033[0;31m"
    Green = "\033[0;32m"
    Yellow = "\033[0;33m"

    Gold = "\033[38;5;220m"  # bright yellow/gold


class Level:
    RUN = Colors.Green + "[RUN]" + Colors.Color_Off
    WARN = Colors.Yellow + "[WARN]" + Colors.Color_Off
    PASS = Colors.Green + "[PASS]" + Colors.Color_Off
    FAIL = Colors.Red + "[FAIL]" + Colors.Color_Off
    REGEN = Colors.Gold + "[REGEN]" + Colors.Color_Off


def remove_ansi_codes(s):
    """abc returns with colors"""
    ansi_escape = re.compile(r"\x1b\[[0-9;]*m")
    return ansi_escape.sub("", s)


def remove_comment_lines(text):
    return "\n".join(
        line for line in text.splitlines() if not line.strip().startswith("#")
    )


def normalize_whitespace(text):
    # Step 1: Replace all sequences of tabs and spaces with a single space
    text = re.sub(r"[ \t]+", " ", text)
    # Step 2: Remove space(s) right before a newline
    text = re.sub(r" +\n", "\n", text)
    return text


def find_abc_executable():
    """Resolve path to the `abc` executable.

    Resolution order:
    1. `ABC_EXE` environment variable if set and executable
    2. `abc` found on `PATH` via `shutil.which`

    Raises FileNotFoundError if no executable is found.
    """
    env_path = os.environ.get("ABC_EXE")
    if env_path:
        env_path = os.path.expanduser(env_path)
        if os.path.isfile(env_path) and os.access(env_path, os.X_OK):
            return env_path

    which_path = shutil.which("abc")
    if which_path:
        return which_path

    raise FileNotFoundError(
        "abc executable not found. Set ABC_EXE  or ensure `abc` is on PATH."
    )


