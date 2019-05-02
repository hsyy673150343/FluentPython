#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/22 17:38
# @Author   : 洪松
# @File     : example3_5.py

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)     # <1>
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)  # <2>

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])