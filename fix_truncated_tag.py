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

def fix_truncated_tag(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. 首先，找到有问题的模式：
    # 即 &lt;/script&gt; 后面跟着一堆 &lt;/div&gt;，然后是被截断的行 "data-id="d4c499d"..."
    problem_pattern = r'(&lt;/script&gt;\s*(?:&lt;/div&gt;\s*)+)\s*(data-id="d4c499d")'
    
    match = re.search(problem_pattern, content, re.DOTALL)
    if not match:
        # 尝试查找其他形式的问题
        print(f"INFO: No obvious truncation found in {page_name}")
        # 检查是否还有缩进问题需要修复
        return check_and_fix_indentation(page_name, content)
    
    # 2. 找到被截断标签前面的正确缩进
    # 找到 script 结束标签前的 widget 结束标签的缩进
    script_end = match.start(1)
    # 往前找 widget div 的缩进
    widget_div_search_end = script_end
    # 找前面最近的 &lt;div class="elementor-widget-container"
    widget_container_start = content.rfind('&lt;div class="elementor-widget-container"', 0, widget_div_search_end)
    if widget_container_start == -1:
        print(f"WARNING: Widget container not found for {page_name}")
        return False
    
    # 获取 widget container 的缩进
    widget_line_start = content.rfind('\n', 0, widget_container_start) + 1
    widget_indent = content[widget_line_start:widget_container_start]
    
    # 现在找到 widget 元素本身的开始标签，获取它的缩进
    widget_element_start = content.rfind('elementor-widget elementor-widget-wpforms', 0, widget_container_start)
    if widget_element_start == -1:
        print(f"WARNING: Widget element start not found for {page_name}")
        return False
    
    widget_element_div_start = content.rfind('&lt;div', 0, widget_element_start)
    widget_element_line_start = content.rfind('\n', 0, widget_element_div_start) + 1
    widget_element_indent = content[widget_element_line_start:widget_element_div_start]
    
    # 3. 现在找到下一个元素 (d4c499d) 应该有的缩进
    # 找后面的 &lt;div class="e-con-inner" 的缩进
    econ_inner_start = content.find('&lt;div class="e-con-inner"', script_end)
    if econ_inner_start == -1:
        print(f"WARNING: e-con-inner not found for {page_name}")
        return False
    
    econ_inner_line_start = content.rfind('\n', 0, econ_inner_start) + 1
    econ_inner_indent = content[econ_inner_line_start:econ_inner_start]
    
    # 下一个元素 (d4c499d) 的缩进应该比 e-con-inner 少一层，或者和前面的 widget-element 一样
    # 看 bank-scam-recovery.html 的例子，它的缩进是 "\t\t" (或者对应的空格)
    # 在 bank-scam-recovery.html 中是 "\t\t"
    # 让我们检查一下前面 widget-element 的缩进对应的级别
    
    # 从 bank-scam-recovery.html 的例子来看：
    # widget-element 用的是 "\t\t" (2个tab)
    # 下一个元素 (d4c499d) 也用的是 "\t\t" (2个tab)
    
    # 4. 构建完整的修复内容
    # 首先，修复表单区域的缩进
    # 找到整个表单区域
    form_start = content.find('&lt;div class="contact-form-container"', widget_element_start)
    if form_start == -1:
        print(f"WARNING: Form container not found for {page_name}")
        return False
    
    # 构建完整的修复块
    # 先找到 widget element 的完整开始标签
    widget_element_end_of_line = content.find('\n', widget_element_div_start)
    widget_element_line = content[widget_element_div_start:widget_element_end_of_line]
    
    # 现在构建完整的正确内容
    fixed_content = content[:widget_element_div_start]
    fixed_content += widget_element_line + '\n'
    fixed_content += widget_element_indent + '\t&lt;div class="elementor-widget-container"&gt;\n'
    fixed_content += widget_element_indent + '\t\t&lt;div class="contact-form-container" id="contact-main-form"&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t&lt;!-- 表单区域 --&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t&lt;div id="form-section"&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t&lt;h2&gt;Free Consultation&lt;/h2&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t&lt;p class="sub-title"&gt;Write us anytime, we will answer to all enquiries within 24 hours.&lt;/p&gt;\n'
    fixed_content += '\n'
    fixed_content += widget_element_indent + '\t\t\t\t&lt;h3&gt;Contact Us.&lt;/h3&gt;\n'
    fixed_content += '\n'
    fixed_content += widget_element_indent + '\t\t\t\t&lt;form id="contact-form" onsubmit="handleFormSubmit(event)"&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;label&gt;Name &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;input type="text" name="name" required&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    fixed_content += '\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;label&gt;Email &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;input type="email" name="email" required&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    fixed_content += '\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;label&gt;Phone Number (WhatsApp number) &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;input type="tel" name="phone" required&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;p class="hint"&gt;Your phone number must be registered on WhatsApp for easy communication.&lt;/p&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    fixed_content += '\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;label&gt;The name of the platform involved in the scam &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;input type="text" name="platform" required&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    fixed_content += '\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;div class="form-group"&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;label&gt;Amount of money defrauded &lt;span&gt;*&lt;/span&gt;&lt;/label&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t\t&lt;input type="text" name="amount" required&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;/div&gt;\n'
    fixed_content += '\n'
    fixed_content += widget_element_indent + '\t\t\t\t\t&lt;button type="submit" class="submit-btn"&gt;Submit&lt;/button&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t\t&lt;/form&gt;\n'
    fixed_content += widget_element_indent + '\t\t\t&lt;/div&gt;\n'
    fixed_content += widget_element_indent + '\t\t&lt;/div&gt;\n'
    fixed_content += widget_element_indent + '\t\t&lt;script src="js/csv-manager.js"&gt;&lt;/script&gt;\n'
    fixed_content += widget_element_indent + '\t\t&lt;script&gt;\n'
    fixed_content += widget_element_indent + '\t\t\tdocument.addEventListener(\'DOMContentLoaded\', function () {\n'
    fixed_content += widget_element_indent + '\t\t\t\tinitContactForm();\n'
    fixed_content += widget_element_indent + '\t\t\t});\n'
    fixed_content += widget_element_indent + '\t\t&lt;/script&gt;\n'
    fixed_content += widget_element_indent + '\t&lt;/div&gt;\n'
    fixed_content += widget_element_indent + '&lt;/div&gt;\n'
    
    # 现在添加后面完整的 element，使用正确的缩进
    # 找到后面元素应该从哪里开始
    # 找到原来被截断后的位置的完整内容应该是什么
    # 从 bank-scam-recovery.html 来看，应该是：
    # '\t\t<div class="elementor-element elementor-element-d4c499d e-flex e-con-boxed e-con e-parent" data-id="d4c499d" data-element_type="container" data-e-type="container">'
    
    # 找到原来被截断的部分
    truncated_line_start = match.start(2)
    # 找到这一行的结尾
    truncated_line_end = content.find('\n', truncated_line_start)
    if truncated_line_end == -1:
        truncated_line_end = len(content)
    
    # 找到应该替换到哪里 - 找到下一个完整的 element 开始
    # 先找到 e-con-inner 的缩进，然后确定 d4c499d 的缩进
    # 在 bank-scam-recovery.html 中，e-con-inner 的缩进是 "\t\t\t" (3个tab)，而 d4c499d 是 "\t\t" (2个tab)
    
    # 所以，找到 e-con-inner 之前的行
    next_element_full_line = widget_element_indent + '&lt;div class="elementor-element elementor-element-d4c499d e-flex e-con-boxed e-con e-parent" data-id="d4c499d" data-element_type="container" data-e-type="container"&gt;'
    
    # 现在，找到需要替换的终点 - 即找到 e-con-inner 标签，我们保留它以及后面的内容
    # 找到 e-con-inner 的完整行
    econ_inner_line_start = content.rfind('\n', 0, econ_inner_start) + 1
    
    # 拼接完整内容
    fixed_content += next_element_full_line + '\n'
    fixed_content += content[econ_inner_line_start:]
    
    # 保存文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"OK: Fixed {page_name}")
    return True

def check_and_fix_indentation(page_name, content):
    # 检查是否只有缩进问题需要修复
    # 查找表单区域
    widget_marker = 'elementor-widget elementor-widget-wpforms'
    widget_idx = content.find(widget_marker)
    if widget_idx == -1:
        return False
    
    # 简单检查是否看起来正确
    if 'initContactForm()' in content:
        print(f"OK: {page_name} appears to be correct already")
        return True
    return False

# 处理所有页面
print("Starting to fix truncated tags...")
fixed_count = 0
for page in pages_to_fix:
    if fix_truncated_tag(page):
        fixed_count += 1

print(f"\nDone! Fixed {fixed_count} out of {len(pages_to_fix)} pages.")
