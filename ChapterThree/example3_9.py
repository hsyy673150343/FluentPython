#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/22 20:35
# @Author   : 洪松
# @File     : example3_9.py

'''用MappingProxyType来获取字典的只读实例mappingproxy'''

from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
# d_proxy[2] = 'x'#TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'
print(d_proxy)

