#-*- coding: utf-8 -*-

from random import choice, shuffle, randint

from src.utils.notify import Notify
from src.event.event_engine import EVT_UI_COINCHE 
from src.game.hand import Hand 
from src.game.coinche import COINCHE_CODE

class UIPlayer(Notify):


    def __init__(self, ui, pid):
        Notify.__init__(self)
        self._ui = ui
        self.event = dict()
        self.id = pid
        self._hand = Hand()


    def give_cards(self, cards):
        self._hand.add(cards)
        h = self._hand.get_cards()
        self._ui._table._hands[self.id].hand = h 


    def get_hand(self):
        return self._hand  


    def team(self):
        return self.id % 2


    def get_card(self, played, playable):
        # Get the card
        card = self._ui.get_card(self.id, playable)
        # Update the hand
        self._hand.remove([card]) 
        # Return the card
        return card


    def get_coinche(self):
        return self._ui.get_coinche()

    def get_bid(self, bidded, biddable):
        return self._ui.get_bid(self.id, bidded, biddable)


    def bidded(self, bid):
        pass


    def played(self, pid, card):
        pass


    def is_removable(self):
        return false 


    def reset_hand(self):
        self._hand.clear()

    
    def set_method(self, evt, method):
        """
            Overwriting set_method 

        """
        self._event[evt] = method
        if evt == COINCHE_CODE:
            self.coinche = method
            self._ui._table._bidding.set_method(EVT_UI_COINCHE, self.coinche) 
