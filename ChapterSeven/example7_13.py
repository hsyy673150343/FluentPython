#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 16:36
# @Author   : 洪松
# @File     : example7_13.py


# def make_average():
#     count = 0
#     total = 0
#
#     def average(new_value):
#         count += 1
#         total += new_value
#         return total/count
#     return average
#
# avg = make_average()
# # UnboundLocalError: local variable 'count' referenced before assignment
# print(avg(10))


def make_average():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return average


avg = make_average()
print(avg(10))
