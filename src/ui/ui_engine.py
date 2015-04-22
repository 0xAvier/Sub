# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button
from threading import Thread, Condition, Event
from time import sleep

from src.game.game_engine import GameEngine 
from src.event.event_engine import EVT_UI_PLAYER_LEFT 
from src.utils.notify import Notify

from src.ui.ui_controllers import UIControllers, EVT_CONTROL_QUIT 
from src.ui.ui_table import UITable

class UIEngine(Thread, Notify):
    """
        Handle a Tk Interface

    """


    def __init__(self):
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
        self._root = Tk()
        # Resize the window
        # compute h according to the table
        h = UITable.TABLE_HEIGHT + 100
        # fixed size for the width
        w = 900
        # translate it in string
        dim = str(w) + "x" + str(h)
        self._root.geometry(dim)


    def _init_table(self):
        """
            Init the table frame
            This part is responsible for all

        """
        self._table = UITable(self._root)


    def _init_controllers(self):
        """
            Init the controllers frame
            This part is responsible for all the non-game stuff

        """
        # Add the frame
        self._controllers = UIControllers(self._root)
        # Initialize the quit callback
        quit_callback = lambda: self._event[EVT_UI_PLAYER_LEFT]( \
                                 self._table.interface_player)
        self._controllers.set_method(EVT_CONTROL_QUIT, quit_callback) 


    def _init_ui(self):
        """
            Sets the interface and enter the tk mainloop

        """
        # Init the interface
        self._init_tk_window()
        # Init the game parts 
        self._init_table()
        # Add some controllers 
        self._init_controllers()

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


    def new_hand(self, player, hand):
        """
            Set a new hand hand for player player
            Method called by an event engine to refresh display
            @param player   id of the player that is given the hand
            @param hand list of tuples (val, col) composing the hand

        """
        self._table.new_hand(player, hand)


    def add_player(self, p):
        """
            Add a player handled by the UI
            @param p    player handled  

        """
        self._table.add_player(p)

