import os
import glob

# 文件列表，排除contact-us.html
files = [
    "unauthorized-transaction-reversal.html",
    "wishlist.html",
    "teams.html",
    "welcome.html",
    "testimonial.html",
    "thank-you.html",
    "investment-fraud-recovery.html",
    "general-online-scam-recovery.html",
    "reviews.html",
    "services.html",
    "hack-recovery-services.html",
    "privacy-policy-2.html",
    "identity-theft-restoration.html",
    "ransomeware-decryption-and-recover.html",
    "index.html",
    "drained-crypto-wallet-recovery.html",
    "cryptocurrency-scam-recovery.html",
    "customer-phishing-protection.html",
    "crypto-rug-pull-recvery.html",
    "bank-scam-recovery.html",
    "about-us.html",
    "phishing-detection-mitigation.html"
]

def update_buttons_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换 href="/contact-us.html" 为 href="contact-us.html"
        old_str = 'href="/contact-us.html"'
        new_str = 'href="contact-us.html"'
        
        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath}")
        else:
            print(f"No changes needed: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    base_dir = r"c:\Users\电脑\Desktop\us.com"
    
    print("Starting batch update...")
    print("=" * 50)
    
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            update_buttons_in_file(filepath)
        else:
            print(f"File not found: {filename}")
    
    print("=" * 50)
    print("Batch update completed!")
