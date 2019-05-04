# -*- coding:utf8 -*-
# @TIME     :2019/5/4 20:10
# @Author   : 洪松
# @File     : example11_11.py

from example11_9 import Tombola


class Fake(Tombola):
    def pick(self):
        return 123


print(Fake)
# TypeError: Can't instantiate abstract class Fake with abstract methods load
f = Fake()
