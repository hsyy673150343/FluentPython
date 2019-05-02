#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 20:33
# @Author   : 洪松
# @File     : example2_23.py

'''使用双向队列'''
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-3)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 22, 33])
print(dq)

dq.extendleft([44, 55, 66])
print(dq)