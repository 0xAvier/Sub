# -*- coding:utf-8 -*-

from src.event.event_engine import EVT_NEW_ROUND, EVT_CARD_PLAYED, EVT_NEW_DEAL, EVT_NEW_BID
from src.ia.ia_player import IAPlayer
from src.game.deck import Deck
from src.game.round import Round
from src.adapter.game_local_player_adapter import GameLocalPlayerAdapter

class GameEngine(object):

    # Number of players of the game
    # (included IA and real players)
    NB_PLAYER = 4
    # Max number of cards that one can have in its hand
    MAX_CARD = Deck.NB_CARD / NB_PLAYER

    def __init__(self):
        # Creation of a deck of cards to play
        self.deck = Deck()
        # Creation of a set of players
        self.players = list()
        for pid in xrange(self.NB_PLAYER):
            p = IAPlayer(pid)
            adapt = GameLocalPlayerAdapter(self, p)
            self.players.append(adapt)
        # Event notication methods
        self.event = dict()


    def new_round(self):
        # If a notification method is defined
        if EVT_NEW_ROUND in self.event.keys():
            # Notify the event manager that a new round has begun
            self.event[EVT_NEW_ROUND]()

        self.rd = Round(self.deck, self.players, self.event)
        while not self.rd.over():
            if EVT_NEW_DEAL in self.event.keys():
                # Notify the event manager that a new deal has begun
                self.event[EVT_NEW_DEAL]()
            self.rd.deal()


    def set_method(self, evt_id, method):
        """
            Set a new method to be called on a certain type
            of event

        """
        self.event[evt_id] = method


    def add_player(self, p):
        # Check if pid is already used by a 
        # non-removable player
        if not self.players[p.id].is_removable():
            raise IndexError
        # Otherwise, add player
        self.players[p.id] = p

