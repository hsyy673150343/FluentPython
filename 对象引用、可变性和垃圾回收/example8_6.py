#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 16:53
# @Author   : 洪松
# @File     : example8_6.py

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)
