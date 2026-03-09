import argparse
import subprocess
import os

import util

# TODO convert all tabs and spaces to one space
# TODO command line arg to only run under certain dirs
# TODO handle error output (stderr) in expects
# TODO show diff
# could i run all sequential benchmarks x all recipes?

# https://people.eecs.berkeley.edu/~alanmi/abc/abc.htm
DEBUG_OUTPUT_STRING = False


def run_test(script_file: str, abc_exe: str, regen: bool = False):
    expected_file = script_file.replace(".abc", ".expect")

    proc = subprocess.run(
        [abc_exe, "-f", script_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if regen:
        with open(expected_file, "w") as f:
            stripped_content = "\n".join(
                line.strip() for line in proc.stdout.splitlines()
            )
            f.write(stripped_content)
        print(f"{util.Level.REGEN} Regolden {script_file}")
        return

    if proc.stderr:
        print(f"{util.Level.FAIL} {proc.stderr}")

    if os.path.exists(expected_file):
        with open(expected_file) as f:
            expected = f.read().strip()
            expected = util.remove_ansi_codes(expected)
            expected = util.remove_comment_lines(expected)
            expected = util.normalize_whitespace(expected)

        received = util.remove_ansi_codes(proc.stdout.strip())
        received = util.remove_comment_lines(received)
        received = util.normalize_whitespace(received)

        def aggressive_normalize(text):
            # Splits by ANY whitespace (space, tab, newline) and joins with a single space
            text = util.remove_comment_lines(text)
            # 2. Split into lines, strip each line, filter out empty lines
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            # 3. Rejoin with standard Unix newlines
            return "\n".join(lines)

        # Inside your test logic:
        expected = aggressive_normalize(util.remove_comment_lines(expected))
        received = aggressive_normalize(util.remove_comment_lines(received))
        print(f"{util.Level.RUN} Running test {script_file}")
        if expected not in received:
            print(f"DEBUG - Expected (hex): {expected.encode().hex(' ')}")
            print(f"DEBUG - Got      (hex): {received.encode().hex(' ')}")
            print(f"{util.Level.FAIL} {script_file}")
            print(f"Expected:\n'{expected}'")
            print(f"Got:\n'{received}'")
        elif expected == "":
            print(f"{util.Level.WARN} Empty .expect file for {script_file}")
        else:
            print(f"{util.Level.PASS} {script_file}")

        if DEBUG_OUTPUT_STRING:
            print(repr(received))
            print(repr(expected))
    else:
        print(f"{util.Level.WARN} No .expect file for {script_file}")

        # TODO temp
        received = util.remove_ansi_codes(proc.stdout.strip())
        print(received)


def main(regen: bool = False):
    util.print_command_coverage()

    abc_exe = util.find_abc_executable()
    print(f"Using abc executable at: {abc_exe}")

    for root, dirs, files in os.walk("tests/"):
        print("-------------- " + root + " --------------")
        for file in files:
            if file.endswith(".abc"):
                run_test(os.path.join(root, file), abc_exe, regen)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--regen",
        action="store_true",
        help="Regenerate .expect files instead of testing",
    )
    args = parser.parse_args()
    main(args.regen)
