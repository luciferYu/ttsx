from django.test import TestCase
from .models import *
import random

# Create your tests here.
cags = ['新鲜水果', '海鲜水产', '猪牛羊肉', '禽类蛋品', '新鲜蔬菜', '速冻食品']

for cag in cags:
    i = 0
    c = Category()
    c.cag_name = cag
