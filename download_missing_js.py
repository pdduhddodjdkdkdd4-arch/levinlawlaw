import os
import urllib.request
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

BASE_URL = "https://levinlawlaw.com"
PROJECT_DIR = r"c:\Users\电脑\Desktop\us.com"

# Missing JS files from previous download
MISSING_JS = [
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-86233e0c.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-880d38d1.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-72896553.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-fc6a3ed0.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-2e2296c8.min.js",
    "wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-footer-e9dc3978.min.js",
]

def download_file(url, local_path):
    """Download a single file"""
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
            print(f"OK {os.path.basename(local_path)} ({size_kb:.1f} KB)")
            return True
    except Exception as e:
        print(f"ERROR {os.path.basename(local_path)} - {e}")
        return False

def main():
    print("=" * 60)
    print("  Downloading missing JS files")
    print("=" * 60)
    print()
    
    success = 0
    skipped = 0
    failed = 0
    
    for resource_path in MISSING_JS:
        local_path = os.path.join(PROJECT_DIR, resource_path.replace('/', os.sep))
        
        if os.path.exists(local_path):
            file_size = os.path.getsize(local_path)
            if file_size > 100:
                print(f"SKIP: {os.path.basename(resource_path)}")
                skipped += 1
                continue
        
        url = f"{BASE_URL}/{resource_path}"
        print(f"DOWNLOAD: {os.path.basename(resource_path)}")
        
        if download_file(url, local_path):
            success += 1
        else:
            failed += 1
    
    print()
    print("=" * 60)
    print(f"Complete! Success: {success}, Skipped: {skipped}, Failed: {failed}")
    print("=" * 60)

if __name__ == "__main__":
    main()
