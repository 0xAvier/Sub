# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button, LEFT

from src.game.game_engine import GameEngine 


from src.ui.ui_hand import UIHand
# width of the table
TABLE_WIDTH = (UIHand.HAND_WIDTH + UIHand.HAND_OFFSET) * 3 
# height of the table
TABLE_HEIGHT = UIHand.HAND_HEIGHT * 5 

from src.ui.ui_heap import UIHeap
from src.ui.image_loader import ImageLoader

class UITable(object):
    """
        Handle all the table parts for the interface.
        Contains hands, central heaps & score board
    """


    def __init__(self, root):
        # Memorise the root
        self._root = root  
        # Create a new frame only for controllers
        self._frame = Frame(self._root, width = TABLE_WIDTH, 
                                        height = TABLE_HEIGHT)
        self._frame.pack(side = LEFT)

        # Index of the tab: the id of the player owning the hands
        # Value of the tab: the position of the player
        # Will be updated during the game 
        #   to place the (first) active player south
        self._hands_id_to_position = ['N', 'E', 'S', 'W']
        # Init the hands
        self._init_hands()
        # Init the central heaps
        self._init_heap()



    def _init_hands(self):
        """
            Initialise the ui hands object of the players
        """
        # add a hand for each ids 
        self._hands = []
        for i in self._hands_id_to_position:
            self._hands.append(UIHand(self._frame, i)) 


    def _init_heap(self):
        """
            Initialise the ui hands object of the players
        """
        # add a hand for each ids 
        self._heaps = []
        for i in self._hands_id_to_position:
            self._heaps.append(UIHeap(self._frame, i)) 


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
        """
            last_played are the last card played during this trick by the
            players.
            Reset it to None to notify that the players haven't played during
            this trick.
        """
        for h in self._hands:
            h.last_card_played = None


    def get_card(self, p, playable):
        """
            Wait for the user p to choose a card between
            the possible ones given in playable
            @param p            id of the player expected to play
            @param playable     list of cards that can be played

        """
        self._hands[p].last_card_played = None
        # Wait to have a new card
        # It must be a playable card
        while self._hands[p].last_card_played is None or \
                not self.last_card_played(p) in playable:
            self._hands[p].card_played_event.wait(5)
        # Finally, the user clicked on a good card
        return self.last_card_played(p)


    def new_hand(self, player, hand):
        """
            Set a new hand hand for player player
            @param player   id of the player that is given the hand
            @param hand list of tuples (val, col) composing the hand

        """
        self._hands[player].hand = hand

    
    def card_played(self, p, c):
        """

            Notification that the card c has been played by player p
            @param c    tuple (val, col) of the card played
            @param p    id of the player that played the card

        """
        # Remove the card in the hand
        # Copy the list
        new_hand = list(self._hands[p].hand)
        # Remove the card from the copy
        new_hand.remove(c)
        # Refresh the hand
        self.new_hand(p, new_hand)
        # Place it into the central heap
        self._heaps[p].heap = c 

