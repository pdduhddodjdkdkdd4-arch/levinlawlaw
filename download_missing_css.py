import os
import urllib.request

base_dir = r"c:\Users\电脑\Desktop\us.com\wp-content\cache\wpo-minify\1776568923\assets"
base_url = "/wp-content/cache/wpo-minify/1776568923/assets"

files_to_check = [
    "wpo-minify-header-b34c13d4.min.css",
    "wpo-minify-header-b65513ef.min.css"
]

def download_file(filename):
    url = f"{base_url}/{filename}"
    target_path = os.path.join(base_dir, filename)
    
    print(f"正在下载: {url}")
    try:
        urllib.request.urlretrieve(url, target_path)
        size = os.path.getsize(target_path)
        print(f"下载成功! 文件大小: {size} 字节")
        return True
    except Exception as e:
        print(f"下载失败: {e}")
        return False

if __name__ == "__main__":
    print("检查并下载CSS文件...")
    print("=" * 60)
    
    for filename in files_to_check:
        file_path = os.path.join(base_dir, filename)
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"\n文件已存在: {filename}")
            print(f"当前大小: {size} 字节")
            
            # 如果文件太小，可能是不完整的
            if size < 1000:
                print("文件可能不完整，正在重新下载...")
                download_file(filename)
            else:
                print("文件大小正常，跳过下载")
        else:
            print(f"\n文件不存在: {filename}，正在下载...")
            download_file(filename)
    
    print("\n" + "=" * 60)
    print("检查完成!")
