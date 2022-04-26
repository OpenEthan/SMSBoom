# -*- coding: utf8 -*-
# 腾讯云函数执行入口

import os
from pathlib import Path
path = os.path.join(os.getcwd(), "src")

def main_handler(event, context):
    print("云函数执行中.....")
    print(f"云函数路径:{path}")
    os.chdir(path)
    # 自定义命令
    os.system("python3 smsboom.py run -p 19820294268 -t 16")

if __name__ == "__main__":
    main_handler(1,2)