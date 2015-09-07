# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod

class IPlayer(object):
    """
       Interface for a player 
    """

    __metaclass__ = ABCMeta


    @abstractmethod
    def __init__(self):
        raise NotImplemented


    @abstractmethod
    def give_cards(self, cards):
        raise NotImplemented


    @abstractmethod
    def team(self):
        raise NotImplemented


    @abstractmethod
    def get_card(self, played, playable):
        raise NotImplemented


    @abstractmethod
    def get_coinche(self):
        raise NotImplemented


    @abstractmethod
    def get_bid(self, bidded, biddable):
        raise NotImplemented


    @abstractmethod
    def bidded(self, bid):
        raise NotImplemented


    @abstractmethod
    def played(self, pid, card):
        raise NotImplemented


    @abstractmethod
    def is_removable(self):
        raise NotImplemented


    @abstractmethod
    def reset_hand(self):
        raise NotImplemented
