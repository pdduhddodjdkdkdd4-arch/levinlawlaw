import os
import urllib.request

# 目标路径
target_dir = r"c:\Users\电脑\Desktop\us.com\wp-content\plugins\cookie-law-info\lite\frontend\images"
target_file = os.path.join(target_dir, "revisit.svg")

# 下载地址
url = "/wp-content/uploads/2024/08/revisit.svg"

# 创建目录
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"创建目录: {target_dir}")

# 下载文件
print(f"正在下载: {url}")
try:
    urllib.request.urlretrieve(url, target_file)
    print(f"下载成功! 文件已保存到: {target_file}")
except Exception as e:
    print(f"下载失败: {e}")
