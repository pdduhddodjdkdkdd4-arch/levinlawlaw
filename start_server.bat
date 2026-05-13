@echo off
echo ========================================
echo    Elementor Static Website - 本地服务器
echo ========================================
echo.
echo 正在启动本地服务器...
echo 服务器将在 https://localhost:8000 运行
echo 按 Ctrl+C 停止服务器
echo.
python -m http.server 8000
pause
