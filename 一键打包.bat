@echo off
chcp 65001 > nul

set APP_NAME=音乐播放器
set ICON_FILE=app.ico
set MAIN_SCRIPT=webview_app.py
set VERSION_FILE=version_info.txt

pyinstaller --onefile --windowed --add-data "index.html;." --name "%APP_NAME%" --icon="%ICON_FILE%" --version-file="%VERSION_FILE%" %MAIN_SCRIPT%

echo 打包完成！输出文件：dist\%APP_NAME%.exe
pause