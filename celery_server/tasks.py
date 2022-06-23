from .celery import app
from .celery import logger
import time

@app.task
def test(x, y):
    logger.info("开始执行 test() 方法")
    time.sleep(5)
    logger.info("test() 方法执行成功")