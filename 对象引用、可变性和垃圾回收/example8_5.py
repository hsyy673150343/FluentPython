#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 16:46
# @Author   : 洪松
# @File     : example8_5.py

# 元组的值会随着引用的可变对象的变化而变。元组中不可变的是元素的标识。
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(id(t1[-1]))

print(t1 == t2)
