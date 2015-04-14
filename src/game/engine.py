
from src.game.player import Player
from src.game.deck import Deck
from src.game.round import Round

class Engine(object):

	pos = ['N', 'W', 'S', 'E']

	def __init__(self):
		# Creation of a deck of cards to play
		self.deck = Deck()
		# Creation of a set of players
		self.players = [Player(p) for p in self.pos]

	def new_round(self):
		self.rd = Round(self.deck, self.players)
		while not self.rd.over():
			self.rd.deal()
