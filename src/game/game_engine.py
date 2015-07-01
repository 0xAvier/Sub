# -*- coding:utf-8 -*-

from src.utils.notify import Notify
from src.event.event_engine import EVT_NEW_ROUND, EVT_CARD_PLAYED, EVT_NEW_DEAL, EVT_NEW_BID
from src.player.player import Player
from src.game.deck import Deck
from src.game.round import Round
from src.adapter.game_local_player_adapter import GameLocalPlayerAdapter


class GameEngine(Notify):

    # Number of players of the game
    # (included IA and real players)
    NB_PLAYER = 4
    # Max number of cards that one can have in its hand
    MAX_CARD = Deck.NB_CARD / NB_PLAYER

    def __init__(self):
        # Call parent constructor
        super(GameEngine, self).__init__()
        # Creation of a deck of cards to play
        self.deck = Deck()
        # Creation of a set of players
        self.__players = list()
        for pid in xrange(self.NB_PLAYER):
            # This player is removable
            p = Player(pid, True)
            adapt = GameLocalPlayerAdapter(self, p)
            self.__players.append(adapt)
        self.__team = [0, 1, 0, 1]


    def new_round(self):
        # Notify the event manager that a new round has begun
        self.notify(EVT_NEW_ROUND)
        # Create a new round oject
        self.rd = Round(self.deck, self.__players, self._event, self.__team)
        while not self.rd.over():
            # Notify the event manager that a new deal has begun
            self.notify(EVT_NEW_DEAL)
            # Start new deal
            self.rd.deal()


    def add_player(self, p):
        # Check if pid is already used by a 
        # non-removable player
        if not self.__players[p.id].is_removable():
            raise IndexError
        # Otherwise, add player
        self.__players[p.id] = p


    def get_team(self, pid):
        return self.__team[pid]

