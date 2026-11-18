@echo off
setlocal
pushd "%~dp0"
if errorlevel 1 exit /b 1
python "%~dp0working_drawer_labels.py" %*
set "label_exit=%errorlevel%"
popd
if not "%label_exit%"=="0" echo Drawer label generation failed. See the error above.
exit /b %label_exit%
