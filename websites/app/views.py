# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.tasks import count_time, on_result_ready
from celery.result import ResultBase
# Create your views here.

def home(request):
    print "***START Power Card Introduction PAGE***"

    # result = count_time.delay(10)
    # call other task for done DB
    result = count_time.apply_async((10,), link=on_result_ready.s())
    print 'result ', result
    # try:
    return render(request, 'websites/home.html')
    # except Exception, e:
    #     print "Error: ", e
    #     raise Exception( "ERROR : Internal Server Error .Please contact administrator.")


