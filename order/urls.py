#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^place_order/$',place_order,name='place_order'),
    url(r'^order_handle/$',order_handle,name='order_handle'),
]



if __name__ == '__main__':
    pass