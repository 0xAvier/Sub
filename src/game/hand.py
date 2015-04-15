
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
		return sorted(self.__cards, cmp=Card.cmp)

	
	def remove(self, cards):
		for card in cards:
			self.__cards.remove(card)

	
	def add(self, cards):
		"""
			Add some cards to a hand

		"""
		self.__cards += cards

