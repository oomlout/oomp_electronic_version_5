@echo off
setlocal

cd /d "%~dp0"
set "PATH=C:\Program Files\KiCad\10.0\bin;%PATH%"

echo Running the full SparkFun ADXL345 Breakout import and generation process...
echo.
where py >nul 2>nul
if not errorlevel 1 (
    py -u action_generate.py --filter oomp_project_github_sparkfun_adxl345_breakout_adxl345_breakout_current
) else (
    python -u action_generate.py --filter oomp_project_github_sparkfun_adxl345_breakout_adxl345_breakout_current
)

set "PROCESS_EXIT_CODE=%ERRORLEVEL%"
echo.
if not "%PROCESS_EXIT_CODE%"=="0" (
    echo ADXL345 generation failed with exit code %PROCESS_EXIT_CODE%.
) else (
    echo ADXL345 generation completed successfully.
)

exit /b %PROCESS_EXIT_CODE%
