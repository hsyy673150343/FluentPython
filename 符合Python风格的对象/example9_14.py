# -*- coding:utf8 -*-
# @TIME     :2019/5/3 15:52
# @Author   : 洪松
# @File     : example9_14.py

from example9_9 import Vector2d


class ShortVector2d(Vector2d):
    typecode = 'f'


sv = ShortVector2d(1/11, 1/27)

print(sv)

print(len(bytes(sv)))