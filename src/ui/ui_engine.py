# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button
import tkMessageBox
from random import randint

from threading import Thread, Condition
import time

from src.ui.ui_cards import UICards
from src.ui.ui_hand import UIHand
from src.game.deck import Deck
from src.event.event_engine import EVT_UI_PLAYER_LEFT 

# TODO : modify all hard coded 4 values (max players)
class UIEngine(Thread):
    """
        Handle a Tk Interface
    """


    def __init__(self):
        """
            Constructor
        """
        Thread.__init__(self)
        # This condition will notify the main thread when init is over
        self._wait_for_init = Condition()
        self._wait_for_init.acquire()
        # Run the UI thread
        self.start()
        # Wait for the initialisation of the ui
        #   to continue
        self._wait_for_init.wait(10)
        # Event notification methods
        self._event = dict()


    def _init_tk_window(self):
        """
            Initialize the window for the Tk Interface
        """
        # Create the instance
        self._root = Tk()
        # Resize the window
        self._root.geometry("1000x700+1510+30") 
        # Bind the close action with our own callback 
        self._root.protocol("WM_DELETE_WINDOW", self._quit_root)
        # Memorise the frame of the app
        self._frame = Frame(self._root)
        self._frame.pack()


    def _init_game_control_buttons(self):
        """
            Add buttons to control the game proceedings
            For the moment, only a "Quit" button is added.
        
        """
        self._quit = Button(self._frame, text = "Quit",
                                command=self._quit_root)
        self._quit.grid(row = 7, column = 13)
        

    def _quit_root(self):
        """ 
            Own callback to handle "close window" event 
        """
        # Double check the user intentions
        if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
            # If he's sure (at least twice in a row), quit
            self._root.destroy()
            # Notify the event_engine
            self._event[EVT_UI_PLAYER_LEFT]( \
                    self._hands_id_to_position.index("S"))
            exit(0)


    def _init_hands(self):
        """
            Initialise the ui hands object of the players
        """
        # add a hand for each ids 
        self._hands = []
        for i in self._hands_id_to_position:
            self._hands.append(UIHand(self._frame, i)) 

    def _init_game_logic(self):
        # Index of the tab: the id of the player owning the hands
        # Value of the tab: the position of the player
        # Will be updated during the game 
        #   to place the (first) active player south
        self._hands_id_to_position = ['N', 'E', 'S', 'W']
        # Init the hands
        self._init_hands()

    def _init_ui(self):
        """
            Sets the interface and enter the tk mainloop
        """
        # Init the interface
        self._init_tk_window()
        # Init the game parts 
        self._init_game_logic()
        # Add some buttons
        self._init_game_control_buttons()


    def run(self):
        """
            This method will be called when the UI thread starts.
            It initialise and launch the UI. 
        """
        # Acquire the lock
        self._wait_for_init.acquire()
        # Launch the initialisation
        self._init_ui()
        # Notify the end of the initialisation 
        self._wait_for_init.notify()
        # Release the condition, now useless
        self._wait_for_init.release()
        # Enter the infinite loop, see you lata
        self._root.mainloop()

    
    def set_reference_player(self, p):
        for i in xrange(0, 4):
            self._hands_id_to_position[(p + i) % 4] = \
                    ['S', 'W', 'N', 'E'][i]

    def set_method(self, evt_id, method):
        """
            Set a new method to be called on a certain type
            of event
            @param evt_id   id of the event
            @param method   method that must be called on event occurence
        """ 
        self._event[evt_id] = method

    def add_event_engine(self):
        """
            Add an event engine to 
        """

    def new_round(self):
        """
            Notification for the beginning of a new round

        """
        print("Not implemented")


    def card_played(self, p, c):
        """

            Notification that the card c has been played by player p
            @param c    tuple (val, col) of the card played
            @param p    id of the player that played the card

        """
        print("Not implemented")

    def end_of_trick(self, p):
        """
            Notification that the current trick is finished 
            (it should reasonnably mean that four cards have
            been played since the beginning of the trick)
            @param p    id of the player that wins the trick

        """
        print("Not implemented")

    def get_card(self, p, playable):
        """
            Wait for the user p to choose a card between
            the possible ones given in playable
            @param p            id of the player expected to play
            @param playable     list of cards that can be played

        """
        # Wait to have a new card
        # It must be a playable card
        while self._hands[p].last_card_played is None or not self._hands[p].last_card_played in playable:
            pass
        # Finally, the user clicked on a good card
        return self._hands[p].last_card_played


    def new_hand(self, p, h):
        """
            Set a new hand h for player p
            Method called by an event engine to refresh display
            @param p    id of the player that is given the hand
            @param h    list of tuples (val, col) composing the hand

        """
        self._hands[p].hand = h
