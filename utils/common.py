#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from .wrappers import *

def user_is_login(request):
    return get_session(request,'username')




if __name__ == '__main__':
    pass