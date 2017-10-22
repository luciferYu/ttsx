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
    url(r'^edit_goods/$',edit_goods_num,name='edit_goods_num'),
    url(r'^remove_goods/$',remove_goods,name='remove_goods'),
]



if __name__ == '__main__':
    pass