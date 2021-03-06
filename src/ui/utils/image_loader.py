# -*- coding:utf-8 -*-
from Tkinter import PhotoImage
from utils import subimage

class ImageLoader:
    """
        Provides an abstraction for the image file.
        Allow the user to consider the image file as 
            a table of cards image.

    """
    
    # unique instance of the image
    # will be initialized on demand
    _instance = 0


    @staticmethod
    def _init_uicards():
        """
            Create the unique instance of the cards image

        """
        ImageLoader._instance = ImageLoader._get_cards_image();
        if ImageLoader._instance == 0:
            raise NameError('Unable to open image file')

    @staticmethod    
    def _get_uicards():
        """
            Return the image containing all the cards

        """
        # If the unique instance has not been initialized...
        if ImageLoader._instance == 0:
            # ... initialize it
            ImageLoader._init_uicards()
        return ImageLoader._instance


    @staticmethod
    def _get_cards_image():
        """ 
            Return an instance of the cards image

        """
        return PhotoImage(file='data/classic_playing_cards.gif')


    # Card width in pixel
    CARD_WIDTH = 71
    # Card height in pixel
    CARD_HEIGHT = 96


    @staticmethod
    def _index_to_coordinates((x_index, y_index)):
        """ 
            Get the cards coordinates at the given index
            @param x_index  index of the row in the file
            @param y_index  index of the column in the file

        """
        # Number of pixel before each cards
        x_white_space = 2; 
        y_white_space = 2;
        # Compute coordinates 
        x = ImageLoader.CARD_WIDTH * x_index + x_white_space * (x_index + 1)
        y = ImageLoader.CARD_HEIGHT * y_index + y_white_space * (y_index + 1)
        # Return a 4-uplet  
        return x, y, x + ImageLoader.CARD_WIDTH, y + ImageLoader.CARD_HEIGHT

    @staticmethod
    def get_card_image(index):
        """
            Get the cards at the given index
            @param index    tupple in the following format [x_index, y_index]

        """
        coordinates = ImageLoader._index_to_coordinates(index)
        return subimage(ImageLoader._get_uicards(), coordinates)
