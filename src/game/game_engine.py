
from src.event.event_engine import EVT_NEW_ROUND, EVT_CARD_PLAYED
from src.game.player import Player
from src.game.deck import Deck
from src.game.round import Round

class GameEngine(object):

    pos = ['N', 'W', 'S', 'E']

    def __init__(self):
        # Creation of a deck of cards to play
        self.deck = Deck()
        # Creation of a set of players
        self.players = [Player(p) for p in self.pos]
        # Event notication methods
        self.event = dict()

    def new_round(self):
        # If a notification method is defined
        if EVT_NEW_ROUND in self.event.keys():
            # Notify the event manager that a new round has begun
            self.event[EVT_NEW_ROUND]()

        self.rd = Round(self.deck, self.players, self.event)
        while not self.rd.over():
            self.rd.deal()

    def set_method(self, evt_id, method):
        """
            Set a new method to be called on a certain type
            of event

        """
        # If the event is relative to players
        if evt_id == EVT_CARD_PLAYED:
            for p in self.players:
                # Set the method for each player
                p.set_method(evt_id, method)
        # Else set it for the Game Engine
        else:
            self.event[evt_id] = method

