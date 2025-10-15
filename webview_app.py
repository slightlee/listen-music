import webview
import os
import sys

# 处理资源路径
def get_resource_path(relative_path):
    """获取资源的绝对路径，兼容开发环境和打包环境"""
    try:
        # 打包后的临时目录
        base_path = sys._MEIPASS
    except Exception:
        # 开发环境
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def main():
    # 获取 HTML 文件路径
    html_file = get_resource_path("index.html")
    
    # 创建窗口
    window = webview.create_window(
        " ",
        html_file,
        width=1440,
        height=960,
        resizable=True
    )
    
    webview.start()

if __name__ == "__main__":
    main()
    
   