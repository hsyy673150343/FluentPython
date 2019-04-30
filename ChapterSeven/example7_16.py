#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 18:19
# @Author   : 洪松
# @File     : example7_16.py

import time
from example7_15 import clock


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))