from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('ok')

def carts(request):
    return render(request,'carts/cart.html')
