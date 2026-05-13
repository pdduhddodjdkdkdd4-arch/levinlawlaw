import os
import re

# 需要修改的页面列表
pages_to_fix = [
    'investment-fraud-recovery.html',
    'bank-scam-recovery.html',
    'crypto-rug-pull-recvery.html',
    'cryptocurrency-scam-recovery.html',
    'customer-phishing-protection.html',
    'drained-crypto-wallet-recovery.html',
    'general-online-scam-recovery.html',
    'hack-recovery-services.html',
    'identity-theft-restoration.html',
    'phishing-detection-mitigation.html',
    'ransomeware-decryption-and-recover.html',
    'unauthorized-transaction-reversal.html'
]

def simple_fix(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 找到问题模式：&lt;/script&gt; 后面跟着 &lt;/div&gt;&lt;/div&gt; 然后是被截断的 data-id 行
    # 例如：
    # &lt;/script&gt;
    #                                                                          &lt;/div&gt;
    #                                                                          &lt;/div&gt;
    # 								data-id="d4c499d" data-element_type="container" data-e-type="container"&gt;
    
    # 首先，找到被截断的行
    truncated_pattern = r'^\s*data-id="d4c499d"'
    match = re.search(truncated_pattern, content, re.MULTILINE)
    
    if not match:
        print(f"INFO: No truncated tag found in {page_name}")
        return False
    
    # 找到被截断行的位置
    truncated_start = match.start()
    # 找到这一行的开始
    line_start = content.rfind('\n', 0, truncated_start) + 1
    
    # 现在，找到前面 &lt;/script&gt; 的位置
    script_end = content.rfind('&lt;/script&gt;', 0, line_start)
    if script_end == -1:
        print(f"WARNING: Script end not found in {page_name}")
        return False
    
    # 找到前面 widget 的缩进
    # 往前找 &lt;div class="elementor-widget elementor-widget-wpforms"
    widget_marker = 'elementor-widget elementor-widget-wpforms'
    widget_pos = content.rfind(widget_marker, 0, script_end)
    if widget_pos == -1:
        print(f"WARNING: Widget not found in {page_name}")
        return False
    
    # 找到 widget div 开始的位置
    widget_div_start = content.rfind('&lt;div', 0, widget_pos)
    widget_line_start = content.rfind('\n', 0, widget_div_start) + 1
    widget_indent = content[widget_line_start:widget_div_start]
    
    # 现在，找到 e-con-inner 的位置，来确定正确的缩进
    econ_inner = content.find('&lt;div class="e-con-inner"', truncated_start)
    if econ_inner == -1:
        print(f"WARNING: e-con-inner not found in {page_name}")
        return False
    
    econ_line_start = content.rfind('\n', 0, econ_inner) + 1
    econ_indent = content[econ_line_start:econ_inner]
    
    # 下一个元素 (d4c499d) 的缩进应该和 widget 的缩进一样
    # 构建完整的下一个元素标签
    next_element_line = widget_indent + '&lt;div class="elementor-element elementor-element-d4c499d e-flex e-con-boxed e-con e-parent" data-id="d4c499d" data-element_type="container" data-e-type="container"&gt;'
    
    # 现在，我们需要找到替换的开始和结束位置
    # 开始位置：widget div 开始
    replace_start = widget_div_start
    
    # 结束位置：e-con-inner 行开始
    replace_end = econ_line_start
    
    # 现在，我们需要重新构建整个 widget 部分，确保缩进正确
    # 让我们先提取原来的 widget 开始行
    widget_line_end = content.find('\n', widget_div_start)
    widget_line = content[widget_div_start:widget_line_end]
    
    # 现在，构建正确的 widget 块
    # 我们使用 widget_indent 作为基准
    widget_content = widget_line + '\n'
    widget_content += widget_indent + '\t&lt;div class="elementor-widget-container"&gt;\n'
    widget_content += widget_indent + '\t\t&lt;div class="contact-form-container" id="contact-main-form"&gt;\n'
    widget_content += widget_indent + '\t\t\t&lt;!-- 表单区域 --&gt;\n'
    widget_content += widget_indent + '\t\t\t&lt;div id="form-section"&gt;\n'
    widget_content += widget_indent + '\t\t\t\t&lt;h2&gt;Free Consultation&lt;/h2&gt;\n'
    widget_content += widget_indent + '\t\t\t\t&lt;p class="sub-title"&gt;Write us anytime, we will answer to all enquiries within 24 hours.&lt;/p&gt;\n'
    widget_content += '\n'
    widget_content += widget_indent + '\t\t\t\t&lt;h3&gt;Contact Us.&lt;/h3&gt;\n'
    widget_content += '\n'
    widget_content += widget_indent + '\t\t\t\t&lt;form id="contact-form" onsubmit="handleFormSubmit(event)"&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;label&gt;Name &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;input type="text" name="name" required&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    widget_content += '\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;label&gt;Email &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;input type="email" name="email" required&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    widget_content += '\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;label&gt;Phone Number (WhatsApp number) &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;input type="tel" name="phone" required&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;p class="hint"&gt;Your phone number must be registered on WhatsApp for easy communication.&lt;/p&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    widget_content += '\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;label&gt;The name of the platform involved in the scam &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;input type="text" name="platform" required&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    widget_content += '\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;label&gt;Amount of money defrauded &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t\t&lt;input type="text" name="amount" required&gt;\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    widget_content += '\n'
    widget_content += widget_indent + '\t\t\t\t\t&lt;button type="submit" class="submit-btn"&gt;Submit&lt;/button&gt;\n'
    widget_content += widget_indent + '\t\t\t\t&lt;/form&gt;\n'
    widget_content += widget_indent + '\t\t\t&lt;/div&gt;\n'
    widget_content += widget_indent + '\t\t&lt;/div&gt;\n'
    widget_content += widget_indent + '\t\t&lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;\n'
    widget_content += widget_indent + '\t\t&lt;script&gt;\n'
    widget_content += widget_indent + '\t\t\tdocument.addEventListener(\'DOMContentLoaded\', function () {\n'
    widget_content += widget_indent + '\t\t\t\tinitContactForm();\n'
    widget_content += widget_indent + '\t\t\t});\n'
    widget_content += widget_indent + '\t\t&lt;/script&gt;\n'
    widget_content += widget_indent + '\t&lt;/div&gt;\n'
    widget_content += widget_indent + '&lt;/div&gt;\n'
    widget_content += next_element_line + '\n'
    
    # 替换内容
    new_content = content[:replace_start] + widget_content + content[replace_end:]
    
    # 保存文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"OK: Fixed {page_name}")
    return True

# 处理所有页面
print("Starting simple fix...")
fixed_count = 0
for page in pages_to_fix:
    if simple_fix(page):
        fixed_count += 1

print(f"\nDone! Fixed {fixed_count} out of {len(pages_to_fix)} pages.")
