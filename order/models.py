from django.db import models
from db.AbstractModel import *
# Create your models here.

class OrderDetail(AbstractModel):
    detail_name = models.CharField(max_length=50) # 商品名称
    detail_price = models.DecimalField(max_digits=10, decimal_places=2)  #商品价格
    detail_amount = models.IntegerField() #商品数量
    detail_unit = models.CharField(max_length=20)
    detail_img = models.ImageField(upload_to='goods')
    detail_goodsid = models.IntegerField()
    order = models.ForeignKey('order.Order')



class Order(AbstractModel):
    status = (
        (1,'待付费'),
        (2,'待发货'),
        (3,'待收货'),
        (4,'待完成'),
    )

    pay = (
        (1,'货到付款'),
        (2,'微信支付'),
        (3,'支付宝支付'),
        (4,'银联支付'),
    )

    order_number = models.CharField(max_length=50) # 订单编号
    order_addr = models.CharField(max_length=100)  # 收货地址
    order_recv = models.CharField(max_length=10)  # 收货人
    order_fee = models.DecimalField(default=10,decimal_places=2,max_digits=10)  # 运费
    order_status = models.SmallIntegerField(choices=status,default=1)#送货方式
    order_pay = models.SmallIntegerField(choices=pay,default=1) # 支付方式
    order_user = models.ForeignKey('users.User')  # 订单商品列表
















