import os
import re

print("=" * 60)
print("  Fixing absolute paths in all HTML files")
print("=" * 60)

# 项目目录
project_dir = r"c:\Users\电脑\Desktop\us.com"

# 获取所有HTML文件
html_files = [f for f in os.listdir(project_dir) if f.endswith('.html')]
print(f"\nFound {len(html_files)} HTML files")

fixed_count = 0

for filename in html_files:
    filepath = os.path.join(project_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # 修复所有 /wp-content/... 为 wp-content/...
        # 1. 修复 href="/wp-content
        content = re.sub(r'href=["\']/wp-content/', r'href="wp-content/', content)
        
        # 2. 修复 src="/wp-content
        content = re.sub(r'src=["\']/wp-content/', r'src="wp-content/', content)
        
        # 3. 修复 _assetsURL:"/wp-content
        content = re.sub(r'"_assetsURL":"\/wp-content/', r'"_assetsURL":"wp-content/', content)
        
        # 检查是否有变化
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Fixed: {filename}")
            fixed_count += 1
        else:
            print(f"[SKIP] No changes: {filename}")
            
    except Exception as e:
        print(f"[ERROR] Failed {filename}: {e}")

print("\n" + "=" * 60)
print(f"  Done! Fixed {fixed_count} files")
print("=" * 60)
print("\nNow you can:")
print("1. Double-click start_server.bat to start local server")
print("2. Visit https://localhost:8000 to see all pages")
