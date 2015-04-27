#-*- coding: utf-8 -*-

from src.adapter.i_player_adapter import IPlayerAdapter
from src.adapter.i_game_adapter import IGameAdapter


class GameLocalPlayerAdapter(IGameAdapter, IPlayerAdapter):


    def __init__(self, game, player):
        self.game = game
        self.player = player


    @property
    def id(self):
        return self.player.id


    def give_cards(self, cards):
        return self.player.give_cards(cards)


    def get_card(self, played, playable):
        return self.player.get_card(played, playable)


    def get_coinche(self):
        return self.player.get_coinche()

    def get_bid(self, bidded, biddable):
        return self.player.get_bid(bidded, biddable)


    def bidded(self, bid):
        return self.player.bidded(bid)


    def played(self, pid, card):
        return self.player.played(pid, card)


    def is_removable(self):
        return self.player.is_removable()


    def join(self):
        return self.game.add_player(self)

    
    def reset_hand(self):
        self.player.reset_hand()


    def coinche(self):
        self.game.coinche(self.id) 


    def belote(self):
        self.game.belote(self.id) 

