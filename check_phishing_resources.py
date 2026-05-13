import os
import re

# Read the file
file_path = r'c:\Users\电脑\Desktop\us.com\phishing-detection-mitigation.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all resource paths
print("Checking resources in phishing-detection-mitigation.html")
print("=" * 70)

# Find all wpo-minify references
wpo_pattern = r'(wpo-minify-[^"\']+\.(?:css|js))'
wpo_files = set(re.findall(wpo_pattern, content))

# Find all wp-content/uploads references
uploads_pattern = r'(wp-content/uploads/[^"\']+)'
uploads_files = set(re.findall(uploads_pattern, content))

print(f"\nFound {len(wpo_files)} wpo-minify assets:")
for f in sorted(wpo_files):
    print(f"  - {f}")

print(f"\nFound {len(uploads_files)} upload files:")
for f in sorted(uploads_files)[:20]:
    print(f"  - {f}")
if len(uploads_files) > 20:
    print(f"  ... and {len(uploads_files)-20} more")

# Check which resources exist locally
assets_dir = r'c:\Users\电脑\Desktop\us.com\wp-content\cache\wpo-minify\1776568923\assets'
existing_assets = os.listdir(assets_dir) if os.path.exists(assets_dir) else []

print(f"\nChecking resource availability...")
missing = []

for resource in wpo_files:
    if resource not in existing_assets:
        missing.append(resource)

if missing:
    print(f"\n⚠️  MISSING RESOURCES ({len(missing)}):")
    for res in missing:
        print(f"  - {res}")
else:
    print(f"\n✅ All wpo-minify resources are present!")

# Check uploads
uploads_dir = r'c:\Users\电脑\Desktop\us.com\wp-content\uploads'
missing_uploads = []

for upload in uploads_files:
    local_path = os.path.join(r'c:\Users\电脑\Desktop\us.com', upload)
    if not os.path.exists(local_path):
        missing_uploads.append(upload)

if missing_uploads:
    print(f"\n⚠️  MISSING UPLOADS ({len(missing_uploads)}):")
    for up in missing_uploads[:10]:
        print(f"  - {up}")
    if len(missing_uploads) > 10:
        print(f"  ... and {len(missing_uploads)-10} more")
else:
    print(f"\n✅ All upload resources are present!")

print("\n" + "=" * 70)
print("Done!")
