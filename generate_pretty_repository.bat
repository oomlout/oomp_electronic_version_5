@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel% equ 0 (
    py -3 generate_pretty_repository.py --config pretty_repository_config.json %*
) else (
    python generate_pretty_repository.py --config pretty_repository_config.json %*
)

if errorlevel 1 (
    echo.
    echo Pretty repository generation failed.
    exit /b 1
)

echo.
echo Pretty repository generation complete.
endlocal
