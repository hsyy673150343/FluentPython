#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/28 16:53
# @Author   : 洪松
# @File     : example5_15.py


def clip(text, max_len=80):
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