#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 16:37
# @Author   : 洪松
# @File     : example5_9.py


class C:
    pass


obj = C()


def fuc():
    pass


print(sorted(set(dir(fuc)) - set(dir(obj))))


