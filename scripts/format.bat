@echo off

:: Formats ethosian

:: Usage:
:: .\scripts\format.bat

set "CURR_DIR=%~dp0"
set "REPO_ROOT=%~dp0.."

:: Ensure that _utils.bat is correctly located and called
set "UTILS_BAT=%CURR_DIR%_utils.bat"

:main
call "%UTILS_BAT%" print_heading "Formatting ethosian"

call "%UTILS_BAT%" print_heading "Running: ruff format %REPO_ROOT%"
call "%REPO_ROOT%\ethenv\Scripts\ruff" format "%REPO_ROOT%"
if %ERRORLEVEL% neq 0 (
    echo Failed to format with ruff.
    goto :eof
)

call "%UTILS_BAT%" print_heading "Running: ruff check %REPO_ROOT%"
call "%REPO_ROOT%\ethenv\Scripts\ruff" check "%REPO_ROOT%"
if %ERRORLEVEL% neq 0 (
    echo Failed ruff check.
    goto :eof
)

call "%UTILS_BAT%" print_heading "Running: mypy %REPO_ROOT%"
call "%REPO_ROOT%\ethenv\Scripts\mypy" "%REPO_ROOT%"
if %ERRORLEVEL% neq 0 (
    echo Failed mypy check.
    goto :eof
)

call "%UTILS_BAT%" print_heading "Running: pytest %REPO_ROOT%"
call "%REPO_ROOT%\ethenv\Scripts\pytest" "%REPO_ROOT%"
if %ERRORLEVEL% neq 0 (
    echo Failed pytest.
    goto :eof
)

goto :eof