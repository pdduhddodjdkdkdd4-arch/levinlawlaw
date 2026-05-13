import os
import re

# 新的联系信息
NEW_ADDRESS = "2665 South Bayshore Dr, PH2B<br>Miami, Florida 33133"

# 需要更新的地址模式
OLD_ADDRESS_PATTERNS = [
    r'110\s+E?\s*Houston\s+St.*?San\s+Antonio.*?TX.*?United\s+States',
    r'110\s+E?\s*Houston\s+St.*?San\s+Antonio.*?TX.*?78205',
    r'2665\s+South\s+Bayshore\s+Dr.*?Miami.*?Florida.*?33133',
    r'Bayshore\s+Dr.*?Miami.*?Florida',
]

# 查找所有HTML文件
HTML_FILES = []
for root, dirs, files in os.walk(r'c:\Users\电脑\Desktop\us.com'):
    dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'wp-content/uploads']]
    for file in files:
        if file.endswith('.html'):
            HTML_FILES.append(os.path.join(root, file))

print(f"Found {len(HTML_FILES)} HTML files")

total_updates = 0

for file_path in HTML_FILES:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        file_changed = False
        
        # 检查是否有需要替换的地址
        if 'Houston' in content or ('Bayshore' in content and 'Miami' in content):
            
            # 替换旧的San Antonio地址
            content = re.sub(
                r'110\s+E?\s*Houston\s+St.*?San\s+Antonio.*?TX\s*\d{5}[^\n<]*',
                NEW_ADDRESS,
                content,
                flags=re.IGNORECASE | re.DOTALL
            )
            
            # 替换旧的Miami地址（如果格式不对）
            content = re.sub(
                r'2665\s+South\s+Bayshore\s+Dr.*?(?:PH2B\s*)?<br>.*?Miami.*?Florida\s*\d{5}[^\n<]*',
                NEW_ADDRESS,
                content,
                flags=re.IGNORECASE | re.DOTALL
            )
            
            # 也处理没有<br>标签的情况
            content = re.sub(
                r'2665\s+South\s+Bayshore\s+Dr[^\n<]*\s*Miami[^\n<]*\s*Florida[^\n<]*',
                NEW_ADDRESS,
                content,
                flags=re.IGNORECASE | re.DOTALL
            )
            
            if content != original:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                total_updates += 1
                print(f"[OK] Updated address in: {os.path.basename(file_path)}")
                file_changed = True
        
        # 检查Google Maps iframe
        if 'San Antonio' in content and 'maps.google.com' in content:
            # 替换Google Maps链接
            content = re.sub(
                r'https://maps\.google\.com/maps\?q=[^&]+&',
                'https://maps.google.com/maps?q=2665+South+Bayshore+Dr+Miami+FL+33133&',
                content
            )
            
            if content != original:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                total_updates += 1
                print(f"[OK] Updated Google Maps in: {os.path.basename(file_path)}")
    
    except Exception as e:
        print(f"[ERROR] {file_path}: {e}")

print(f"\nTotal {total_updates} files updated")
