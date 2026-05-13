file_path = r'c:\Users\电脑\Desktop\us.com\investment-fraud-recovery.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# 查看第1894行的缩进
line_num = 1894
line = lines[line_num-1]
print(f"Line {line_num}:")
print(f"  Leading whitespace: {repr(line[:len(line)-len(line.lstrip())])}")
print(f"  Length: {len(line)-len(line.lstrip())}")

# 查看第2134行的缩进
line_num = 2134
line = lines[line_num-1]
print(f"\nLine {line_num}:")
print(f"  Leading whitespace: {repr(line[:len(line)-len(line.lstrip())])}")
print(f"  Length: {len(line)-len(line.lstrip())}")

# 查看第2195行的缩进
line_num = 2195
line = lines[line_num-1]
print(f"\nLine {line_num}:")
print(f"  Leading whitespace: {repr(line[:len(line)-len(line.lstrip())])}")
print(f"  Length: {len(line)-len(line.lstrip())}")
