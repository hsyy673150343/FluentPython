#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 16:59
# @Author   : 洪松
# @File     : example5_17.py

from example5_15 import clip
from inspect import signature

sig = signature(clip)
print(sig)

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)