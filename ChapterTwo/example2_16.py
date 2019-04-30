#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 16:45
# @Author   : 洪松
# @File     : example2_16.py

import dis
'''查看字节码'''
byte_code = dis.dis('s[a] += b')
print(byte_code)