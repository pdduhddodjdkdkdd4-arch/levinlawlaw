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

def fix_page(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 找到widget区域
    widget_marker = 'elementor-element-d6c697f'
    widget_pos = content.find(widget_marker)
    
    if widget_pos == -1:
        print(f"WARNING: Widget not found in {page_name}")
        return False
    
    # 找到widget的开始标签
    widget_div_start = content.rfind('&lt;div', 0, widget_pos)
    widget_line_start = content.rfind('\n', 0, widget_div_start) + 1
    
    # 找到这个widget的结束 - 找到后面的两个&lt;/div&gt;
    # 先找到&lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;
    script_end = content.find('initContactForm();', widget_pos)
    if script_end == -1:
        print(f"WARNING: Script end not found in {page_name}")
        return False
    
    # 找到后面的两个&lt;/div&gt;
    div1 = content.find('&lt;/div&gt;', script_end)
    if div1 == -1:
        return False
    div2 = content.find('&lt;/div&gt;', div1 + 1)
    if div2 == -1:
        return False
    
    # 找到后面元素的开始
    # 从前面的正确格式可以看到，widget_indent应该是'\t\t\t\t\t\t\t'（7个tabs？）
    # 让我们从widget_line_start提取缩进
    widget_indent = content[widget_line_start:widget_div_start]
    
    # 构建正确的表单块
    correct_block = f'''{widget_indent}&lt;div class="elementor-element elementor-element-d6c697f elementor-widget elementor-widget-wpforms" data-id="d6c697f" data-element_type="widget" data-e-type="widget" data-settings="{{&quot;ultimate_floating_fx_translate_y&quot;:{{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:&quot;&quot;,&quot;sizes&quot;:[]}}}}" data-widget_type="wpforms.default"&gt;
{widget_indent}	&lt;div class="elementor-widget-container"&gt;
{widget_indent}		&lt;div class="contact-form-container" id="contact-main-form"&gt;
{widget_indent}			&lt;!-- 表单区域 --&gt;
{widget_indent}			&lt;div id="form-section"&gt;
{widget_indent}				&lt;h2&gt;Free Consultation&lt;/h2&gt;
{widget_indent}				&lt;p class="sub-title"&gt;Write us anytime, we will answer to all enquiries within 24 hours.&lt;/p&gt;

{widget_indent}				&lt;h3&gt;Contact Us.&lt;/h3&gt;

{widget_indent}				&lt;form id="contact-form" onsubmit="handleFormSubmit(event)"&gt;
{widget_indent}					&lt;div class="form-group"&gt;
{widget_indent}						&lt;label&gt;Name &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}						&lt;input type="text" name="name" required&gt;
{widget_indent}					&lt;/div&gt;

{widget_indent}					&lt;div class="form-group"&gt;
{widget_indent}						&lt;label&gt;Email &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}						&lt;input type="email" name="email" required&gt;
{widget_indent}					&lt;/div&gt;

{widget_indent}					&lt;div class="form-group"&gt;
{widget_indent}						&lt;label&gt;Phone Number (WhatsApp number) &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}						&lt;input type="tel" name="phone" required&gt;
{widget_indent}						&lt;p class="hint"&gt;Your phone number must be registered on WhatsApp for easy communication.&lt;/p&gt;
{widget_indent}					&lt;/div&gt;

{widget_indent}					&lt;div class="form-group"&gt;
{widget_indent}						&lt;label&gt;The name of the platform involved in the scam &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}						&lt;input type="text" name="platform" required&gt;
{widget_indent}					&lt;/div&gt;

{widget_indent}					&lt;div class="form-group"&gt;
{widget_indent}						&lt;label&gt;Amount of money defrauded &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
{widget_indent}						&lt;input type="text" name="amount" required&gt;
{widget_indent}					&lt;/div&gt;

{widget_indent}					&lt;button type="submit" class="submit-btn"&gt;Submit&lt;/button&gt;
{widget_indent}				&lt;/form&gt;
{widget_indent}			&lt;/div&gt;
{widget_indent}		&lt;/div&gt;
{widget_indent}		&lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;
{widget_indent}		&lt;script&gt;
{widget_indent}			document.addEventListener('DOMContentLoaded', function () {{
{widget_indent}				initContactForm();
{widget_indent}			}});
{widget_indent}		&lt;/script&gt;
{widget_indent}	&lt;/div&gt;
{widget_indent}&lt;/div&gt;'''
    
    # 找到替换的开始和结束位置
    replace_start = widget_div_start
    replace_end = div2 + len('&lt;/div&gt;')
    
    # 替换
    new_content = content[:replace_start] + correct_block + content[replace_end:]
    
    # 保存
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"OK: Fixed {page_name}")
    return True

# 处理所有页面
print("Fixing all pages...")
fixed_count = 0
for page in pages_to_fix:
    if fix_page(page):
        fixed_count += 1

print(f"\nDone! Fixed {fixed_count} out of {len(pages_to_fix)} pages.")
