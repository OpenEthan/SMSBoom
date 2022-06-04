#broker(消息中间件来接收和发送任务消息)
BROKER_URL = 'redis://localhost:6379/1'
#backend(存储worker执行的结果)
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

#设置时间参照，不设置默认使用的UTC时间
CELERY_TIMEZONE = 'Asia/Shanghai'
#指定任务的序列化
CELERY_TASK_SERIALIZER='json'
#指定执行结果的序列化
CELERY_RESULT_SERIALIZER='json'