# ！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 17:26
# @Author   : 洪松
# @File     : example8_11.py


def f(a, b):
    a += b
    return a


x = 1
y = 2
print(f(x, y))
print(x, y)

a = [1, 2]
b = [3, 4]
print(f(a, b))

print(a, b, sep=' ')

t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t, u, sep=' ')