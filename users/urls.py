#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_handle/$',views.login_handle,name='login_handle'),#处理登录请求
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^register/',views.register,name='register'),
    url(r'^user_center_info/',views.user_center_info,name='user_center_info'),
    url(r'^user_center_order/',views.user_center_order,name='user_center_order'),
    url(r'^user_center_site/',views.user_center_site,name='user_center_site'),
    #处理用户注册
    url(r'^register_handle/$',views.register_handle,name='register_handle'),
    #检测用户名是否存在的ajax请求
    url(r'check_username',views.check_username,name='check_username'),
    url(r'^user_addr_edit/$',views.user_addr_edit,name='user_addr_edit')
]



if __name__ == '__main__':
    pass