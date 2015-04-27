
from random import choice

from src.game.card import Card

class Hand(object):

    def __init__(self):
        self.__cards = list()

    
    def get_cards(self):
        """
            Getter for hand cards
            Sort cards by color before

        """
        return sorted(self.__cards)

    
    def remove(self, cards):
        for card in cards:
            self.__cards.remove(card)

    
    def add(self, cards):
        """
            Add some cards to a hand

        """
        self.__cards += cards


    def pop(self):
        """
            Pop a card from the hand (no matter which one)

        """
        return self.__cards.pop()


    def is_empty(self):
        return len(self.__cards) == 0


    def clear(self):
        """
            Remove all cards from the hand

        """
        self.__cards = list()
