#!/bin/bash
# Script to run tests and generate Allure report (Linux/Mac)

echo "========================================"
echo "  EM2M Test Automation - Report Generation"
echo "========================================"
echo

# Clean previous results
if [ -d "allure-results" ]; then
    echo "Cleaning previous results..."
    rm -rf allure-results
fi
mkdir -p allure-results

# Run tests with Allure formatter
echo "Running tests..."
behave -f allure_behave.formatter:AllureFormatter -o allure-results

# Check if Allure is installed
if ! command -v allure &> /dev/null; then
    echo
    echo "[ERROR] Allure CLI is not installed!"
    echo "Please install Allure:"
    echo "  Mac: brew install allure"
    echo "  Linux: Download from https://github.com/allure-framework/allure2/releases"
    echo
    exit 1
fi

# Generate report
echo
echo "Generating Allure report..."
allure generate allure-results --clean -o allure-report

# Open report
echo
echo "Opening report in browser..."
allure open allure-report
