#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from haystack import indexes
from .models import GoodsInfo


# 指定对于某个类的某些数据建立索引
class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()




if __name__ == '__main__':
    pass