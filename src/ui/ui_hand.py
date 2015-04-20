# -*- coding:utf-8 -*-
from Tkinter import Button, CENTER
from threading import Event 

from src.game.deck import Deck
from src.game.game_engine import GameEngine

from src.ui.ui_cards import UICards
from src.ui.image_loader import ImageLoader  

COVERING = 1.0 / 3 

class UIHand(object):
    """
       Handle the interface for the hand of a player 
       Contains as few logic as possible
    """


    def __init__(self, frame, position):
        # Memorise the frame
        self.frame = frame

        # Translate to a more usable index
        pos_to_index = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
        self.position = pos_to_index[position]

        # List of cards in the hand
        self._hand = []
        # Last card clicked in this hand
        # Must be None if no card were clicked during this round
        self.last_card_played = None 
        # Will be used to notify the main thread when waiting for a card
        self.card_played_event = Event() 

        # List for recording the images itself
        self.cards_image = [None] * GameEngine.MAX_CARD
        # Contains the index of the buttons in the layout
        self.button_index = [None] * GameEngine.MAX_CARD
        # Contains the buttons 
        self.buttons = [None] * GameEngine.MAX_CARD
        # Init button
        self.init_buttons_index()
        self.update_buttons_index()


    def return_first_card_column(self):
        """
            Define the column of the first card for each hand
        """
        # magical formula
        hand_width = (GameEngine.MAX_CARD - 1) * COVERING  + 10
        # less magical formula
        column = [hand_width, hand_width * 2, hand_width, 0]
        return column[self.position]


    def return_first_card_row(self):
        """
            Define the row of the first card for each hand
        """
        row = [0, 2, 4, 2]
        # Return the position
        return row[self.position]


    def click_card(self, index):
        """
            Callback function for the card selection
            @param index    the clicked card (from 0 to 7)
        """
        # Set the last played card
        self.last_card_played = self.hand[index]
        # Notify the consumer (main thread)
        self.card_played_event.set()
        # Reset the event
        self.card_played_event.clear()


    def init_buttons_index(self):
        """
            Fill the buttons layout index 
        """
        # Defines if the hand must be displayed vertically
        #   or horizonthally 
        for i in xrange(0, GameEngine.MAX_CARD):
            # Define the button
            self.buttons[i] = Button(self.frame, image=self.cards_image[i], 
                                        command=lambda i=i: self.click_card(i))
            # Which row
            row = self.return_first_card_row() 
            # Which column
            column = self.return_first_card_column() 
            column += i
            # Place the button
            self.button_index[i] = [row, column]


    def update_button_index(self, i):
        """
            Place one button to its corresponding location
            @param i    index of the button
        """
        row, column = self.button_index[i]
        # Place the button
        x = row * ImageLoader.card_height 
        y = column * ImageLoader.card_width * COVERING 
        self.buttons[i].place(x = y, y = x)


    def update_buttons_index(self):
        """
            Place the buttons to their corresponding locations
        """
        for i in xrange(0, GameEngine.MAX_CARD):
            self.update_button_index(i)


    def update_button_image(self, buttonNumber, card):
        """
            Change one card image
            @param buttonNumber index of the button
            @param card         card to display
        """
        # Get the card mage
        new_card = UICards.get_card_image(card)
        # Display it
        self.buttons[buttonNumber].configure(image = new_card)
        # Save it
        self.cards_image[buttonNumber] = new_card
        # Be sure that the button is visible
        self.update_button_index(buttonNumber)
            

    def updateCardsImage(self):
        """
            Modify a cards for 
            Refresh images for the buttons

        """
        # Update new cards
        for i in xrange(0, len(self.hand)):
            self.update_button_image(i, self.hand[i])
        # Hide the remaining buttons
        for i in xrange(len(self.hand), GameEngine.MAX_CARD):
            self.buttons[i].place_forget();
            

    @property
    def hand(self):
        """
            The hand property contains the corresponding cards
        """
        return self._hand

    @hand.setter
    def hand(self, value):
        """
            When modified, the button are automatically updated 
            @param value    new hand
        """
        self._hand = value
        self.updateCardsImage()
            
