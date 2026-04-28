import os
import subprocess

import util


def _get_all_abc_commands() -> set:
    try:
        abc_exe = util.find_abc_executable()
    except FileNotFoundError:
        return set()

    proc = subprocess.run(
        [abc_exe, "-q", "help"],
        capture_output=True,
        text=True,
    )

    all_abc_commands = set()
    for line in proc.stdout.strip().splitlines():
        if line.startswith("Welcome to ABC"):
            continue
        if "commands:" in line:
            continue
        parts = line.strip().split()
        for part in parts:
            all_abc_commands.add(part)

    return all_abc_commands


def _get_covered_abc_commands() -> set:
    # TODO also support .abc with ';'
    covered_abc_commands = set()

    for root, dirs, files in os.walk("tests/"):
        for filename in files:
            if filename.endswith(".abc"):
                filepath = os.path.join(root, filename)
                with open(filepath) as f:
                    for line in f:
                        stripped = line.strip()
                        if stripped:
                            command = stripped.split()[0]
                            covered_abc_commands.add(command)

    return covered_abc_commands


def get_command_coverage() -> tuple[int, int]:
    """Return (covered_count, total_count) of ABC commands."""
    all_cmds = _get_all_abc_commands()
    covered_cmds = _get_covered_abc_commands()
    return len(covered_cmds & all_cmds), len(all_cmds)


def print_command_coverage():
    """
    Print how many commands available through abc's `help` are covered.
    `help` refers to e.g. `abc -q help`, not `abc -help`
    """
    covered, total = get_command_coverage()
    uncovered = total - covered

    if uncovered > 0:
        print(
            f"{util.Level.WARN} There are {uncovered}/"
            f"{total} ABC commands with no coverage.\n"
        )


def generate_coverage_badge_svg(covered: int, total: int) -> str:
    label = "ABC command coverage"
    value = f"{covered} / {total}"

    pct = covered / total if total > 0 else 0
    if pct >= 0.5:
        color = "#4c1"
    elif pct >= 0.1:
        color = "#dfb317"
    else:
        color = "#e05d44"

    # Pixel widths: ~7px per char + 10px side padding each section
    label_w = max(int(len(label) * 7) + 10, 60)
    value_w = max(int(len(value) * 7) + 10, 40)
    total_w = label_w + value_w

    # Centers and text lengths in 10x scaled coordinate space
    label_cx = label_w * 5
    value_cx = label_w * 10 + value_w * 5
    label_text_len = (label_w - 10) * 10
    value_text_len = (value_w - 10) * 10

    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{total_w}" height="20" role="img" aria-label="{label}: {value}">
  <title>{label}: {value}</title>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r">
    <rect width="{total_w}" height="20" rx="3" fill="#fff"/>
  </clipPath>
  <g clip-path="url(#r)">
    <rect width="{label_w}" height="20" fill="#555"/>
    <rect x="{label_w}" width="{value_w}" height="20" fill="{color}"/>
    <rect width="{total_w}" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="110">
    <text aria-hidden="true" x="{label_cx}" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="{label_text_len}" lengthAdjust="spacing">{label}</text>
    <text x="{label_cx}" y="140" transform="scale(.1)" textLength="{label_text_len}" lengthAdjust="spacing">{label}</text>
    <text aria-hidden="true" x="{value_cx}" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="{value_text_len}" lengthAdjust="spacing">{value}</text>
    <text x="{value_cx}" y="140" transform="scale(.1)" textLength="{value_text_len}" lengthAdjust="spacing">{value}</text>
  </g>
</svg>"""
