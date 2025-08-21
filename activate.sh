#!/bin/bash

if [ -d "./venv" ]; then
  echo "venv exists."
else
  echo "venv does not exist, creating now."
  py -m venv venv
fi

source ./venv/bin/activate