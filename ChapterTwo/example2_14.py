#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 16:33
# @Author   : 洪松
# @File     : example2_14.py

t = (1, 2, [30, 40])
t[2] += [50, 60]#TypeError: 'tuple' object does not support item assignment
print(t)

