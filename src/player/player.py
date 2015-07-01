#-*- coding: utf-8 -*-

class Player(IPlayer):
    """

    """


    def __init__(self, pid, is_removable = false):
        self.pid = pid
        self._player_mind = None 
        self._player_renders = [] 
        self._is_removable = is_removable
        self._hand = Hand()


    def set_mind(self, mind):
        self._player_mind = mind


    def add_render(self, render):
        self._player_renders.append(render)


    def give_cards(self, cards):
        # Both render and mind 
        self._hand.add(cards)
        for render in self._player_renders:
            render.give_cards(self, cards)


    def get_hand(self):
        return self._hand  


    def team(self):
        # Do not depend from render nor mind 
        return self.id % 2


    def get_card(self, played, playable):
        # Pure mind
        card = self._player_mind.get_card(self, played, playable)
        # Update the hand
        self._hand.remove([card]) 
        return card


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
        self._hand.clear()

