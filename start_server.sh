#!/bin/bash
echo "========================================"
echo "   Elementor Static Website - 本地服务器"
echo "========================================"
echo ""
echo "正在启动本地服务器..."
echo "服务器将在 https://localhost:8000 运行"
echo "按 Ctrl+C 停止服务器"
echo ""

# 尝试使用Python 3
if command -v python3 &> /dev/null; then
    python3 -m http.server 8000
elif command -v python &> /dev/null; then
    python -m http.server 8000
else
    echo "错误：未找到Python，请先安装Python"
    exit 1
fi
