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
    return render(request,'carts/cart.html')

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





