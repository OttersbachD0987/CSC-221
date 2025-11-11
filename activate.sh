#!/bin/bash

echo "Checking the Virtual Environment..."
if [ -d "./venv" ]; then
  echo "The Virtual Environment already exists."
else
  echo "The Virtual Environment does not exist, creating now."
  py -m venv venv
  echo "The Virtual Environment has been created."
fi


echo:

echo "Activating the Virtual Environment..."
source ./venv/bin/activate
echo "The Virtual Environment has been activated."
echo ""
source ./dependencies install_log.balrog
echo ""
echo "Activation has been completed."