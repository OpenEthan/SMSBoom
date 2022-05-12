# encoding=utf8
# 请求的方法
import httpx
from typing import Union

from utils import default_header
from utils.models import API
from utils.log import logger


def reqAPI(api: API, client: httpx.Client) -> httpx.Response:
    if isinstance(api.data, dict):
        resp = client.request(method=api.method, json=api.data,
                              headers=api.header, url=api.url)
    else:
        resp = client.request(method=api.method, data=api.data,
                              headers=api.header, url=api.url)
    return resp


def reqFunc(api: Union[API, str], phone: Union[tuple, str]):
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
                return True
            except httpx.HTTPError as why:
                logger.error(f"请求失败{why}")
                return False
