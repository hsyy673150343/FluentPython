#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/22 17:52
# @Author   : 洪松
# @File     : example3_6.py

class StrKeyDict0(dict):  # <1>

    def __missing__(self, key):
        if isinstance(key, str):  # <2>
            raise KeyError(key)
        return self[str(key)]  # <3>

    def get(self, key, default=None):
        try:
            return self[key]  # <4>
        except KeyError:
            return default  # <5>

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()  # <6>

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])