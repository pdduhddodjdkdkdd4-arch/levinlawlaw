import os
import re

# 需要修改的页面列表
pages_to_fix = [
    'investment-fraud-recovery.html',
    'phishing-detection-mitigation.html',
    'ransomeware-decryption-and-recover.html',
    'unauthorized-transaction-reversal.html'
]

def fix_truncated_only(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 找到被截断的行
    # 模式：&lt;/div&gt; 后面跟着 &lt;/div&gt; 然后是只包含 data-id 的行
    pattern = r'(&lt;/div&gt;\s*&lt;/div&gt;\s*)(\n\s*data-id="d4c499d"[^\n]*)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        # 尝试另一种模式
        pattern2 = r'(&lt;/script&gt;\s*&lt;/div&gt;\s*&lt;/div&gt;\s*)(\n\s*data-id="d4c499d"[^\n]*)'
        match = re.search(pattern2, content, re.DOTALL)
    
    if not match:
        print(f"INFO: No truncation found in {page_name}")
        return False
    
    # 找到前面 widget 的缩进
    # 往前找 &lt;div class="elementor-element elementor-element-d6c697f"
    widget_marker = 'elementor-element-d6c697f'
    widget_pos = content.rfind(widget_marker, 0, match.start(1))
    
    if widget_pos == -1:
        print(f"WARNING: Widget not found in {page_name}")
        return False
    
    widget_div_start = content.rfind('&lt;div', 0, widget_pos)
    widget_line_start = content.rfind('\n', 0, widget_div_start) + 1
    widget_indent = content[widget_line_start:widget_div_start]
    
    # 构建完整的标签
    full_tag = widget_indent + '&lt;div class="elementor-element elementor-element-d4c499d e-flex e-con-boxed e-con e-parent" data-id="d4c499d" data-element_type="container" data-e-type="container"&gt;'
    
    # 替换
    new_content = content[:match.start(2)] + '\n' + full_tag + content[match.end(2):]
    
    # 保存
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"OK: Fixed {page_name}")
    return True

# 处理页面
print("Fixing truncated tags...")
fixed_count = 0
for page in pages_to_fix:
    if fix_truncated_only(page):
        fixed_count += 1

print(f"\nDone! Fixed {fixed_count} pages.")
