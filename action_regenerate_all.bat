@echo off
setlocal
cd /d "%~dp0"
python "%~dp0action_regenerate_all.py" %*
exit /b %errorlevel%
