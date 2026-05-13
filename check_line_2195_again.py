file_path = r'c:\Users\电脑\Desktop\us.com\investment-fraud-recovery.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# 查看第1894、2134、2183、2195行的缩进
for line_num in [1894, 2134, 2183, 2195]:
    line = lines[line_num-1]
    print(f"Line {line_num}:")
    print(f"  Leading whitespace: {repr(line[:len(line)-len(line.lstrip())])}")
    print(f"  Length: {len(line)-len(line.lstrip())}")
    print(f"  First 80 chars: {repr(line[:80])}")
    print()
