# ABC-One Two One Two
## 🎤 *Is this thing on?*

This is a regression testing framework for the [ABC: System for Sequential Logic Synthesis and Formal Verification ](https://github.com/berkeley-abc/abc) synthesis framework.  The intent is to provide a framework to allow for developers of ABC to more confidently make improvements and add new features.

## Setup
Have a build of abc accessible on your `$PATH`.  If you built your own abc:  
`PATH=$PATH:<path_to_abc>`

```
sudo apt update
sudo apt install graphviz
sudo apt install gv
```
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

## TODO
- Goals:
    - Test the command line interface into abc
    - Monitor regression of specific calls on given inputs, and *sequences* of calls
        - Quality of Result (QoR), maintained equivalence
        - Memory and runtime regression
        - Framework for abc developers to monitor specific bug fixes

### Lessons

- The Verilog parser is incomplete. Effort could be made to replace it with slang (even if few people are using this frontend)