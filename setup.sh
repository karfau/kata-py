#!/bin/bash

pip install virtualenv &&\
virtualenv -p python2 .venv &&\
source .venv/bin/activate &&\
pip install -r requirements.txt
cat README.md
