# -*- coding:utf-8 -*-
from Tkinter import Button, CENTER
from threading import Event 

from src.game.game_engine import GameEngine
from src.game.card import Card 

from src.ui.utils.ui_card import UICard
from src.ui.utils.image_loader import ImageLoader  
from src.ui.ui_positioning import UIPositioning
from src.ui.table.player.ui_belote import UIBelote


class UIHand(object):
    """
       Interface object for the hand of a player 
       Contains as few logic as possible

    """

    def __init__(self, frame, position):
        # Memorise the frame
        self._frame = frame

        self._position = position

        # List of cards in the hand
        self._hand = []
        # Size of the hand
        self._size = 0 
        # Last card clicked in this hand
        # Must be None if no card were clicked during this round
        self.last_card_played = None 
        # Will be used to notify the main thread when waiting for a card
        self.card_played_event = Event() 

        # Indicates wheter the hand is displayed or not
        self.hidden = True 
        self._human_hand = False

        # List for recording the images itself
        self.cards_image = [None] * GameEngine.MAX_CARD
        # Contains the buttons 
        self._buttons = [None] * GameEngine.MAX_CARD
        # Init buttons
        self._init_buttons()
        self._update_buttons_position()
        self._update_first_card_column()
        self._update_first_card_row()
        # Init belote
        self._init_belote()


    def _update_first_card_column(self):
        """
            Define the column of the first card for each hand

        """
        # keep the hand centered
        nb_cards_missing = GameEngine.MAX_CARD - len(self._hand)
        missing_offset = nb_cards_missing / 2.0 * ImageLoader.CARD_WIDTH 
        # don't forget covering
        missing_offset *= UIPositioning.COVERING
        # magical formula
        space_taken = UIPositioning.HAND_WIDTH + UIPositioning.HAND_OFFSET
        UIPositioning.initial_first_card_column = [space_taken, 
                                    space_taken * 2, 
                                    space_taken, 
                                    0]
        UIPositioning.first_card_column = [space_taken + missing_offset, 
                                    space_taken * 2 + missing_offset, 
                                    space_taken + missing_offset, 
                                    missing_offset]
        # Add horizontal offset
        UIPositioning.first_card_column = [x + UIPositioning.HAND_OFFSET / 2.0 \
                                            for x in UIPositioning.first_card_column]
        UIPositioning.initial_first_card_column = [x + UIPositioning.HAND_OFFSET / 2.0 \
                                            for x in UIPositioning.initial_first_card_column]


    def _update_first_card_row(self):
        """
            Define the row of the first card for each hand

        """
        height = UIPositioning.HAND_HEIGHT
        UIPositioning.first_card_row = [0, height * 2, height * 4, height * 2] 
        # Add vertical offset
        UIPositioning.first_card_row = [x + height / 2.0 for x in UIPositioning.first_card_row]


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


    def get_card(self, playable):
        """
            Wait for the player to choose a card between
            the possible ones given in playable
            @param playable     list of cards that can be played

        """
        # Forgot the last_card_played
        self.last_card_played = None
        # Wait to have a new card
        # It must be a playable card
        while self.last_card_played is None or \
                not self.last_card_played in playable:
            if not self.last_card_played is None: 
                self._event[CONSOLE_RED]("This card is not playable!")
            # Wait for a click (notified by ui_hand)
            # Time out of 5 seconds to avoid deadlock
            self.card_played_event.wait(5)

        belote = self._belote.clicked
        self._belote.clicked = False
        # Finally, the user clicked on a good card
        return (self.last_card_played, belote)


    def _init_buttons(self):
        """
            Init the buttons that will be used to modelise the cards

        """
        for i in xrange(0, GameEngine.MAX_CARD):
            # Define the button
            self._buttons[i] = Button(self._frame, image = self.cards_image[i],
                                      command=lambda i=i: self.click_card(i))

    
    def _compute_belote_position(self):
        """

        """
        x = UIPositioning.initial_first_card_column[self._position] 
        y = UIPositioning.first_card_row[self._position]
        y += ImageLoader.CARD_HEIGHT + 10 
        return round(x), round(y) 


    def _init_belote(self):
        """
            Init the belote for human player
    
        """
        size_x, size_y = UIPositioning.HAND_WIDTH, 30
        x, y = self._compute_belote_position()
        self._belote = UIBelote(self._frame, x, y, size_x, size_y)        


    def _update_button_position(self, i):
        """
            Place one button to its corresponding location
            @param i    index of the button

        """
        # Compute new positions
        self._update_first_card_column()
        self._update_first_card_row()
        # Place the button
        x = UIPositioning.first_card_column[self._position] + i * UIPositioning.CARD_SHIFTING
        y = UIPositioning.first_card_row[self._position]
        self._buttons[i].place(x = x, y = y)


    def _update_buttons_position(self):
        """
            Place the buttons to their corresponding locations

        """
        for i in xrange(0, self._size):
            self._update_button_position(i)


    def _update_button_image(self, buttonNumber, card):
        """
            Change one card image
            @param buttonNumber index of the button
            @param card         card to display

        """
        assert buttonNumber in range(0, GameEngine.MAX_CARD), \
                "Button number is out of range: " + str(buttonNumber)
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
        for i in xrange(0, self._size):
            self._update_button_image(i, self.hand[i])
        # Hide the remaining buttons
        for i in xrange(self._size, GameEngine.MAX_CARD):
            self._buttons[i].place_forget();

    
    def end_of_trick(self):
        self.last_card_played = None
        self._belote.clicked = False


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
        assert len(value) <= GameEngine.MAX_CARD,\
               "Hand is to big: " + str(len(value))
        self._hand = value
        self._size = len(self._hand)
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


    @property
    def human_hand(self):
        """

        """
        return self._human_hand


    @human_hand.setter
    def human_hand(self, is_human):
        """

        """
        self._human_hand = is_human 
        self.hidden = not is_human 
        if is_human:
            self._belote.display()
        else:
            self._belote.hide()

    
    @property
    def position(self):
        return self._position


    @position.setter
    def position(self, p):
        self._position = p
        if self._human_hand:
            x, y = self._compute_belote_position()
            self._belote.set_position(x, y)
            self._belote.display()

