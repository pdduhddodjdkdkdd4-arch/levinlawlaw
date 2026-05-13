import os
import urllib.request
import ssl

# 禁用SSL验证
ssl._create_default_https_context = ssl._create_unverified_context

BASE_URL = "https://levinlawlaw.us.com"
PROJECT_DIR = r"c:\Users\电脑\Desktop\us.com"

# 收集到的所有需要的文件
ALL_RESOURCES = [
    # Header JS files
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-2e7a05c5.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-ceb60cc1.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-7aca0e30.min.js",
    
    # Footer JS files (from all pages)
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-9d54901e.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-93074a5a.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-33593826.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-a790b08d.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-869a11b8.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-39707780.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-86233e0c.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-880d38d1.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-72896553.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-fc6a3ed0.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-2e2296c8.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-e9dc3978.min.js",
    
    # Header CSS files (let's get all variations)
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-0930eedc.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-1343fea2.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-425a09df.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-453e09de.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-45eb09e6.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-466e09e0.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-46c409e4.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-47c309e4.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-4cd909e5.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-4d0109e7.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-519909ee.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-58910321.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-5a49f3a4.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-63bc1847.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-6b509528.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-aa39f485.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-b34c13d4.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-d3f7fc4f.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-e039ecd0.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-f95afe51.min.css",
    
    # Footer CSS files (all variations)
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-0cc42ac6.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-1fda20f7.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-3d9623c5.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-44f118a6.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-4e433315.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-782661d5.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-80621f3d.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-96423389.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-a9c32946.min.css",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-b77b182e.min.css",
]

def download_file(url, local_path):
    """下载单个文件"""
    try:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=60) as response:
            content = response.read()
            with open(local_path, 'wb') as out_file:
                out_file.write(content)
            
            size_kb = len(content) / 1024
            print(f"  OK {os.path.basename(local_path)} ({size_kb:.1f} KB)")
            return True
    except Exception as e:
        print(f"  ERROR {os.path.basename(local_path)} - {e}")
        return False

def main():
    print("=" * 70)
    print("  Downloading all missing Elementor resources")
    print("=" * 70)
    print()
    
    success = 0
    skipped = 0
    failed = 0
    
    for resource_path in ALL_RESOURCES:
        local_path = os.path.join(PROJECT_DIR, resource_path.replace('/', os.sep))
        
        # Check if already exists
        if os.path.exists(local_path):
            file_size = os.path.getsize(local_path)
            if file_size > 100:  # Valid if larger than 100 bytes
                print(f"SKIP: {os.path.basename(resource_path)}")
                skipped += 1
                continue
        
        # Download the file
        url = f"{BASE_URL}/{resource_path}"
        print(f"DOWNLOAD: {os.path.basename(resource_path)}")
        
        if download_file(url, local_path):
            success += 1
        else:
            failed += 1
    
    print()
    print("=" * 70)
    print(f"  Complete! Success: {success}, Skipped: {skipped}, Failed: {failed}")
    print("=" * 70)
    print()
    print("Now you can start local server!")
    print("  Windows: Double-click start_server.bat")
    print("  Then visit: https://localhost:8000")

if __name__ == "__main__":
    main()
