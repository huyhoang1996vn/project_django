# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.tasks import add_app
from main.tasks import add_main

# Create your views here.

def home(request):
    print "***START Power Card Introduction PAGE***"

    add_app.delay(10)
    add_main.delay()

    # try:
    return render(request, 'websites/home.html')
    # except Exception, e:
    #     print "Error: ", e
    #     raise Exception( "ERROR : Internal Server Error .Please contact administrator.")


