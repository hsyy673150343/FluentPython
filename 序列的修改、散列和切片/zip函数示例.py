# -*- coding:utf8 -*-
# @TIME     :2019/5/4 16:25
# @Author   : 洪松
# @File     : zip函数示例.py

from itertools import zip_longest

x = zip(range(3), 'ABC')
print(x)
print(list(x))


y = list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))
print(y)

z = list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1))
print(z)