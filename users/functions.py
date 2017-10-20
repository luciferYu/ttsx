#!/usr/bin/python3
# -*- coding:utf-8 -*-
# auth:zhiyi


# 用户注册信息校验
from django.shortcuts import redirect
from django.urls import reverse

from utils.wrappers import *
import re
from .models import *
from django.contrib import messages  # 使网页间传递消息


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
        add_messages(request, 'user_name_err', '用户名长度应该在5到20之间')  # add_message(请求，消息级别，消息内容)

    # 判断密码长度
    if not (8 <= len(user_pass1) <= 20):
        flag = False
        add_messages(request, 'user_pass_err', '密码长度应该在8到20之间')  # add_message(请求，消息级别，消息内容)

    if user_pass1 != user_pass2:
        flag = False
        add_messages(request, 'user_pass_diff_err', '两次密码必须一致')  # add_message(请求，消息级别，消息内容)

    # 判断邮箱是否合法
    reg = '^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(reg, user_mail):
        flag = False
        add_messages(request, 'user_mail_err', '邮箱不符合规则')  # add_message(请求，消息级别，消息内容)

    # 判断用户是否存在
    if User.objects.get_user_by_name(user_name):
        flag = False

    return flag


def user_is_exist(request):
    '''
    验证用户是否存在
    :param request:
    :return:返回用户信息对象
    '''
    # 获取请求的用户名
    username = post(request, 'user_name')
    # 查询用户信息并返回
    return User.objects.get_user_by_name(username)


def check_login_params(request):
    '''
    验证登录表单
    :param request:
    :return: 用户 or False
    '''
    # 获取表单数据
    user_name = post(request, 'user_name')
    user_pass = post(request, 'user_pass')

    # 对数据做校验
    if not (5 <= len(user_name) <= 20):  # 验证用户名长度
        return False

    if not (8 <= len(user_pass) <= 20):  # 验证密码长度
        return False

    user = user_is_exist(request)
    if not user:  # 验证用户是否存在
        return False
    else:
        return user


def auth_user(request, user):
    '''
    验证用户，并返回响应
    :param user: 基础校验后的用户
    :return: 验证成功登录主页，验证失败返回登录界面
    '''
    salt = user.user_salt  # 3.用户salt
    submit_passwd = password_encryption(post(request, 'user_pass'), salt)
    user_passwd = user.user_pass
    if submit_passwd == user_passwd:  # 3.匹配密码
        prev_url = get_session(request, 'pre_url')
        if not prev_url:
            response = redirect(reverse('goods:index'))
        else:
            response = redirect(prev_url)
        keep_user_online(request)
        remeber_username(request, response)
        return response
    else:
        return redirect(reverse('users:login'))


def keep_user_online(request):
    '''
    登录用户记录其用户名,和id
    :param request: 用户的请求
    :return:
    '''
    user = User.objects.get_user_by_name(post(request, 'user_name'))
    set_session(request, 'username', user.user_name)
    set_session(request, 'uid', user.id)


def remeber_username(request, response):
    '''
    用户是否在登录页面勾选了记住我,将用户名放入到响应的cookie中
    :param request:
    :param response:
    :return:
    '''
    username_remeber = post(request, 'user_remb')
    if username_remeber:
        set_cookie(response, 'username', post(request, 'user_name'))


def check_addr_param(request):
    '''
    检查修改收件人信息函数参数
    :param request:
    :return:
    '''
    user_recv = post(request, 'user_recv')
    user_addr = post(request, 'user_addr')
    user_code = post(request, 'user_code')
    user_tele = post(request, 'user_tele')

    if len(user_recv) == 0:  # 收件人为空
        return False
    if len(user_addr) == 0:  # 地址为空
        return False
    if len(user_code) != 6:  # 邮政编码不是6位
        return False
    if len(user_tele) != 11:  # 电话号码不是11位
        return False

    return True


if __name__ == '__main__':
    pass
