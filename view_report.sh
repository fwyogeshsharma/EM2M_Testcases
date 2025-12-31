#!/bin/bash
# Script to view existing Allure report

echo "Generating and opening Allure report..."

# Check if results exist
if [ ! -d "allure-results" ]; then
    echo "[ERROR] No test results found!"
    echo "Please run tests first: ./run_tests_with_report.sh"
    exit 1
fi

# Check if Allure is installed
if ! command -v allure &> /dev/null; then
    echo "[ERROR] Allure CLI is not installed!"
    echo
    echo "To install Allure:"
    echo "  Mac: brew install allure"
    echo "  Linux: Download from https://github.com/allure-framework/allure2/releases"
    echo
    exit 1
fi

# Generate and open report
allure generate allure-results --clean -o allure-report
allure open allure-report
