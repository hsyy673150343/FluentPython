#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/22 20:53
# @Author   : 洪松
# @File     : example3_13.py

'''新建一个Latin-1字符集合，该集合里的每个字符的Unicode名字里都有‘SIGN’这个单词'''

from unicodedata import name

st = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(st)

