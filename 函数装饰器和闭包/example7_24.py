#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 21:38
# @Author   : 洪松
# @File     : example7_24.py

from example7_23 import *

print(registry)

# register()表达式返回decorate,然后把它应用到f3上
register()(f3)

print(registry)

# 这次调用从registry中删除f2
register(active=False)(f2)

print(registry)
