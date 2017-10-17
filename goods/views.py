from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    title= '天天生鲜-首页'
    return render(request,'goods/index.html',locals())

def detail(request):
    title= '天天生鲜-商品详情'
    return render(request,'goods/detail.html',locals())

def list(request):
    title= '天天生鲜-商品列表'
    return render(request,'goods/list.html',locals())