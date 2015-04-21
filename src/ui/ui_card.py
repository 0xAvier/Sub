# -*- coding:utf-8 -*-
from image_loader import ImageLoader

class UICard:
    """
        Provides cards image 

    """
    

    @staticmethod
    def _get_random_card_coord():
        """
            Return the coordinates of a random card

        """
        # Get a random position for a card...
        x_index = randint(0, 12);
        y_index = randint(0, 3);
        # ... and translate it into coordinates
        return UICard._index_to_coordinates([x_index, y_index])


    # Dictionnary for the row and column index
    #   Key: value (resp. color) of the card
    #   Data: column index (resp. row index) in the tab
    _index_x_dictionary = {'7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, \
                           'Q': 11, 'K': 12, 'A':0}
    _index_y_dictionary = {'S': 1, 'H':2, 'C':0, 'D':3}
    

    @staticmethod
    def _get_card_index((value, color)):
        """
            Get the index of the given card
            @param value    value of the given card
            @param color    color of the given card

        """
        return [UICard._index_x_dictionary[value], \
                UICard._index_y_dictionary[color]]


    @staticmethod
    def get_card_image(card):
        """
            Get the card image of the given card 
            @param card     object containing the card 

        """
        index = UICard._get_card_index(card)
        return ImageLoader.get_card_image(index) 
