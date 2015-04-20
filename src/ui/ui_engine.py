# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button
from threading import Thread, Condition, Event

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
        self._root.geometry("1000x700+1510+30") 


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
                                 self._table.interface_player())
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
        self._table.set_interface_player(p)

    def new_round(self):
        """
            Notification for the beginning of a new round

        """
        # Reset score board
        pass


    def card_played(self, p, c):
        """

            Notification that the card c has been played by player p
            @param c    tuple (val, col) of the card played
            @param p    id of the player that played the card

        """
        # Remove the card in the hand
        pass
        # Place it into the central heap
        pass


    def end_of_trick(self, p):
        """
            Notification that the current trick is finished 
            (it should reasonnably mean that four cards have
            been played since the beginning of the trick)
            @param p    id of the player that wins the trick

        """
        # Reset the heap 
        pass
        # Reset last_played for all hands
        self._table.reset_last_played()


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
