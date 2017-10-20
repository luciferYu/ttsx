from django.db import models
from db.AbstractModel import *
from tinymce.models import HTMLField


# Create your models here.

class Category(AbstractModel):
    '''
    商品分类类
    '''
    cag_name = models.CharField(max_length=30)  # 分类名称
    cag_image = models.ImageField(upload_to='banner')  # 分类图片


class GoodsInfoManager(models.Manager):
    def get_new_goods(self,cag):
        '''获得最新添加的商品4个'''
        return self.filter(goods_cag=cag).order_by('-id')[:4]

    def get_hot_goods(self,cag):
        return self.filter(goods_cag=cag).order_by('-goods_visits')[:3]

    def get_new_by_all_goods(self):
        return self.all().order_by('-id')[:2]

    def get_goods_by_cagid(self,cag_id):
        return self.filter(goods_cag_id=cag_id)


class GoodsInfo(AbstractModel):
    '''
    商品信息类
    '''

    goods_name = models.CharField(max_length=30)  # 商品名称
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)  # 商品价格
    goods_image = models.ImageField(upload_to='goods')  # 商品图片
    goods_short = models.CharField(max_length=100)  # 商品简述
    goods_desc = HTMLField()  # 商品详情
    goods_status = models.BooleanField(default=True)  # 商品上架
    goods_unit = models.CharField(max_length=20)  # 商品单位
    goods_visits = models.IntegerField(default=0)  # 商品访问量
    goods_sales = models.IntegerField(default=0)  # 商品销量
    goods_discount = models.FloatField(default=1.0)  # 商品折扣
    goods_invetory = models.IntegerField(default=0) # 商品库存

    goods_cag = models.ForeignKey(Category)  # 商品所属分类

    objects = GoodsInfoManager()


class Advertise(AbstractModel):
    ad_name = models.CharField(max_length=30)  # 广告名称
    ad_image = models.ImageField(upload_to='adv')  # 广告图片
    ad_link = models.CharField(max_length=200)  # 广告链接



