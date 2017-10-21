#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^carts/$',carts,name='carts'),
    url(r'^add_goods/$',add_goods,name='add_goods'),
    url(r'^goods_num/$',goods_num,name='goods_num'),
]



if __name__ == '__main__':
    pass