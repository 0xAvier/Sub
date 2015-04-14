
from random import choice 

class Round(object):

	def __init__(self, deck, players):
		# To be set by the user later
		self.max_pts = 2000
		# Deck to use in this roud
		self.deck = deck
		self.players = players
		self.score = {'NS': 0, 'WE': 0}
		self.dealer = choice(self.players)


	def deal(self):
		# Distribute hands
		pass
		# Annonces
		pass
		# Jeu
		pass    
		# To be removed
		self.score['NS'] = 2000


	def over(self):
		return self.score['NS'] >= self.max_pts \
				or self.score['WE'] >= self.max_pts 
