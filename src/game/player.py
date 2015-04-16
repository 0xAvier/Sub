
from random import choice 

from src.event.event_engine import EVT_UI_GET_CARD, EVT_CARD_PLAYED
from src.game.hand import Hand

class Player(object):

	# Counter of the number of player objects created so far
	nb_p = 0

	def __init__(self, pos):
		self.pos = pos
		self.nick = ""
	 	self._hand = Hand()
		self.event = dict()
		self.id = self.__class__.nb_p
		self.__class__.nb_p += 1


	def set_method(self, evt_id, method):
		self.event[evt_id] = method


	def get_cards(self):
		return self._hand.get_cards()


	def get_card(self, played, playable):
		if EVT_UI_GET_CARD in self.event.keys():
			return self.event[EVT_UI_GET_CARD](self.id, playable)
		else:
			return choice(playable)

	
	def played(self, card):
		"""
			Notification to the player that a card has been
			played.
			If this player is himself (ie pid == self.id), then it 
			must also remove the card from its hand

		"""
		if EVT_UI_CARD_PLAYED in self.event.keys():
			self.event[EVT_CARD_PLAYED](self.id, card)
		self._hand.remove(card)	

	
	def give_cards(self, cards):
		"""
			Add some cards to a hand

		"""
		self._hand.add(cards)
