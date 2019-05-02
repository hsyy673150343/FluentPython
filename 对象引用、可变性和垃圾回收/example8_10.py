#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 17:19
# @Author   : 洪松
# @File     : example8_10.py
from copy import deepcopy

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)

c = deepcopy(a)
print(c)
