import time

from django.shortcuts import render
from django.db import transaction  #事务支持
# Create your views here.
from django.http import HttpResponse,JsonResponse


# Create your views here.
from carts.models import *
from order.models import *
from utils.wrappers import *
from users.models import *


def index(request):
    return HttpResponse('ok')

@check_permission
def place_order(request):
    title = '天天生鲜-提交订单'
    try:
        user = User.objects.get(id=get_session(request,'uid'))
    except User.DoesNotExist:
        return redirect(reverse('order:place_order'))

    # 提交订单时 购物车里选中的商品的id列表
    goods_ids = post_list(request,'goods_id')
    #print(goods_ids)
    goods_ids_string = ','.join(goods_ids)  #将提交的商品ID拼接成 ，隔开的字符串


    carts = Cart.objects.filter(cart_user_id=get_session(request,'uid'),cart_goods_id__in=goods_ids)
    total_nums = 0 #用于累计商品总数
    total_money = 0 #用于累计商品总价
    for cart in carts:
        #计算单品总价
        cart.total = cart.cart_amount * cart.cart_goods.goods_price
        total_money += cart.total
        total_nums += cart.cart_amount
    #绑定总价
    carts.total_money = total_money
    carts.total_nums = total_nums


    return render(request,'order/place_order.html',locals())


@check_permission
@transaction.atomic #当做事务函数处理
def order_handle(request):
    save_point = transaction.savepoint() #创建回滚点

    try:
        ids = post(request,'ids').split(',') # 获取订单商品
        goods_pay = post(request,'pay')  #获取订单支付方式
        #获取商品详细信息
        carts = Cart.objects.filter(cart_user_id=get_session(request,'uid'),cart_goods_id__in=ids)
        #获取用户信息
        user = User.objects.get(id=get_session(request,'uid'))
        #创建订单基础信息
        order = Order()
        order.order_addr = user.user_addr
        order.order_recv = user.user_recv
        order.order_pay = goods_pay
        order.order_user = user
        #订单编号
        order.order_number = str(user.id) + str(int(time.time())) + str(random.randint(1000,9999))
        order.save()

        #创建订单商品详细信息
        for cart in carts:
            detail = OrderDetail()
            detail.order = order
            detail.detail_amount = cart.cart_amount
            detail.detail_goodsid = cart.cart_goods_id
            detail.detail_img = cart.cart_goods.goods_image
            detail.detail_price = cart.cart_goods.goods_price
            detail.detail_name = cart.cart_goods.goods_name
            detail.detail_unit = cart.cart_goods.goods_unit
            detail.save()
        #删除购物车里相关的数据
        carts.delete()

        transaction.savepoint_commit(save_point) # 成功提交事务
    except:
        transaction.savepoint_rollback(save_point) # 失败滚回保存点

    return JsonResponse({'ret':1})












