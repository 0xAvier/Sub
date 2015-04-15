
from random import choice, shuffle

from src.event.event_engine import EVT_NEW_HAND

class Round(object):

	def __init__(self, deck, players, events):
		# To be set by the user later
		self.max_pts = 2000
		# Deck to use in this roud
		self.deck = deck
		# Notification to send to event manager
		self.event = events
		self.players = players
		self.score = {'NS': 0, 'WE': 0}
		self.dealer = choice(self.players)


	def deal(self):
		# Distribute hands
		# Distribution sequence generation
		npr = [2, 3, 3]
		shuffle(npr)
		for n in npr:
			for p in self.players:
				p.give_cards([self.deck.pop() for i in xrange(n)])
		assert self.deck.empty()
		if EVT_NEW_HAND in self.event.keys():
			for p in self.players:
				self.event[EVT_NEW_HAND](p.id, p.get_cards())
		# Annonces
		pass
		# Jeu
		pass    
		# To be removed
		self.score['NS'] = 2000


	def over(self):
		return self.score['NS'] >= self.max_pts \
				or self.score['WE'] >= self.max_pts 
