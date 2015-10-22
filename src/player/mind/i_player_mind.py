#-*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class IPlayerMind(object):
    """
        Interface that must implement a player mind

    """

    __metaclass__ = ABCMeta


    def __init__(self):
        pass


    @abstractmethod
    def get_card(self, played, playable):
        """
            @ret        a tuple (card, belote) where card is the 
                        card played by the player, and belote is a
                        boolean which indicates a belote (True) or 
                        not (False).

        """
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
    def set_method(self, evt, method):
        """
            Overwriting set_method 

        """
        raise NotImplemented

