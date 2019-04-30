#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 15:34
# @Author   : 洪松
# @File     : example2_9.py

'''定义和使用具名元组'''

from collections import namedtuple

StudentInformation = namedtuple('StudentInformation', 'name age sex heightandweight')

student_1 = StudentInformation('李四','35', 'male', (156, 50))
print(student_1)
print(student_1.name)
print(student_1[0])


