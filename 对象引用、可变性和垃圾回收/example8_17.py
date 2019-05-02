# ！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 18:28
# @Author   : 洪松
# @File     : example8_17.py

import weakref
a_set = {0, 1}
# 创建弱引用对象wref
wref = weakref.ref(a_set)
print(wref)
print(wref())

a_set = {2, 3, 4}
print(wref())