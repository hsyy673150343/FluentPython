#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 16:00
# @Author   : 洪松
# @File     : example8_1.py


# 变量a和b引用同一个列表,而不是那个列表的副本
a = [1, 2, 3]
b = a
a.append(4)
print(b)
