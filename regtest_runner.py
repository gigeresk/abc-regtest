import subprocess
import os
    
from util import Level
import util
# TODO check that abc is on path
# TODO could strip lines that start with #? 
# TODO convert all tabs and spaces to one space
# TODO util
# TODO function that checks every single `abc >help ` command against all the functions in .abc files.


def run_test(script_file):
    expected_file = script_file.replace('.abc', '.expect')
    with open(script_file) as f:
        cmd = f.read()  # TODO

    proc = subprocess.run(
        ["./../abc/abc", "-f", script_file],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    if os.path.exists(expected_file):
        print(f"{Level.RUN} {script_file}")
        with open(expected_file) as f:
            expected = f.read().strip()

        got = util.remove_ansi_codes(proc.stdout.strip())
        if expected not in got:
            print(f"{Level.FAIL} {script_file}")
            print(f"Expected:\n'{expected}'")
            print(f"Got:\n'{got}'")
        elif expected == "":
            print(f"{Level.WARN} Empty .expect file for {script_file}")
        else:
            print(f"{Level.PASS} {script_file}")
    else:
        print(f"{Level.WARN} No .expect file for {script_file}")


def main():
    util.print_command_coverage()
    
    for root, dirs, files in os.walk("tests/"):
        for file in files:
            if file.endswith(".abc"):
                run_test(os.path.join(root, file))

if __name__ == "__main__":
    main()
