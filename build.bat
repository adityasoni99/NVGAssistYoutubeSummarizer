@echo off
REM Build script for G-Assist YouTube Summarizer plugin

echo [*] Cleaning old build...
rmdir /s /q build
rmdir /s /q dist

echo [*] Creating new build...
pyinstaller yt.spec

echo [*] Build completed. Executable is in dist\youtube_summarizer_plugin.exe
pause
