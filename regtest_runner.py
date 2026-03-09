import subprocess
import os

import util

# TODO check that abc is on path
# TODO could strip lines that start with #? 
# TODO convert all tabs and spaces to one space
# TODO flake8
# TODO command line arg to only run under certain dirs
# TODO return how many tests were skipped
# TODO methods of validating expects outside of abc command parsing.
# TODO handle error output (stderr) in expects
# TODO show diff
# TODO sequential benchmarks
# could i run all sequential benchmarks x all recipes?

# https://people.eecs.berkeley.edu/~alanmi/abc/abc.htm
DEBUG_OUTPUT_STRING = False

def run_test(script_file, abc_exe):


    expected_file = script_file.replace('.abc', '.expect')
    with open(script_file) as f:
        cmd = f.read()  # TODO

    proc = subprocess.run(
        [abc_exe, "-f", script_file],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if proc.stderr:
        print(f"{util.Level.FAIL} {proc.stderr}")

    # TODO: remove comments from got and expected

    if os.path.exists(expected_file):
        
        with open(expected_file) as f:
            expected = f.read().strip()
            expected = util.remove_comment_lines(expected)
            expected = util.normalize_whitespace(expected)

        got = util.remove_ansi_codes(proc.stdout.strip())
        got = util.remove_comment_lines(got)
        got = util.normalize_whitespace(got)

        print(f"{util.Level.RUN} Running test {script_file}")
        if expected not in got:
            print(f"{util.Level.FAIL} {script_file}")
            print(f"Expected:\n'{expected}'")
            print(f"Got:\n'{got}'")
        elif expected == "":
            print(f"{util.Level.WARN} Empty .expect file for {script_file}")
        else:
            print(f"{util.Level.PASS} {script_file}")

        if(DEBUG_OUTPUT_STRING):
            print(repr(got))
            print(repr(expected))
    else:
        print(f"{util.Level.WARN} No .expect file for {script_file}")
        
        # TODO temp
        got = util.remove_ansi_codes(proc.stdout.strip())
        print(got)


def main():
    util.print_command_coverage()
    
    abc_exe = util.find_abc_executable()
    print(f"Using abc executable at: {abc_exe}")

    for root, dirs, files in os.walk("tests/"):
        print("-------------- "+root+" --------------")
        for file in files:
            if file.endswith(".abc"):
                run_test(os.path.join(root, file), abc_exe)

if __name__ == "__main__":
    main()
