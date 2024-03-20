#!/bin/bash

py_version=$(python --version)
matches=($(echo "$py_version" | grep -oP "\d+"))

major=${matches[0]}
minor=${matches[1]}

if [ "$major" -lt 3 ] || { [ "$major" -eq 3 ] && [ "$minor" -lt 10 ]; }; then
    echo -e "\033[91m✘ Please upgrade your Python version to 3.10 or later\033[0m"
    exit 1
fi


if [ ! -d "./.venv" ]
then
    echo -e "\033[96mCreating virtual environment (./.venv)...\033[0m"
    python -m venv ./.venv
    echo -e "\033[92m✔ Created virtual environment\033[0m"
fi

source ./.venv/bin/activate
echo -e "\033[92m✔ Activated virtual environment\033[0m"

echo -e "\n\033[96mInstalling requirements (./requirements.txt)...\033[0m"
pip install -r "./requirements.txt"

echo -e "\n\033[92m✔ Installed requirements\033[0m"
