
import filecmp
import os

css1 = r'c:\Users\电脑\Desktop\us.com\wp-content\cache\wpo-minify\1776568923\assets\wpo-minify-header-b34c13d4.min.css'
css2 = r'c:\Users\电脑\Desktop\us.com\wp-content\cache\wpo-minify\1776568923\assets\wpo-minify-header-b65513ef.min.css'

print("比较两个CSS文件...")
print(f"文件1: {css1}")
print(f"文件2: {css2}")
print()

# 检查文件是否存在
if not os.path.exists(css1):
    print(f"错误: 文件1不存在")
if not os.path.exists(css2):
    print(f"错误: 文件2不存在")

# 比较文件大小
size1 = os.path.getsize(css1)
size2 = os.path.getsize(css2)
print(f"文件1大小: {size1} 字节")
print(f"文件2大小: {size2} 字节")
print()

# 检查文件是否完全相同
if filecmp.cmp(css1, css2, shallow=False):
    print("两个文件完全相同")
else:
    print("两个文件内容不同")
    
    # 逐行比较
    with open(css1, 'r', encoding='utf-8', errors='ignore') as f1, open(css2, 'r', encoding='utf-8', errors='ignore') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
        print(f"文件1行数: {len(lines1)}")
        print(f"文件2行数: {len(lines2)}")
        
        # 检查是否包含 .elementor-column 样式
        content1 = ''.join(lines1)
        content2 = ''.join(lines2)
        
        print()
        print("检查 elementor-column 样式...")
        if '.elementor-column' in content1:
            print("OK 文件1包含 .elementor-column 样式")
        else:
            print("FAIL 文件1缺少 .elementor-column 样式")
            
        if '.elementor-column' in content2:
            print("OK 文件2包含 .elementor-column 样式")
        else:
            print("FAIL 文件2缺少 .elementor-column 样式")
