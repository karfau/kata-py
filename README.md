
With some python2 installed run

    ./setup.py
    
to work on the project using CLI run

    source .venv/bin/activate
    export PYTHONPATH="${PYTHONPATH}:src"

you will then be able to run

    pyhton src/script.py
    
and 
    
    py.test test
    
Have fun.