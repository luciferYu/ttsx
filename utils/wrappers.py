#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi

# 封装post请求,把送过来的参数去掉前后空格
import hashlib


def post(request,key):
    return request.POST.get(key,'').strip()

#get方法去掉空格
def get(request,key):
    return request.GET.get(key,'').strip()

#
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

if __name__ == '__main__':
    pass