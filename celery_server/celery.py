from celery import Celery
from celery.utils.log import get_task_logger

app = Celery(
    'celery_server',
    include=[
        'celery_server.tasks'
        ]
)
app.config_from_object(
    'celery_server.config',
)

logger = get_task_logger(__name__)

if __name__ == '__main__':
    app.start()