import os
import re

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

def fix_page_indentation(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 找到 form-container 开始标签，确定其缩进
    container_start = '&lt;div class="contact-form-container" id="contact-main-form"&gt;'
    start_idx = content.find(container_start)
    
    if start_idx == -1:
        print(f"WARNING: Form container not found in {page_name}")
        return False
    
    # 确定 form-container 的缩进
    line_start = content.rfind('\n', 0, start_idx) + 1
    container_indent = content[line_start:start_idx]
    
    # 现在我们要重新构建整个表单区域，使用正确的缩进
    # 首先找到整个表单区域的范围
    first_script = '&lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;'
    first_script_idx = content.find(first_script, start_idx)
    
    if first_script_idx == -1:
        print(f"WARNING: First script not found in {page_name}")
        return False
    
    # 找到第二个 script 的结束
    second_script_start = content.find('&lt;script&gt;', first_script_idx)
    if second_script_start == -1:
        print(f"WARNING: Second script start not found in {page_name}")
        return False
    
    second_script_end = content.find('&lt;/script&gt;', second_script_start)
    if second_script_end == -1:
        print(f"WARNING: Second script end not found in {page_name}")
        return False
    
    # 找到结束的两个 </div> 标签
    end_divs_idx = second_script_end + len('&lt;/script&gt;')
    
    # 现在，基于 contact-us.html 的正确格式，我们重新构建这个区域
    # 但是我们需要根据该页面原来的缩进进行调整
    
    # 首先，我们找到该页面在修改前，form-container 的父元素的缩进
    # 通过查找前面的 elementor-widget-container 标签
    widget_container_start = '&lt;div class="elementor-widget-container"&gt;'
    widget_idx = content.rfind(widget_container_start, 0, start_idx)
    
    if widget_idx == -1:
        print(f"WARNING: Widget container not found in {page_name}")
        return False
    
    # 获取 widget-container 的缩进
    widget_line_start = content.rfind('\n', 0, widget_idx) + 1
    widget_indent = content[widget_line_start:widget_idx]
    
    # 构建完整的、正确缩进的表单块
    # 缩进层级：
    # widget-container: widget_indent
    # contact-form-container: widget_indent + "        " (8 spaces)
    # 然后里面的元素继续增加缩进
    
    form_block = f'''{widget_indent}&lt;div class="elementor-widget-container"&gt;
{widget_indent}        &lt;div class="contact-form-container" id="contact-main-form"&gt;
{widget_indent}                &lt;!-- 表单区域 --&gt;
{widget_indent}                &lt;div id="form-section"&gt;
{widget_indent}                        &lt;h2&gt;Free Consultation&lt;/h2&gt;
{widget_indent}                        &lt;p class="sub-title"&gt;Write us anytime, we will answer to all enquiries within 24 hours.&lt;/p&gt;

{widget_indent}                        &lt;h3&gt;Contact Us.&lt;/h3&gt;

{widget_indent}                        &lt;form id="contact-form" onsubmit="handleFormSubmit(event)"&gt;
{widget_indent}                                &lt;div class="form-group"&gt;
{widget_indent}                                        &lt;label&gt;Name &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                        &lt;input type="text" name="name" required&gt;
{widget_indent}                                &lt;/div&gt;

{widget_indent}                                &lt;div class="form-group"&gt;
{widget_indent}                                        &lt;label&gt;Email &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                        &lt;input type="email" name="email" required&gt;
{widget_indent}                                &lt;/div&gt;

{widget_indent}                                &lt;div class="form-group"&gt;
{widget_indent}                                        &lt;label&gt;Phone Number (WhatsApp number) &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                        &lt;input type="tel" name="phone" required&gt;
{widget_indent}                                        &lt;p class="hint"&gt;Your phone number must be registered on WhatsApp for easy communication.&lt;/p&gt;
{widget_indent}                                &lt;/div&gt;

{widget_indent}                                &lt;div class="form-group"&gt;
{widget_indent}                                        &lt;label&gt;The name of the platform involved in the scam &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                        &lt;input type="text" name="platform" required&gt;
{widget_indent}                                &lt;/div&gt;

{widget_indent}                                &lt;div class="form-group"&gt;
{widget_indent}                                        &lt;label&gt;Amount of money defrauded &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}                                        &lt;input type="text" name="amount" required&gt;
{widget_indent}                                &lt;/div&gt;

{widget_indent}                                &lt;button type="submit" class="submit-btn"&gt;Submit&lt;/button&gt;
{widget_indent}                        &lt;/form&gt;
{widget_indent}                &lt;/div&gt;
{widget_indent}        &lt;/div&gt;
{widget_indent}        &lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;
{widget_indent}        &lt;script&gt;
{widget_indent}                document.addEventListener('DOMContentLoaded', function () {{
{widget_indent}                        initContactForm();
{widget_indent}                }});
{widget_indent}        &lt;/script&gt;
{widget_indent}&lt;/div&gt;'''
    
    # 现在找到需要替换的准确范围
    # 从 widget-container 开始到第二个 script 结束后的两个 </div>
    replace_start = widget_idx
    replace_end = end_divs_idx
    
    # 但是我们需要找到准确的结束位置，避免截断后面的内容
    # 找到 widget-container 对应的结束标签
    # 先找到 widget-container 后的两个 </div>
    div1_start = content.find('&lt;/div&gt;', second_script_end)
    if div1_start == -1:
        print(f"WARNING: First closing div not found in {page_name}")
        return False
    
    div2_start = content.find('&lt;/div&gt;', div1_start + 1)
    if div2_start == -1:
        print(f"WARNING: Second closing div not found in {page_name}")
        return False
    
    replace_end = div2_start + len('&lt;/div&gt;')
    
    # 替换内容
    new_content = content[:replace_start] + form_block + content[replace_end:]
    
    # 保存
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"OK: Fixed indentation for {page_name}")
    return True

# 处理所有页面
print("Starting to fix indentation for all pages...")
fixed_count = 0
for page in pages_to_fix:
    if fix_page_indentation(page):
        fixed_count += 1

print(f"\nDone! Fixed {fixed_count} out of {len(pages_to_fix)} pages.")
