
With some python2 and virtualenv installed run

    ./setup.sh
    
to work on the project using CLI run

    source .venv/bin/activate
    export PYTHONPATH="${PYTHONPATH}:src"

you will then be able to run

    pyhton src/script.py
    
and 
    
    py.test test
    
To point your IDE or toolchain to the virtual env:
it is located inside `.venv` after executing `setup.sh`

Have fun.
