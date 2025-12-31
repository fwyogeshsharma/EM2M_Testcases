@echo off
REM Cleanup script for temporary and debug files

echo Cleaning up temporary files...

REM Remove debug/inspection scripts
del /Q inspect_*.py 2>nul
del /Q debug_*.py 2>nul
del /Q check_*.py 2>nul
del /Q find_*.py 2>nul

REM Remove temporary screenshots
del /Q error_screenshot.png 2>nul
del /Q dropdown_screenshot.png 2>nul
del /Q test_*.png 2>nul

REM Remove Python cache
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
del /Q *.pyc 2>nul

REM Clean old reports (optional - comment out if you want to keep reports)
REM rd /s /q reports\screenshots 2>nul
REM mkdir reports\screenshots

echo Cleanup complete!
pause
