import os
import urllib.request
import ssl
import time

# 禁用SSL证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# 配置
BASE_URL = "https://levinlawlaw.us.com"
DOWNLOAD_DIR = os.getcwd()

# 所有需要的文件
ALL_FILES = [
    # Header JS
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-2e7a05c5.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-ceb60cc1.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-7aca0e30.min.js",
    
    # Footer JS
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-9d54901e.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-93074a5a.min.js",
]

def download_file(url, local_path, max_retries=3):
    """带重试的文件下载"""
    for attempt in range(max_retries):
        try:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            print(f"[{attempt+1}/{max_retries}] 正在下载: {os.path.basename(local_path)}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            req = urllib.request.Request(url, headers=headers)
            
            with urllib.request.urlopen(req, timeout=60) as response:
                content = response.read()
                with open(local_path, 'wb') as out_file:
                    out_file.write(content)
                
                file_size = len(content)
                print(f"   ✅ 成功! 大小: {file_size:,} bytes")
                return True
                
        except Exception as e:
            print(f"   ❌ 尝试 {attempt+1} 失败: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
    
    return False

def main():
    print("=" * 60)
    print("  Elementor 完整资源下载工具")
    print("=" * 60)
    print()
    print(f"目标网站: {BASE_URL}")
    print(f"下载数量: {len(ALL_FILES)} 个文件")
    print()
    
    success = 0
    failed = 0
    skipped = 0
    
    for file_path in ALL_FILES:
        url = f"{BASE_URL}/{file_path}"
        local_path = os.path.join(DOWNLOAD_DIR, file_path.replace('/', os.sep))
        
        print(f"\n{'='*60}")
        print(f"处理: {file_path}")
        print(f"{'='*60}")
        
        # 检查是否已存在
        if os.path.exists(local_path):
            size = os.path.getsize(local_path)
            if size > 0:
                print(f"ℹ️ 文件已存在且有效 ({size:,} bytes)")
                skipped += 1
                continue
            else:
                print(f"⚠️ 文件存在但为空，重新下载")
        
        # 下载
        if download_file(url, local_path):
            success += 1
        else:
            failed += 1
    
    # 统计
    print()
    print("=" * 60)
    print("  下载完成统计")
    print("=" * 60)
    print(f"✅ 成功: {success}")
    print(f"⏭️ 跳过: {skipped}")
    print(f"❌ 失败: {failed}")
    print("=" * 60)
    
    # 验证
    print("\n📁 验证文件...")
    all_good = True
    for file_path in ALL_FILES:
        local_path = os.path.join(DOWNLOAD_DIR, file_path.replace('/', os.sep))
        if os.path.exists(local_path) and os.path.getsize(local_path) > 100:
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} (缺失或过小)")
            all_good = False
    
    if all_good:
        print("\n🎉 所有资源已就绪！现在可以启动本地服务器测试了！")
        print("   双击 start_server.bat 或运行: python -m http.server 8000")
    else:
        print("\n⚠️ 部分文件缺失，请尝试重新下载或手动获取")

if __name__ == "__main__":
    main()
