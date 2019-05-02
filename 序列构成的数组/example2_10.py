#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 15:52
# @Author   : 洪松
# @File     : example2_10.py
from collections import namedtuple

'''具名元组的属性和方法'''
Student = namedtuple('StudentInformation', 'name age sex nameandage')

print(Student._fields)

NA = namedtuple('NA', ' name age')
info = ('Bob', '23', 'famale', NA('Bob', 24))
info_recv = Student._make(info)
print(info_recv._asdict())