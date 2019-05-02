# ！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 20:29
# @Author   : 洪松
# @File     : example8_20.py

# 使用另一个元组构建元组,得到的其实是同一个元组
t1 = (1, 2, 3)
t2 = tuple(t1)

print(t2 is t1)

t3 = t1[:]
print(t3 is t1)