from django.shortcuts import render
from django.http import HttpResponse
from utils.wrappers import *
# Create your views here.
def index(request):
    return HttpResponse('ok')
@check_permission
def carts(request):
    return render(request,'carts/cart.html')
