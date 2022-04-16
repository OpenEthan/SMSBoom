# encoding=utf8
# 储存数据库模型
from . import db
from datetime import datetime
from . import ModelView

class ApisModelVies(ModelView):
    create_template = 'api_edit.html'
    edit_template = 'api_edit.html'
    # 在当前页面编辑
    # create_modal = True
    # edit_modal = True
    # 启用搜索
    column_searchable_list = ['desc']
    # 可以导出 csv
    can_export = True

class Apis(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    desc = db.Column(db.String(100), default="Default")  # 描述
    url = db.Column(db.String(100), unique=True, nullable=False)  # 链接
    method = db.Column(db.Enum("GET","POST"), nullable=False)  # 请求方法
    header = db.Column(db.String(9999))  # 请求头
    data = db.Column(db.String(9999))  # 请求数据
    add_time = db.Column(db.DateTime(), default=datetime.now)  # 添加时间
