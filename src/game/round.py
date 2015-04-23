#-*- coding: utf-8 -*-

from random import choice, shuffle, randint

from src.event.event_engine import EVT_NEW_HAND, EVT_END_OF_TRICK, EVT_NEW_BID
from src.game.card import Card
from src.game.score import Score
from src.game.bidding import Bidding


MUST_UNDERCUT = False


class Round(object):

    def __init__(self, deck, players, events):
        # To be set by the user later
        self.max_pts = 2000
        # Deck to use in this round
        self.deck = deck
        # Notification to send to event manager
        self.event = events
        self.players = players
        self.score = Score(self.event)
        # TO MODIFY
        #self.dealer = choice(self.players)
        self.dealer = players[0]
        # List of played cards by trick and by team
        self.__tricks = [list(), list()]


    def next_player(self, p):
        return self.players[(p.id + 1) % len(self.players)]


    def compute_biddable(self, p, bidded):
        biddable = [Bidding(p)]
        # Get max bid so far
        highest_bid = max(bidded)
        for val in Bidding.values:
            if val <= highest_bid.val:
                continue
            for col in Bidding.colors:
                # If the player to bid hold the last bidding, he must change color
                if len([b for b in bidded if b.is_pass()]) == len(bidded) - 1 and col == highest_bid.col:
                    continue
                biddable.append(Bidding(p, val, col))
        return biddable


    def handle_biddings(self):
        """
            Handle the rounds of biddings, from 
            the first one to the final one.
            Return the highest bid.

        """
        bid = [Bidding(p) for p in self.players]
        last_bid = None
        passed = 0
        # Starting player is the one after the dealer
        p = self.next_player(self.dealer)
        while passed != 4:
            biddable = self.compute_biddable(p, bid)
            bid[p.id] = p.get_bid(bid, biddable)
            while bid[p.id] not in biddable:
                bid[p.id] = p.get_bid(bid, biddable)
            p.bidded(bid[p.id])
            if bid[p.id].is_pass():
                passed += 1
            else:
                # Last not "pass" bid
                last_bid = bid[p.id]
                passed = 0
            # Next player
            p = self.next_player(p)

        return last_bid


    def deal(self):
        """
            Handle a whole deal from the distribution
            of cards to the last card played

        """
        # Reset deal cards
        self.__deal_cards = list()
        # Distribution sequence generation
        npr = [2, 3, 3]
        shuffle(npr)
        for n in npr:
            for p in self.players:
                p.give_cards([self.deck.pop() for i in xrange(n)])
        # check that all cards have been given
        assert self.deck.empty()
        # Notify UIs 
        if EVT_NEW_HAND in self.event.keys():
            for p in self.players:
                self.event[EVT_NEW_HAND](p.id, p.get_cards())

        # Starting player is the one after the dealer
        p = self.next_player(self.dealer)
        # Updating next dealer for next deal
        self.dealer = self.next_player(self.dealer)

        # Annonces
        bid = self.handle_biddings()
        if bid is None:
            self.end_of_deal(False)
            return

        # Jeu
        while len(self.players[0].get_cards()) > 0:
            p = self.trick(bid.col, p)
            if EVT_END_OF_TRICK in self.event.keys():
                # Notify the event manager that the trick is over
                self.event[EVT_END_OF_TRICK](p)
            
        self.score.deal_score(self.__tricks, p.team(), bid)
        self.end_of_deal()


    def end_of_deal(self, played=True):
        """
            Handler of each end of deal
            In charge of putting back cards into the deck, 
            notify the event manager of the update of score 

            @param played   Boolean to indicate if the deal has 
                            been played or not (pass * 4)
    
        """
        if played:
            # Random if we reconstruct the deck by putting deck 1 on deck 2
            # or the opposite
            rdm = randint(0, 1)
            # Adding one by one the cards of one subdeck eto the deck
            while len(self.__tricks[rdm]) != 0:
                trick = self.__tricks[rdm].pop(0)
                while len(trick[0]) != 0:
                    self.deck.push(trick[0].pop(0))
            rdm = 1 - rdm
            # Adding the cards of the other subdeck to the deck
            while len(self.__tricks[rdm]) != 0:
                trick = self.__tricks[rdm].pop(0)
                while len(trick[0]) != 0:
                    self.deck.push(trick[0].pop(0))
        else:
            # Take hands one by one
            pid = range(4)
            shuffle(pid)
            while len(pid) != 0:
                p = self.players[pid.pop()]
                while not p.get_hand().is_empty():
                    self.deck.push(p.get_hand().pop())


    def trick(self, trump, p):
        played = list()
        best_card = None
        wins = None
        for i in xrange(len(self.players)):
            playable = self.compute_playable(played, p.get_cards(), trump)
            card = None
            while card is None or not card in playable:
                card = p.get_card(played, playable)
            # Add the card to played cards
            played.append(card)
            # Notify user that its card has been played
            p.played(card)
            # Check if the card is the best played until now
            if best_card is None or Card.highest([card, best_card], 
                    played[0][1], trump) == card:
                best_card = card
                wins = p
            p = self.next_player(p)    
        self.__tricks[wins.team()].append((played, wins))
        # return the player that wins the trick
        return wins


    def compute_playable(self, played, cards, trump):
        # If payer is the first to play, he can choose
        # any card in its hand
        if len(played) == 0:
            return cards
        else:
            # Color that has been played first
            asked = played[0][1]
            # Compute the highest card played so far
            highest = Card.highest(played, asked, trump)
            # Compute the cards in the same color
            same_col = [c for c in cards if c[1] == played[0][1]]
            # If player has the asked color
            if len(same_col) > 0:
                # If asked color is not trump
                if asked != trump:
                    # Return cards with same color as asked
                    return same_col
                # If asked color is trump
                else:
                    # Compute cards that are higher than the highest one 
                    # played so far
                    higher = [c for c in same_col if c.higher(highest, trump)]
                    # If player can provide higher trump
                    if len(higher) > 0:
                        return higher
                    else:
                        return same_col
            # If player cannot provide asked color
            else:
                # Is its partner winning ?
                if played.index(highest) == len(played) - 2:
                    # Then player can play whatever card we wants
                    return cards
                # Partner is not winning
                else:
                    # Compute trumps
                    tr = [c for c in cards if c[1] == trump]
                    # If no trumps, can play any card
                    if len(tr) == 0:
                        return cards
                    # If no trump has been played before, can play
                    # any trump
                    elif highest[1] != trump:
                        return tr
                    else:
                        # Compute cards that are higher than the highest one 
                        # played so far
                        higher = [c for c in same_col if c.higher(highest, trump)]
                        # If player can provide higher trump
                        if len(higher) > 0:
                            return higher
                        # Else, depend on variants of the game
                        elif MUST_UNDERCUT:
                            return tr
                        else:
                            return cards

    def over(self):
        return self.score.get_score(0) >= self.max_pts \
                or self.score.get_score(1) >= self.max_pts 
