# -*- coding: utf-8 -*-
# @Time : 2022/1/11 1:46
# @Author : WhaleFall
# @Site : 
# @File : config.py
# @Description : 项目的配置文件
import os
from pathlib import Path
import platform
import sys


class Config:
    BASE_DIR = Path(__file__).resolve().parent  # 项目绝对目录
    SQLITE_PATH = os.path.join(BASE_DIR, 'db', 'data.db')
    # 默认UA
    DEFAULT_UA = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 " \
                 "Safari/534.50"
    LOGS_DIR = Path(BASE_DIR, 'logs')
    if platform.system() == "Windows":
        DATABASE_URI = 'sqlite:///' + SQLITE_PATH
    else:
        DATABASE_URI = 'sqlite:////' + SQLITE_PATH

    engine = create_engine(DATABASE_URI)  # 数据库引擎

    def __init__(self):
        dirs = [Path(self.BASE_DIR, 'db'), self.LOGS_DIR]
        for dir_ in dirs:
            dir_.mkdir(exist_ok=True)


config = Config()  # 实例化配置

log_config = {
    # 添加接收器
    "handlers": [
        # 写入日志文件不必用颜色,rotation="1 day": 文件超过一天就会分割
        # run_{time:YYYY_M_D}.log: 日志格式
        {"sink": str(config.LOGS_DIR) + "/run_{time:YYYY_M_D}.log", "rotation": "1 day", "encoding": "utf-8",
         "backtrace": True, "diagnose": True, "colorize": False, "level": "DEBUG"},
        # 标准输出流
        {"sink": sys.stdout, "backtrace": True, "diagnose": True, "colorize": True, "level": "DEBUG"},
    ],
}
