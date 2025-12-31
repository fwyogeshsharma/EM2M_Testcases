@echo off
REM Script to view existing Allure report

echo Generating and opening Allure report...

REM Check if results exist
if not exist allure-results (
    echo [ERROR] No test results found!
    echo Please run tests first: run_tests_with_report.bat
    pause
    exit /b 1
)

REM Check if Allure is installed
where allure >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Allure CLI is not installed!
    echo.
    echo To install Allure on Windows:
    echo   1. Install Scoop: https://scoop.sh/
    echo   2. Run: scoop install allure
    echo.
    echo OR download manually from:
    echo   https://github.com/allure-framework/allure2/releases
    pause
    exit /b 1
)

REM Generate and open report
allure generate allure-results --clean -o allure-report
allure open allure-report
