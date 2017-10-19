#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from django.template import Library
from django.core.urlresolvers import reverse

register = Library()

def create_user_center_left_menu(flag):
    '''
    传入过滤器用户中心菜单左侧的菜单项
    :param flag:
    :return:  返回一个菜单的集合 link：url name：显示菜单的内容 flag：判断是否当前菜单调用css的active
    '''
    menu = [
        {'link':reverse('users:user_center_info'),'name':'·个人信息','active': flag == 'info' and 'active' or ''},
        {'link':reverse('users:user_center_order'),'name':'·全部订单','active': flag == 'order' and 'active' or ''},
        {'link':reverse('users:user_center_site'),'name':'·收货地址','active': flag == 'site' and 'active' or ''},
    ]
    return menu

register.filter('create_user_center_left_menu',create_user_center_left_menu)  # 注册自定义过滤器


if __name__ == '__main__':
    pass