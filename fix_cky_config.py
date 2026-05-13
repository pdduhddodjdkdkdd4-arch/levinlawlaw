import os
import re

HTML_FILES = []
for root, dirs, files in os.walk(r'c:\Users\电脑\Desktop\us.com'):
    dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'wp-content/uploads']]
    for file in files:
        if file.endswith('.html'):
            HTML_FILES.append(os.path.join(root, file))

print(f"Found {len(HTML_FILES)} HTML files")

total_fixes = 0

for file_path in HTML_FILES:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # 修复被错误替换的背景颜色
        # 模式: "background-color": "#+1 302-300-800800" 
        # 应该是: "background-color": "#000000"
        content = re.sub(
            r'"background-color":\s*"#\+1\s*302-300-800800"',
            '"background-color": "#000000"',
            content
        )
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            total_fixes += 1
            print(f"[FIXED] {os.path.basename(file_path)}")
    
    except Exception as e:
        print(f"[ERROR] {file_path}: {e}")

print(f"\nFixed {total_fixes} files")
