#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 21:17
# @Author   : 洪松
# @File     : example7_22.py

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


print('running main()')
print('registry ->', registry)
f1()
