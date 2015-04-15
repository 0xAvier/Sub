from Tkinter import Frame, Button
from src.ui.utils import subimage 
from src.ui.cards_image import UICards
from src.game.deck import Deck
from random import randint

class UIHand(object):
    # number of cards in the hand
    # must be 8 for the Coinche
    max_cards = 8

    # define the first card column
    def return_first_card_column(self):
        column = [2, 2 + self.max_cards, 2, 0]
        # return the position
        return column[self.position]
    
    # define the first card row
    def return_first_card_row(self):
        row = [0, 1, 1 + self.max_cards, 1]
        # return the position
        return row[self.position]

    # index correspond to the clicked card (from 0 to 7)
    # nothing to be done now
    def play_card(self, index):
        a = 0

    # fill the buttons index
    def init_buttons_index(self):
        # defines if the hand must be displayed vertically
        # or horizonthally 
        vertical = [0, 1, 0, 1]
        for i in xrange(0, self.max_cards):
            # define the button
            self.buttons[i] = Button(self.frame, image=self.cards_image[i], 
                                     command=lambda : self.play_card(i))
            # which row
            row = self.return_first_card_row() 

            # which column
            column = self.return_first_card_column() 
            # display vertically or horizontally ?
            if vertical[self.position]:
                row += i / 2 * vertical[self.position]            
                if i % 2:
                    # side by side with the previous
                    column += 1
            else:
                # horizontally
                column += i
            # place the button
            self.button_index[i] = [row, column]
            self.buttons[i].grid(row = row, column = column)

    # place one button to its corresponding location
    def update_button_index(self, i):
        [row, column] = self.button_index[i]
        # place the button
        self.buttons[i].grid(row = row, column = column)

    # place the buttons to their corresponding locations
    def update_buttons_index(self):
        for i in xrange(0, self.max_cards):
            self.update_button_index(i)

    # change one card image
    def update_button_image(self, buttonNumber, card):
        # get the card mage
        new_card = UICards.get_card(card)
        # display it
        self.buttons[buttonNumber].configure(image = new_card)
        # save it
        self.cards_image[buttonNumber] = new_card
        # be sure that the button is visible
        self.update_button_index(buttonNumber)
            
    # modify a cards for 
    # refresh images for the buttons
    def updateCardsImage(self):
        # update new cards
        for i in xrange(0, len(self.hand)):
            self.update_button_image(i, self.hand[i])
        # hide the remaining buttons
        for i in xrange(len(self.hand), UIHand.max_cards):
            self.buttons[i].grid_forget();
            
    # The hand property contains the corresponding cards
    # When modified, the 
    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        self._hand = value
        self.updateCardsImage()
            
    # constructor
    def __init__(self, frame, position):
        self.frame = frame
        self.position = position
        # list of cards in the hand
        self._hand = []
        # list for recording the images itself
        self.cards_image = [None]*self.max_cards
        # contains the index of the buttons in the grid layout
        self.button_index = [None]*self.max_cards
        # contains the buttons in the grid layout
        self.buttons = [None]*self.max_cards

        # init button
        self.init_buttons_index()
        self.update_buttons_index()

class App(object):

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


	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.hands = [UIHand(frame, 0),
						UIHand(frame, 1),
						UIHand(frame, 2),
						UIHand(frame, 3)]

		self.refresh = Button(frame, text = "New hand",
								command=self.generate_new_hand)
		self.refresh.grid(row = 6, column = 13)
		self.quit = Button(frame, text = "Quit",
								command=frame.quit)
		self.quit.grid(row = 7, column = 13)

	
	def new_round(self):
		pass


	def new_hand(self, p, h):
		"""
			Set a new hand h for player p
			Method called by an event engine to refresh display

		"""
		self.hands[p].hand = h
        
