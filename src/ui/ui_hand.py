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
       Interface object for the hand of a player 
       Contains as few logic as possible
    """

    # the hand width in pixel
    HAND_WIDTH = (GameEngine.MAX_CARD-1)*(ImageLoader.card_width*COVERING) + \
                    ImageLoader.card_width 
    # the hand height in pixel
    HAND_HEIGHT = ImageLoader.card_height
    # offset between each hands (horizontally)
    HAND_OFFSET = 50
    # width in pixel between two cards
    CARD_SHIFTING = ImageLoader.card_width * COVERING

    # Table for hands position
    first_card_column = [None] * GameEngine.NB_PLAYER
    first_card_row = [None] * GameEngine.NB_PLAYER

    def __init__(self, frame, position):
        # Memorise the frame
        self._frame = frame

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
        # Contains the buttons 
        self._buttons = [None] * GameEngine.MAX_CARD
        # Init buttons
        self._init_buttons()
        self._update_buttons_position()


    def _update_first_card_column(self):
        """
            Define the column of the first card for each hand
        """
        # keep the hand centered
        nb_cards_missing = GameEngine.MAX_CARD - len(self._hand)
        missing_offset = nb_cards_missing / 2.0 * ImageLoader.card_width 
        # don't forget covering
        missing_offset *= COVERING
        # magical formula
        UIHand.first_card_column = [self.HAND_WIDTH + self.HAND_OFFSET + missing_offset, 
                  (self.HAND_WIDTH + self.HAND_OFFSET) * 2 + missing_offset, 
                  self.HAND_WIDTH + self.HAND_OFFSET + missing_offset, 
                  missing_offset]


    def _update_first_card_row(self):
        """
            Define the row of the first card for each hand
        """
        UIHand.first_card_row = [0, self.HAND_HEIGHT*2, self.HAND_HEIGHT*4, self.HAND_HEIGHT*2] 


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


    def _init_buttons(self):
        """
            Init the buttons that will be used to modelise the cards
        """
        for i in xrange(0, GameEngine.MAX_CARD):
            # Define the button
            self._buttons[i] = Button(self._frame, image = self.cards_image[i],
                                      command=lambda i=i: self.click_card(i))

    def _update_button_position(self, i):
        """
            Place one button to its corresponding location
            @param i    index of the button
        """
        # Compute new positions
        self._update_first_card_column()
        self._update_first_card_row()
        # Place the button
        x = self.first_card_column[self.position] + i * self.CARD_SHIFTING
        y = self.first_card_row[self.position]
        self._buttons[i].place(x = x, y = y)


    def _update_buttons_position(self):
        """
            Place the buttons to their corresponding locations
        """
        for i in xrange(0, GameEngine.MAX_CARD):
            self._update_button_position(i)


    def update_button_image(self, buttonNumber, card):
        """
            Change one card image
            @param buttonNumber index of the button
            @param card         card to display
        """
        # Get the card mage
        new_card = UICards.get_card_image(card)
        # Display it
        self._buttons[buttonNumber].configure(image = new_card)
        # Save it
        self.cards_image[buttonNumber] = new_card
        # Be sure that the button is visible
        self._update_button_position(buttonNumber)
            

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
            self._buttons[i].place_forget();
            

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
            
