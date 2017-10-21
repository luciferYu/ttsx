from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
from goods.models import *
from utils.wrappers import *
from .functions import *
from django.core.paginator import Paginator  # 导入分页


def index(request):
    title= '天天生鲜-首页'
    cags = Category.objects.all() # 获取商品分类
    for cag in cags:
        new_goods = GoodsInfo.objects.get_new_goods(cag) #获得最新商品
        hot_goods = GoodsInfo.objects.get_hot_goods(cag) #获得最热商品

        cag.new = new_goods
        cag.hot = hot_goods

    return render(request,'goods/index.html',locals())

def detail(request):
    '''
    商品详情页
    :param request:
    :return:
    '''
    title= '天天生鲜-商品详情'
    cags = Category.objects.all()  # 获取商品分类
    try:
        goods = GoodsInfo.objects.get(pk=get(request,'id'))
        goods.goods_visits = int(goods.goods_visits) + 1 # 增加一次访问量
        goods.save() # 保存访问量
        #获得最新的商品
        goods_new = GoodsInfo.objects.get_new_by_all_goods()
        update_user_browse_record(request) #更新用户浏览记录
    except:
        return redirect(reverse('goods:index'))
    return render(request,'goods/detail.html',locals())

def list(request,cag_id,page_id):
    title= '天天生鲜-商品列表'
    cags = Category.objects.all() # 获取商品分类
    #根据对应的商品分类获取商品
    show = get(request,'show')
    goods_list = GoodsInfo.objects.get_goods_by_cagid(cag_id,show)

    #分页制作
    paginator = Paginator(goods_list,10) #每页分10个商品

    current_page =paginator.page(page_id)  #获得当前分页数据

    #获取连个最新的广告商品
    goods_new = GoodsInfo.objects.get_new_by_all_goods()

    page_id = int(page_id)  #此处一定要转换类型才可以在模板里进行比较，实现分页高亮效果

    return render(request,'goods/list.html',locals())