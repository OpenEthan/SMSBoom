#!/usr/bin/python python3
# coding=utf-8
# 爬取轰炸平台接口
from loguru import logger
import httpx
import requests
import re
from utils import Sql
import queue
import pathlib
import threading
import sys
import json
from prettytable import PrettyTable
import click
import urllib3
urllib3.disable_warnings()

# logger config
logger.remove()
logger.add(
    sink=sys.stdout,
    format="<green>{time:YYYY-MM-DD at HH:mm:ss}</green> - <level>{level}</level> - <level>{message}</level>",
    colorize=True,
    backtrace=True
)


path = pathlib.Path(__file__).parent
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
}


class SMS(object):
    # 默认的请求密钥
    default_phone = "15019682928"
    key_default = f"?hm={default_phone}&ok="

    def __init__(self, website, key) -> None:
        self.url = website
        self.header = header
        if key == "":
            self.key = self.key_default
        self.api_queue = queue.Queue()
        self.db = Sql()
        self.lock = threading.Lock()
        self.ok_api = 0

    def get_sms_api(self):
        '''请求短信轰炸平台'''
        with httpx.Client(verify=False) as ses:
            ses.get(self.url, headers=self.header)
            resp = ses.get(f"{self.url}{self.key}", headers=self.header)

        pat = re.compile(r"<img src='(.*?)' alt")
        apis = pat.findall(resp.text)
        assert not apis == [], "未找到任何接口!"
        # print(resp.text)
        logger.info("获取到的原始接口总数:%s" % (len(apis)))

        for api in apis:

            # 三重校验网址
            # 排除接口中没有电话号码的网址
            if self.default_phone not in api:
                continue

            # 去除空白字符并替换默认手机号
            api = api.strip().replace(" ", "").replace(
                self.default_phone, "[phone]")

            # 校验网址开头
            if not (api.startswith("https://") or api.startswith("http://")):
                continue

            self.api_queue.put(api)

        logger.info("Put到队列的接口总数:%s" % (self.api_queue.qsize()))
        self.size = self.api_queue.qsize()

    def check_theads(self):
        '''多线程检查可用性'''
        while not self.api_queue.empty():
            api = self.api_queue.get()
            try:
                with requests.get(api.replace("[phone]", self.default_phone), headers=self.header, timeout=8, verify=False) as resp:
                    if resp.status_code == 200:
                        with self.lock:
                            self.db.update(api)

            except Exception as e:
                pass
            finally:
                self.api_queue.task_done()

    def main(self):
        self.get_sms_api()
        # 在此设置线程数 int 类型
        threads_count = 254
        threads = [
            threading.Thread(target=self.check_theads,
                             name=f"{i}", daemon=True)
            for i in range(1, threads_count+1)
        ]
        for thread in threads:
            thread.start()
        logger.info("多线程校验进行中......(可能耗时比较长)")
        from tqdm import tqdm
        import time
        with tqdm(total=self.size) as pbar:
            while not self.api_queue.empty():
                pbar.update(self.size-self.api_queue.qsize())
                self.size = self.api_queue.qsize()
                time.sleep(0.5)
        self.api_queue.join()
        logger.info(f"总接口数目(去重后):{len(self.db.select())}")


def test_api_web(url: str) -> tuple:
    """check api web is ok?
    :return: tuple
    """
    if url is None:
        return
    with httpx.Client(headers=header, verify=False) as client:
        try:
            resp = client.get(url=url).text
            title = re.findall('<title>(.*?)</title>', resp)
            if title:
                logger.info(f"{url} title:{title[0]}")
                return (title[0], url)
        except httpx.HTTPError as why:
            logger.error(f"{url} 请求错误! {why}")

    return


def load_api_web():
    """从 json 文件加载轰炸网址.并测试!
    :return:
    """
    json_path = pathlib.Path(path, 'hz-web.json')
    table = PrettyTable(["标题", "链接"])
    if not json_path.exists():
        logger.error(f"hz-web.json not exists in {str(json_path)}!")
        return
    j = json_path.read_text(encoding="utf8")
    ok_web = []
    try:
        webs = json.loads(j)
    except json.decoder.JSONDecodeError as why:
        logger.error(f"json syctax error! {why}")
        return

    for web in webs:
        result = test_api_web(web['url'])
        if result:
            table.add_row([result[0], result[1]])
            ok_web.append(
                {"url": result[1], "key": web.get('key'), "title": result[0]})

    logger.success(f"有效的轰炸网站:\n{table}")
    if input(">>是否写入 hz-web.json?(Y/n)") == "Y":
        with open(json_path, encoding="utf8", mode="w") as fp:
            try:
                json.dump(ok_web, fp, ensure_ascii=False)
                logger.success("save hz-web.json success!")
            except Exception as why:
                logger.error(f"write hz-web.json error {why}")
    return ok_web


@click.group()
def cli():
    pass


@click.command()
def spider_all():
    """
    根据目录下的 hz-web.json 文件更新接口
    """
    websites = load_api_web()
    for website in websites:
        logger.info(f"正在爬取:{website['url']}")
        try:
            sms = SMS(website=website['url'], key=website['key']).main()
        except Exception as why:
            logger.critical(f"爬取:{website['url']} 出错:{why}")


@click.command()
@click.option('--url', help='轰炸网站的网址,结尾需要带/', prompt=True)
@click.option('--key', help='网址携带的参数(可选)', default="")
def spider_one(url, key):
    """爬取单个网址."""
    try:
        sms = SMS(website=url, key=key).main()
    except Exception as why:
        logger.critical(f"爬取:{url} 出错:{why}")


@click.command()
@logger.catch
def save_api():
    """保存api到 GETAPI.json 文件"""
    db = Sql()
    apis = db.select()
    api_lst = [
        api
        for api in apis
    ]
    with open("GETAPI.json", mode="w") as j:
        json.dump(fp=j, obj=api_lst, ensure_ascii=False)
    logger.success("写入到 GETAPI.json 成功!")


cli.add_command(spider_all)
cli.add_command(spider_one)
cli.add_command(save_api)

if __name__ == '__main__':
    cli()
