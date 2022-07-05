# encoding=utf8
import httpx
from .model import API, default_header_user_agent


def test_resq(api: API, phone) -> httpx.Response:
    """测试 API 返回响应
    :param api: API model
    :param phone: 手机号
    :return: httpx 请求对象.
    """
    api = api.handle_API(phone)
    with httpx.Client(headers=default_header_user_agent(), timeout=8) as client:
        # 这个判断没意义.....但是我不知道怎么优化...
        # https://stackoverflow.com/questions/26685248/difference-between-data-and-json-parameters-in-python-requests-package
        # Todo: json 和 data 表单发送的问题,有些服务器不能解释 json,只能接受表单
        # sol: 1. 添加额外字段判断...
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
