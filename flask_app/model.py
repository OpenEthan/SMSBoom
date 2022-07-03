# encoding=utf8
# 储存数据库模型
from utils import default_header_user_agent
from . import db
from datetime import datetime
from . import ModelView
import json
from typing import Union, Optional
from pydantic import BaseModel


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
    desc = db.Column(db.String(20), default="Default")  # 描述
    url = db.Column(db.String(9999), unique=True, nullable=False)  # 链接
    method = db.Column(db.Enum("GET", "POST"), nullable=False)  # 请求方法
    header = db.Column(db.String(9999))  # 请求头
    data = db.Column(db.String(9999))  # 请求数据
    add_time = db.Column(db.DateTime(), default=datetime.now)  # 添加时间


class API(BaseModel):
    desc: str = "Default"
    url: str
    method: str = "GET"
    header: Optional[Union[str, dict]] = default_header_user_agent()
    data: Optional[Union[str, dict]]

    def replace_data(self, content: Union[str, dict], phone) -> str:
        # 统一转换成 str 再替换.
        content = str(content).replace("[phone]", phone).replace(
            "[timestamp]", self.timestamp_new()).replace("'", '"')
        # 尝试 json 化
        try:
            # json.loads(content)
            # print("json成功",content)
            return json.loads(content)
        except:
            # print("json失败",content)
            return content

    def timestamp_new(self) -> str:
        """返回整数字符串时间戳"""
        return str(int(datetime.now().timestamp()))

    def handle_API(self, phone=None):
        """
        :param API: one API basemodel
        :return: API basemodel
        """
        # 仅仅当传入 phone 参数时添加 Referer
        # fix: 这段代码很有问题.......
        if phone:
            # 进入的 header 是个字符串
            if self.header == "":
                self.header = {}
                self.header['Referer'] = self.url  # 增加 Referer

        self.header = self.replace_data(self.header, phone)
        if not self.header.get('Referer'):
            self.header['Referer'] = self.url  # 增加 Referer

        self.data = self.replace_data(self.data, phone)
        self.url = self.replace_data(self.url, phone)
        # print(self)
        return self
