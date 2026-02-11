#!/usr/bin/env bash
# exit on error
set -o errexit

echo "===================================="
echo "BUILD PHASE - Installing dependencies"
echo "===================================="

echo ""
echo "Upgrading pip..."
pip install --upgrade pip

echo ""
echo "Installing Python packages..."
pip install -r requirements.txt

echo ""
echo "===================================="
echo "Build completed!"
echo "Migrations and static files will be"
echo "handled in the start command."
echo "===================================="
