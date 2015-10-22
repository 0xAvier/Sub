#-*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class IPlayerRender(object):
    """
        Interface that must implement a player render

    """

    __metaclass__ = ABCMeta


    def __init__(self):
        pass


    @abstractmethod
    def give_cards(self, cards, new_hand):
        """
            Add some cards to a hand

        """
        raise NotImplemented

