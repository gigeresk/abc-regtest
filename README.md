# ABC-1212
[![Regression Tests](https://github.com/gigeresk/abc-1212/actions/workflows/regression-tests.yml/badge.svg)](https://github.com/gigeresk/abc-1212/actions/workflows/regression-tests.yml)
[![ABC command coverage](https://raw.githubusercontent.com/gigeresk/abc-1212/main/badges/command_coverage.svg)](https://github.com/gigeresk/abc-1212/actions/workflows/regression-tests.yml)

## Overview

This is a regression testing framework for the [ABC: System for Sequential Logic Synthesis and Formal Verification ](https://github.com/berkeley-abc/abc) synthesis framework.  The intent is to provide a framework to allow for developers of ABC to more confidently make improvements and add new features.

## Setup

If ABC is on your $PATH
```
python3 regtest_runner.py
```
otherwise, run with:
```
ABC_EXE=<path/to/abc> python3 regtest_runner.py
```

## Output

Each test prints one of:
- `[PASS]` — output matches the `.expect` file
- `[FAIL]` — output differs; expected and actual values are printed
- `[WARN]` — no `.expect` file found, or `.expect` file is empty

To regenerate `.expect` files after an intentional output change:
```
python3 regtest_runner.py --regen
```

## Adding new tests
Add new tests in the right directory under `tests/`.  Add a `.abc` file with the abc commands you wish to test,
and a matching `.expect` file in the same directory.  The `expect` file should not be empty.
Inputs can be added under the `benchmark` directory structure.

```
├── tests
│   ├── basic
│   │   ├── strash_basic.abc    <--- test script
│   │   └── strash_basic.expect <--- expected output
│   ├── bugfix      <--- when a bug is fixed
│   └── multistep   <--- when you expect a design to behave a certain way
```

## Goals
- Test the command line interface into ABC
- Monitor regression of specific calls on given inputs, and *sequences* of calls
  - Quality of Result (QoR), maintained equivalence
  - Memory and runtime regression
  - Framework for ABC developers to monitor specific bug fixes

## Code formatting (for abc-1212 framework maintainers)
```
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
ruff check --fix
```
