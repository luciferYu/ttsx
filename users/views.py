from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your views here.



def index(request):
    return HttpResponse('ok')

def login(request): #登录页面的逻辑
    title = '天天生鲜-登录'
    return render(request,'users/login.html',locals())

def register(request):
    title = '天天生鲜-注册'
    return render(request,'users/register.html',locals())

def user_center_info(request):
    title = '天天生鲜-用户中心'
    return render(request,'users/user_center_info.html',locals())

def user_center_order(request):
    title = '天天生鲜-用户中心'
    return render(request,'users/user_center_order.html',locals())

def user_center_site(request):
    title = '天天生鲜-用户中心'
    return render(request,'users/user_center_site.html',locals())