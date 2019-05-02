#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 13:54
# @Author   : 洪松
# @File     : example2_3.py

'''用列表推导和map/filter组合创建同样的表单'''
symbols = 'FGHJK'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 72]
print(beyond_ascii)
'''两种写法一致'''
beyond_ascii = list(filter(lambda c: c > 72, map(ord, symbols)))
print(beyond_ascii)