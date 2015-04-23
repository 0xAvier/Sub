# -*- coding:utf-8 -*-
from src.event.event_engine import EVT_NEW_ROUND, EVT_CARD_PLAYED, EVT_NEW_DEAL, EVT_NEW_BID
from src.game.player import Player
from src.game.deck import Deck
from src.game.round import Round


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
        self.players = [Player(p) for p in xrange(self.NB_PLAYER)]
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
        # If the event is relative to players
        if evt_id == EVT_CARD_PLAYED or evt_id == EVT_NEW_BID:
            for p in self.players:
                # Set the method for each player
                p.set_method(evt_id, method)
        # Else set it for the Game Engine
        else:
            self.event[evt_id] = method

