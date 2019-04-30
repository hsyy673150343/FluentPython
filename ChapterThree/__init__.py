#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/22 16:48
# @Author   : 洪松
# @File     : __init__.py.py

from collections import Counter

ct = Counter(['a', 'a','b','b','c','c'])
print(ct)

for key,value in ct.items():
    print(key, value)