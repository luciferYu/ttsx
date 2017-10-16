#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^login/',login,name='login'),
    url(r'^register/',register,name='register'),
    url(r'^user_center_info/',user_center_info,name='user_center_info'),
    url(r'^user_center_order/',user_center_order,name='user_center_order'),
    url(r'^user_center_site/',user_center_site,name='user_center_site'),

]



if __name__ == '__main__':
    pass