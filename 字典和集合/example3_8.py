#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/22 20:19
# @Author   : 洪松
# @File     : example3_8.py

import collections

class StrKeyDict(collections.UserDict):  # <1>

    def __missing__(self, key):  # <2>
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data  # <3>

    def __setitem__(self, key, item):
        self.data[str(key)] = item   # <4>