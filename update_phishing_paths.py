import os
import re

# Read the file
file_path = r'c:\Users\电脑\Desktop\us.com\phishing-detection-mitigation.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace absolute URLs to local paths
original_content = content

# Replace domain-based paths
content = content.replace('/wp-content/', 'wp-content/')
content = content.replace('https://levinlawlaw.us.com/', '')

# Replace absolute paths starting with /wp-content/
content = content.replace('src="/wp-content/', 'src="wp-content/')
content = content.replace('href="/wp-content/', 'href="wp-content/')

# Save the changes
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated phishing-detection-mitigation.html successfully!")
print("\nKey replacements:")
print("- /wp-content/ → wp-content/")
print("- /wp-content/ → wp-content/")

# Find all remaining resource references
print("\nChecking for remaining external references:")
remaining = re.findall(r'(https?://[^\s"\']+)', content)
if remaining:
    print(f"Found {len(remaining)} external references:")
    for ref in remaining[:10]:
        print(f"  - {ref}")
else:
    print("No external domain references found - good!")
