# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button, LEFT
from time import sleep

from src.game.game_engine import GameEngine
from src.game.coinche import COINCHE_CODE 
from src.game.bidding import Bidding
from src.utils.notify import Notify
from src.event.event_engine import CONSOLE, CONSOLE_RED

from src.ui.ui_positioning import UIPositioning
from src.ui.table.general.ui_heap import UIHeap
from src.ui.table.general.ui_scoreboard import UIScoreboard 
from src.ui.table.player.ui_bidding import UIBidding
from src.ui.table.player.ui_hand import UIHand
from src.ui.utils.image_loader import ImageLoader

class UITable(Notify):
    """
        Handle all the table parts for the interface.
        Contains hands, central heaps & score board

    """

    # Width of the table
    TABLE_WIDTH = UIPositioning.HAND_WIDTH * 3 + UIPositioning.HAND_OFFSET * 3
    # Height of the table
    TABLE_HEIGHT = UIPositioning.HAND_HEIGHT * 6 
    # Translate a position index to a number
    POS_TO_INDEX = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

    def __init__(self, root):
        Notify.__init__(self)
        # Memorise the root
        self._root = root  
        # Create a new frame only for controllers
        self._frame = Frame(root, width = self.TABLE_WIDTH, 
                                  height = self.TABLE_HEIGHT,
                                  background = "#27ae60")
        self._frame.pack(side = LEFT)

        # Index of the tab: the id of the player owning the hands
        # Value of the tab: the position of the player
        # Will be updated during the game 
        #   to place the (first) active player south
        self._interface_player = 3
        self._hands_id_to_position = ['N', 'E', 'S', 'W']
        # Player that are handled by this UI
        self._handled_players = []

        # Init the hands
        self._init_hands()
        # Init the central heaps
        self._init_heap()
        # Init the bidding widget
        self._init_bidding()
        # Init the scoreboard widget
        self._init_scoreboard()


    def _init_hands(self):
        """
            Initialise the ui hands object of the players

        """
        # Add a hand for each ids 
        self._hands = []
        for i in self._hands_id_to_position:
            nb_position = UITable.POS_TO_INDEX[i]
            self._hands.append(UIHand(self._frame, nb_position)) 


    def _init_heap(self):
        """
            Initialise the ui hands object of the players

        """
        # Add a hand for each ids 
        self._heaps = []
        #for i in self._hands_id_to_position:
        for i in ['N', 'E', 'S', 'W']:
            nb_position = UITable.POS_TO_INDEX[i]
            self._heaps.append(UIHeap(self._frame, nb_position, 
                                                   self.TABLE_WIDTH / 2.0, \
                                                   self.TABLE_HEIGHT / 2.0)) 

    def _init_bidding(self):
        """
            Initialise the bidding widget

        """
        size_x = 264 + 8 
        size_y = 130
        x = (self.TABLE_WIDTH - size_x) / 2.0 + 3
        y = (self.TABLE_HEIGHT - size_y) / 2.0 
        self._bidding = UIBidding(self._frame, x, y, size_x, size_y) 


    def _init_scoreboard(self):
        """
            Initialise the scoreboard widget

        """
        self._scoreboard = UIScoreboard(self._frame, self.TABLE_WIDTH, \
                                                     self.TABLE_HEIGHT)


    def last_card_played(self, p):
        """
            Return the last card played by a specific palyer
            @param p    player from whom the last card played is requested

        """
        return self._hands[p].last_card_played


    @property
    def interface_player(self):
        """
            Return the id of the player who managed the interface

        """
        return self._interface_player


    @interface_player.setter
    def interface_player(self, pid):  
        """
            Set the id of the player who manages the interface
            @param pid  id of the player 

        """
        if not pid in self._handled_players:
            raise Exception("Player " + str(pid) + " not handled by the ui.")

        for i in xrange(0, GameEngine.NB_PLAYER):
            # interface player get the south position
            self._hands_id_to_position[(pid + i) % GameEngine.NB_PLAYER] = \
                    ['S', 'W', 'N', 'E'][i]
        # Refresh the position for the player
        for i in xrange(0, GameEngine.NB_PLAYER):
            nb_position = UITable.POS_TO_INDEX[self._hands_id_to_position[i]]
            self._hands[i].position = nb_position 
            self._heaps[i].position = nb_position 
        self._interface_player = pid


    def reset_heap(self):
        """
            heap are placed when a player plays a card
            Reset it to None to visualise the end of a trick

        """
        for h in self._heaps:
            h.heap = None


    def end_of_trick(self, p):
        """
            Notification that the current trick is finished 
            (it should reasonnably mean that four cards have
            been played since the beginning of the trick)
            @param p    id of the player that wins the trick

        """
        sleep(1)
        # Reset the heap 
        self.reset_heap()
        # Reset last_played for all hands
        for h in self._hands:
            h.end_of_trick()


    def get_card(self, p, playable):
        """
            Wait for the user p to choose a card between
            the possible ones given in playable
            @param p            id of the player expected to play
            @param playable     list of cards that can be played

        """
        # The player must be handled by the interface
        if not p in self._handled_players:
            raise Exception("Player " + str(p) + " not handled.")
        # If he is handled, process as normal

        return self._hands[p].get_card(playable)


    def get_coinche(self):
        """
            Wait for the user p to coinche 

        """
        self._bidding.coinche_event.wait()
        return COINCHE_CODE


    def get_bid(self, p, bidded, bid_list):
        """
            Wait for the user p to bid 
            the possible ones given in bid list 
            @param p            id of the player expected to play
            @param bidded       last 4 bids
            @param bid_list     list of possible bids

        """
        # Enable the button bidding pannel 
        self._bidding.enable()

        # The player must be handled by the interface
        if not p in self._handled_players:
            raise Exception("Player " + str(p) + " not handled.")
        # If he is handled, process as normal

        # Set the player 
        self._bidding.player_bidding = p
        # Forgot the last bid
        self._bidding.last_bid = None 
        # Wait to have a new bid 
        # It must be a possible bid
        last_incorrect_bid = None
        while self._bidding.last_bid is None or \
                not self._bidding.last_bid in bid_list:
            if not self._bidding.last_bid is None and \
                    last_incorrect_bid != self._bidding.last_bid: 
                self._event[CONSOLE_RED]("This bid is incorrect!")
                last_incorrect_bid = self._bidding._last_bid 
            # Wait for a click (notified by ui_hand)
            # Time out of 5 seconds to avoid deadlock
            self._bidding.need_bid_event.wait(5)

        # Disable the button bidding pannel 
        self._bidding.disable()

        # Finally, the user bid 
        return self._bidding.last_bid


    def new_hand(self, player, hand):
        """
            Set a new hand hand for player player
            @param player   id of the player that is given the hand
            @param hand list of tuples (val, col) composing the hand

        """
        self._hands[player].hand = hand

     
    def new_deal(self):
        """
            Notification for the beginning of a deal

        """
        # New hand for everybody
        for i in xrange(0, GameEngine.NB_PLAYER):
            # Well, in fact only for not handled player
            if not i in self._handled_players:
                self._hands[i].size = GameEngine.MAX_CARD

        # Bidding phase
        if len(self._handled_players) > 0:
            self._bidding.display()


    def end_bidding(self):
        self._bidding.hide()


    def new_round(self):
        """
            Notification for the beginning of a new round

        """
        # Reset score board
        self._scoreboard.score_02 = 0 
        self._scoreboard.score_13 = 0 


    def new_bid(self, bid):
        """
            A new bid has been made 

        """
        # Display the bid beside the player
        pass


    def card_played(self, p, c):
        """

            Notification that the card c has been played by player p
            @param c    tuple (val, col) of the card played
            @param p    id of the player that played the card

        """
        # If the player is not handled ...
        if not p in self._handled_players:
            sleep(1)
            # ... only change its hand size
            self._hands[p].size -= 1
        # Otherwise, process as normal
        else:
            # Remove the card in the hand
            # Copy the list
            new_hand = list(self._hands[p].hand)
            # Remove the card from the copy
            new_hand.remove(c)
            # Refresh the hand
            self.new_hand(p, new_hand)
        # Place it into the central heap
        self._heaps[p].heap = c 


    def add_player(self, pid):
        """
            Add a player handled by the UI
            @param p    player handled  

        """
        # Check if pid is already handle 
        if pid in self._handled_players:
            raise IndexError
        self._handled_players.append(pid)
        self._hands[pid].human_hand = True 


    def update_score(self, score):
        """
            Update the score in ui_table
            @param score    the new score

        """
        self._scoreboard.score_02 = score[0]
        self._scoreboard.score_13 = score[1]


    def belote(self, pid):
        """

        """
        if pid in self._handled_players:
            self._hands[pid].belote_ack()
        self._event[CONSOLE_RED]("[pid] Belote")


    def rebelote(self, pid):
        """

        """
        if pid in self._handled_players:
            self._hands[pid].rebelote_ack()
        self._event[CONSOLE_RED]("[pid] Rebelote")


    def set_method(self, evt_id, method):
        """
            Overwrite set_method

        """
        self._event[evt_id] = method
        self._bidding.set_method(evt_id, method)

