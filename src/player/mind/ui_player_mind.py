#-*- coding: utf-8 -*-

from src.utils.notify import Notify
from src.game.hand import Hand 
from src.game.coinche import COINCHE_CODE
from src.event.event_engine import EVT_UI_COINCHE 

class UIPlayerMind(Notify):


    def __init__(self, pid, ui):
        Notify.__init__(self)
        self._ui = ui
        self.id = pid


    def get_card(self, played, playable):
        """
            @ret        a tuple (card, belote) where card is the 
                        card played by the player, and belote is a
                        boolean which indicates a belote (True) or 
                        not (False).

        """
        return self._ui.get_card(self.id, playable)


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


    def set_method(self, evt, method):
        """
            Overwriting set_method 

        """
        self._event[evt] = method
        if evt == COINCHE_CODE:
            self.coinche = method
            self._ui._table._bidding.set_method(EVT_UI_COINCHE, self.coinche) 

