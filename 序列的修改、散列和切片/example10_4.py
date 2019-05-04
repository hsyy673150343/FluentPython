# -*- coding:utf8 -*-
# @TIME     :2019/5/3 16:19
# @Author   : 洪松
# @File     : example10_4.py


class MySeq:
    def __getitem__(self, item):
        return item


s = MySeq()
print(s[1])
print(s[1:4])
print(s[1:4:2])

print(s[1:4:2, 9])
print(s[1:4:2, 7:9])