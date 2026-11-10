@echo off
title Project Americas - Dev Launcher
cd /d "%~dp0"
where python >nul 2>nul || (echo Python 3.9+ is required. & pause & exit /b 1)
python tools\launcher.py %*
pause
