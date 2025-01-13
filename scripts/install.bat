@echo off
:: Install ethosian
:: Usage:
::   .\scripts\install.bat

set "CURR_DIR=%~dp0"
set "REPO_ROOT=%~dp0.."
set "UTILS_BAT=%CURR_DIR%_utils.bat"

:main
call "%UTILS_BAT%" print_heading "Installing ethosian"

call "%UTILS_BAT%" print_heading "Installing requirements.txt"
call "%REPO_ROOT%\ethenv\Scripts\pip" install --no-deps -r "%REPO_ROOT%\requirements.txt"

call "%UTILS_BAT%" print_heading "Installing ethosian with [dev] extras"
call "%REPO_ROOT%\ethenv\Scripts\pip" install --editable "%REPO_ROOT%[dev]"

goto :eof
