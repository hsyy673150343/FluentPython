# -*- coding:utf8 -*-
# @TIME     :2019/5/4 17:17
# @Author   : 洪松
# @File     : example11_5.py

from Python数据模型 import example1_1
from random import shuffle
# FrenchDeck只实现了不可变的序列协议
deck = example1_1.FrenchDeck()
# TypeError: 'FrenchDeck' object does not support item assignment
shuffle(deck)



