#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-07 14:59:08
LastEditTime: 2021-08-07 21:31:13
Description: python操作数据库
'''
import sqlite3
import sys


class Sql(object):
    def __init__(self) -> None:
        '''初始化数据库'''
        self.client = sqlite3.connect(
            "data.db", timeout=6, check_same_thread=False)
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
        except sqlite3.IntegrityError:
            print(f"{url} 数据重复!")

    def select(self) -> list:
        '''获取所有接口'''
        sql = '''
        SELECT url FROM API200;
        '''
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            # print(result)
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


if __name__ == "__main__":
    s = Sql()
    s.update("SWDWQ")
    print(s.select())
