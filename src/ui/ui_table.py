# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button
# TODO: remove to keep only "right"
from Tkinter import *

from src.game.game_engine import GameEngine 

from src.ui.ui_hand import UIHand

class UITable(object):
    """
        Handle all the table parts for the interface.
        Contains hands, central heaps & score board
    """


    def __init__(self, root):
        # Memorise the root
        self._root = root  
        # Create a new frame only for controllers
        self._frame = Frame(self._root) 
        self._frame.pack(side = LEFT)
        # Memorise the frame of the app
        self._frame = Frame(self._root)
        self._frame.pack()

        # Index of the tab: the id of the player owning the hands
        # Value of the tab: the position of the player
        # Will be updated during the game 
        #   to place the (first) active player south
        self._hands_id_to_position = ['N', 'E', 'S', 'W']
        # Init the hands
        self._init_hands()


    def _init_hands(self):
        """
            Initialise the ui hands object of the players
        """
        # add a hand for each ids 
        self._hands = []
        for i in self._hands_id_to_position:
            self._hands.append(UIHand(self._frame, i)) 


    def last_card_played(self, p):
        """
            Return the last card played by a specific palyer
            @param p    player from whom the last card played is requested
        """
        return self._hands[p].last_card_played


    def interface_player(self):
        """
            Return the id of the player who managed the interface
        """
        self._hands_id_to_position.index("S")


    # TODO : make it in a more pythonic way ?
    def set_interface_player(self, p):  
        """
            Set the id of the player who managed the interface
        """
        for i in xrange(0, GameEngine.NB_PLAYER):
            self._hands_id_to_position[(p + i) % GameEngine.NB_PLAYER] = \
                    ['S', 'W', 'N', 'E'][i]


    def reset_last_played(self):
        for h in self._hands:
            h.last_card_played = None
