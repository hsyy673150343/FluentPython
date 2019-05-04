#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/20 19:44
# @Author   : 洪松
# @File     : example1_1.py

import collections

# 用collections.namedtuple构建了一个简单的类来表示一张纸牌
# namedtuple用以构建只有少数属性但是没有方法的对象---比如数据库条目
Card = collections.namedtuple('Card',['rank','suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = '黑桃 方块 梅花 红桃'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

'''
deck = FrenchDeck()

print(len(deck))


beer_card = Card('7','方块')
print(beer_card)

print(deck[0])
print(deck[-1])


from random import choice

print(choice(deck))

print(deck.ranks)


print(deck[:3])

print([deck[12::13]])


for card in deck:
    print(card)

print(Card('Q','红桃') in deck)
print(Card('7','白桃') in deck)


suit_values = dict(黑桃=3, 红桃=2, 方块=1, 梅花=0)
print(suit_values)
print(len(suit_values))

# 排序
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
'''