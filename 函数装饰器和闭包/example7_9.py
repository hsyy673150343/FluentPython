#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 16:18
# @Author   : 洪松
# @File     : example7_9.py


def make_averager():
    series = []

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return average


avg = make_averager()
print(avg(10))
print(avg(11))
# 编译后的函数定义体中保存局部变量和自由变量的名称
print(avg.__code__.co_varnames)

# 自由变量的名称
print(avg.__code__.co_freevars)

print(avg.__closure__)

print(avg.__closure__[0].cell_contents)