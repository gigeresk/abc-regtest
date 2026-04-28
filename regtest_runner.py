import argparse
import os
import subprocess
import sys

import command_coverage
import util


# https://people.eecs.berkeley.edu/~alanmi/abc/abc.htm
DEBUG_OUTPUT_STRING = False

def process_abc_output(output: str) -> str:
    # Remove ANSI color codes
    output = util.remove_ansi_codes(output)
    # Remove comment lines (lines starting with //)
    output = util.remove_comment_lines(output)
    # Normalize whitespace (convert multiple spaces/tabs to a single space, and trim)
    output = util.normalize_whitespace(output)
    return output.strip()

def run_test(script_file: str, abc_exe: str, regen: bool = False) -> bool:
    """Returns True if the test passed, False if it failed."""
    expected_file = script_file.replace(".abc", ".expect")

    proc = subprocess.run(
        [abc_exe, "-f", script_file],
        capture_output=True,
        text=True,
    )

    if regen:
        print(f"{util.Level.REGEN} Regolden {script_file}")

        with open(expected_file, "w") as f:
            f.write(process_abc_output(proc.stdout))

        return True

    if proc.stderr:
        print(f"{util.Level.FAIL} {proc.stderr}")

    if os.path.exists(expected_file):
        with open(expected_file) as f:
            expected = process_abc_output(f.read())

        received = process_abc_output(proc.stdout.strip())

        def aggressive_normalize(text):
            # Splits by ANY whitespace (space, tab, newline)
            # and joins with a single space
            text = util.remove_comment_lines(text)
            # 2. Split into lines, strip each line, filter out empty lines
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            # 3. Rejoin with standard Unix newlines
            return "\n".join(lines)

        expected = aggressive_normalize(util.remove_comment_lines(expected))
        received = aggressive_normalize(util.remove_comment_lines(received))
        print(f"{util.Level.RUN} Running test {script_file}")
        if expected not in received:
            print(f"DEBUG - Expected (hex): {expected.encode().hex(' ')}")
            print(f"DEBUG - Got      (hex): {received.encode().hex(' ')}")
            print(f"{util.Level.FAIL} {script_file}")
            print(f"Expected:\n'{expected}'")
            print(f"Got:\n'{received}'")
            return False
        elif expected == "":
            print(f"{util.Level.WARN} Empty .expect file for {script_file}")
        else:
            print(f"{util.Level.PASS} {script_file}")

        if DEBUG_OUTPUT_STRING:
            print(repr(received))
            print(repr(expected))
        return True
    else:
        print(f"{util.Level.WARN} No .expect file for {script_file}")

        # TODO temp
        received = util.remove_ansi_codes(proc.stdout.strip())
        print(received)
        return True


def main(regen: bool = False, badge_path: str | None = None):
    command_coverage.print_command_coverage()

    if badge_path is not None:
        covered, total = command_coverage.get_command_coverage()
        svg = command_coverage.generate_coverage_badge_svg(covered, total)
        os.makedirs(os.path.dirname(badge_path) or ".", exist_ok=True)
        with open(badge_path, "w") as f:
            f.write(svg)
        print(f"Coverage badge written to {badge_path}")

    abc_exe = util.find_abc_executable()
    print(f"Using abc executable at: {abc_exe}")

    all_passed = True
    for root, dirs, files in os.walk("tests/"):
        print("-------------- " + root + " --------------")
        for file in files:
            if file.endswith(".abc"):
                passed = run_test(os.path.join(root, file), abc_exe, regen)
                if not passed:
                    all_passed = False

    if not all_passed:
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--regen",
        action="store_true",
        help="Regenerate .expect files instead of testing",
    )
    parser.add_argument(
        "--badge",
        metavar="PATH",
        help="Write a coverage badge SVG to this path (e.g. badges/command_coverage.svg)",
    )
    args = parser.parse_args()
    main(args.regen, args.badge)
