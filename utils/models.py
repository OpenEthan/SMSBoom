# encoding=utf8
# 一些模型
from pydantic import BaseModel
from typing import Union, Optional
from datetime import datetime
import json

from utils import default_header_user_agent



class API(BaseModel):
    """处理自定义 API 数据"""
    desc: str = "Default"
    url: str
    method: str = "GET"

    header: Optional[Union[str, dict]] = default_header_user_agent()

    data: Optional[Union[str, dict]]

    def replace_data(self, content: Union[str, dict], phone: str) -> str:
        # 统一转换成 str 再替换. ' -> "
        if phone:
            content = str(content).replace("[phone]", phone).replace(
                "[timestamp]", self.timestamp_new()).replace("'", '"')

        # 尝试 json 化
        try:
            return json.loads(content.replace("'", '"'))
        except:
            return content

    def timestamp_new(self) -> str:
        """返回整数字符串时间戳"""
        return str(int(datetime.now().timestamp()))


    def handle_API(self, phone: str=None):
        """ 传入手机号处理 API
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
