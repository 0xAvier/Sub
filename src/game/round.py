#-*- coding: utf-8 -*-

from random import choice, shuffle, randint

from src.event.event_engine import EVT_NEW_HAND, EVT_END_OF_TRICK, EVT_NEW_BID, EVT_CARD_PLAYED, EVT_END_BIDDING
from src.game.card import Card
from src.game.score import Score
from src.game.bidding import Bidding
from src.game.hand import Hand


MUST_UNDERCUT = False


class Round(object):

    def __init__(self, deck, players, events, team):
        # To be set by the user later
        self.max_pts = 2000
        # Deck to use in this round
        self.deck = deck
        # Notification to send to event manager
        self.event = events
        self.__players = [(p, Hand()) for p in players]
        self.score = Score(self.event, [0, 1, 0, 1])
        # TO MODIFY
        #self.dealer = choice(self.players)
        self.dealer = self.__players[0]
        # List of played cards by trick and by team
        self.__tricks = [list(), list()]
        # List of team for each player
        self.team = team


    def next_player(self, p):
        return self.__players[(p[0].id + 1) % len(self.__players)]


    def compute_biddable(self, p, bidded):
        biddable = [Bidding(p[0].id)]
        # Get max bid so far
        highest_bid = max(bidded)
        for val in Bidding.values:
            if val <= highest_bid.val:
                continue
            for col in Bidding.colors:
                # If the player to bid hold the last bidding, he must change color
                if len([b for b in bidded if b.is_pass()]) == len(bidded) - 1 and col == highest_bid.col:
                    continue
                biddable.append(Bidding(p[0].id, val, col))
        return biddable


    def handle_biddings(self):
        """
            Handle the rounds of biddings, from 
            the first one to the final one.
            Return the highest bid.

        """
        bid = [Bidding(p[0].id) for p in self.__players]
        last_bid = None
        passed = 0
        # Starting player is the one after the dealer
        p = self.next_player(self.dealer)
        while passed != 4:
            biddable = self.compute_biddable(p, bid)
            bid[p[0].id] = p[0].get_bid(bid, biddable)
            while bid[p[0].id] not in biddable:
                bid[p[0].id] = p[0].get_bid(bid, biddable)
            p[0].bidded(bid[p[0].id])
            # Notify players
            for pl in self.__players:
                pl[0].bidded(bid[p[0].id])
            # Notify event manager 
            if EVT_NEW_BID in self.event.keys():
                self.event[EVT_NEW_BID](bid[p[0].id])
            if bid[p[0].id].is_pass():
                passed += 1
            else:
                # Last not "pass" bid
                last_bid = bid[p[0].id]
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
        cnt = 0
        for n in npr:
            for p in self.__players:
                for i in xrange(n):
                    cnt += 1
                cards  = [self.deck.pop() for i in xrange(n)]
                # Add card to the user's hand
                p[1].add(cards)
                # Notify user that he has a new hand
                p[0].give_cards(cards)
        # check that all cards have been given
        assert self.deck.empty()
        # Notify event manager 
        if EVT_NEW_HAND in self.event.keys():
            for p in self.__players:
                self.event[EVT_NEW_HAND](p[0].id, p[0].get_cards())

        # Starting player is the one after the dealer
        p = self.next_player(self.dealer)

        # Annonces
        bid = self.handle_biddings()
        # Notify end of biddings
        if EVT_END_BIDDING in self.event.keys():
            self.event[EVT_END_BIDDING]()
        if bid is None:
            self.end_of_deal(False)
            return

        # Updating next dealer for next deal
        self.dealer = self.next_player(self.dealer)

        # Jeu
        while len(self.__players[0][1].get_cards()) > 0:
            p = self.trick(bid.col, p)
            if EVT_END_OF_TRICK in self.event.keys():
                # Notify the event manager that the trick is over
                self.event[EVT_END_OF_TRICK](p[0].id)
            
        self.score.deal_score(self.__tricks, self.team[p[0].id], bid)
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
                p = self.__players[pid.pop()]
                while not p[1].is_empty():
                    self.deck.push(p[1].pop())
                p[0].reset_hand()


    def trick(self, trump, p):
        played = list()
        best_card = None
        wins = None
        for i in xrange(len(self.__players)):
            playable = self.compute_playable(played, p[1].get_cards(), trump)
            card = None
            while card is None or not card in playable:
                card = p[0].get_card(played, playable)
            # Add the card to played cards
            played.append(card)
            # Remove it from player's hand
            print card
            p[1].remove([card])
            # Notify users that a card has been played
            for player in self.__players:
                player[0].played(p[0].id, card)
            # Notify event manager
            if EVT_CARD_PLAYED in self.event.keys():
                self.event[EVT_CARD_PLAYED](p[0].id, card)
            # Check if the card is the best played until now
            if best_card is None or Card.highest([card, best_card], 
                    played[0][1], trump) == card:
                best_card = card
                wins = p
            p = self.next_player(p)    
        self.__tricks[self.team[wins[0].id]].append((played, wins[0]))
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


