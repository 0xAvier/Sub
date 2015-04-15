
from src.game.hand import Hand

class Player(object):

	# Counter of the number of player objects created so far
	nb_p = 0

	def __init__(self, pos):
		self.pos = pos
		self.nick = ""
	 	self.hand = Hand()
		self.id = self.__class__.nb_p
		self.__class__.nb_p += 1
