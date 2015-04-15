from random import randint
from Tkinter import PhotoImage
from utils import subimage

"""
Return card images on demand
Coordinates : pixel Coordinates in the image file
Index : assuming that the image file contains rows and columns, 
       it give this position
"""
class UICards:
    instance = 0

    @staticmethod
    def _get_cards_image():
        """ 
            Return an instance of the cards image 
        
        """
    	cards_image = PhotoImage(file='data/classic_playing_cards.gif')
    	return cards_image

    # constant card width
    card_width = 71
    # constant card height
    card_height = 96
    
    @staticmethod
    def _index_to_coordinates((x_index, y_index)):
        """ 
            Get the requested cards 
            by translating an index into pixel coordinates  

        """
        # number of pixel between cards
        x_white_space = 2; 
        y_white_space = 2;
        # compute coordinates taking into account the white space between cards
        x = UICards.card_width * x_index + x_white_space * (x_index + 1)
        y = UICards.card_height * y_index + y_white_space * (y_index + 1)
        # return a 4-uplet in 
        return x, y, x + UICards.card_width, y + UICards.card_height

    @staticmethod
    def _get_random_card_coord():
        """
            return the coordinates of a random card
            the coordinates are in a 4-uplet in the following form (n, e, s, w)
            
        """
        # get a random card ...
        x_index = randint(0, 12);
        y_index = randint(0, 3);
        # ... and translate it into coordinates
        return UICards._index_to_coordinates([x_index, y_index])

    # if the instance does not exist, create it
    @staticmethod
    def _init_uicards():
        UICards.instance = UICards._get_cards_image();

    @staticmethod    
    # return the image containing all the cards
    def _get_uicards():
        if UICards.instance == 0:
            UICards._init_uicards()
        return UICards.instance

    # return a random card image
    @staticmethod
    def get_random_card():
        return subimage(UICards._get_uicards(), UICards._get_random_card_coord())


    # represent the index of the cards 
    _index_x_dictionary = {'7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 
                           'K': 12, 'A':0}
    _index_y_dictionary = {'S': 1, 'H':2, 'C':0, 'D':3}
    # get the index in the cards image for the given cards
    @staticmethod
    def get_card_index((value, color)):
        return [UICards._index_x_dictionary[value], 
                UICards._index_y_dictionary[color]]

    # TO BE CHANGED
    @staticmethod
    def get_card(card):
        index = UICards.get_card_index(card)
        coordinates = UICards._index_to_coordinates(index)
        return subimage(UICards._get_uicards(), coordinates)
    
