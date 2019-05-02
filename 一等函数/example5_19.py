#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 17:11
# @Author   : 洪松
# @File     : example5_19.py


def clip(text: str, max_len: 'int > 0'=80) ->str:#有注解的函数声明
    """在max_len前面或者后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()

print(clip.__annotations__)