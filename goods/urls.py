#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^detail/$',detail,name='detail'),
    url(r'^list/(\d+)/(\d+)$',list,name='list'),
    url(r'^goods_chart/$',goods_chart,name='goods_chart')

]



if __name__ == '__main__':
    pass