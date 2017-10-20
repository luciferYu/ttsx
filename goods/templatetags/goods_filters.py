#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from django.template import Library

register = Library()

def create_banner_image_name(filename):
    return 'images/banner/' + str(filename) + '.jpg'

register.filter('create_banner_image_name',create_banner_image_name)

def create_goods_image_name(filename):
    new_filename = 'goods'
    if len(str(filename)) == 6:
        new_filename += ('0' + str(filename))
    elif len(str(filename)) == 5:
        new_filename += ('00' + str(filename))
    path = 'images/goods/' + new_filename
    return path

register.filter('create_goods_image_name',create_goods_image_name)

def browse_history_sort(goods_list):
    return goods_list.order_by('-update_time')
register.filter('browse_history_sort',browse_history_sort)

if __name__ == '__main__':
    pass