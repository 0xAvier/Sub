
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

	
	def play_card(self, played, playable):
		"""
			Ask the hand to play a card
			@param played is a list of played cards in this trick before (at most three)
			@param playable list of playable cards

		"""
		#todo ask the UI or the IA
		return choice(playable)


	def played(self, card):
		"""
			Notification to the hand that the card has indeed been
			played, and therefore is no longer in the hand

		"""
		self.__cards.remove(card)

	
	def give_cards(self, cards):
		"""
			Add some cards to a hand

		"""
		self.__cards += cards

