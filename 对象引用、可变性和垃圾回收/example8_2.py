#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 16:02
# @Author   : 洪松
# @File     : example8_2.py


class Gizmo:
    def __init__(self):
        print('Gizmo id： %d' % id(self))

# 创建对象之后才会把变量分配给对象
x = Gizmo()
