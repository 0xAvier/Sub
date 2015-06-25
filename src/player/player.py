# -*- coding:utf-8 -*-
from abc import ABCMeta

class Player(IPlayer):
    """

    """


    def __init__(self, pid, controller, render):
        self.pid = pid
        self.controller = controller
        self.render = render


    def give_cards(self, cards):
        # both render and controller
        self.controller.give_cards(self, cards)
        self.render.give_cards(self, cards)


    def team(self):
        # do not depend from render nor controller 
        return self.id % 2


    def get_card(self, played, playable):
        # pure controller
        self.controller.get_card(self, played, playable)


    def get_coinche(self):
        # pure controller
        self.controller.get_coinche()


    def get_bid(self, bidded, biddable):
        # pure controller 
        self.controller.get_bid(bidded, biddable)


    def bidded(self, bid):
        # both render and controller
        self.controller.bidded(bid)
        self.render.bidded(bid)


    def played(self, pid, card):
        # both render and controller
        self.controller.bidded(bid)
        self.render.bidded(bid)


    def is_removable(self):
        # pure controller
        self.controller.is_removable()


    def reset_hand(self):
        # pure controller
        self.controller.reset_hand()
