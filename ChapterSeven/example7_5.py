#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 16:08
# @Author   : 洪松
# @File     : example7_5.py


b = 6


# def f1(a):
#     print(a)
#     print(b)#UnboundLocalError: local variable 'b' referenced before assignment
#     b = 9
#
# f1(3)


def f2(a):
    global b
    print(a)
    print(b)
    b = 9


f2(3)
print(b)
f2(3)

b = 30
print(b)

