
class Card(object):
	values = ['7', '8', '9', 'J', 'Q', 'K', 'T', 'A']
	values_trump = ['7', '8', 'Q', 'K', 'T', 'A', '9', 'J']
	colors = ['S', 'H', 'C', 'D']

	
	def __init__(self, val, col):
		self.val = val
		self.col = col


	def __getitem__(self, idx):
		if idx == 0:
			return self.val
		elif idx == 1:
			return self.col
		else:
			raise IndexError


	def __str__(self):
		return str(self.val) + str(self.col)


	def __cmp__(self, card):
		"""
			Compare two cards

		"""
		if self[1] == card[1]:
			return -cmp(Card.values.index(self[0]), Card.values.index(card[0]))
		else:
			return cmp(Card.colors.index(self[1]), Card.colors.index(card[1]))

	
	def higher(self, card, trump = None):
		if trump is None:
			return max(self, card)
		else:
			if self[1] == trump and card[1] != trump:
				return self
			elif self[1] != trump and card[1] == trump:
				return card
			else:
				if self.values_trump.index(self[0]) > self.values_trump.index(card[0]):
					return self
				else:
					return card


	@staticmethod
	def highest(cards, asked, trump = None):
		# Are there trumps ?
		tr = [c for c in cards if c[1] == trump]
		if trump == None or len(tr) == 0:
			return max([c for c in cards if c[1] == asked])
		else:
			high = tr[0]
			for c in tr:
				if self.values_trump.index(c[0]) > self.values_trump.index(high[0]):
					high = c
			return c

