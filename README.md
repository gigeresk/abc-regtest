# ABC-One Two One Two
## 🎤 *Is this thing on?*

This is a regression testing framework for the [ABC: System for Sequential Logic Synthesis and Formal Verification ](https://github.com/berkeley-abc/abc)
synthesis framework.  The intent is to provide a framework to allow for developers of ABC to more confidently make improvements and add new features.

## Setup
Have a build of abc accessible on your PATH.  If you built your own abc:  
`PATH=$PATH:<path_to_abc>`

sudo apt update
sudo apt install graphviz
sudo apt install gv

*TODO: How necessary is this?  Do we depend on any third-party packages?*
Build your virtual environment and activate it:
`python3 -m venv .venv`  
`source .venv/bin/activate`

## Adding new tests
Add new tests in the right directory under `tests/`.  Add a `.abc` file with the abc commands you wish to test,
and a matching `.expect` file in the same directory.  The `expect` file should not be empty.
Inputs can be added under the `benchmark` directory structure. 

├── tests
│   ├── basic
│   │   ├── strash_basic.abc    <--- test
│   │   └── strash_basic.expect <--- expected




├── tests
│   ├── basic
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

## TODO
- Write tests (see below)
- Immediate goals:
    - read/write blif/aig/verilog tests
    - is there equivalence testing? (abc -c "cec original.blif result.blif")
    - test cec itself
- methods of validating expects outside of abc command parsing.

Longer term:
- parametrized test generation
- add test requested by Thierry
- memory regression testing
- some runtime regression testing

### Lessons

- The Verilog parser is incomplete. Effort could be made to replace it with slang (even if few people are using this frontend)