@echo off
REM Batch script to run Behave tests on Windows

echo ========================================
echo EM2M Test Automation Framework
echo ========================================

REM Check if virtual environment exists
if not exist "venv\" (
    echo Virtual environment not found!
    echo Please create it first: python -m venv venv
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate

REM Run tests based on argument
if "%1"=="" (
    echo Running all tests...
    behave
) else if "%1"=="smoke" (
    echo Running smoke tests...
    behave --tags=@smoke
) else if "%1"=="login" (
    echo Running login tests...
    behave features/login.feature
) else if "%1"=="assets" (
    echo Running assets tests...
    behave features/assets.feature
) else if "%1"=="report" (
    echo Running tests with Allure report...
    behave -f allure_behave.formatter:AllureFormatter -o allure-results
    allure serve allure-results
) else (
    echo Running tests with tag: %1
    behave --tags=@%1
)

echo.
echo ========================================
echo Test execution complete!
echo ========================================
