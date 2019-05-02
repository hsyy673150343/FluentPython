#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 16:53
# @Author   : 洪松
# @File     : example5_16.py

from example5_15 import clip

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)#函数中的参数的名称
print(clip.__code__.co_argcount)