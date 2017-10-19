#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

# 封装post请求,把送过来的参数去掉前后空格
import hashlib
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def post(request,key):
    return request.POST.get(key,'').strip()

#get方法去掉空格
def get(request,key):
    return request.GET.get(key,'').strip()


def set_cookie(response,key,value):
    '''
    设置cookie函数
    :param response:将要返回的响应
    :param key: cookie的键
    :param value: cookie的值
    :return:
    '''
    response.set_cookie(key,value,max_age=86400)

def get_cookie(request,key):
    '''
    获得cookie
    :param request:客户端请求
    :param key: 要获得的cookie的键
    :return: 查询的cookie的值
    '''
    return request.COOKIES.get(key,'')

def del_cookie(response,key):
    '''
    删除cookie
    :param response:将要返回的响应
    :param key: 要删除的cokkie值
    :return:
    '''
    response.delete_cookie(key)

def set_session(request,key,value):
    '''
    设置session
    :param request: 用户的请求
    :param key: 要设置session的键
    :param value: 要设置session的值
    :return:
    '''
    request.session[key] = value

def get_session(request,key):
    '''
    获取session
    :param request: 用户的请求
    :param key: 要获取session的键
    :return:
    '''
    return request.session.get(key,'')

def flush_session(request):
    '''
    设置session
    :param request: 用户的请求
    :return:
    '''
    request.session.flush()

def password_encryption(password,salt=''):
    '''
    用户密码加密
    :param password: 原密码
    :param salt:盐
    :return:hash256的密码
    '''
    sha = hashlib.sha256()
    new_password = password + str(salt)
    sha.update(new_password.encode('utf-8'))
    return sha.hexdigest()

def add_messages(request,key,value):
    '''
    构造对消息增加key的函数
    :param request: 请求
    :param key: 消息的键
    :param value: 消息的值
    :return:
    '''
    messages.add_message(request,messages.INFO,key + ':' + value)

def get_messages(request):
    '''
    获取请求的消息，并拆分成键值对
    :param request: 请求
    :return: 消息的字典形式
    '''
    mess = messages.get_messages(request)
    info = {}
    for message in mess:
        dic_mess = str(message).split(':')
        info[dic_mess[0]] = dic_mess[1]
    return info


def check_user_login(request):
    '''
    检测用户是否登录
    :param request:
    :return: 登录的话返回用户的用户名
    '''
    return get_session(request,'username')

def check_permission(view_func):
    def wrapper(request,*args,**kwargs):
        if check_user_login(request):
            #如果用户登录，则正常访问
            return view_func(request,*args,**kwargs)
        else:
            return redirect(reverse('users:login'))
    return wrapper




if __name__ == '__main__':
    pass