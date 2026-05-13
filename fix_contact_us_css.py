
file_path = r'c:\Users\电脑\Desktop\us.com\contact-us.html'

with open(file_path, 'rb') as f:
    content = f.read()

# 查找并删除多余的CSS引用
old_css = b'\t<link rel="stylesheet" id="wpo_min-header-0-css"\r\n\t\thref="/wp-content/cache/wpo-minify/1776568923/assets/wpo-minify-header-b65513ef.min.css"\r\n\t\tmedia="all">'

if old_css in content:
    content = content.replace(old_css, b'')
    print("已删除多余的CSS引用: wpo-minify-header-b65513ef.min.css")
    
    # 同时也删除重复的shortcut icon
    # 只保留一个，删除第二个
    icon_str = b'\t<link rel="shortcut icon" href="/static/image/logo.ico" />'
    # 找到所有出现的位置
    pos_list = []
    pos = 0
    while True:
        pos = content.find(icon_str, pos)
        if pos == -1:
            break
        pos_list.append(pos)
        pos += len(icon_str)
    
    if len(pos_list) > 1:
        # 删除第二个出现
        start = pos_list[1]
        end = start + len(icon_str)
        # 检查是否有换行符
        if content[end:end+2] == b'\r\n':
            end += 2
        content = content[:start] + content[end:]
        print("已删除重复的shortcut icon")
    
    # 保存文件
    with open(file_path, 'wb') as f:
        f.write(content)
    
    print("文件已保存")
else:
    print("未找到需要删除的CSS引用")
