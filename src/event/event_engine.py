
# Define global constants to identify events
EVT_NEW_ROUND = 0
EVT_NEW_HAND = 1
EVT_UI_GET_CARD = 2
EVT_UI_CARD_PLAYED = 3

class EventEngine(object):
	

	def __init__(self, game):
		self.game = game
		# Define the function of the event manager that the 
		# game engine should call at each new round
		self.game.set_method(EVT_NEW_ROUND, self.new_round)
		self.game.set_method(EVT_NEW_HAND, self.new_hand)
		self.ui = list()


	def add_ui(self, ui, p = None):
		"""
			Add a user interface to the list of interfaces
			to whom events must be notified
			p is a list of players that play through this interface

		"""
		if ui not in [ui[0] for ui in self.ui]:
			self.ui.append((ui, p))
		for player in p:
			self.game.players[player].set_method(EVT_UI_GET_CARD, ui.get_card)
			self.game.players[player].set_method(EVT_UI_CARD_PLAYED, ui.card_played)


	def new_round(self):
		"""
			Notify all interfaces that a new round has begun
			
		"""
		for ui in self.ui:
			ui[0].new_round()

	
	def new_hand(self, p, h):
		"""
			Notify interfaces that a new hand has beend given to player p
			@param p player concerned by the hand
			@param h new hand for player p

		"""
		print p, h
		for ui in self.ui:
			if p in ui[1]:
				ui[0].new_hand(p, h)
