#!/usr/bin/env bash
# POSIX shell setup script for Unix / WSL / macOS
# Run from project root (where manage.py lives):
#   bash scripts/setup_env.sh

set -euo pipefail

echo "Creating virtual environment at .venv..."
python3 -m venv .venv

echo "Activating virtual environment..."
# shellcheck disable=SC1091
source .venv/bin/activate

echo "Upgrading pip and installing requirements..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Done. Activate with: 'source .venv/bin/activate' and run 'python manage.py runserver'"
