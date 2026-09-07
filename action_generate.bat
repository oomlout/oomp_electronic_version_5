@echo off
setlocal
cd /d "%~dp0"
python "%~dp0action_generate.py" %*
exit /b %errorlevel%
