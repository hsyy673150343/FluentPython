#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 21:00
# @Author   : 洪松
# @File     : example7_19.py

import functools
from example7_16 import clock


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(30))
