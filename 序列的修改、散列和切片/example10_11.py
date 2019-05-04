# -*- coding:utf8 -*-
# @TIME     :2019/5/4 15:47
# @Author   : 洪松
# @File     : example10_11.py

import functools
import operator
# 计算整数0-5的累计异或的三种方式
n = 0
for i in range(1, 6):
    n ^= i
print(n)

# -----------------------#
x = functools.reduce(lambda a, b: a^b, range(6))
print(x)

# -----------------------#
y = functools.reduce(operator.xor, range(6))
print(y)