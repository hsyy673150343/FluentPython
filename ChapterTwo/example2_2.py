#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 13:43
# @Author   : 洪松
# @File     : example2_2.py

'''列表推导 '''
symbols = 'ABC'
codes = [ord(symbol) for symbol in symbols]
print(codes)