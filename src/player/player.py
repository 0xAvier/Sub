#-*- coding: utf-8 -*-

class Player(IPlayer):
    """

    """


    def __init__(self, pid, is_removable = false):
        self.pid = pid
        self._player_mind = None 
        self._player_renders = [] 
        self._is_removable = is_removable


    def set_mind(self, mind):
        self._player_mind = mind


    def add_render(self, render):
        self._player_renders.append(render)


    def give_cards(self, cards):
        # Both render and mind 
        self._player_mind.give_cards(self, cards)
        for render in self._player_renders:
            render.give_cards(self, cards)


    def team(self):
        # Do not depend from render nor mind 
        return self.id % 2


    def get_card(self, played, playable):
        # Pure mind
        self._player_mind.get_card(self, played, playable)


    def get_coinche(self):
        # Pure mind
        self._player_mind.get_coinche()


    def get_bid(self, bidded, biddable):
        # Pure mind 
        self._player_mind.get_bid(bidded, biddable)


    def bidded(self, bid):
        # Both render and mind
        self._player_mind.bidded(bid)
        for render in self._player_renders:
            render.bidded(bid)


    def played(self, pid, card):
        # Both render and mind
        self._player_mind.played(pid, card)
        for render in self._player_renders:
            render.played(pid, card)


    def is_removable(self):
        return self._is_removable


    def reset_hand(self):
        # Pure mind
        self._player_mind.reset_hand()

