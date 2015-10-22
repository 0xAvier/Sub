#-*- coding: utf-8 -*-

from src.player.render.i_player_render import IPlayerRender
from src.utils.notify import Notify
from src.game.coinche import COINCHE_CODE
from src.event.event_engine import EVT_UI_COINCHE 


class UIPlayerRender(Notify, IPlayerRender):
    """
        TODO
    """


    def __init__(self, pid, ui):
        Notify.__init__(self)
        self.pid = pid
        self._ui = ui


    def give_cards(self, cards, new_hand):
        """
            Add some cards to a hand

        """
        self._ui.new_hand(self.pid, new_hand.get_cards())


    def set_method(self, evt, method):
        """
            Overwriting set_method 

        """
        self._event[evt] = method
        if evt == COINCHE_CODE:
            self.coinche = method
            self._ui._table._bidding.set_method(EVT_UI_COINCHE, self.coinche) 

