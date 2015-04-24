#-*- coding: utf-8 -*-

from abc import ABCMeta

class IEventAdapter(object):

    __metaclass__ = ABCMeta


    def __init__(self):
        pass


    def card_played(self, p, c):
        raise NotImplemented

    
    def new_bid(self, b):
        raise NotImplemented


    def new_round(self): 
        raise NotImplemented


    def new_deal(self): 
        raise NotImplemented


    def end_of_trick(self, p): 
        raise NotImplemented


    def new_hand(self):
        raise NotImplemented


    def update_score(self, s): 
        raise NotImplemented


    def get_consoles(self):
        raise NotImplemented
