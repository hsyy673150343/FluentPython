#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 15:49
# @Author   : 洪松
# @File     : example7_1.py


def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


target()
print(target)