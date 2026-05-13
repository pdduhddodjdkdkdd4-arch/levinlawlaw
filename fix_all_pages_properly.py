import os

# 需要修改的页面列表
pages_to_fix = [
    'bank-scam-recovery.html',
    'crypto-rug-pull-recvery.html',
    'cryptocurrency-scam-recovery.html',
    'customer-phishing-protection.html',
    'drained-crypto-wallet-recovery.html',
    'general-online-scam-recovery.html',
    'hack-recovery-services.html',
    'identity-theft-restoration.html',
    'investment-fraud-recovery.html',
    'phishing-detection-mitigation.html',
    'ransomeware-decryption-and-recover.html',
    'unauthorized-transaction-reversal.html'
]

def fix_page_properly(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. 首先找到整个有问题的区域的起点
    # 查找 "elementor-widget elementor-widget-wpforms" 这个 widget 的开始
    widget_marker = 'elementor-widget elementor-widget-wpforms'
    widget_idx = content.find(widget_marker)
    
    if widget_idx == -1:
        print(f"WARNING: Widget marker not found in {page_name}")
        return False
    
    # 找到这个 widget div 的开始标签
    div_start = content.rfind('&lt;div', 0, widget_idx)
    if div_start == -1:
        print(f"WARNING: Widget div start not found in {page_name}")
        return False
    
    # 2. 找到需要替换区域的起点和终点
    # 起点：widget div 开始
    replace_start = div_start
    
    # 终点：在表单之后找到下一个完整的 elementor-element (d4c499d) 的开始
    # 先找到表单结束后的位置
    form_container_end = '&lt;/div&gt;\n'
    second_script_end = content.find('initContactForm();\n                });\n        &lt;/script&gt;', div_start)
    
    if second_script_end == -1:
        # 尝试其他模式
        second_script_end = content.find('initContactForm()', div_start)
    
    if second_script_end == -1:
        print(f"WARNING: Script end not found in {page_name}")
        return False
    
    # 现在找到下一个完整的 element 开始 - 即包含 'data-id="d4c499d"' 的 div
    next_element_marker = 'data-id="d4c499d"'
    next_element_idx = content.find(next_element_marker, second_script_end)
    
    if next_element_idx == -1:
        print(f"WARNING: Next element marker not found in {page_name}")
        # 尝试查找其他可能的后续 marker
        next_element_idx = content.find('Clients Feedback', second_script_end)
        if next_element_idx == -1:
            print(f"WARNING: No suitable marker found in {page_name}")
            return False
        # 往前找到 div 开始
        next_element_idx = content.rfind('&lt;div', 0, next_element_idx)
    
    # 找到这个 div 的真正开始
    div_before = content.rfind('&lt;div', 0, next_element_idx)
    while div_before &gt; second_script_end and content[div_before:div_before+4] == '&lt;div':
        candidate = content.rfind('\n', 0, div_before) + 1
        if content[candidate:div_before+4].strip().startswith('&lt;div'):
            replace_end = candidate
            break
        div_before = content.rfind('&lt;div', 0, div_before - 1)
    else:
        # 如果找不到，就用 next_element_idx 往前一点
        replace_end = content.rfind('\n', 0, next_element_idx) + 1
    
    # 3. 现在我们需要：
    # - 保留原 widget div 的开始标签（因为缩进可能因页面而异）
    # - 找到原 widget div 的开始标签和缩进
    widget_div_start = content.rfind('\n', 0, div_start) + 1
    widget_indent = content[widget_div_start:div_start]
    
    # 提取原来的 widget 开始标签（第一行）
    widget_line_end = content.find('\n', div_start)
    original_widget_line = content[div_start:widget_line_end]
    
    # 构建正确的表单块，基于原始的 widget 缩进
    # 我们会保留原始的 widget 开始标签，然后构建正确的内容
    form_block = f'''{original_widget_line}
{widget_indent}        &lt;div class="elementor-widget-container"&gt;
{widget_indent}                &lt;div class="contact-form-container" id="contact-main-form"&gt;
{widget_indent}                        &lt;!-- 表单区域 --&gt;
{widget_indent}                        &lt;div id="form-section"&gt;
{widget_indent}                                &lt;h2&gt;Free Consultation&lt;/h2&gt;
{widget_indent}                                &lt;p class="sub-title"&gt;Write us anytime, we will answer to all enquiries within 24 hours.&lt;/p&gt;

{widget_indent}                                &lt;h3&gt;Contact Us.&lt;/h3&gt;

{widget_indent}                                &lt;form id="contact-form" onsubmit="handleFormSubmit(event)"&gt;
{widget_indent}                                        &lt;div class="form-group"&gt;
{widget_indent}                                                &lt;label&gt;Name &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                                &lt;input type="text" name="name" required&gt;
{widget_indent}                                        &lt;/div&gt;

{widget_indent}                                        &lt;div class="form-group"&gt;
{widget_indent}                                                &lt;label&gt;Email &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                                &lt;input type="email" name="email" required&gt;
{widget_indent}                                        &lt;/div&gt;

{widget_indent}                                        &lt;div class="form-group"&gt;
{widget_indent}                                                &lt;label&gt;Phone Number (WhatsApp number) &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                                &lt;input type="tel" name="phone" required&gt;
{widget_indent}                                                &lt;p class="hint"&gt;Your phone number must be registered on WhatsApp for easy communication.&lt;/p&gt;
{widget_indent}                                        &lt;/div&gt;

{widget_indent}                                        &lt;div class="form-group"&gt;
{widget_indent}                                                &lt;label&gt;The name of the platform involved in the scam &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                                &lt;input type="text" name="platform" required&gt;
{widget_indent}                                        &lt;/div&gt;

{widget_indent}                                        &lt;div class="form-group"&gt;
{widget_indent}                                                &lt;label&gt;Amount of money defrauded &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                                &lt;input type="text" name="amount" required&gt;
{widget_indent}                                        &lt;/div&gt;

{widget_indent}                                        &lt;button type="submit" class="submit-btn"&gt;Submit&lt;/button&gt;
{widget_indent}                                &lt;/form&gt;
{widget_indent}                        &lt;/div&gt;
{widget_indent}                &lt;/div&gt;
{widget_indent}                &lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;
{widget_indent}                &lt;script&gt;
{widget_indent}                        document.addEventListener('DOMContentLoaded', function () {{
{widget_indent}                                initContactForm();
{widget_indent}                        }});
{widget_indent}                &lt;/script&gt;
{widget_indent}        &lt;/div&gt;
{widget_indent}&lt;/div&gt;'''
    
    # 替换内容
    new_content = content[:replace_start] + form_block + content[replace_end:]
    
    # 保存
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"OK: Fixed {page_name}")
    return True

# 处理所有页面
print("Starting to fix all pages properly...")
fixed_count = 0
for page in pages_to_fix:
    if fix_page_properly(page):
        fixed_count += 1

print(f"\nDone! Fixed {fixed_count} out of {len(pages_to_fix)} pages.")
