from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your views here.
from utils.wrappers import *


def index(request):
    return HttpResponse('ok')

@check_permission
def place_order(request):
    title = '天天生鲜-提交订单'
    return render(request,'order/place_order.html',locals())