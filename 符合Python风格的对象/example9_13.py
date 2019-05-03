# -*- coding:utf8 -*-
# @TIME     :2019/5/3 15:47
# @Author   : 洪松
# @File     : example9_13.py

from example9_9 import Vector2d

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)

print(len(dumpd))

v1.typecode = 'f'
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))

print(Vector2d.typecode)