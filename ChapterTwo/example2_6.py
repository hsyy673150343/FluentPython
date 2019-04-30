#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 14:23
# @Author   : 洪松
# @File     : example2_6.py

'''使用生成器表达式计算笛卡儿积'''

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshrit in ('%s, %s' % (c, s) for c in colors for s in sizes):
    print(tshrit)