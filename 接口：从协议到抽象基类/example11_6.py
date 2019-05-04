# -*- coding:utf8 -*-
# @TIME     :2019/5/4 17:21
# @Author   : 洪松
# @File     : example11_6.py

from Python数据模型 import example1_1
from random import shuffle


def set_card(deck, position, card):
    deck._cards[position] = card


deck = example1_1.FrenchDeck()
example1_1.FrenchDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])