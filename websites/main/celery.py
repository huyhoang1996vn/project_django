from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

app = Celery('project_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def debug_task(self):
    print '=================='

@app.task
def add():
    print '============================'

# cd websites$ celery -A main worker -l info
