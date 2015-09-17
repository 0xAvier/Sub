#-*- coding: utf-8 -*-

from src.adapter.i_ui_adapter import IUIAdapter
from src.ui.ui_engine import UIEngine

class LocalUIAdapter(IUIAdapter):


    def __init__(self, ui):
        self.ui = ui


    def card_played(self, p, c):
        return self.ui.card_played(p, c)
    

    def new_bid(self, b):
        return self.ui.new_bid(b)


    def new_round(self): 
        return self.ui.new_round()


    def new_deal(self): 
        return self.ui.new_deal()


    def end_of_trick(self, p): 
        return self.ui.end_of_trick(p)


    def end_bidding(self):
        return self.ui.end_bidding()


    def new_hand(self):
        return self.ui.new_hand(p, h)


    def update_score(self, s): 
        return self.ui.update_score(s)

    
    def get_consoles(self):
        return self.ui.get_consoles()
