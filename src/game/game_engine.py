# -*- coding:utf-8 -*-

from src.utils.notify import Notify
from src.event.event_engine import EVT_NEW_ROUND, EVT_CARD_PLAYED, EVT_NEW_DEAL, EVT_NEW_BID
from src.ia.ia_player import IAPlayer
from src.game.deck import Deck
from src.game.round import Round
from src.adapter.game_local_player_adapter import GameLocalPlayerAdapter


class GameEngine(object):
    """
        Master class of the game 
        Controls rules, manage players and
        notify event manager at each event

    """

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
            p = IAPlayer(pid)
            adapt = GameLocalPlayerAdapter(self, p)
            self.__players.append(adapt)
        self.__team = [0, 1, 0, 1]
        # Function to notify for each new event
        self.evt_notify = None


    def new_round(self):
        # Notify the event manager that a new round has begun
        self.notify(EVT_NEW_ROUND)
        # Create a new round oject
        self.rd = Round(self.deck, self.__players, self.notify, self.__team)
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


    def add_event_manager(self, evt):
        # Check if there already is a notify method
        if self.evt_notify is not None:
            raise Exception("Trying to attach several Event Engine objects \
                    to the same game. Aborting.")
        # Get the method to notify the event manager 
        # at each event
        self.evt_notify = evt.notify


    def get_team(self, pid):
        return self.__team[pid]


    def notify(self, EVT_CODE, *args):
        # If a notification function has been set, call it
        if self.evt_notify is not None:
            self.evt_notify(EVT_CODE, *args)
