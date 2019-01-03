# coding:utf-8
import os, sys
import random


class Rule:

    def __init__(self):
        self.poker = {}
        self.poker_list = os.listdir('./static/poker/')
        self.poker_list.remove('.DS_Store')
        for i in self.poker_list:
            j = i.replace('', '.jpg')
            k = j.split('_')
            self.poker[i] = {'color': k[0], 'value': k[1]}

    def deal(self):
        player1 = random.sample(self.poker_list, 3)
        for i in range(0, 3):
            self.poker_list.remove(player1[i])
        player2 = random.sample(self.poker_list, 3)
        return player1, player2

    def is_baozi(self):
        pass

    def is_jinhua(self):
        pass

    def is_shunzi(self):
        pass

    def is_pair(self):
        pass

    def compare(self):
        pass


if __name__ == '__main__':
    rule = Rule()
    print(rule.deal()[0])
