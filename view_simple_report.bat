@echo off
REM Generate and view simple HTML report without Allure CLI

echo ========================================
echo   EM2M - Simple HTML Report Generator
echo ========================================
echo.

REM Check if allure-results exists
if not exist allure-results (
    echo [ERROR] No test results found!
    echo.
    echo Please run tests first:
    echo   behave -f allure_behave.formatter:AllureFormatter -o allure-results
    echo.
    pause
    exit /b 1
)

REM Generate HTML report
echo Generating HTML report from JSON results...
python generate_html_report.py

pause
