#-*- coding: utf-8 -*-

from random import choice, shuffle, randint

from src.game.hand import Hand

class UIPlayer(object):


    def __init__(self, ui, pid):
        self._ui = ui
        self.event = dict()
        self.id = pid
        self._hand = Hand()


    def give_cards(self, cards):
        self._hand.add(cards)
        h = self._hand.get_cards()
        self._ui._table._hands[self.id].hand = h 


    def get_hand(self):
        # why ?
        return self._hand  


    def team(self):
        return self.id % 2


    def get_card(self, played, playable):
        # For now, return a random card
        return self._ui.get_card(self.id, playable)


    def get_bid(self, bidded, biddable):
        # For now, return a random bidding
        return self._ui.get_bid(self.id, bidded, biddable)


    def bidded(self, bid):
        pass


    def played(self, pid, card):
        pass


    def is_removable(self):
        return false 