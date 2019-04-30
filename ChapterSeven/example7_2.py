#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/30 15:57
# @Author   : 洪松
# @File     : example7_2.py

registry = []  # <1>


def register(func):  # <2>
    print('running register(%s)' % func)  # <3>
    registry.append(func)  # <4>
    return func  # <5>


@register  # <6>
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():  # <7>
    print('running f3()')


def main():  # <8>
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__=='__main__':
    main()  # <9>
