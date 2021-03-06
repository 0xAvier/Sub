# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button, RIGHT, Toplevel
from threading import Thread, Condition, Event
from time import sleep

from src.game.game_engine import GameEngine 
from src.event.event_engine import EVT_UI_PLAYER_LEFT, CONSOLE, CONSOLE_RED 
from src.utils.notify import Notify

from src.ui.side_pannel.ui_controllers import UIControllers, EVT_CONTROL_QUIT 
from src.ui.table.ui_table import UITable 
from src.ui.side_pannel.ui_side_pannel import UISidePannel

class UIEngine(Thread, Notify):
    """
        Handle a Tk Interface

    """

    interface_id = -1

    def __init__(self):
        UIEngine.interface_id += 1
        Notify.__init__(self)
        Thread.__init__(self)
        # This condition will notify the main thread when init is over
        self._wait_init_event = Event()
        # Run the UI thread
        self.start()
        # Wait for the initialisation of the ui
        #   to continue
        self._wait_init_event.wait(10)


    def _init_tk_window(self):
        """
            Initialize the window for the Tk Interface

        """
        # Create the instance
        if UIEngine.interface_id == 0:
            self._root = Tk() 
        else:
            self._root = Toplevel() 
        # Resize the window
        # compute h according to the table
        h = UITable.TABLE_HEIGHT
        # fixed size for the width
        w = 1200
        # translate it in string
        dim = str(w) + "x" + str(h)
        self._root.geometry(dim)


    def _init_table(self):
        """
            Init the table frame
            This part is responsible for all

        """
        self._table = UITable(self._root)
        self._table.set_method(CONSOLE_RED, \
                               lambda msg, c=True: self.add_message(msg, c)) 


    def _init_side_pannel(self):
        """
            The side pannel 
        
        """
        self._side_pannel = UISidePannel(self._root)
        # Initialize the quit callback
        quit_callback = lambda: self._event[EVT_UI_PLAYER_LEFT]( \
                                 self._table.interface_player)
        self._side_pannel.set_method(EVT_CONTROL_QUIT, quit_callback) 


    def _init_ui(self):
        """
            Sets the interface and enter the tk mainloop

        """
        # Init the interface
        self._init_tk_window()
        # Init the game parts 
        self._init_table()
        # Init the other part
        self._init_side_pannel()


    def run(self):
        """
            This method will be called when the UI thread starts.
            It initialise and launch the UI. 

        """
        # Launch the initialisation
        self._init_ui()
        # Notify the end of the initialisation 
        self._wait_init_event.set()
        # Release the condition, now useless
        self._wait_init_event.clear()
        # Enter the infinite loop, see you lata
        if UIEngine.interface_id == 0: 
            self._root.mainloop()

    
    def set_reference_player(self, p):
        """
            Reference player is the player who manage the interface
            Will be positioned South
            @param p    future reference player 
            
        """
        self._table.interface_player = p


    def new_round(self):
        """
            Notification for the beginning of a new round

        """
        self._table.new_round()


    def new_bid(self, bid):
        """
            A new bid has been made, need to forward it to the table

        """
        self._table.new_bid(bid)


    def new_deal(self):
        """
            Notification for the beginning of a deal 

        """
        self._table.new_deal()


    def card_played(self, p, c):
        """

            Notification that the card c has been played by player p
            @param c    tuple (val, col) of the card played
            @param p    id of the player that played the card

        """
        self._table.card_played(p, c)


    def end_of_trick(self, p):
        """
            Notification that the current trick is finished 
            (it should reasonnably mean that four cards have
            been played since the beginning of the trick)
            @param p    id of the player that wins the trick

        """
        self._table.end_of_trick(p)


    def get_card(self, p, playable):
        """
            Wait for the user p to choose a card between
            the possible ones given in playable
            @param p            id of the player expected to play
            @param playable     list of cards that can be played

        """
        return self._table.get_card(p, playable)


    def get_coinche(self):
        """
            Wait for the user to coinche. 

        """
        return self._table.get_coinche()


    def get_bid(self, p, bidded, bid_list):
        """
            Wait for the user p to bid 
            the possible ones given in bid list 
            @param p            id of the player expected to play
            @param bidded       last 4 bids
            @param bid_list     list of possible bids

        """
        return self._table.get_bid(p, bidded, bid_list)


    def new_hand(self, player, hand):
        """
            Set a new hand hand for player player
            Method called by an event engine to refresh display
            @param player   id of the player that is given the hand
            @param hand list of tuples (val, col) composing the hand

        """
        self._table.new_hand(player, hand)


    def end_bidding(self):
        self._table.end_bidding()


    def add_player(self, p):
        """
            Add a player handled by the UI
            @param p    player handled  

        """
        self._table.add_player(p)


    def add_message(self, msg, red = False):
        """
            Add a message to the UIConsole

        """
        self._side_pannel.add_message(msg, red)


    def get_consoles(self):
        """
            Return the list of the consoles for this UI

        """
        return [self._side_pannel._console]


    def update_score(self, score):
        """
            Update the score in ui_table
            @param score    the new score

        """
        self._table.update_score(score)


    def belote(self, pid):
        """

        """
        self._table.belote(pid)

    def rebelote(self, pid):
        """

        """
        self._table.rebelote(pid)
         

    def set_method(self, evt_id, method):
        """
            Overwrite set_method
            Because UIEngine is only an entry-point, set_method need
                to be called on every child of UIEngine

        """
        self._event[evt_id] = method
        self._side_pannel.set_method(evt_id, method)
        self._table.set_method(evt_id, method)
