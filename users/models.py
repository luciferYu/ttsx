from django.db import models
from db.AbstractModel import *
# Create your models here.
from utils.wrappers import *
import random


class UserManager(models.Manager):
    '''自定义管理器类'''
    def get_user_by_name(self,username):
        try:
            return self.get(user_name=username)
        except:
            return None

    #用户注册数据保存
    def user_register_save(self,request):
        user = User()
        user.user_name = post(request,'user_name')
        user.user_salt = random.randint(100000,999999)
        user.user_pass = password_encryption(post(request,'user_pass1'),user.user_salt)
        user.user_mail = post(request,'user_mail')
        user.save()


#用户模型类
class User(AbstractModel):
    user_name = models.CharField(max_length=20)  #用户名
    user_pass = models.CharField(max_length=100) #用户密码
    user_mail = models.CharField(max_length=50)  #用户邮箱
    user_addr = models.CharField(max_length=50)  #用户地址
    user_tele = models.CharField(max_length=11)  #用户手机
    user_code = models.CharField(max_length=10)   #邮政编码
    user_salt = models.CharField(max_length=6)  #用户salt

    objects = UserManager()
