from random import randint
from Tkinter import PhotoImage
from utils import subimage


# TODO : split into two classes + rename files

class UICards:
    """
        Returns cards images for the interface
        Naming convention:
            - Coordinates: pixel Coordinates in the image file
            - Index: assuming that the image file is a table of cards, 
                     it has also row and column index 


        The coordinates are in a 4-uplet in the following format (n, e, s, w)
    """
    
    # unique instance of the image
    # will be initialized on demand
    _instance = 0


    @staticmethod
    def _init_uicards():
        """
            Create the unique instance of the cards image

        """
        UICards._instance = UICards._get_cards_image();


    @staticmethod    
    def _get_uicards():
        """
            Return the image containing all the cards

        """
        # if the unique instance has not been initialized...
        if UICards._instance == 0:
            # ... initialize it
            UICards._init_uicards()
        return UICards._instance


    @staticmethod
    def _get_cards_image():
        """ 
            Return an instance of the cards image

        """
        return PhotoImage(file='data/classic_playing_cards.gif')


    # card width in pixel
    _card_width = 71
    # card height in pixel
    _card_height = 96


    @staticmethod
    def _index_to_coordinates((x_index, y_index)):
        """ 
            Get the cards coordinates at the given index
            @param x_index  index of the row in the file
            @param y_index  index of the column in the file

        """
        # number of pixel before each cards
        x_white_space = 2; 
        y_white_space = 2;
        # compute coordinates 
        x = UICards._card_width * x_index + x_white_space * (x_index + 1)
        y = UICards._card_height * y_index + y_white_space * (y_index + 1)
        # return a 4-uplet  
        return x, y, x + UICards._card_width, y + UICards._card_height


    @staticmethod
    def _get_random_card_coord():
        """
            Return the coordinates of a random card

        """
        # get a random position for a card...
        x_index = randint(0, 12);
        y_index = randint(0, 3);
        # ... and translate it into coordinates
        return UICards._index_to_coordinates([x_index, y_index])


    @staticmethod
    def get_random_card():
        """
            Return a random card image

        """
        return subimage(UICards._get_uicards(), \
                        UICards._get_random_card_coord())


    # Dictionnary for the row and column index
    #   Key: value (resp. color) of the card
    #   Data: column index (resp. row index) in the tab
    _index_x_dictionary = {'7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, \
                           'Q': 11, 'K': 12, 'A':0}
    _index_y_dictionary = {'S': 1, 'H':2, 'C':0, 'D':3}
    

    @staticmethod
    def get_card_index((value, color)):
        """
            Get the index of the given card
            @param value    value of the given card
            @param color    color of the given card
        """
        return [UICards._index_x_dictionary[value], \
                UICards._index_y_dictionary[color]]


    @staticmethod
    def get_card_image(card):
        """
            Get the card image of the given card 
            
            @param card     object containing the card 

        """
        index = UICards.get_card_index(card)
        coordinates = UICards._index_to_coordinates(index)
        return subimage(UICards._get_uicards(), coordinates)
    
