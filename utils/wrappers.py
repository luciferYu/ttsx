#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

# 封装post请求,把送过来的参数去掉前后空格
import hashlib
from django.contrib import messages

def post(request,key):
    return request.POST.get(key,'').strip()

#get方法去掉空格
def get(request,key):
    return request.GET.get(key,'').strip()


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






if __name__ == '__main__':
    pass