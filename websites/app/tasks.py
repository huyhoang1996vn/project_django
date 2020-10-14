from __future__ import unicode_literals

import time

from main.celery import app as celery_app
@celery_app.task
def add_app(total):
    print 'add_app'

    for i in range(total):
        time.sleep(1)
        print '============================'
        print '============================'
   