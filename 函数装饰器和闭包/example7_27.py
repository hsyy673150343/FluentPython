#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 22:02
# @Author   : 洪松
# @File     : example7_27.py

import time
from example7_25 import clock


@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze(.123)