from random import randint
from Tkinter import PhotoImage
from utils import subimage

"""
   pseudo-singleton that can return a card image 
"""
class UICards:
    instance = 0

    """ return an instance of the cards image """
    @staticmethod
    def _get_cards_image():
        cards_image = PhotoImage(file='../../data/classic_playing_cards.gif')
        return cards_image

    # constant card width
    card_width = 71
    # constant card height
    card_height = 96
    
    """ get the requested cards 
        by translating an index into pixel coordinates  
     """
    @staticmethod
    def _index_to_coordinates(x_index, y_index):
        # number of pixel between cards
        x_white_space = 2; 
        y_white_space = 2;
        # compute position taking into account the white space between cards
        x = UICards.card_width * x_index + x_white_space * (x_index + 1)
        y = UICards.card_height * y_index + y_white_space * (y_index + 1)
        # return a 4-uplet in 
        return x, y, x + UICards.card_width, y + UICards.card_height

    # return the coordinates of a random card
    # the coordinates are in a 4-uplet in the following form (n, e, s, w)
    @staticmethod
    def _get_random_card_coord():
        # get a random card ...
        x_index = randint(0, 12);
        y_index = randint(0, 3);
        # ... and translate it into coordinates
        return UICards._index_to_coordinates(x_index, y_index)

    @staticmethod
    def _init_uicards():
        UICards.instance = UICards._get_cards_image();

    @staticmethod    
    def _get_uicards():
        if UICards.instance == 0:
            UICards._init_uicards()
        return UICards.instance

    @staticmethod
    def get_random_card():
        return subimage(UICards._get_uicards(), UICards._get_random_card_coord())

    
