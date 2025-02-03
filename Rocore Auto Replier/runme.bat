@echo off
title Discord Status Rotator
color 0A
cls

echo ======================================================
echo         Rocore Discord Status Rotator
echo ======================================================
echo.

:: Install required Python packages (if not already installed)
echo Installing required packages...
pip install -r requirements.txt

:: Launch the Python script
echo Starting Auto Replier 1.0
python Replier.py

:: Pause the window so you can read any messages
pause
