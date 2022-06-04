# Celery 异步服务器后端模块

## 部署
```shell
pip install celery gevent -i https://pypi.doubanio.com/simple/
celery -A celery_server worker -l info --pool=eventlet
```
需要在 celery 5.0 中才能使用 async
