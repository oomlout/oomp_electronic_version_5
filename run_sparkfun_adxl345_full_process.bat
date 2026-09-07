@echo off
setlocal

cd /d "%~dp0"
set "PATH=C:\Program Files\KiCad\10\bin;%PATH%"
set "OOMP_KICAD_ROOT=C:\Program Files\KiCad\10"
set "KICAD_PYTHON=C:\Program Files\KiCad\10\bin\python.exe"

kicad-cli --help | findstr /r /c:"^[ ]*import[ ]" >nul
if errorlevel 1 (
    echo This Eagle pipeline requires a KiCad CLI version with the top-level "import" command.
    echo Install a newer KiCad build, then run this batch file again.
    exit /b 1
)

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
