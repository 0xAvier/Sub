#-*- coding: utf-8 -*-

from abc import ABCMeta

class IGameAdapter(object):
    """
        Interface that must implement a game object 
        to be correctly interfaced with players

    """

    __metaclass__ = ABCMeta


    def __init__(self):
        pass


    def join(self, player):
        """
            Notify the game that a new player joined the game
            Note that if player.id is already used by a non
            amovible player, it will raise an exception

        """
        raise NotImplemented
