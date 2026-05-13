import os
import re

NEW_PHONE = "+1 302-300-8008"
NEW_EMAIL = "info@levinlawlaw.us.com"
NEW_ADDRESS = "2665 South Bayshore Dr, PH2B\nMiami, Florida 33133"

HTML_FILES = []

for root, dirs, files in os.walk(r'c:\Users\电脑\Desktop\us.com'):
    dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'wp-content/uploads']]
    
    for file in files:
        if file.endswith('.html'):
            HTML_FILES.append(os.path.join(root, file))

print(f"Found {len(HTML_FILES)} HTML files")
print("Starting contact info update...\n")

total_replacements = 0

for file_path in HTML_FILES:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        replacements_in_file = 0
        
        # Replace phone numbers with various patterns
        phone_patterns = [
            r'\+?\s*1?\s*[\-\(]?\s*210\s*[\-\)]?\s*756\s*[\-]?\s*5099',
            r'\+?\s*1?\s*[\-\(]?\s*936\s*[\-\)]?\s*766\s*[\-]?\s*9082',
            r'\+?\s*0{5,}.*?\d{4}',
            r'1-800-800-\d{4}',
            r'\+\d[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{4}',
        ]
        
        for pattern in phone_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                replacement = NEW_PHONE
                content = content.replace(match, replacement)
                replacements_in_file += 1
                print(f"  Replace phone: {match} -> {replacement}")
        
        # Replace email
        if 'info@' in content:
            email_pattern = r'info@[\w\.-]+\.us\.com'
            matches = re.findall(email_pattern, content, re.IGNORECASE)
            for match in matches:
                if match != NEW_EMAIL:
                    content = content.replace(match, NEW_EMAIL)
                    replacements_in_file += 1
                    print(f"  Replace email: {match} -> {NEW_EMAIL}")
        
        # Replace address
        content = re.sub(
            r'2665\s*South\s*Bayshore\s*Dr.*?(?:Miami,\s*)?Florida\s*\d{5}[^\n<]*',
            NEW_ADDRESS.replace('\n', ', '),
            content,
            flags=re.IGNORECASE | re.DOTALL
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            total_replacements += replacements_in_file
            print(f"[OK] Updated: {os.path.basename(file_path)} ({replacements_in_file} changes)")
    
    except Exception as e:
        print(f"[ERROR] {file_path} - {str(e)}")

print(f"\nDone! Total {total_replacements} replacements made")
