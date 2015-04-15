
class Card(object):
	values = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	colors = ['S', 'H', 'C', 'D']

	@staticmethod
	def cmp((v1, c1), (v2, c2)):
		"""
			Compare two cards

		"""
		if c1 == c2:
			return -cmp(Card.values.index(v1), Card.values.index(v2))
		else:
			return cmp(Card.colors.index(c1), Card.colors.index(c2))
