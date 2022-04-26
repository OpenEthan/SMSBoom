# encoding=utf8
import httpx
import json
from .model import API, default_header


def test_resq(api: API, phone) -> httpx.Response:
    """测试 API 返回响应
    :param api: API model
    :param phone: 手机号
    :return: httpx 请求对象.
    """
    api = api.handle_API(phone)
    default_header['Referer'] = api.url
    with httpx.Client(headers=default_header, timeout=8) as client:
        if not isinstance(api.data, dict):
            print("data")
            resp = client.request(method=api.method, headers=api.header,
                                  url=api.url, data=api.data)
        else:
            print('json')
            resp = client.request(
                method=api.method, headers=api.header, url=api.url, json=api.data)
    return resp


if __name__ == '__main__':
    pass
