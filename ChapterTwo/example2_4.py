#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 14:03
# @Author   : 洪松
# @File     : example2_4.py

'''使用列表推导计算笛卡儿积'''
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print('先颜色,后尺码的顺序排序--',tshirts)

for color in colors:
    for size in sizes:
        print(color, size)

tshirts = [(color, size) for size in sizes for color in colors]
print('先尺码,后颜色的顺序排序--',tshirts)