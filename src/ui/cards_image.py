from random import randint
from Tkinter import PhotoImage
from utils import subimage

"""
Return card images on demand

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
    def _index_to_coordinates(x_index, y_index):
        """ 
            Get the requested cards 
            by translating an index into pixel coordinates  

        """
        # number of pixel between cards
        x_white_space = 2; 
        y_white_space = 2;
        # compute position taking into account the white space between cards
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
        return UICards._index_to_coordinates(x_index, y_index)

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
    # shouldn't be used outside testing
    @staticmethod
    def get_random_card():
        return subimage(UICards._get_uicards(), UICards._get_random_card_coord())

    
