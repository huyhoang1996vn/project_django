from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

celery_app = Celery('project_django', broker='amqp://guest:guest@127.0.0.1:5672//',backend='cache+memcached://127.0.0.1:11211/')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@celery_app.task
def debug_task(self):
    print '*** RUNING CELERY ***'



# from celery.result import AsyncResult
# celery_task_result = AsyncResult(task.task_id).state

# cd websites$ celery -A main worker -l info
