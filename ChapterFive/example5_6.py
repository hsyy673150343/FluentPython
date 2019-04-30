#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 16:21
# @Author   : 洪松
# @File     : example5_6.py

from functools import reduce
from operator import add

print(reduce(add, range(100)))

print(sum(range(100)))