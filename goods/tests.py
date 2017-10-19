from django.test import TestCase
from .models import *
import random

# Create your tests here.
cags = ['新鲜水果', '海鲜水产', '猪牛羊肉', '禽类蛋品', '新鲜蔬菜', '速冻食品']
i = 1
for cag in cags:
    c = Category()
    c.cag_name = cag
    c.cag_image = 'banner0' + str(i)
    i += 1
    c.save()

units = ['500克', '1吨', '2个', '3条', '1包', '5支', '1头', '2瓶']

with open('.\\goods\\data.txt','r',encoding='utf-8') as f:
    for goods_name in f:
        #创建商品对象
        goods = GoodsInfo()
        goods.good_name = goods_name[:-1]
        goods.goods_short = '商品非常好，一天销量破百万!'
        goods.goods_desc = '商品非常非常详细的描述在这里!'
        goods.goods_cag_id = random.randint(1, len(cags))
        goods.goods_image =  str(random.randint(1, 18)) + '.jpg'
        goods.goods_price = random.random() * 999
        goods.goods_unit = random.choice(units)

        # 保存商品
        goods.save()


