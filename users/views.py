from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse,JsonResponse
from .functions import *
from django.contrib import messages


def index(request):
    return HttpResponse('ok')


def login(request):  # 登录页面的逻辑
    title = '天天生鲜-登录'
    return render(request, 'users/login.html', locals())

def login_handle(request):
    '''
    用于处理登录请求
    :param request:
    :return:
    '''
    #1.对用户名和密码做简单的校验
    print('1111')
    user = check_login_params(request)
    if user:
        print('222')
        response = auth_user(request,user)
        return response
    else:
        print('333')
        return  redirect(reverse('users:login'))# 如果用户名和密码简单校验失败则直接重回登录页面

def logout(request):
    '''
    注销操作
    :param request:
    :return:
    '''
    # 1.清除session
    flush_session(request)
    # 2.页面跳转
    return redirect(reverse('users:login'))

def register(request):
    title = '天天生鲜-注册'
    mess = get_messages(request)  # 取出错误信息
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

@check_permission
def user_center_info(request):
    title = '天天生鲜-用户中心'
    current_user = User.objects.get_user_by_name(get_session(request,'username'))
    return render(request, 'users/user_center_info.html', locals())

@check_permission
def user_center_order(request):
    title = '天天生鲜-用户中心'
    return render(request, 'users/user_center_order.html', locals())

@check_permission
def user_center_site(request):
    title = '天天生鲜-用户中心'
    current_user = User.objects.get_user_by_name(get_session(request,'username'))
    userrecv = current_user.user_recv
    useraddr = current_user.user_addr
    usercode = current_user.user_code
    usertele = current_user.user_tele
    usertele2 = usertele[:3] + '****' + usertele[-4:]
    return render(request, 'users/user_center_site.html', locals())


def check_username(request):
    '''
    检查用户名密码是否存在
    :param request:
    :return:
    '''
    if user_is_exist(request):
        return JsonResponse({'ret':1})
    else:
        return JsonResponse({'ret':0})

def user_addr_edit(request):
    '''
    更新用户信息
    :param request:
    :return:
    '''
    if check_addr_param(request):
        User.objects.user_addr_update(request)
    return redirect(reverse('users:user_center_site'))











