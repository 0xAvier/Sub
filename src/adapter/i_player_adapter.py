#-*- coding: utf-8 -*-

from abc import ABCMeta

class IPlayerAdapter(object):
    """
        Interface that must implement a player object
        to be correctly interfaced with a game

    """

    __metaclass__ = ABCMeta


    def __init__(self):
        pass


    def give_cards(self, cards):
        """
            Add some cards to a hand

        """
        raise NotImplemented


    def get_hand(self):
        """
            Getter for player's hand

        """
        raise NotImplemented

    
    def get_cards(self):
        """
            Return the cards possessed by player

        """
        raise NotImplemented


    def team(self):
        """
            Return the id of the team of the player

        """
        raise NotImplemented


    def get_card(self, played, playable):
        """
            Player must play a card among playable

            @param played   list of cards played so far in this trick
            @param playable list of player's cards that he can play

        """
        raise NotImplemented

    
    def get_bid(self, bidded, biddable):
        """
            Player must announce a bid (possibly "Pass") among biddable

            @param bidded   list of biddings announced in the current round
                            (bidded[i] is the last bidding from player i)
            @param biddable list of possible biddings

        """
        raise NotImplemented

    
    def played(self, pid, card):
        """
            Notification to the user that a card has been played

            @param pid      id of the player who played
            @param card     card played by player pid

        """
        raise NotImplemented

    
    def bidded(self, bid):
        """
            Notification to the user that a bidding has been announced

            @param bid      Bidding announced (note that bid.taker returns the 
                            id of player who announced)

        """
        raise NotImplemented

    
    def is_removable(self):
        """
            Return True iif the player can be replaced by another player
            (e.g. a bot filling empty places while no human player is here)

        """
        raise NotImplemented
