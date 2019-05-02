#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 16:10
# @Author   : 洪松
# @File     : example8_3.py

# charles和lewis指代同一个对象
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis), sep='\n')
lewis['sex'] = 'male'
print(charles)


alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'sex': 'male'}
print(alex == charles)
print(alex is not charles)