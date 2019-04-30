#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 16:08
# @Author   : 洪松
# @File     : example5_1.py

def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))