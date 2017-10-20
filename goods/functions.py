#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from utils.common import *
from users.models import *
def update_user_browse_record(request):
    if not user_is_login(request): #如果用户没有登录直接返回
        print('1111')
        return
    browse_history_limit = 5
    #如果用户登录
    goods_id = get(request,'id') # 获得正在浏览的商品id
    user_id = get_session(request,'uid') # 获得浏览用户id
    print(goods_id,user_id)
    try:
        print('2222')
        # 如果商品已经存在历史记录，则更新商品浏览记录的时间
        record = UserBrowseHistory.objects.get(browse_goods=goods_id,browse_user=user_id)
        record.save()
    except UserBrowseHistory.DoesNotExist:
    # 如果商品不存在
        record = UserBrowseHistory.objects.filter(browse_user=user_id).order_by('update_time')
        # 如果浏览记录不到5条，则插入新记录
        if record.count() < browse_history_limit:
            print('3333')
            ubh = UserBrowseHistory()
            ubh.browse_goods_id = goods_id
            ubh.browse_user_id = user_id
            ubh.save()
        else:
            # 如果浏览记录超过5条，则更新最旧记录
            print('44444')
            ubh = record[0]
            ubh.browse_goods_id = goods_id
            ubh.save()
    finally:
        return




if __name__ == '__main__':
    pass