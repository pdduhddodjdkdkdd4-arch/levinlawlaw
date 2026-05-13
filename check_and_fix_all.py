import os

# 需要检查的页面列表
PAGES_TO_FIX = [
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

def check_and_fix_page(page_name):
    file_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', page_name)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {page_name}")
        return False
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 检查是否有缺失的标签
    need_fix = False
    old_str = '\t\t\t\t\t\telementor-element-8e8f95e'
    if old_str in content:
        need_fix = True
        content = content.replace(
            '\t\t\t\t\t\telementor-element-8e8f95e',
            '\t\t\t\t\t\t<div class="elementor-element elementor-element-8e8f95e'
        )
        print(f"  Fixed missing div tag in: {page_name}")
    
    # 保存文件
    if need_fix:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    print(f"  No fix needed for: {page_name}")
    return False

def main():
    print("Checking and fixing all pages...")
    print("=" * 60)
    
    fixed_count = 0
    for page in PAGES_TO_FIX:
        print(f"\nChecking: {page}...")
        if check_and_fix_page(page):
            fixed_count += 1
    
    print("\n" + "=" * 60)
    print(f"Done! Fixed {fixed_count}/{len(PAGES_TO_FIX)} pages.")

if __name__ == "__main__":
    main()
