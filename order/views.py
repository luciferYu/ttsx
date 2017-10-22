from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your views here.
from carts.models import Cart
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