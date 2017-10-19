"""ttsx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include # 引入包 转url到应用中的url里
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$',RedirectView.as_view(url=r'static/images/favicon.ico'),name='favicon'),
    #以下是url委托
    url(r'^$',RedirectView.as_view(url=r'/goods/index/')),
    url(r'^users/',include('users.urls',namespace='users')), #用户模块
    url(r'^order/',include('order.urls',namespace='order')), #订单模块
    url(r'^carts/',include('carts.urls',namespace='carts')), #购物车模块
    url(r'^goods/',include('goods.urls',namespace='goods')), #商品模块
]
