# -*- coding:utf-8 -*-

from src.game.game_engine import GameEngine
from src.ui.utils.image_loader import ImageLoader

class UIPositioning():
    """
        Define various positions used in the UI

    """

    # Translate a position index to a number
    POS_TO_INDEX = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

    # Part of the card that will be visible
    COVERING = 1 / 3.0 
    # Width in pixel between two cards
    CARD_SHIFTING = ImageLoader.CARD_WIDTH * COVERING

    # hand width in pixel
                 # Number of card that will be covered
                 # Multiplied by the width of a covered card 
                 # Plus an unconvered card
    HAND_WIDTH = (GameEngine.MAX_CARD - 1) * \
                 (ImageLoader.CARD_WIDTH * COVERING) + \
                 ImageLoader.CARD_WIDTH 

    # hand height in pixel
    HAND_HEIGHT = ImageLoader.CARD_HEIGHT
    # Offset between two hands (horizontally)
    HAND_OFFSET = 50

    # Width of the table
    TABLE_WIDTH = HAND_WIDTH * 3 + HAND_OFFSET * 3
    # Height of the table
    TABLE_HEIGHT = HAND_HEIGHT * 6 

    # Table for hands position
    first_card_column = [None] * GameEngine.NB_PLAYER
    first_card_row = [None] * GameEngine.NB_PLAYER


    def __init__(self):
        pass

