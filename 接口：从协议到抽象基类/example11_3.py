# -*- coding:utf8 -*-
# @TIME     :2019/5/4 17:08
# @Author   : 洪松
# @File     : example11_3.py

class Foo:
    def __getitem__(self, item):
        return range(0, 30, 10)[item]


f = Foo()
print(f[1])

for i in f:
    print(i)

print(10 in f)
print(15 in f)