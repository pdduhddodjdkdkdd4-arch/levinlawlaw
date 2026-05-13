
file_path = r'c:\Users\电脑\Desktop\us.com\contact-us.html'

with open(file_path, 'rb') as f:
    content = f.read()

# 查找相关片段
target = b'wpo-minify-header-b65513ef.min.css'
index = content.find(target)

if index != -1:
    # 显示目标位置前后200字节
    start = max(0, index - 200)
    end = min(len(content), index + 200)
    snippet = content[start:end]
    
    print("找到目标片段:")
    print(f"位置: {index}")
    print("内容:")
    print(snippet.decode('utf-8', errors='ignore'))
    print("\n原始字节:")
    print(repr(snippet))
else:
    print("未找到目标片段")
