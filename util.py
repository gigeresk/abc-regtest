import os
import re
import subprocess


class Colors:
    # Reset
    Color_Off='\033[0m'       # Text Reset

    # Regular Colors
    Red='\033[0;31m'          # Red
    Green='\033[0;32m'        # Green
    Yellow='\033[0;33m'       # Yellow

class Level:
    RUN = Colors.Green + "[RUN]" + Colors.Color_Off
    WARN = Colors.Yellow + "[WARN]" + Colors.Color_Off
    PASS = Colors.Green + "[PASS]" + Colors.Color_Off
    FAIL = Colors.Red + "[FAIL]" + Colors.Color_Off

def remove_ansi_codes(s):
    '''abc returns with colors'''
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', s)

def print_command_coverage():
    '''Print how many commands available through `help` are not covered'''
    def get_all_abc_commands() -> set:

        proc = subprocess.run(
            ["./../abc/abc", "-q", "help"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        all_abc_commands = set()
        for line in proc.stdout.strip().splitlines():
            # Extract words that look like commands (e.g., &abc, :cmd, %cmd, |cmd, cmd)
            if line.startswith("Welcome to ABC"):
                continue
            if "commands:" in line:
                continue
            parts = line.strip().split()
            for part in parts:
                all_abc_commands.add(part)

        return all_abc_commands


    def get_covered_abc_commands() -> set:
        # TODO also support .abc with ';'
        covered_abc_commands = set()

        for root, dirs, files in os.walk("tests/"):
            for filename in files:
                if filename.endswith(".abc"):
                    filepath = os.path.join(root, filename)
                    with open(filepath, "r") as f:
                        for line in f:
                            stripped = line.strip()
                            if stripped:
                                command = stripped.split()[0]
                                covered_abc_commands.add(command)

        return covered_abc_commands
        
    all_abc_commands = get_all_abc_commands()
    covered_abc_commands = get_covered_abc_commands()

    uncovered_abc_commands = all_abc_commands - covered_abc_commands

    if len(uncovered_abc_commands) > 0:
        print(f"{Level.WARN} There are {len(uncovered_abc_commands)}/{len(all_abc_commands)} ABC commands with no coverage.\n")