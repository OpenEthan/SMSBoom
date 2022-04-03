# encoding=utf8
import httpx
import json
import sys
import pathlib
import asyncio
from loguru import logger
from pydantic import BaseModel, validator
from typing import Optional, List, Union
from datetime import datetime
from urllib3 import disable_warnings
disable_warnings()

# logger config
logger.remove()
logger.add(
    sink=sys.stdout,
    format="<green>{time:YYYY-MM-DD at HH:mm:ss}</green> - <level>{level}</level> - <level>{message}</level>",
    colorize=True,
    backtrace=True
)

default_header = {
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 10; zh-cn; Mi 10 Build/QKQ1.191117.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.5.40"
}

# current directory
path = pathlib.Path(__file__).parent

phone = "19820294268"


class API(BaseModel):
    desc: str = "Default"
    url: str
    method: str = "GET"
    header: Optional[dict]
    data: Optional[Union[str, dict]]

    @validator('url')
    def name_must_contain_space(cls, v: str):
        """验证链接是否正确"""
        if not v.startswith('https' or 'http'):
            raise ValueError('url must startswith http(s)!')
        return v


def load_json() -> List[API]:
    """
    load json for api.json
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
            return APIs
        except Exception as why:
            logger.error(f"Json file syntax error:{why}")
            return None


def timestamp_new() -> str:
    """返回整数字符串时间戳"""
    return str(int(datetime.now().timestamp()))


def replace_data(content: Union[str, dict]) -> str:
    if isinstance(content, dict):
        for key, value in content.items():
            content[key] = value.replace("{phone}", phone).replace(
                "{timestamp}", timestamp_new())
    else:
        # fix: add str判断
        if isinstance(content, str):
            content.replace("{phone}", phone).replace(
                "{timestamp}", timestamp_new())
    return content


def handle_API(API: API) -> API:
    """
    :param API: one API basemodel
    :return: API basemodel
    """
    if API.method != "POST":
        API.method = "GET"
    API.data = replace_data(API.data)
    API.url = replace_data(API.url)
    return API


async def rqs(API: API):
    """requests api async function
    :param API: one API basemodel
    :return:
    """
    API = handle_API(API)
    # print(API.dict())
    async with httpx.AsyncClient(headers=default_header) as client:
        try:
            # 判断是否传递 json 数据
            if isinstance(API.data, dict):
                r = await client.request(method=API.method, url=API.url, json=API.data, headers=API.header)
            else:
                r = await client.request(method=API.method, url=API.url, data=API.data, headers=API.header)
            logger.info(f"{API.desc} {r.text}")
        except httpx.HTTPError as exc:
            logger.error(f"{API.desc} Error:{exc}")


@logger.catch
async def main():
    APIs = load_json()
    if APIs is None:
        return

    # 接收一个元组需要用 * 传参
    await asyncio.gather(
        *(rqs(api)
          for api in APIs)
    )


if __name__ == "__main__":
    asyncio.run(main())
