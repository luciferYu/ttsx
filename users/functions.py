#!/usr/bin/python3
# -*- coding:utf-8 -*-
# auth:zhiyi


# 用户注册信息校验
from utils.wrappers import *
import re
from .models import *


def check_register_params(request):
    # 获得注册参数
    user_name = post(request, 'user_name')
    user_mail = post(request, 'user_mail')
    user_pass1 = post(request, 'user_pass1')
    user_pass2 = post(request, 'user_pass2')

    flag = True

    # 判断用户名长度
    if not (5 <= len(user_name) <= 20):
        print('username')
        flag = False

    # 判断密码长度
    if not (8 <= len(user_pass1) <= 20):
        print('passlen')
        flag = False

    if not user_pass1 == user_pass2:
        print('pass.pass')
        flag = False

    # 判断邮箱是否合法
    reg = '^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(reg, user_mail):
        print('mail')
        flag = False

    # 判断用户是否存在
    if User.objects.get_user_by_name(user_name):
        print('user exsist')
        flag = False

    return flag


if __name__ == '__main__':
    pass
