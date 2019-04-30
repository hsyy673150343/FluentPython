#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/22 17:26
# @Author   : 洪松
# @File     : example3_2.py

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point
            # occurrences = index.get(word, [])  # <1>
            # occurrences.append(location)       # <2>
            # index[word] = occurrences          # <3>
            index.setdefault(word, []).append(location)#可以代替以上三行代码

# print in alphabetical order
for word in sorted(index, key=str.upper):  # <4>
    print(word, index[word])