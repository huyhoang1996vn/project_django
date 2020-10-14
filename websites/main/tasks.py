from __future__ import unicode_literals

import time

from main.celery import app as celery_app
@celery_app.task
def add_main():
    print 'add_main'

    for i in range(3):
        time.sleep(1)
        print '============================'
        print '============================'
   