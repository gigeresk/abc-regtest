# ABC-1212
## 🎤 *Is this thing on?*

This is a regression testing framework for the [ABC: System for Sequential Logic Synthesis and Formal Verification ](https://github.com/berkeley-abc/abc) synthesis framework.  The intent is to provide a framework to allow for developers of ABC to more confidently make improvements and add new features.

## Setup

if abc is on your $PATH  
```
python3 regtest_runner.py  
```
otherwise, run with:  
```
ABC_EXE=<path/to/abc> python3 regtest_runner.py
```
## Adding new tests
Add new tests in the right directory under `tests/`.  Add a `.abc` file with the abc commands you wish to test,
and a matching `.expect` file in the same directory.  The `expect` file should not be empty.
Inputs can be added under the `benchmark` directory structure. 


├── tests  
│   ├── basic  
│   │   ├── strash_basic.abc    <--- test script  
│   │   └── strash_basic.expect <--- expected output  
│   ├── bugfix      <--- when a bug is fixed  
│   ├── cec  
│   ├── errors  
│   ├── functional  
│   ├── multistep   <--- when you expect a design to behave a certain way  
│   ├── logic_opt  
│   ├── perf  
│   ├── sat  
│   ├── sequential  
│   └── techmap  

## Goals:
    - Test the command line interface into abc
    - Monitor regression of specific calls on given inputs, and *sequences* of calls
        - Quality of Result (QoR), maintained equivalence
        - Memory and runtime regression
        - Framework for abc developers to monitor specific bug fixes

### Code formatting (for abc-1212 framework maintainers)
```
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
ruff check --fix
```