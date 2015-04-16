# -*- coding:utf-8 -*-
from Tkinter import Frame, Button, Tk
from random import randint
import threading
import time

from src.ui.ui_cards import UICards
from src.ui.ui_hand import UIHand

from src.game.deck import Deck

class UIEngine(threading.Thread):


    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
        
    def run(self):
        # create the instance
        self.root = Tk()
        # resize the window
        self.root.geometry("1000x700+1510+30") 
        # ? 
        self.root.protocol("WM_DELETE_WINDOW", self.quit_root)

        frame = Frame(self.root)
        frame.pack()

        # define the hands
        # must difference player number from display position
        self.hands = [UIHand(frame, 0),
                      UIHand(frame, 1),
                      UIHand(frame, 2),
                      UIHand(frame, 3)]

        # add some buttons
        self.refresh = Button(frame, text = "New hand",
                                command=self.generate_new_hand)
        self.refresh.grid(row = 6, column = 13)
        self.quit = Button(frame, text = "Quit",
                                command=frame.quit)
        self.quit.grid(row = 7, column = 13)

        self.root.mainloop()

    # quit the TkInter instance   
    def quit_root(self):
        self.root.quit()

    def generate_new_hand(self):
        # distribution    
        # test only, should be removed later
        deck = Deck()
        nb_card = randint(0, UIHand.max_cards)
        for player in xrange(0, 4):
            hand = [None] * nb_card
            for i in xrange(0, nb_card):
                hand[i] = deck.pop()
            self.hands[player].hand = hand


    def new_round(self):
        """
            Notification for the beginning of a new round

        """
        pass


    def card_played(self, p, c):
        """

            Notification that the card c has been played by player p
            @param c    tuple (val, col) of the card played
            @param p    id of the player that played the card

        """
        pass

    def end_of_trick(self, p):
        """
            Notification that the current trick is finished 
            (it should reasonnably mean that four cards have
            been played since the beginning of the trick)
            @param p    id of the player that wins the trick

        """
        pass


    def get_card(self, p, playable):
        """
            Wait for the user p to choose a card between
            the possible ones given in playable
            @param p            id of the player expected to play
            @param playable     list of cards that can be played

        """
        print("Interface.get_card")
        # wait to have a new card
        # it must be a playable card
        #while self.hands[p].last_card_played is None: 
        print playable
        while self.hands[p].last_card_played is None or not self.hands[p].last_card_played in playable:
            pass
        # finally
        print("Hey!")
        return self.hands[p].last_card_played


    def new_hand(self, p, h):
        """
            Set a new hand h for player p
            Method called by an event engine to refresh display
            @param p    id of the player that is given the hand
            @param h    list of tuples (val, col) composing the hand

        """
        self.hands[p].hand = h
        
