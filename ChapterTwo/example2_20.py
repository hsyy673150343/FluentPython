#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 17:04
# @Author   : 洪松
# @File     : example2_20.py

'''一个浮点型数组的创建、存入文件和从文件读取的过程'''
from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open(r'D:\float.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open(r'D:\float.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats == floats2)