# encoding=utf8
# 请求的方法
from smsboom import load_getapi, load_json
from utils.log import logger
from utils.models import API
from utils import default_header_user_agent
import httpx
from httpx import Limits
from typing import Union, List
import asyncio

import sys
sys.path.append("E:\coding\SMSBoom")


def reqAPI(api: API, client: httpx.AsyncClient):
    if isinstance(api.data, dict):
        resp = client.request(method=api.method, json=api.data,
                              headers=api.header, url=api.url, timeout=10)
    else:
        resp = client.request(method=api.method, data=api.data,
                              headers=api.header, url=api.url, timeout=10)
    return resp


async def asyncReqs(src: Union[API, str], phone: Union[tuple, str], semaphore):
    """异步请求方法
    :param: 
    :return: 
    """
    # 多手机号支持
    if isinstance(phone, tuple):
        phone_lst = [_ for _ in phone]
    else:
        phone_lst = [phone]
    async with semaphore:
        async with httpx.AsyncClient(
            limits=Limits(max_connections=1000,
                          max_keepalive_connections=2000),
            headers=default_header_user_agent(),
            verify=False,
            timeout=99999
        ) as c:

            for ph in phone_lst:
                try:
                    if isinstance(src, API):
                        src = src.handle_API(ph)
                        r = await reqAPI(src, c)
                    else:
                        # 利用元组传参安全因为元组不可修改
                        s = (src.replace(" ", "").replace("\n", "").replace("\t", "").replace(
                            "&amp;", "").replace('\n', '').replace('\r', ''),)
                        r = await c.get(*s)
                    return r
                except httpx.HTTPError as why:
                    # logger.error(f"异步请求失败{type(why)}")
                    pass
                except TypeError:
                    # logger.error("类型错误")
                    pass
                except Exception as wy:
                    # logger.exception(f"异步失败{wy}")
                    pass

def callback(result):
    """异步回调函数"""
    log = result.result()
    if log is not None:
        # logger.info(f"请求结果:{log.text[:30]}")
        print(log.text[:30])
        pass


async def runAsync(apis: List[Union[API, str]], phone: Union[tuple, str]):

    tasks = []

    for api in apis:
        semaphore = asyncio.Semaphore(999999)
        task = asyncio.create_task(asyncReqs(api, phone, semaphore))
        task.add_done_callback(callback)
        tasks.append(task)

    await asyncio.gather(
        *tasks
    )
