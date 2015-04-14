from Tkinter import *
from utils import *
from cards_image import *

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
            
    # initialize the button for the cards
    def init_cards_button(self):
        # defines if the hand must be displayed vertically
        # or horizonthally 
        vertical = [0, 1, 0, 1]

        cards = Cards_image.get_cards_image_instance()
        for i in xrange(0, self.nb_cards):
            print(i)
            card = subimage(cards, self.cards_coord[i])
            # define the button
            self.buttons[i] = Button(self.frame, image=card, 
                                     command=self.frame.quit)
            # which row
            row = self.return_first_card_row() 
            row += i * vertical[self.position]
            # which column
            column = self.return_first_card_column() 
            column +=i * vertical[self.position]
            # place the button
            self.buttons[i].grid(row = row, column = column)
            
    # constructor
    def __init__(self, frame, position):
        self.frame = frame
        #self.position = position
        # init the cards
        #self.cards_coord = [None]*self.nb_cards
        # must be modified (non-random cards must be given)
        #self.get_random_cards()
        # place corresponding buttons
        #self.buttons = [None]*self.nb_cards
        #self.init_cards_button()
        # local test
        cards = Cards_image.get_cards_image_instance()
        self.card = subimage(cards, get_random_card_coord())
        self.hands_north = Button(frame, image=self.card,
                                  command=frame.quit)
        self.hands_north.grid(row = 0, column = 1)
        
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.cards = Cards_image.get_cards_image_instance()
        if self.cards == 0:
            frame.quit()

        self.hands = HandDisplay(frame, 0)

        #self.card_north = subimage(self.cards, get_random_card_coord())
        #self.hands_north = Button(frame, image=self.card_north, 
        #                          command=frame.quit)
        #self.hands_north.grid(row = 0, column = 1)

        self.card_east = subimage(self.cards, get_random_card_coord())
        self.hands_east = Button(frame, image=self.card_east, 
                                 command=frame.quit)
        self.hands_east.grid(row = 1, column = 2)

        self.card_south = subimage(self.cards, get_random_card_coord())
        self.hands_south = Button(frame, image=self.card_south, 
                                  command=frame.quit)
        self.hands_south.grid(row = 2, column = 1)

        self.card_west = subimage(self.cards, get_random_card_coord())
        self.hands_west = Button(frame, image=self.card_west, 
                                 command=frame.quit)
        self.hands_west.grid(row = 1, column = 0)

root = Tk()

app = App(root)

root.mainloop()
#root.destroy() # optional; see description below
