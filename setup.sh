#!/bin/bash

# Ensure dependencies are installed
if ! command -v git &> /dev/null
then
	echo "git could not be found"
	exit
fi

if ! command -v python3 &> /dev/null
then
	echo "python3 could not be found"
	exit
fi

# Update check
if [ -d ".git" ]; then
	git pull
fi

# Install dependencies
if [ -f "requirements.txt" ]; then
	python3 -m pip install -Ur requirements.txt
fi

# Launch setup.py
python3 setup.py
