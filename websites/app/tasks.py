from __future__ import unicode_literals

import time

from main.celery import celery_app

@celery_app.task
def count_time(total):
    print '*** count_time ***'

    for i in range(total):
        time.sleep(1)
        print '============================'
        print '============================ ',i

    return True

@celery_app.task
def on_result_ready(self):
    print '********** DONE **********', self
