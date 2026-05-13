import os
import re

# 定义修复函数
def fix_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复路径：去掉开头的斜杠
    # 修复 href="/wp-content/..." 为 href="wp-content/..."
    content = re.sub(r'href="/wp-content/', r'href="wp-content/', content)
    # 修复 src="/wp-content/..." 为 src="wp-content/..."
    content = re.sub(r'src="/wp-content/', r'src="wp-content/', content)
    # 修复 _assetsURL":"/wp-content/... 为 _assetsURL":"wp-content/...
    content = re.sub(r'"_assetsURL":"\/wp-content/', r'"_assetsURL":"wp-content/', content)
    # 修复 _publicURL":"https://... 可以保持不变，但我们也可以处理其他绝对路径
    
    # 保存修改后的文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已修复: {file_path}")

# 获取当前目录下所有的HTML文件
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# 修复所有HTML文件
for html_file in html_files:
    fix_html_file(html_file)

print(f"\n修复完成！共修复 {len(html_files)} 个HTML文件。")
