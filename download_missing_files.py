import os
import urllib.request
import ssl

# 禁用SSL证书验证（避免HTTPS错误
ssl._create_default_https_context = ssl._create_unverified_context

# 原站地址
BASE_URL = "https://levinlawlaw.us.com"

# 缺失的JS文件列表
MISSING_FILES = [
    # Header JS
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-2e7a05c5.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-ceb60cc1.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-7aca0e30.min.js",
    # Footer JS
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-9d54901e.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-93074a5a.min.js",
]

def download_file(url, local_path):
    """下载单个文件"""
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        print(f"正在下载: {url}")
        
        # 添加User-Agent避免被拦截
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=30) as response, \
             open(local_path, 'wb') as out_file:
            out_file.write(response.read())
        
        file_size = os.path.getsize(local_path)
        print(f"✅ 成功下载! 大小: {file_size} bytes")
        return True
    except Exception as e:
        print(f"❌ 下载失败: {e}")
        return False

def main():
    print("=" * 50)
    print("  Elementor 资源下载工具")
    print("=" * 50)
    print()
    
    success_count = 0
    fail_count = 0
    
    for file_path in MISSING_FILES:
        url = f"{BASE_URL}/{file_path}"
        local_path = os.path.join(os.getcwd(), file_path.replace('/', os.sep))
        
        print(f"\n处理: {file_path}")
        
        # 检查文件是否已存在
        if os.path.exists(local_path):
            file_size = os.path.getsize(local_path)
            print(f"ℹ️ 文件已存在 ({file_size} bytes)，跳过")
            success_count += 1
            continue
        
        if download_file(url, local_path):
            success_count += 1
        else:
            fail_count += 1
    
    print()
    print("=" * 50)
    print(f"下载完成! 成功: {success_count}, 失败: {fail_count}")
    print("=" * 50)
    
    if fail_count > 0:
        print("\n提示: 如果下载失败，您可以:")
        print("1. 检查网络连接")
        print("2. 手动从浏览器下载")
        print("3. 使用HTTrack等工具完整抓取网站")

if __name__ == "__main__":
    main()
