from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse
from .functions import *
from django.contrib import messages


def index(request):
    return HttpResponse('ok')


def login(request):  # 登录页面的逻辑
    title = '天天生鲜-登录'
    return render(request, 'users/login.html', locals())


def register(request):
    title = '天天生鲜-注册'
    mess = get_messages(request) #取出错误信息
    return render(request, 'users/register.html', locals())


def register_handle(request):  # 处理注册
    '''
     #检测注册参数是否合法
    :param request: 请求
    :return: 成功 数据入库返回登录页面 失败重新跳转注册页面
    '''
    if check_register_params(request):
        User.objects.user_register_save(request)  # 合法 用户入库
        print('用户合法')
        return redirect(reverse('users:login'))  # 跳转到登录页面
    else:
        # 如何验证失败，跳回验证页面
        print('用户不合法')
        return redirect(reverse('users:register'))


def user_center_info(request):
    title = '天天生鲜-用户中心'
    return render(request, 'users/user_center_info.html', locals())


def user_center_order(request):
    title = '天天生鲜-用户中心'
    return render(request, 'users/user_center_order.html', locals())


def user_center_site(request):
    title = '天天生鲜-用户中心'
    return render(request, 'users/user_center_site.html', locals())
