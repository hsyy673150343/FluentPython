# ！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 21:16
# @Author   : 洪松
# @File     : example9_4.py


class Demo:
    @classmethod
    def kclassmeth(*args):
        return args
    @staticmethod
    def statmeth(*args):
        return args

# 不管怎么调用类方法,它的第一个参数始终是Demo类
print(Demo.kclassmeth())
print(Demo.kclassmeth('spam'))

# 静态方法的行为与普通的函数相似
print(Demo.statmeth())
print(Demo.statmeth('spam'))
