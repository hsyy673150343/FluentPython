#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 18:12
# @Author   : 洪松
# @File     : example7_15.py

import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter()
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
