#-*- coding: utf-8 -*-

from src.player.i_player import IPlayer
from src.game.hand import Hand 
from src.utils.notify import Notify

from src.player.mind.ia.basic_ia_player_mind import BasicIAPlayerMind


class Player(IPlayer, Notify):
    """
        TODO

    """


    def __init__(self, pid, is_removable = False):
        Notify.__init__(self)
        self.id = pid
        # Default mind is a basic (who said stupid?) IA
        self._player_mind = BasicIAPlayerMind(pid) 

        self._player_renders = [] 
        self._is_removable = is_removable
        self._hand = Hand()


    def set_mind(self, mind):
        """
            Replace the current mind of the Player

        """
        self._player_mind = mind


    def add_render(self, render):
        """
            Add a new render for the Player

        """
        self._player_renders.append(render)


    def give_cards(self, cards):
        """
            Add some cards to a hand

        """
        # Add the new cards to the player's hand
        self._hand.add(cards)
        # Notify renders
        for render in self._player_renders:
            render.give_cards(cards, self._hand)


    def team(self):
        """
            Return the id of the team of the player

        """
        # Do not depend from render nor mind 
        return self.id % 2


    def get_card(self, played, playable):
        """
            TODO

        """
        # Get a card from the Mind
        played = self._player_mind.get_card(played, playable)
        # Update the hand
        self._hand.remove([played[1]]) 
        return played 


    def get_coinche(self):
        """
            TODO

        """
        # Wait for a coinche from the Mind
        self._player_mind.get_coinche()


    def get_bid(self, bidded, biddable):
        """
            TODO

        """
        # Get the bid from the Mind
        return self._player_mind.get_bid(bidded, biddable)


    def bidded(self, bid):
        """
            TODO

        """
        # Indicate to the Mind what as been bidded 
        self._player_mind.bidded(bid)


    def played(self, pid, card):
        """
            Notification to the player that a card has been
            played.
            If this player is himself (ie pid == self.id), then it 
            must also remove the card from its hand

        """
        # Indicate to the Mind what as been played 
        self._player_mind.played(pid, card)


    def is_removable(self):
        """
            TODO

        """
        return self._is_removable


    def reset_hand(self):
        """ 
            TODO

        """
        self._hand.clear()

    
    def set_method(self, evt, method):
        self._player_mind.set_method(evt, method)
        for render in self._player_renders:
            render.set_method(evt, method)
