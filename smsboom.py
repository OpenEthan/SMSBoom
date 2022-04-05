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

phone = "19820294267"


class API(BaseModel):
    desc: str = "Default"
    url: str
    method: str = "GET"
    header: Optional[dict]
    data: Optional[Union[str, dict]]


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
    if not phone:
        return content
    # 统一转换成 str 再替换.
    content = str(content).replace("[phone]", phone).replace(
        "[timestamp]", timestamp_new()).replace("'",'"')
    # 尝试 json 化
    try:
        return json.loads(content)
    except:
        return content


def handle_API(API: API) -> API:
    """
    :param API: one API basemodel
    :return: API basemodel
    """
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
            if not isinstance(API.data, dict):
                resp = await client.request(method=API.method, headers=API.header,
                            url=API.url, data=API.data)
            else:
                resp = await client.request(
                    method=API.method, headers=API.header, url=API.url, json=API.data)
            logger.success(f"{API.desc}-{resp.text}")
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
