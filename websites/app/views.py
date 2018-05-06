# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    print "***START Power Card Introduction PAGE***"
    # try:
    return render(request, 'websites/home.html')
    # except Exception, e:
    #     print "Error: ", e
    #     raise Exception( "ERROR : Internal Server Error .Please contact administrator.")


