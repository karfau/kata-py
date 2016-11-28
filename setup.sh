#!/usr/bin/bash

pip install virtualenv &&\
virtualenv -p python2 .venv &&\
source .venv/bin/activate &&\
pip nstall -r requirements.txt
cat README.md
