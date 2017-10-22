from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from utils.wrappers import *
from utils.common import *
from .models import *

# Create your views here.
def index(request):
    return HttpResponse('ok')
@check_permission
def carts(request):
    '''购物车主页函数
    '''
    #获取当前用户的购物车数据
    carts = Cart.objects.filter(cart_user_id=get_session(request,'uid'))
    #计算购物总价
    total = 0
    #计算购物总数
    money = 0

    for cart in carts:
        cart.single_total = cart.cart_amount * cart.cart_goods.goods_price # 单品总价小计
        total += cart.cart_amount # 累加商品总价
        money += cart.single_total #累加商品总数

    # 绑定到购物车
    carts.money = money
    carts.total = total


    return render(request,'carts/cart.html',locals())

@check_permission
def add_goods(request):
    '''
    添加购物车逻辑
    :param request:
    :return:
    '''
    # 获取用户ID、获取商品ID、获得商品数量
    goods_id = get(request,'goods_id')
    user_id = get_session(request,'uid')
    goods_num = get(request,'goods_num')
    # 判断商品是否已经在购物车中
    try:
        #存在： 则只更新商品数量
        cart = Cart.objects.get(cart_goods_id=goods_id,cart_user_id=user_id)
        cart.cart_amount = cart.cart_amount + int(goods_num)
        cart.save()
    except Cart.DoesNotExist:
        #不存在： 新增一条购物车商品数据
        cart = Cart()
        cart.cart_goods_id = goods_id
        cart.cart_user_id = user_id
        cart.cart_amount = int(goods_num)
        cart.save()
    # 将当前用户购物车中的商品与数量返回
    # 通过聚合获取
    #goods_num_in_cart = Cart.objects.filter(cart_user_id=user_id).aggregate(models.Sum('cart_amount'))
    goods_in_cart = Cart.objects.filter(cart_user_id=user_id)
    total = 0
    for goods in goods_in_cart:
        total += goods.cart_amount

    return JsonResponse({'total':total})


def goods_num(request):
    '''初始化购物车数量'''
    user_id = get_session(request, 'uid')
    if user_id:
        goods_in_cart = Cart.objects.filter(cart_user_id=user_id)
        total = 0
        for goods in goods_in_cart:
            total += goods.cart_amount

        return JsonResponse({'total': total})
    else:
        return JsonResponse({'total': 0})

def edit_goods_num(request):
    goods_id = get(request,'goods_id')#从ajax请求获取商品id
    goods_num = get(request,'goods_num') # 获取购物车里的商品数量

    try:
        #如果正常取出购物车里的信息，则更新该商品的数量并保存，返回成功
        cart = Cart.objects.get(cart_user_id=get_session(request,'uid'),cart_goods_id=goods_id)
        cart.cart_amount = goods_num
        cart.save()
    except Cart.DoesNotExist:
        #否则更新失败
        return JsonResponse({'ret':0})
    return JsonResponse({'ret': 1})

def remove_goods(request):
    '''
    接受删除商品的ajax请求
    :param request:
    :return:
    '''
    goods_id = get(request, 'goods_id')  # 从ajax请求获取商品id
    try:
        # 找到商品的ID的条目并删除
        cart = Cart.objects.get(cart_user_id=get_session(request, 'uid'), cart_goods_id=goods_id)
        cart.delete()
    except Cart.DoesNotExist:
        # 如果没有查到数据，什么都不做
        pass
    return JsonResponse({'ret': 1})


