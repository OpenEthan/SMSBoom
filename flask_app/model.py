# encoding=utf8
# 储存数据库模型
from . import db
from datetime import datetime

class Apis(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    desc = db.Column(db.String(100))  # 描述
    url = db.Column(db.String(100))  # 链接
    method = db.Column(db.String(10))  # 请求方法
    header = db.Column(db.String(9999))  # 请求头
    data = db.Column(db.String(9999))  # 请求数据
    add_time = db.Column(db.DateTime(), default=datetime.now())  # 添加时间
