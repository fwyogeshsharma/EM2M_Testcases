@echo off
REM Quick script to run tests and generate report

echo Running tests with Allure reporting...
echo.

REM Run tests
behave -f allure_behave.formatter:AllureFormatter -o allure-results --tags=@smoke

echo.
echo Tests completed! Run 'view_report.bat' to see the results.
pause
