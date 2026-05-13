import os
import re

base_dir = r"c:\Users\电脑\Desktop\us.com"

def fix_css_references():
    print("开始修复elementor样式问题...")
    print("=" * 60)
    
    # 找到所有HTML文件
    html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]
    
    for filename in html_files:
        file_path = os.path.join(base_dir, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否有需要修复的引用
            # 替换 wpo-minify-header-63bc1847.min.css 为 wpo-minify-header-b34c13d4.min.css
            # 或者使用其他包含elementor样式的文件
            old_css = "wpo-minify-header-63bc1847.min.css"
            new_css = "wpo-minify-header-b34c13d4.min.css"
            
            if old_css in content:
                print(f"修复: {filename}")
                content = content.replace(old_css, new_css)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"  OK - 已更新CSS引用")
            else:
                print(f"跳过: {filename} (无需修复)")
                
        except Exception as e:
            print(f"错误: 处理 {filename} 时出错: {e}")
    
    print("\n" + "=" * 60)
    print("修复完成!")

if __name__ == "__main__":
    fix_css_references()
