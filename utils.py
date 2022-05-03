# coding=utf-8
# utils 实用工具类
import sqlite3
import json
from datetime import datetime
from pathlib import Path
from pydantic import BaseModel
from typing import Union, Optional

default_header = {
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 10; zh-cn; Mi 10 Build/QKQ1.191117.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.5.40"
}


class Sql(object):
    """处理SQL数据"""

    def __init__(self) -> None:
        '''初始化数据库'''
        # 数据库路径
        db_path = Path.cwd().joinpath("api.db")
        # 连接数据库,不检查是否在同一个路径.
        self.client = sqlite3.connect(
            db_path, timeout=6, check_same_thread=False)
        self.cursor = self.client.cursor()
        self.newTable()

    def newTable(self):
        '''初始化表结构'''
        sql = '''
CREATE TABLE IF NOT EXISTS API200 (
   id INT NULL,
   url           TEXT    NOT NULL,
   primary key (url)
);
            '''
        self.cursor.execute(sql)
        self.client.commit()

    def update(self, url):
        '''插入数据'''
        sql = '''
        INSERT INTO API200 (ID,url) VALUES (null,?)
        '''
        try:
            self.cursor.execute(sql, (url,))
            self.client.commit()
            return True
        except sqlite3.IntegrityError:
            # print(f"{url} 数据重复!")
            return False

    def select(self) -> list:
        '''获取所有接口'''
        sql = '''
        SELECT url FROM API200;
        '''
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            urls = []
            for url in result:
                urls.append(url[0])
            return urls
        except Exception as e:
            print('读取出现错误!', e)

    def __del__(self) -> None:
        '''对象被删除时执行的函数'''
        print(f"共改变{self.client.total_changes}条数据!,正在关闭数据库连接......")
        self.client.close()


class API(BaseModel):
    """处理自定义 API 数据"""
    desc: str = "Default"
    url: str
    method: str = "GET"
    header: Optional[Union[str, dict]] = default_header
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
        # 如果传入的 header 是字符串,就转为字典.
        if self.header == "":
            self.header = {}
            self.header['Referer'] = self.url  # 增加 Referer
        else:
            self.header = self.replace_data(self.header, phone)
        
        self.data = self.replace_data(self.data, phone)
        self.url = self.replace_data(self.url, phone)
        return self
