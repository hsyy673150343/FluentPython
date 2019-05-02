# ！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 18:14
# @Author   : 洪松
# @File     : example8_16.py

import weakref
s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind')


ender = weakref.finalize(s1, bye)
print(ender.alive)
# del不会删除对象,但执行del操作后可能会导致对象不可获取,从而被删除
del s1
print(ender.alive)

s2 = 'spam'
print(ender.alive)