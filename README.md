
With some python2 installed run

    ./setup.sh
    
to work on the project using CLI run

    source .venv/bin/activate
    export PYTHONPATH="${PYTHONPATH}:src"

you will then be able to run the script that takes any number of arguments

    $ pyhton src/script.py hello
    
or any any input from stdin

    $ cat my.data | pyhton src/script.py
    
or to run all tests (the project comes with a single failing one)
    
    py.test
    
To point your IDE or toolchain to the virtual env:
it is located inside `.venv` after executing `setup.sh`

Have fun.
