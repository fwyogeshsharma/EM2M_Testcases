#!/bin/bash
# Generate and view simple HTML report without Allure CLI

echo "========================================"
echo "  EM2M - Simple HTML Report Generator"
echo "========================================"
echo

# Check if allure-results exists
if [ ! -d "allure-results" ]; then
    echo "[ERROR] No test results found!"
    echo
    echo "Please run tests first:"
    echo "  behave -f allure_behave.formatter:AllureFormatter -o allure-results"
    echo
    exit 1
fi

# Generate HTML report
echo "Generating HTML report from JSON results..."
python generate_html_report.py
