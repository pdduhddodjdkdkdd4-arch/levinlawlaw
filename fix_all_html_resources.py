import os
import re

# Paths
project_dir = r'c:\Users\电脑\Desktop\us.com'

# Target resources (matching index.html)
target_header_css = 'wpo-minify-header-63bc1847.min.css'
target_footer_css = 'wpo-minify-footer-44f118a6.min.css'
target_footer_js1 = 'wpo-minify-footer-9d54901e.min.js'
target_footer_js2 = 'wpo-minify-footer-93074a5a.min.js'

# Resource base path
resource_base = 'wp-content/cache/wpo-minify/1776568923/assets'

def fix_html_file(file_path):
    print(f"Processing: {os.path.basename(file_path)}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Step 1: Convert absolute URLs to local paths
    content = content.replace('/wp-content/', 'wp-content/')
    content = content.replace('https://levinlawlaw.com/', '')
    content = content.replace('src="/wp-content/', 'src="wp-content/')
    content = content.replace('href="/wp-content/', 'href="wp-content/')
    
    # Step 2: Update wpo-minify CSS/JS to match index.html
    # Find and replace header CSS
    header_css_pattern = r'wpo-minify-header-[^"\']+\.min\.css'
    content = re.sub(header_css_pattern, target_header_css, content)
    
    # Find and replace footer CSS
    footer_css_pattern = r'wpo-minify-footer-[^"\']+\.min\.css'
    content = re.sub(footer_css_pattern, target_footer_css, content)
    
    # Find and replace footer JS - we need to be careful here
    # The footer has two JS files, let's look for the pattern
    js_pattern = r'(wpo-minify-footer-[^"\']+\.min\.js)'
    js_matches = re.findall(js_pattern, content)
    
    # Replace footer JS files
    if len(js_matches) >= 2:
        # We need to replace the first two footer JS files
        content = content.replace(js_matches[0], target_footer_js1, 1)
        content = content.replace(js_matches[1], target_footer_js2, 1)
    
    # Save
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    print("=" * 70)
    print("Fixing all HTML files to use consistent Elementor resources")
    print("=" * 70)
    
    # Find all HTML files
    html_files = [f for f in os.listdir(project_dir) if f.endswith('.html')]
    
    print(f"\nFound {len(html_files)} HTML files:")
    for f in html_files:
        print(f"  - {f}")
    
    print(f"\nTarget resources (from index.html):")
    print(f"  - Header CSS: {target_header_css}")
    print(f"  - Footer CSS: {target_footer_css}")
    print(f"  - Footer JS 1: {target_footer_js1}")
    print(f"  - Footer JS 2: {target_footer_js2}")
    print("\n" + "=" * 70)
    
    # Process each file
    success_count = 0
    for html_file in html_files:
        file_path = os.path.join(project_dir, html_file)
        if fix_html_file(file_path):
            success_count += 1
    
    print("\n" + "=" * 70)
    print(f"Done! Processed {success_count}/{len(html_files)} files.")
    print("\nNext step: Check for and download missing resources.")

if __name__ == "__main__":
    main()
