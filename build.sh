#!/usr/bin/env bash
# exit on error
set -o errexit

echo "===================================="
echo "Starting build process..."
echo "===================================="

echo ""
echo "Step 1: Upgrading pip..."
pip install --upgrade pip

echo ""
echo "Step 2: Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Step 3: Collecting static files..."
python manage.py collectstatic --no-input

echo ""
echo "Step 4: Initializing database..."
python init_db.py

echo ""
echo "===================================="
echo "Build completed successfully!"
echo "===================================="
