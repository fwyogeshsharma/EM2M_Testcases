#!/bin/bash
# Cleanup script for temporary and debug files

echo "Cleaning up temporary files..."

# Remove debug/inspection scripts
rm -f inspect_*.py
rm -f debug_*.py
rm -f check_*.py
rm -f find_*.py

# Remove temporary screenshots
rm -f error_screenshot.png
rm -f dropdown_screenshot.png
rm -f test_*.png

# Remove Python cache
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null

# Clean old reports (optional - comment out if you want to keep reports)
# rm -rf reports/screenshots/*

echo "Cleanup complete!"
