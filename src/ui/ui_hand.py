# -*- coding:utf-8 -*-
from Tkinter import Button, CENTER
from threading import Event 

from src.game.game_engine import GameEngine
from src.game.card import Card 

from src.ui.ui_card import UICard
from src.ui.image_loader import ImageLoader  


class UIHand(object):
    """
       Interface object for the hand of a player 
       Contains as few logic as possible

    """

    # Part of the card that will be visible
    COVERING = 1.0 / 3 
    # hand width in pixel
                 # Number of card that will be covered
                 # Multiplied by the width of a covered card 
                 # Plus an unconvered card
    HAND_WIDTH = (GameEngine.MAX_CARD - 1) * \
                 (ImageLoader.CARD_WIDTH * COVERING) + \
                 ImageLoader.CARD_WIDTH 

    # hand height in pixel
    HAND_HEIGHT = ImageLoader.CARD_HEIGHT
    # Offset between two hands (horizontally)
    HAND_OFFSET = 50
    # Width in pixel between two cards
    CARD_SHIFTING = ImageLoader.CARD_WIDTH * COVERING

    # Table for hands position
    first_card_column = [None] * GameEngine.NB_PLAYER
    first_card_row = [None] * GameEngine.NB_PLAYER


    def __init__(self, frame, position):
        # Memorise the frame
        self._frame = frame

        self.position = position

        # List of cards in the hand
        self._hand = []
        # Size of the hand
        self._size = GameEngine.MAX_CARD
        # Last card clicked in this hand
        # Must be None if no card were clicked during this round
        self.last_card_played = None 
        # Will be used to notify the main thread when waiting for a card
        self.card_played_event = Event() 

        # Indicates wheter the hand is displayed or not
        self.hidden = True 

        # List for recording the images itself
        self.cards_image = [None] * self._size 
        # Contains the buttons 
        self._buttons = [None] * self._size 
        # Init buttons
        self._init_buttons()
        self._update_buttons_position()


    def _update_first_card_column(self):
        """
            Define the column of the first card for each hand

        """
        # keep the hand centered
        nb_cards_missing = GameEngine.MAX_CARD - len(self._hand)
        missing_offset = nb_cards_missing / 2.0 * ImageLoader.CARD_WIDTH 
        # don't forget covering
        missing_offset *= UIHand.COVERING
        # magical formula
        space_taken = UIHand.HAND_WIDTH + UIHand.HAND_OFFSET
        UIHand.first_card_column = [space_taken + missing_offset, 
                                    space_taken * 2 + missing_offset, 
                                    space_taken + missing_offset, 
                                    missing_offset]
        # Add horizontal offset
        UIHand.first_card_column = [x + UIHand.HAND_OFFSET / 2 \
                                            for x in UIHand.first_card_column]


    def _update_first_card_row(self):
        """
            Define the row of the first card for each hand

        """
        height = UIHand.HAND_HEIGHT
        UIHand.first_card_row = [0, height * 2, height * 4, height * 2] 
        # Add vertical offset
        UIHand.first_card_row = [x + height / 2 for x in UIHand.first_card_row]


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
        x = self.first_card_column[self.position] + i * UIHand.CARD_SHIFTING
        y = self.first_card_row[self.position]
        self._buttons[i].place(x = x, y = y)


    def _update_buttons_position(self):
        """
            Place the buttons to their corresponding locations

        """
        for i in xrange(0, GameEngine.MAX_CARD):
            self._update_button_position(i)


    def _update_button_image(self, buttonNumber, card):
        """
            Change one card image
            @param buttonNumber index of the button
            @param card         card to display

        """
        # Get the card mage
        if self.hidden:
            new_card = UICard.get_card_image(Card('7', 'S'))
        else:
            new_card = UICard.get_card_image(card)
        # Display it
        self._buttons[buttonNumber].configure(image = new_card)
        # Save it
        self.cards_image[buttonNumber] = new_card
        # Be sure that the button is visible
        self._update_button_position(buttonNumber)
            

    def update_cards_image(self):
        """
            Modify a cards for 
            Refresh images for the buttons

        """
        # Update new cards
        for i in xrange(0, len(self.hand)):
            self._update_button_image(i, self.hand[i])
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
        self.update_cards_image()

    @property
    def size(self):
        """
            Return the number of card in the hand
        
        """
        return self._size

    @size.setter
    def size(self, value):
        """
            When modified, the button are automatically updated
            Used only for not handled players
            @param value    number of cards in the new hand
        """
        self._size = value
        self._hand = [None] * self._size
        self.update_cards_image()
