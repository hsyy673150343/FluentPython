# -*- coding:utf8 -*-
# @TIME     :2019/5/4 20:19
# @Author   : 洪松
# @File     : example11_12.py


import random

from example11_9 import Tombola


class BingoCage(Tombola):  # <1>

    def __init__(self, items):
        self._randomizer = random.SystemRandom()  # <2>
        self._items = []
        self.load(items)  # <3>

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)  # <4>

    def pick(self):  # <5>
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):  # <7>
        self.pick()
