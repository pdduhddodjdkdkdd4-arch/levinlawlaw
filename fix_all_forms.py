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

# contact-us.html 中的标准表单结构（保持相同的缩进）
standard_form_html = '''                                        &lt;div class="contact-form-container" id="contact-main-form"&gt;
                                                &lt;!-- 表单区域 --&gt;
                                                &lt;div id="form-section"&gt;
                                                        &lt;h2&gt;Free Consultation&lt;/h2&gt;
                                                        &lt;p class="sub-title"&gt;Write us anytime, we will answer to all enquiries within 24 hours.&lt;/p&gt;

                                                        &lt;h3&gt;Contact Us.&lt;/h3&gt;

                                                        &lt;form id="contact-form" onsubmit="handleFormSubmit(event)"&gt;
                                                                &lt;div class="form-group"&gt;
                                                                        &lt;label&gt;Name &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
                                                                        &lt;input type="text" name="name" required&gt;
                                                                &lt;/div&gt;

                                                                &lt;div class="form-group"&gt;
                                                                        &lt;label&gt;Email &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
                                                                        &lt;input type="email" name="email" required&gt;
                                                                &lt;/div&gt;

                                                                &lt;div class="form-group"&gt;
                                                                        &lt;label&gt;Phone Number (WhatsApp number) &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
                                                                        &lt;input type="tel" name="phone" required&gt;
                                                                        &lt;p class="hint"&gt;Your phone number must be registered on WhatsApp for easy communication.&lt;/p&gt;
                                                                &lt;/div&gt;

                                                                &lt;div class="form-group"&gt;
                                                                        &lt;label&gt;The name of the platform involved in the scam &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
                                                                        &lt;input type="text" name="platform" required&gt;
                                                                &lt;/div&gt;

                                                                &lt;div class="form-group"&gt;
                                                                        &lt;label&gt;Amount of money defrauded &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;
                                                                        &lt;input type="text" name="amount" required&gt;
                                                                &lt;/div&gt;

                                                                &lt;button type="submit" class="submit-btn"&gt;Submit&lt;/button&gt;
                                                        &lt;/form&gt;
                                                &lt;/div&gt;
                                        &lt;/div&gt;
                                        &lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;
                                        &lt;script&gt;
                                                document.addEventListener('DOMContentLoaded', function () {
                                                        initContactForm();
                                                });
                                        &lt;/script&gt;'''

def fix_page(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 查找并替换表单部分
    start_marker = '&lt;div class="contact-form-container" id="contact-main-form"&gt;'
    first_script_marker = '&lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;'
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print(f"WARNING: Start marker not found in {page_name}")
        return False
    
    # 找到第一个 script 标签的位置
    first_script_idx = content.find(first_script_marker, start_idx)
    if first_script_idx == -1:
        print(f"WARNING: First script not found in {page_name}")
        return False
    
    # 找到第二个 script 的结束标签
    second_script_start = content.find('&lt;script&gt;', first_script_idx)
    if second_script_start == -1:
        print(f"WARNING: Second script start not found in {page_name}")
        return False
    
    second_script_end = content.find('&lt;/script&gt;', second_script_start)
    if second_script_end == -1:
        print(f"WARNING: Second script end not found in {page_name}")
        return False
    
    # 结束位置是第二个 script 结束标签之后
    end_idx = second_script_end + len('&lt;/script&gt;')
    
    # 检查是否已经是标准格式（避免重复修改）
    old_content = content[start_idx:end_idx]
    if 'initContactForm()' in old_content:
        print(f"OK: Already fixed {page_name}")
        return False
    
    # 替换
    new_content = content[:start_idx] + standard_form_html + content[end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"OK: Fixed {page_name}")
    return True

# 处理所有页面
print("Starting to fix all pages...")
fixed_count = 0
for page in pages_to_fix:
    if fix_page(page):
        fixed_count += 1

print(f"\nDone! Fixed {fixed_count} out of {len(pages_to_fix)} pages.")

