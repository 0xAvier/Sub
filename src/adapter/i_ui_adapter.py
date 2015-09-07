#-*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class IUIAdapter(object):

    __metaclass__ = ABCMeta


    def __init__(self):
        pass

    
    @abstractmethod
    def card_played(self, p, c):
        raise NotImplemented

    
    @abstractmethod
    def new_bid(self, b):
        raise NotImplemented


    @abstractmethod
    def new_round(self): 
        raise NotImplemented


    @abstractmethod
    def new_deal(self): 
        raise NotImplemented


    @abstractmethod
    def end_of_trick(self, p): 
        raise NotImplemented


    @abstractmethod
    def end_bidding(self):
        raise NotImplemented


    @abstractmethod
    def new_hand(self):
        raise NotImplemented


    @abstractmethod
    def update_score(self, s): 
        raise NotImplemented


    @abstractmethod
    def get_consoles(self):
        raise NotImplemented
