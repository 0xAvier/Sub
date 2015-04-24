#-*- coding: utf-8 -*-


class UIPlayer(object):


    def __init__(self, ui, pid):
        self._ui = ui
        self.event = dict()
        self.id = pid


    def give_cards(self, cards):
        hand = self.get_hand()
        hand.append(cards)
        self._ui._table._hands[self.id].hand = hand


    def get_hand(self):
        # why ?
        return self._ui._table._hands[self.id]._hand


    def team(self):
        return self.id % 2


    def get_card(self, played, playable):
        # For now, return a random card
        return self._ui.get_card(self.id, played, playable)


    def get_bid(self, bidded, biddable):
        # For now, return a random bidding
        return choice(biddable)


    def bidded(self, bid):
        pass


    def played(self, pid, card):
        pass


    def is_removable(self):
        return false 
