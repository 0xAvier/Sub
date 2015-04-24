#-*- coding: utf-8 -*-

from random import choice

from src.game.bidding import Bidding
from src.game.hand import Hand

class IAPlayer(object):


    def __init__(self, pid, removable=True):
        self.nick = ""
        self.event = dict()
        self._hand = Hand()
        self.id = pid
        self.__removable = removable


    def give_cards(self, cards):
        pass


    def get_card(self, played, playable):
        # For now, return a random card
        return choice(playable)


    def get_bid(self, bidded, biddable):
        # For now, always pass
        return Bidding(self.id)


    def bidded(self, bid):
        pass


    def played(self, pid, card):
        pass

    def is_removable(self):
        return self.__removable


    def reset_hand(self):
        pass
