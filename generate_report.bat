@echo off
REM Script to run tests and generate Allure report (Windows)

echo ========================================
echo   EM2M Test Automation - Report Generation
echo ========================================
echo.

REM Clean previous results
if exist allure-results (
    echo Cleaning previous results...
    rd /s /q allure-results
    mkdir allure-results
)

REM Run tests with Allure formatter
echo Running tests...
behave -f allure_behave.formatter:AllureFormatter -o allure-results

REM Check if Allure is installed
where allure >nul 2>nul
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Allure CLI is not installed!
    echo Please install Allure:
    echo   1. Download from: https://github.com/allure-framework/allure2/releases
    echo   2. Extract and add to PATH
    echo   OR use: scoop install allure
    echo.
    pause
    exit /b 1
)

REM Generate report
echo.
echo Generating Allure report...
allure generate allure-results --clean -o allure-report

REM Open report
echo.
echo Opening report in browser...
allure open allure-report

pause
