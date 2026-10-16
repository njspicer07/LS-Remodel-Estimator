pyinstaller --onefile main.py

@echo off
echo ========================================
echo Deploying RemodelEstimator
echo ========================================
echo.

set "SOURCE=C:\Users\Nick\PycharmProjects\RemodelEstimator\dist"
set "DEST=\\STEMSERV2019\Users\Public\Nicks Python Tools\RemodelEstimator"

robocopy "%SOURCE%" "%DEST%" /MIR /R:2 /W:2

if %ERRORLEVEL% LEQ 7 (
    echo.
    echo ========================================
    echo Deployment successful!
    echo ========================================
) else (
    echo.
    echo ========================================
    echo Deployment FAILED!
    echo ========================================
)

pause