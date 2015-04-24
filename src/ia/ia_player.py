#-*- coding: utf-8 -*-

from random import choice

from src.game.hand import Hand

class IAPlayer(object):


    def __init__(self, pid, removable=True):
        self.nick = ""
        self.event = dict()
        self._hand = Hand()
        self.id = pid
        self.__removable = removable


    def give_cards(self, cards):
        self._hand.add(cards)


    def get_hand(self):
        return self._hand


    def team(self):
        return self.id % 2


    def get_card(self, played, playable):
        # For now, return a random card
        return choice(playable)


    def get_bid(self, bidded, biddable):
        # For now, return a random bidding
        return choice(biddable)


    def bidded(self, bid):
        pass


    def played(self, pid, card):
        pass


    def is_removable(self):
        return self.__removable
