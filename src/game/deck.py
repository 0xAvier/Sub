
from random import random, randint, shuffle

from src.game.card import Card


class DeckTooSmall(Exception):
    pass


class Deck(object):

    def __init__(self):
        self.stack = list()
        # Add all cards to the deck (ordered)
        for val in Card.values:
            for color in Card.colors:
                self.push(Card(val, color))
        # Shuffle the order
        shuffle(self.stack)


    def empty(self):
        return len(self.stack) == 0


    def push(self, c):
        """
            Add a card on the top of the deck

        """
        # Internal convention: top of the stack at index -1
        self.stack.append(c)


    def pop(self):
        """
            Pick a card from the top of the deck

        """
        # Check if the deck is empty
        if self.empty():
            raise DeckTooSmall
        # Internal convention: top of the stack at index -1
        return self.stack.pop(-1)


    def shuffle(self):
        """
            Shuffle the deck with uniform random

        """
        shuffle(self.stack)


    def cut(self):
        """
            Cut the deck in two randomly with at least 3
            cards in each sub-deck
            The deck must contain at least 6 cards.

        """
        if len(deck) < 6:
            raise DeckTooSmall
        idx = randint(3, len(deck) - 4)
        self.stack = self.stack[idx:] + self.stack[:idx]


    def merge(self, a, b):
        """
            Merge packs a and b (whether by putting a on b or b on a)
            and put (a + b) on the top of the deck

        """
        if random() > 0.5:
            self.stack += a + b
        else:
            self.stack += b + a

