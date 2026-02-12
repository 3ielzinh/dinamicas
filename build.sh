#!/usr/bin/env bash
# exit on error
set -o errexit

echo "===================================="
echo "BUILD PHASE"
echo "===================================="

echo ""
echo "Upgrading pip..."
pip install --upgrade pip

echo ""
echo "Installing Python packages..."
pip install -r requirements.txt

echo ""
echo "Collecting static files..."
python manage.py collectstatic --no-input

echo ""
echo "Running migrations..."
python manage.py migrate --noinput

echo ""
echo "Setting up Django Site..."
python manage.py setup_site

echo ""
echo "===================================="
echo "Build completed!"
echo "===================================="
