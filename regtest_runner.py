import subprocess
import os
    
from util import Level
import util

# TODO check that abc is on path
# TODO could strip lines that start with #? 
# TODO convert all tabs and spaces to one space
# TODO flake8
# TODO command line arg to only run under certain dirs
# TODO return how many tests were skipped

# TODO handle error output (stderr) in expects

# https://people.eecs.berkeley.edu/~alanmi/abc/abc.htm
DEBUG_OUTPUT_STRING = False

def run_test(script_file):


    expected_file = script_file.replace('.abc', '.expect')
    with open(script_file) as f:
        cmd = f.read()  # TODO

    proc = subprocess.run(
        ["./../abc/abc", "-f", script_file],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if proc.stderr:
        print(f"{Level.FAIL} {proc.stderr}")

    # TODO: remove comments from got and expected

    if os.path.exists(expected_file):
        
        with open(expected_file) as f:
            expected = f.read().strip()
            expected = util.remove_comment_lines(expected)
            expected = util.normalize_whitespace(expected)

        got = util.remove_ansi_codes(proc.stdout.strip())
        got = util.remove_comment_lines(got)
        got = util.normalize_whitespace(got)

        if expected not in got:
            print(f"{Level.FAIL} {script_file}")
            print(f"Expected:\n'{expected}'")
            print(f"Got:\n'{got}'")
        elif expected == "":
            print(f"{Level.WARN} Empty .expect file for {script_file}")
        else:
            print(f"{Level.PASS} {script_file}")

        if(DEBUG_OUTPUT_STRING):
            print(repr(got))
            print(repr(expected))
    else:
        print(f"{Level.WARN} No .expect file for {script_file}")
        
        # TODO temp
        got = util.remove_ansi_codes(proc.stdout.strip())
        print(got)


def main():
    util.print_command_coverage()
    
    for root, dirs, files in os.walk("tests/"):
        for file in files:
            if file.endswith(".abc"):
                run_test(os.path.join(root, file))

if __name__ == "__main__":
    main()
