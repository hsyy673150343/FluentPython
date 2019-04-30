#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 16:30
# @Author   : 洪松
# @File     : example5_8.py
import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))