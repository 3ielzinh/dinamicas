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
echo "Step 4: Running database migrations..."
python manage.py migrate --noinput

echo ""
echo "Step 5: Setting up Django Site..."
python manage.py setup_site

echo ""
echo "===================================="
echo "Build completed successfully!"
echo "===================================="
