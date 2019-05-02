# ！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 18:35
# @Author   : 洪松
# @File     : example8_18.py

import weakref


class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
                Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese


print(sorted(stock.keys()))

del catalog
print(sorted(stock.keys()))