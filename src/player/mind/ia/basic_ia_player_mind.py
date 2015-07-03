#-*- coding: utf-8 -*-

from random import choice, randint
from time import sleep
from src.game.bidding import Bidding
from src.utils.notify import Notify

from src.game.coinche import COINCHE_CODE


class BasicIAPlayerMind(Notify):
    """
        TODO

    """

    def __init__(self, pid):
        Notify.__init__(self)
        self.id = pid
        self.__nb_bid = 0
        self.coinche = None


    def get_card(self, played, playable):
        sleep(randint(1, 3))
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
            self.coinche()


    def played(self, pid, card):
        pass


    def set_method(self, evt, method):
        if evt == COINCHE_CODE:
            self.coinche = method

