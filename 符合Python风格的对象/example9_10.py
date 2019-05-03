# -*- coding:utf8 -*-
# @TIME     :2019/5/3 14:57
# @Author   : 洪松
# @File     : example9_10.py

from example9_9 import Vector2d

# Python会把私有属性名存入实例的__dict__属性中,而且会在前面加上一个下划线和类名。
v1 = Vector2d(3, 4)
print(v1.__dict__)

print(v1._Vector2d__x)