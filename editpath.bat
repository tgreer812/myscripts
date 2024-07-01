@echo off
setlocal

echo Opening Environment Variables...

REM Using PowerShell to open the System Properties window directly at the Environment Variables section
powershell -Command "Start-Process 'rundll32.exe' -ArgumentList 'sysdm.cpl,EditEnvironmentVariables'"

endlocal
