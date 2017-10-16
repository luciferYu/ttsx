#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$',index,name='index'),
]



if __name__ == '__main__':
    pass