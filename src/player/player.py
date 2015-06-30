# -*- coding:utf-8 -*-
from abc import ABCMeta

class Player(IPlayer):
    """

    """


    def __init__(self, pid):
        self.pid = pid
        self._player_mind = None 
        self._player_renders = [] 


    def set_mind(self, mind):
        self._player_mind = mind


    def add_render(self, render):
        self._player_renders.append(render)


    def give_cards(self, cards):
        # both render and mind 
        self._player_mind.give_cards(self, cards)
        for render in self._player_renders:
            render.give_cards(self, cards)


    def team(self):
        # do not depend from render nor mind 
        return self.id % 2


    def get_card(self, played, playable):
        # pure mind
        self._player_mind.get_card(self, played, playable)


    def get_coinche(self):
        # pure mind
        self._player_mind.get_coinche()


    def get_bid(self, bidded, biddable):
        # pure mind 
        self._player_mind.get_bid(bidded, biddable)


    def bidded(self, bid):
        # both render and mind
        self._player_mind.bidded(bid)
        for render in self._player_renders:
            render.bidded(bid)


    def played(self, pid, card):
        # both render and mind
        self._player_mind.played(pid, card)
        for render in self._player_renders:
            render.played(pid, card)


    def is_removable(self):
        # can be rewritten for the AI
        # TODO abstract method ? Or in mind ?
        return false;


    def reset_hand(self):
        # pure mind
        self._player_mind.reset_hand()
