#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/27 16:12
# @Author   : 洪松
# @File     : example4_3.py

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)