import subprocess
import os
import re

# TODO check that abc is on path
# TODO could strip lines that start with #? 
# TODO convert all tabs and spaces to one space
# TODO util

# Reset
Color_Off='\033[0m'       # Text Reset

# Regular Colors
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow

RUN = Green + "[RUN]" + Color_Off
WARN = Yellow + "[WARN]" + Color_Off
PASS = Green + "[PASS]" + Color_Off
FAIL = Red + "[FAIL]" + Color_Off

def remove_ansi_codes(s):
    '''abc returns with colors'''
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', s)

def run_test(script_file):
    expected_file = script_file.replace('.abc', '.expect')
    with open(script_file) as f:
        cmd = f.read()  # TODO

    proc = subprocess.run(
        ["./../abc/abc", "-f", script_file],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    if os.path.exists(expected_file):
        print(f"{RUN} {script_file}")
        with open(expected_file) as f:
            expected = f.read().strip()

        got = remove_ansi_codes(proc.stdout.strip())
        if expected not in got:
            print(f"{FAIL} {script_file}")
            print(f"Expected:\n'{expected}'")
            print(f"Got:\n'{got}'")
        elif expected == "":
            print(f"{WARN} Empty .expect file for {script_file}")
        else:
            print(f"{PASS} {script_file}")
    else:
        print(f"{WARN} No .expect file for {script_file}")

def main():
    for root, dirs, files in os.walk("tests/"):
        for file in files:
            if file.endswith(".abc"):
                run_test(os.path.join(root, file))

if __name__ == "__main__":
    main()
