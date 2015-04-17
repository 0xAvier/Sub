# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button
import tkMessageBox
from random import randint
import threading
import time

from src.ui.ui_cards import UICards
from src.ui.ui_hand import UIHand

from src.game.deck import Deck

class UIEngine(threading.Thread):
    """
        Handle a Tk Interface
    """


    def __init__(self):
        """
            Constructor
        """
        threading.Thread.__init__(self)
        self.start()
        time.sleep(1)


    def _init_tk_window(self):
        """
            Initialize the window for the Tk Interface
        """
        # create the instance
        self._root = Tk()
        # resize the window
        self._root.geometry("1000x700+1510+30") 
        # bind the close action with our own callback 
        self._root.protocol("WM_DELETE_WINDOW", self._quit_root)
        # memorise the frame of the app
        self._frame = Frame(self._root)
        self._frame.pack()


    def _init_game_control_buttons(self):
        """
            Add buttons to control the game proceedings
            For the moment, only a "Quit" button is added.
        
        """
        self._quit = Button(self.frame, text = "Quit",
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


    def _init_hands(self):
        """
            Initialise the ui hands object of the players
        """
        # index of the tab: the id of the player owning the hands
        # value of the tab: the position of the player
        # will be updated during the game 
        #   to place the (first) active player south
        self._hands_id_to_position = ['N', 'E', 'S', 'W']
        # add a hand for each ids 
        self._hands = []
        for i in self._hands_id_to_position:
            self._hands.append(UIHand(self._frame, i)) 


    def run(self):
        """
            This method wll be called when the thread starts.
            It sets the interface and enter the tk mainloop
        """
        # init the interface
        self._init_tk_window()
        # init the hands
        self._init_hands()
        # add some buttons
        self._init_game_control_buttons()
        # enter the infinite loop, see you lata
        self.root.mainloop()


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
        # wait to have a new card
        # it must be a playable card
        print playable
        while self.hands[p].last_card_played is None or not self.hands[p].last_card_played in playable:
            pass
        # finally, the user clicked on a good card
        return self.hands[p].last_card_played


    def new_hand(self, p, h):
        """
            Set a new hand h for player p
            Method called by an event engine to refresh display
            @param p    id of the player that is given the hand
            @param h    list of tuples (val, col) composing the hand

        """
        self.hands[p].hand = h
        
