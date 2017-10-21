from django.db import models
from db.AbstractModel import *
# Create your models here.

class CartManager(models.Manager):
    pass

class Cart(AbstractModel):
    '''
    购物车模型类
    '''
    cart_goods = models.ForeignKey('goods.GoodsInfo')  # 商品
    cart_amount = models.IntegerField()  #购买数量
    cart_user = models.ForeignKey('users.User')# 购买用户

    objects = CartManager()
