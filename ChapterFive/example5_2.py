#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 16:12
# @Author   : 洪松
# @File     : example5_2.py

from example5_1 import factorial

fact = factorial
print(fact)
print(fact(5))

x = map(factorial, range(11))
print(x)
print(list(x))

print(dir(factorial))