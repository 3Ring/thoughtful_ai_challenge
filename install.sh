#!/bin/bash

py_version=$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1,2)

if [ "$(echo "$py_version < 3.11" | bc)" -eq 1 ]; then
    echo "requires python 3.11 or higher"
    exit 1
else
    echo "python version is $py_version"
fi
if [ ! -d "thoughtful_venv" ]; then
    python -m venv thoughtful_venv
else
    echo "virtual environment already exists"
fi
source thoughtful_venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt