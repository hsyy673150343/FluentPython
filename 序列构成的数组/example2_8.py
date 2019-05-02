#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 15:15
# @Author   : 洪松
# @File     : example2_8.py

'''嵌套元组拆包'''

students_info = [
    ('小明', '24', 'male', (166, 50)),
    ('张三', '36', 'female', (178, 67)),
    ('李四', '35', 'male', (156, 50)),
    ('王明', '36', 'male', (167, 56))
]

print('{:8}   {:^9}   {:^9}'.format('', '身高', '体重'))
fmt = '{:8} | {:9.4f} | {:9.4f}'
for name, age, sex, (height, weight) in students_info:
    if height <= 170:
        print(fmt.format(name, height, weight))