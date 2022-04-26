# -*- coding: utf8 -*-
# 腾讯云函数执行入口

import os
from pathlib import Path
path = Path(__file__).parent.absolute()

def main_handler(event, context):
    print("云函数执行中.....")
    print(f"当前目录:{path}")
    os.chdir(path)
    # 自定义命令
    os.system("python3 smsboom.py -p 19820294268 -t 16")