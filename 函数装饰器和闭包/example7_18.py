#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 20:58
# @Author   : 洪松
# @File     : example7_18.py

from example7_16 import clock


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(30))
