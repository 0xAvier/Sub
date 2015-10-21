#-*- coding: utf-8 -*-

from src.game.card import Card
from src.game.belote_code import *


class Belote(object):

    def __init__(self):
        self.__state = BLT_NORMAL    
        self.__pid = -1


    def reset(self):
        self.__state = BLT_NORMAL
        self.__pid = -1


    def __belote(self, pid):
        self.__state = BLT_BELOTE
        self.__pid = pid


    def __rebelote(self):
        self.__state = BLT_REBELOTE
        self.__pid = pid


    def is_belote(self):
        return self.__state == BLT_BELOTE


    def is_belote_and_rebelote(self):
        return self.__state == BLT_REBELOTE


    @staticmethod
    def belote_is_valid(hand, card, trump):
        """
            Check if the belote is valid, regarding the 
            card being played and the cards that the player 
            holds in his hand.

            @param hand         cards hold in the player's hand
            @param card         card being played
            @param trump        color of the trump

            @ret                True iif the belote is valid

        """
        # First condition: the card being played must be either a king or a queen
        # of the trump color 
        if (card.val != 'K' and card.val != 'Q') or card.col != trump:
            return False
        # Second condition: the other card must be hold by the player
        if card.val == 'Q':
            return Card('K', card.col) in hand
        else:
            return Card('Q', card.col) in hand


    @staticmethod
    def rebelote_is_valid(card, trump):
        """
            Check if the rebelote is valid, assuming that 
            the belote was. 

            @param card         card being played
            @param trump        color of the trump

            @ret                True iif the belote is valid

        """
        # First condition: the card being played must be either a king or a queen
        # of the trump color 
        if (card.val != 'K' and card.val != 'Q') or card.col != trump:
            return False
        else: 
            return True


    def check(self, player, card, trump):
        """
            Check if a belote is valid, regarding the player's
            hand, the trump color and the card he is playing. 
            If valid, updates internal state.

            @param player      tuple (Player, Hand) of the player
            @param card        card being played by player
            @param trump       color of trump

            @ret   A BLT code (either BLT_BELOTE, BLT_REBELOTE or 
                   BLT_INVALID_BELOTE 

        """
        if self.__state == BLT_NORMAL and self.belote_is_valid(player[1], card, trump):
            self.__state = BLT_BELOTE
            self.__pid = player[0].id
            return BLT_BELOTE
            #TODO
            #  self.notify(EVT_BELOTE, p[0].id)
        elif (self.__state == BLT_BELOTE and self.__pid == player[0].id and 
                self.rebelote_is_valid(card, trump)):
            self.__state = BLT_REBELOTE
            return BLT_REBELOTE
            #TODO
            # self.notify(EVT_REBELOTE, p[0].id)
        else:
            return BLT_INVALID_BELOTE
            #TODO
            # self.notify(EVT_BELOTE_INVALID, p[0].id)

