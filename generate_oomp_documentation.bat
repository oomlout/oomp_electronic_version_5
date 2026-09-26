@echo off
setlocal

set "OOMP_TOOL_ROOT=%~dp0"
set "OOMP_SOURCE_DIRECTORY=%CD%"

echo Generating OOMP documentation for:
echo   "%OOMP_SOURCE_DIRECTORY%"
echo.

if exist "%OOMP_TOOL_ROOT%.venv\Scripts\python.exe" (
    "%OOMP_TOOL_ROOT%.venv\Scripts\python.exe" -u "%OOMP_TOOL_ROOT%kicad_agents\standalone_documentation_action.py" --source "%OOMP_SOURCE_DIRECTORY%" %*
    set "OOMP_EXIT_CODE=%ERRORLEVEL%"
    goto :finished
)

where py >nul 2>nul
if not errorlevel 1 (
    py -3 -u "%OOMP_TOOL_ROOT%kicad_agents\standalone_documentation_action.py" --source "%OOMP_SOURCE_DIRECTORY%" %*
    set "OOMP_EXIT_CODE=%ERRORLEVEL%"
    goto :finished
)

where python >nul 2>nul
if not errorlevel 1 (
    python -u "%OOMP_TOOL_ROOT%kicad_agents\standalone_documentation_action.py" --source "%OOMP_SOURCE_DIRECTORY%" %*
    set "OOMP_EXIT_CODE=%ERRORLEVEL%"
    goto :finished
)

echo ERROR: Python 3 was not found. Install Python or create the repository .venv.
set "OOMP_EXIT_CODE=1"

:finished
echo.
if not "%OOMP_EXIT_CODE%"=="0" echo Documentation generation failed with exit code %OOMP_EXIT_CODE%.
exit /b %OOMP_EXIT_CODE%
