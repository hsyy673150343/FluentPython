#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/21 16:18
# @Author   : 洪松
# @File     : example2_12.py

'''建立由列表组成的列表'''

board = [['_']*3 for i in range(3)]
print(board)
board[1][1] = 'hs'
print(board)


'''与上面等效'''

board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)
board[1][1] = 'yy'
print(board)