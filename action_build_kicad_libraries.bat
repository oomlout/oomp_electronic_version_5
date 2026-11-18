@echo off
cd /d "%~dp0"
python -m kicad_agents.kicad_library_agent %*
if errorlevel 1 exit /b 1
