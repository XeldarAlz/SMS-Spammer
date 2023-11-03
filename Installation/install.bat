@echo off
chcp 65001 > nul
echo Remember, if you have not installed Python, it will not be installed.
timeout /t 2 > nul
echo To install Python, double-click the Python file in the folder or download from the official site, then run this tool again.

timeout /t 7 > nul
cls
echo Installation started.
echo ///////////////////////////
timeout /t 2 > nul
pip3 install -r requirements.txt

if %errorlevel% neq 0 (
    echo Something went wrong during installation!
    pause
    exit /b
)
cls
echo Installation is completed. SMS Spammer is starting. Use it at your own risk.
timeout /t 3 > nul
cd..
python smsspammer.py

pause