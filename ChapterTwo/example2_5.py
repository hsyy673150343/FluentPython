#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 14:15
# @Author   : 洪松
# @File     : example2_5.py

'''用生成器表达式初始化元组和数组'''

symbols = 'JHDLSE'
tp = tuple(ord(symbol) for symbol in symbols)
print(tp)

import array

ar = array.array('I', (ord(symbol) for symbol in symbols))
print(ar)