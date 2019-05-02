# ！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 17:41
# @Author   : 洪松
# @File     : example8_12.py

# 没有指定初始乘客的HauntedBus实例会共享同一个乘客列表
class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)

bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)

# bus3 一开始也是空的, 因此还是赋值默认的列表,但是默认列表此时不为空
bus3 = HauntedBus()
print(bus3.passengers)
# 登上bus3的Dave出现在bus2中
bus3.pick('Dave')
print(bus2.passengers)

print(bus2.passengers is bus3.passengers)

print(bus1.passengers)

print(dir(HauntedBus.__init__))
print(HauntedBus.__init__.__defaults__)
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)