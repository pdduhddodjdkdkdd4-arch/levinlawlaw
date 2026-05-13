import os
import re
import urllib.request
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

BASE_URL = "https://levinlawlaw.com"
PROJECT_DIR = r"c:\Users\电脑\Desktop\us.com"

def collect_all_resources():
    """Collect all referenced resources from HTML files"""
    all_resources = set()
    
    html_files = [f for f in os.listdir(PROJECT_DIR) if f.endswith('.html')]
    
    for filename in html_files:
        filepath = os.path.join(PROJECT_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find wpo-minify assets
            pattern = r'wpo-minify-[^"\']+\.(css|js)'
            matches = re.findall(pattern, content)
            
            # Also get full paths
            full_pattern = r'wp-content/cache/wpo-minify/[^"\']+\.(css|js)'
            full_matches = re.findall(full_pattern, content, re.IGNORECASE)
            
            # Extract unique filenames
            filename_pattern = r'(wpo-minify-[^"\']+\.(?:css|js))'
            filename_matches = re.findall(filename_pattern, content)
            
            for match in filename_matches:
                all_resources.add(match)
                
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    
    return all_resources

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
            print(f"  OK {os.path.basename(local_path)} ({size_kb:.1f} KB)")
            return True
    except Exception as e:
        print(f"  ERROR {os.path.basename(local_path)} - {e}")
        return False

def main():
    print("=" * 70)
    print("  Scanning all HTML files for resources")
    print("=" * 70)
    print()
    
    all_resources = collect_all_resources()
    
    print(f"Found {len(all_resources)} unique resource references")
    print()
    
    assets_dir = os.path.join(PROJECT_DIR, "wp-content", "cache", "wpo-minify", "1776568923", "assets")
    
    print("=" * 70)
    print("  Checking and downloading resources")
    print("=" * 70)
    print()
    
    success = 0
    skipped = 0
    failed = 0
    
    for filename in sorted(all_resources):
        local_path = os.path.join(assets_dir, filename)
        
        if os.path.exists(local_path):
            file_size = os.path.getsize(local_path)
            if file_size > 100:
                print(f"SKIP: {filename}")
                skipped += 1
                continue
        
        resource_path = f"wp-content/cache/wpo-minify/1776568923/assets/{filename}"
        url = f"{BASE_URL}/{resource_path}"
        print(f"DOWNLOAD: {filename}")
        
        if download_file(url, local_path):
            success += 1
        else:
            failed += 1
    
    print()
    print("=" * 70)
    print(f"  Complete! Success: {success}, Skipped: {skipped}, Failed: {failed}")
    print("=" * 70)
    print()
    print("Verifying assets...")
    
    # Count final assets
    if os.path.exists(assets_dir):
        final_files = [f for f in os.listdir(assets_dir) if os.path.isfile(os.path.join(assets_dir, f))]
        css_files = [f for f in final_files if f.endswith('.css')]
        js_files = [f for f in final_files if f.endswith('.js')]
        print(f"  Total assets: {len(final_files)}")
        print(f"  CSS files: {len(css_files)}")
        print(f"  JS files: {len(js_files)}")
    
    print()
    print("Now you can start local server!")
    print("  Windows: Double-click start_server.bat")
    print("  Then visit: https://localhost:8000")

if __name__ == "__main__":
    main()
