#-*- coding: utf-8 -*-

from random import choice, randint
from time import sleep

from src.game.coinche import COINCHE_CODE
from src.game.bidding import Bidding
from src.game.hand import Hand

class IAPlayer(object):


    def __init__(self, pid, removable=True):
        self.nick = ""
        self.event = dict()
        self._hand = Hand()
        self.id = pid
        self.__removable = removable
        self.__nb_bid = 0
        self.coinche = None


    def set_method(self, evt, method):
        if evt == "coinche":
            self.coinche = method

    def give_cards(self, cards):
        pass


    def get_card(self, played, playable):
        # For now, return a random card
        return choice(playable)


    def get_bid(self, bidded, biddable):
        sleep(randint(1, 3))
        if self.__nb_bid == 0 and randint(0, 1)  == 1:
            self.__nb_bid += 1
            return biddable[1]
        else:
            return Bidding(self.id)


    def bidded(self, bid):
        if bid.val >= 100 and self.coinche is not None:
            print "Je coinche"
            self.coinche()


    def played(self, pid, card):
        pass


    def is_removable(self):
        return self.__removable


    def reset_hand(self):
        pass


