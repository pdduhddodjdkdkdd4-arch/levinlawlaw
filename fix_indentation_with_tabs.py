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
    next_element_start = -1
    
    for i, line in enumerate(lines):
        if widget_marker in line:
            start_line = i
        if 'elementor-element-d4c499d' in line and start_line != -1:
            next_element_start = i
            break
    
    if start_line == -1 or next_element_start == -1:
        print(f"WARNING: Could not find widget area in {page_name}")
        return False
    
    # 构建正确的表单块 - 使用 10 个 tabs 作为基础缩进
    base = '\t\t\t\t\t\t\t\t\t\t'  # 10 tabs
    level1 = base + '\t'
    level2 = base + '\t\t'
    level3 = base + '\t\t\t'
    level4 = base + '\t\t\t\t'
    level5 = base + '\t\t\t\t\t'
    
    correct_lines = [
        f'{base}&lt;div class="elementor-element elementor-element-d6c697f elementor-widget elementor-widget-wpforms" data-id="d6c697f" data-element_type="widget" data-e-type="widget" data-settings="{{&quot;ultimate_floating_fx_translate_y&quot;:{{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:&quot;&quot;,&quot;sizes&quot;:[]}}}}" data-widget_type="wpforms.default"&gt;\n',
        f'{level1}&lt;div class="elementor-widget-container"&gt;\n',
        f'{level2}&lt;div class="contact-form-container" id="contact-main-form"&gt;\n',
        f'{level3}&lt;!-- 表单区域 --&gt;\n',
        f'{level3}&lt;div id="form-section"&gt;\n',
        f'{level4}&lt;h2&gt;Free Consultation&lt;/h2&gt;\n',
        f'{level4}&lt;p class="sub-title"&gt;Write us anytime, we will answer to all enquiries within 24 hours.&lt;/p&gt;\n',
        f'\n',
        f'{level4}&lt;h3&gt;Contact Us.&lt;/h3&gt;\n',
        f'\n',
        f'{level4}&lt;form id="contact-form" onsubmit="handleFormSubmit(event)"&gt;\n',
        f'{level5}&lt;div class="form-group"&gt;\n',
        f'{level5}\t&lt;label&gt;Name &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{level5}\t&lt;input type="text" name="name" required&gt;\n',
        f'{level5}&lt;/div&gt;\n',
        f'\n',
        f'{level5}&lt;div class="form-group"&gt;\n',
        f'{level5}\t&lt;label&gt;Email &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{level5}\t&lt;input type="email" name="email" required&gt;\n',
        f'{level5}&lt;/div&gt;\n',
        f'\n',
        f'{level5}&lt;div class="form-group"&gt;\n',
        f'{level5}\t&lt;label&gt;Phone Number (WhatsApp number) &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{level5}\t&lt;input type="tel" name="phone" required&gt;\n',
        f'{level5}\t&lt;p class="hint"&gt;Your phone number must be registered on WhatsApp for easy communication.&lt;/p&gt;\n',
        f'{level5}&lt;/div&gt;\n',
        f'\n',
        f'{level5}&lt;div class="form-group"&gt;\n',
        f'{level5}\t&lt;label&gt;The name of the platform involved in the scam &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{level5}\t&lt;input type="text" name="platform" required&gt;\n',
        f'{level5}&lt;/div&gt;\n',
        f'\n',
        f'{level5}&lt;div class="form-group"&gt;\n',
        f'{level5}\t&lt;label&gt;Amount of money defrauded &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n',
        f'{level5}\t&lt;input type="text" name="amount" required&gt;\n',
        f'{level5}&lt;/div&gt;\n',
        f'\n',
        f'{level5}&lt;button type="submit" class="submit-btn"&gt;Submit&lt;/button&gt;\n',
        f'{level4}&lt;/form&gt;\n',
        f'{level3}&lt;/div&gt;\n',
        f'{level2}&lt;/div&gt;\n',
        f'{level2}&lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;\n',
        f'{level2}&lt;script&gt;\n',
        f'{level2}\tdocument.addEventListener(\'DOMContentLoaded\', function () {{\n',
        f'{level2}\t\tinitContactForm();\n',
        f'{level2}\t}});\n',
        f'{level2}&lt;/script&gt;\n',
        f'{level1}&lt;/div&gt;\n',
        f'{base}&lt;/div&gt;\n',
    ]
    
    # 替换
    new_lines = lines[:start_line] + correct_lines + lines[next_element_start:]
    
    # 保存
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"OK: Fixed indentation for {page_name}")
    return True

# 处理所有页面
print("Fixing indentation with tabs for all pages...")
fixed_count = 0
for page in pages_to_fix:
    if fix_indentation(page):
        fixed_count += 1

print(f"\nDone! Fixed {fixed_count} out of {len(pages_to_fix)} pages.")
