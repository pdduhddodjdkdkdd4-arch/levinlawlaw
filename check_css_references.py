
import os
import re

project_root = r'c:\Users\电脑\Desktop\us.com'
css_files = [
    'wpo-minify-header-b34c13d4.min.css',
    'wpo-minify-header-b65513ef.min.css',
    'wpo-minify-header-63bc1847.min.css'
]

html_files = []
for root, dirs, files in os.walk(project_root):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

print(f"找到 {len(html_files)} 个HTML文件")
print()

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    references = []
    for css in css_files:
        if css in content:
            references.append(css)
    
    if references:
        relative_path = os.path.relpath(html_file, project_root)
        print(f"{relative_path}:")
        for ref in references:
            print(f"  - {ref}")
        print()
