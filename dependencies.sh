#!/bin/bash

local ARG1 = $1

echo Installing dependencies via pip...

local RESULTS = $(pip install -r "requirements.txt")

if [ $? -eq 0 ]; then
  echo All dependencies have been installed.
else
  RESULTS > %ARG1%
  echo There was an error during the installation process, goto %ARG1% for more details.
fi

source ./venv/bin/activate