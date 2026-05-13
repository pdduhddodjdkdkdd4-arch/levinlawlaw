import os
import re

PROJECT_DIR = r"c:\Users\电脑\Desktop\us.com"
ASSETS_DIR = os.path.join(PROJECT_DIR, "wp-content", "cache", "wpo-minify", "1776568923", "assets")

def check_html_page(filename):
    filepath = os.path.join(PROJECT_DIR, filename)
    
    missing_resources = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract all resource filenames
        pattern = r'(wpo-minify-[^"\']+\.(?:css|js))'
        resources = re.findall(pattern, content)
        
        for resource in set(resources):
            resource_path = os.path.join(ASSETS_DIR, resource)
            if not os.path.exists(resource_path):
                missing_resources.append(resource)
            else:
                file_size = os.path.getsize(resource_path)
                if file_size < 100:
                    missing_resources.append(resource + " (empty)")
        
    except Exception as e:
        print(f"Error checking {filename}: {e}")
    
    return missing_resources

def main():
    print("=" * 70)
    print("  Verifying all HTML pages have their resources")
    print("=" * 70)
    print()
    
    html_files = [f for f in os.listdir(PROJECT_DIR) if f.endswith('.html')]
    
    all_good = True
    
    for filename in sorted(html_files):
        missing = check_html_page(filename)
        
        if missing:
            all_good = False
            print(f"[FAIL] {filename}:")
            for res in missing:
                print(f"   Missing: {res}")
        else:
            print(f"[OK] {filename}: OK")
    
    print()
    print("=" * 70)
    
    # Final asset count
    if os.path.exists(ASSETS_DIR):
        final_files = [f for f in os.listdir(ASSETS_DIR) if os.path.isfile(os.path.join(ASSETS_DIR, f))]
        css_files = [f for f in final_files if f.endswith('.css')]
        js_files = [f for f in final_files if f.endswith('.js')]
        print()
        print(f"Total assets: {len(final_files)}")
        print(f"  CSS files: {len(css_files)}")
        print(f"  JS files: {len(js_files)}")
    
    print()
    if all_good:
        print("[SUCCESS] All resources are ready!")
        print()
        print("You can now:")
        print("  1. Double-click start_server.bat to start server")
        print("  2. Visit https://localhost:8000 in your browser")
    else:
        print("[WARNING] Some resources are still missing!")

if __name__ == "__main__":
    main()
