import os
import re
import urllib.request
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

BASE_URL = "https://levinlawlaw.com"
PROJECT_DIR = r'c:\Users\电脑\Desktop\us.com'

def collect_all_resources():
    """Collect all resource references from all HTML files"""
    all_resources = set()
    
    html_files = [f for f in os.listdir(PROJECT_DIR) if f.endswith('.html')]
    
    for filename in html_files:
        file_path = os.path.join(PROJECT_DIR, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all wpo-minify assets
            wpo_pattern = r'(wpo-minify-[^"\']+\.(?:css|js))'
            resources = re.findall(wpo_pattern, content)
            
            for res in resources:
                all_resources.add(res)
                
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    
    return all_resources

def download_file(resource_name):
    """Download a single resource"""
    url = f"{BASE_URL}/wp-content/cache/wpo-minify/1776568923/assets/{resource_name}"
    local_dir = os.path.join(PROJECT_DIR, "wp-content", "cache", "wpo-minify", "1776568923", "assets")
    local_path = os.path.join(local_dir, resource_name)
    
    try:
        os.makedirs(local_dir, exist_ok=True)
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=60) as response:
            content = response.read()
            with open(local_path, 'wb') as out_file:
                out_file.write(content)
            
            size_kb = len(content) / 1024
            print(f"  [OK] {resource_name} ({size_kb:.1f} KB)")
            return True
    except Exception as e:
        print(f"  [FAIL] {resource_name} - {str(e)[:100]}")
        return False

def main():
    print("=" * 70)
    print("Finding and Downloading Missing Elementor Resources")
    print("=" * 70)
    
    # Step 1: Collect all resources from HTML files
    print("\n[1/3] Collecting resource references from all HTML files...")
    all_resources = collect_all_resources()
    
    print(f"Found {len(all_resources)} unique resource references:")
    for res in sorted(all_resources):
        print(f"  - {res}")
    
    # Step 2: Check which resources exist locally
    print("\n[2/3] Checking resource availability...")
    assets_dir = os.path.join(PROJECT_DIR, "wp-content", "cache", "wpo-minify", "1776568923", "assets")
    existing_assets = set(os.listdir(assets_dir)) if os.path.exists(assets_dir) else set()
    
    missing_resources = []
    existing_resources = []
    
    for res in all_resources:
        if res in existing_assets:
            existing_resources.append(res)
        else:
            missing_resources.append(res)
    
    print(f"  Existing: {len(existing_resources)}")
    print(f"  Missing: {len(missing_resources)}")
    
    # Step 3: Download missing resources
    if missing_resources:
        print(f"\n[3/3] Downloading {len(missing_resources)} missing resources...")
        success_count = 0
        
        for res in sorted(missing_resources):
            if download_file(res):
                success_count += 1
        
        print(f"\nDownload complete! Success: {success_count}/{len(missing_resources)}")
    else:
        print("\n[3/3] No missing resources - all are present!")
    
    # Final summary
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    
    if os.path.exists(assets_dir):
        final_files = os.listdir(assets_dir)
        css_files = [f for f in final_files if f.endswith('.css')]
        js_files = [f for f in final_files if f.endswith('.js')]
        
        print(f"\nTotal assets in cache: {len(final_files)}")
        print(f"  - CSS files: {len(css_files)}")
        print(f"  - JS files: {len(js_files)}")
        
        print(f"\nALL RESOURCES READY!")
        print(f"Start the local server and test any HTML file!")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
