file_path = r'c:\Users\电脑\Desktop\us.com\investment-fraud-recovery.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# 查看第1894行（索引1893）的内容
line_num = 1894
line = lines[line_num-1]
print(f"Line {line_num}:")
print(f"  Content: {repr(line)}")
print(f"  Leading whitespace: {repr(line[:len(line)-len(line.lstrip())])}")
print(f"  Length of leading whitespace: {len(line)-len(line.lstrip())}")

# 再看第1898行
line_num = 1898
line = lines[line_num-1]
print(f"\nLine {line_num}:")
print(f"  Content: {repr(line)}")
print(f"  Leading whitespace: {repr(line[:len(line)-len(line.lstrip())])}")

# 现在看第2134行（我们修复后的）
line_num = 2134
line = lines[line_num-1]
print(f"\nLine {line_num} (fixed):")
print(f"  Content: {repr(line)}")
print(f"  Leading whitespace: {repr(line[:len(line)-len(line.lstrip())])}")
