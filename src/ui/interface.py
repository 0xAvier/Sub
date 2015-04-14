
from Tkinter import Frame, Button

from src.ui.utils import subimage 
from src.ui.cards_image import get_random_card_coord, Cards_image

class HandDisplay:
    # number of cards in the hand
    # must be 8 for the Coinche
    nb_cards = 8

    # define the first card column
    def return_first_card_column(self):
        column = [1, 1 + self.nb_cards, 1, 0]
        # return the position
        return column[self.position]

    # define the first card row
    def return_first_card_row(self):
        row = [0, 1, 1 + self.nb_cards, 1]
        # return the position
        return row[self.position]

    # init the cards with randomness
    def get_random_cards(self):
        for i in xrange(0, self.nb_cards):
            self.cards_coord[i] = get_random_card_coord()
            
    #
    def remove_card(self):
        print("Not implemented")
    
    #
    def play_card(self):
        print("Not implemented")

    # initialize the button for the cards
    def init_cards_button(self):
        # defines if the hand must be displayed vertically
        # or horizonthally 
        vertical = [0, 1, 0, 1]

        cards = Cards_image.get_cards_image_instance()
        for i in xrange(0, self.nb_cards):
            self.cards_image[i] = subimage(cards, self.cards_coord[i])
            # define the button
            self.buttons[i] = Button(self.frame, image=self.cards_image[i], 
                                     command=self.frame.quit)
            # which row
            row = self.return_first_card_row() 

            # which column
            column = self.return_first_card_column() 
            # display vertically or horizontally ?
            if vertical[self.position]:
                
                row += i / 2 * vertical[self.position]            
                if not i % 2:
                    # side by side with the previous
                    column += 1
            else:
                # horizontally
                column += i
            # place the button
            self.buttons[i].grid(row = row, column = column)
            
    # constructor
    def __init__(self, frame, position):
        self.frame = frame
        self.position = position
        # init the cards
        # list for the placement of the cards
        self.cards_coord = [None]*self.nb_cards
        # list for recording the images itself
        self.cards_image = [None]*self.nb_cards
        # place corresponding buttons
        self.buttons = [None]*self.nb_cards
        
        # give random cards
        self.get_random_cards()
        # init button
        self.init_cards_button()
        
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.hands = [HandDisplay(frame, 0),
                      HandDisplay(frame, 1),
                      HandDisplay(frame, 2),
                      HandDisplay(frame, 3)]

