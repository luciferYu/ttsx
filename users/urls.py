#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^login/$',login,name='login'),
    url(r'^login_handle/$',login_handle,name='login_handle'),#处理登录请求
    url(r'^logout/$',logout,name='logout'),
    url(r'^register/',register,name='register'),
    url(r'^user_center_info/',user_center_info,name='user_center_info'),
    url(r'^user_center_order/',user_center_order,name='user_center_order'),
    url(r'^user_center_site/',user_center_site,name='user_center_site'),
    #处理用户注册
    url(r'^register_handle/$',register_handle,name='register_handle'),
    #检测用户名是否存在的ajax请求
    url(r'check_username',check_username,name='check_username')
]



if __name__ == '__main__':
    pass