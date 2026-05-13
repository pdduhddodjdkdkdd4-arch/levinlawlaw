import os

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

def fix_indentation(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    # 找到问题区域的起始和结束行
    widget_marker = 'elementor-element-d6c697f'
    start_line = -1
    end_line = -1
    next_element_start = -1
    
    for i, line in enumerate(lines):
        if widget_marker in line:
            start_line = i
            # 找到前面的缩进
            indent_len = len(line) - len(line.lstrip())
            base_indent = line[:indent_len]
        if 'elementor-element-d4c499d' in line and start_line != -1:
            next_element_start = i
            # 找到这个div的结束标签后的位置
            end_line = i
            # 往前找合适的结束位置
            for j in range(i, max(0, i-20), -1):
                if '&lt;/div&gt;' in lines[j] and 'elementor-widget-container' in lines[j-1]:
                    end_line = j + 1
                    break
            break
    
    if start_line == -1 or end_line == -1:
        print(f"WARNING: Could not find widget area in {page_name}")
        return False
    
    # 获取正确的基础缩进
    base_indent = lines[start_line][:len(lines[start_line]) - len(lines[start_line].lstrip())]
    
    # 构建正确的表单块
    correct_lines = [
        f'{base_indent}&lt;div class="elementor-element elementor-element-d6c697f elementor-widget elementor-widget-wpforms" data-id="d6c697f" data-element_type="widget" data-e-type="widget" data-settings="{{&quot;ultimate_floating_fx_translate_y&quot;:{{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:&quot;&quot;,&quot;sizes&quot;:[]}}}}" data-widget_type="wpforms.default"&gt;\n',
        f'{base_indent}\t&lt;div class="elementor-widget-container"&gt;\n',
        f'{base_indent}\t\t&lt;div class="contact-form-container" id="contact-main-form"&gt;\n',
        f'{base_indent}\t\t\t&lt;!-- 表单区域 --&gt;\n',
        f'{base_indent}\t\t\t&lt;div id="form-section"&gt;\n',
        f'{base_indent}\t\t\t\t&lt;h2&gt;Free Consultation&lt;/h2&gt;\n',
        f'{base_indent}\t\t\t\t&lt;p class="sub-title"&gt;Write us anytime, we will answer to all enquiries within 24 hours.&lt;/p&gt;\n',
        f'\n',
        f'{base_indent}\t\t\t\t&lt;h3&gt;Contact Us.&lt;/h3&gt;\n',
        f'\n',
        f'{base_indent}\t\t\t\t&lt;form id="contact-form" onsubmit="handleFormSubmit(event)"&gt;\n',
        f'{base_indent}\t\t\t\t\t&lt;div class="form-group"&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;label&gt;Name &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;input type="text" name="name" required&gt;\n',
        f'{base_indent}\t\t\t\t\t&lt;/div&gt;\n',
        f'\n',
        f'{base_indent}\t\t\t\t\t&lt;div class="form-group"&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;label&gt;Email &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;input type="email" name="email" required&gt;\n',
        f'{base_indent}\t\t\t\t\t&lt;/div&gt;\n',
        f'\n',
        f'{base_indent}\t\t\t\t\t&lt;div class="form-group"&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;label&gt;Phone Number (WhatsApp number) &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;input type="tel" name="phone" required&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;p class="hint"&gt;Your phone number must be registered on WhatsApp for easy communication.&lt;/p&gt;\n',
        f'{base_indent}\t\t\t\t\t&lt;/div&gt;\n',
        f'\n',
        f'{base_indent}\t\t\t\t\t&lt;div class="form-group"&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;label&gt;The name of the platform involved in the scam &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;input type="text" name="platform" required&gt;\n',
        f'{base_indent}\t\t\t\t\t&lt;/div&gt;\n',
        f'\n',
        f'{base_indent}\t\t\t\t\t&lt;div class="form-group"&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;label&gt;Amount of money defrauded &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{base_indent}\t\t\t\t\t\t&lt;input type="text" name="amount" required&gt;\n',
        f'{base_indent}\t\t\t\t\t&lt;/div&gt;\n',
        f'\n',
        f'{base_indent}\t\t\t\t\t&lt;button type="submit" class="submit-btn"&gt;Submit&lt;/button&gt;\n',
        f'{base_indent}\t\t\t\t&lt;/form&gt;\n',
        f'{base_indent}\t\t\t&lt;/div&gt;\n',
        f'{base_indent}\t\t&lt;/div&gt;\n',
        f'{base_indent}\t\t&lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;\n',
        f'{base_indent}\t\t&lt;script&gt;\n',
        f'{base_indent}\t\t\tdocument.addEventListener(\'DOMContentLoaded\', function () {{\n',
        f'{base_indent}\t\t\t\tinitContactForm();\n',
        f'{base_indent}\t\t\t}});\n',
        f'{base_indent}\t\t&lt;/script&gt;\n',
        f'{base_indent}\t&lt;/div&gt;\n',
        f'{base_indent}&lt;/div&gt;\n',
    ]
    
    # 替换
    new_lines = lines[:start_line] + correct_lines + lines[next_element_start:]
    
    # 保存
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"OK: Fixed indentation for {page_name}")
    return True

# 处理所有页面
print("Fixing indentation for all pages...")
fixed_count = 0
for page in pages_to_fix:
    if fix_indentation(page):
        fixed_count += 1

print(f"\nDone! Fixed {fixed_count} out of {len(pages_to_fix)} pages.")
