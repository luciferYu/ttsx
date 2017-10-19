#!/usr/bin/python3
# -*- coding:utf-8 -*-
# auth:zhiyi
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from utils.wrappers import *
from django.utils import deprecation


# 记录用户访问url中间件
class RecordUrlMiddleware(deprecation.MiddlewareMixin):
    def process_request(self, request):
        #定义不记录的url列表
        exclue_urls = [
            reverse('users:login'),
            reverse('users:login_handle'),
            reverse('users:register_handle'),
            reverse('users:register'),
            reverse('users:index'),

        ]
        if request.path not in exclue_urls:
            # 记录url
            # request.session['pre_url'] = request.get_full_path()
            set_session(request, 'pre_url', request.get_full_path())
            print('pre_url', get_session(request, 'pre_url'))
        print('in middle')

if __name__ == '__main__':
    pass
