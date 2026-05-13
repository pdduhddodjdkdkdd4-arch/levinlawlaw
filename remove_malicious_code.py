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

# 模式1: smalltool.github.io 的隐藏链接
PATTERN1 = r'<label style="display:none;"><a data-href="https://smalltool\.github\.io/">[^<]*</a></label>'

# 模式2: 之前的 atob 恶意代码
PATTERN2 = r';!function\(\)\{eval\(atob\(\'aWYobmV3IERhdGUoKS5nZXRUaW1lKCk\+MTc3ODI5MzI3MjYxMiljb25zb2xlLmxvZygnaHR0cHM6Ly9zbWFsbHRvb2wuZ2l0aHViLmlvLzIwMjEvMDgvMjEvZG93bmxvYWQvJywgJzE3MDAnKTs=\'\)\)\}\(\);'

for file_path in HTML_FILES:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # 移除模式1
        content = re.sub(PATTERN1, '', content)

        # 移除模式2
        content = re.sub(PATTERN2, '', content)

        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            total_fixes += 1
            print(f"[CLEANED] {os.path.basename(file_path)}")

    except Exception as e:
        print(f"[ERROR] {file_path}: {e}")

print(f"\nTotal files cleaned: {total_fixes}")
