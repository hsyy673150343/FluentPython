# ！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/2 18:07
# @Author   : 洪松
# @File     : example8_15-1.py


class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        # 创建副本
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)