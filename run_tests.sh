#!/bin/bash
# Shell script to run Behave tests on macOS/Linux

echo "========================================"
echo "EM2M Test Automation Framework"
echo "========================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found!"
    echo "Please create it first: python3 -m venv venv"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Run tests based on argument
if [ -z "$1" ]; then
    echo "Running all tests..."
    behave
elif [ "$1" = "smoke" ]; then
    echo "Running smoke tests..."
    behave --tags=@smoke
elif [ "$1" = "login" ]; then
    echo "Running login tests..."
    behave features/login.feature
elif [ "$1" = "assets" ]; then
    echo "Running assets tests..."
    behave features/assets.feature
elif [ "$1" = "report" ]; then
    echo "Running tests with Allure report..."
    behave -f allure_behave.formatter:AllureFormatter -o allure-results
    allure serve allure-results
else
    echo "Running tests with tag: $1"
    behave --tags=@$1
fi

echo ""
echo "========================================"
echo "Test execution complete!"
echo "========================================"
