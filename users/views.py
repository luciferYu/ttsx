from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your views here.



def index(request):
    return HttpResponse('ok')

def login(request): #登录页面的逻辑
    title = '天天生鲜登录'
    return render(request,'users/login.html',locals())

def register(request):
    pass

def user_center_info(request):
    pass

def user_center_order(request):
    pass

def user_center_site(request):
    pass