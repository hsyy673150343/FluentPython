# ！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 18:00
# @Author   : 洪松
# @File     : example8_15.py


class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    # 在self.passengers上调用.remove和.append方法其实会修改传给构造方法的那个列表
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)
