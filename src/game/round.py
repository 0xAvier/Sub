
from random import choice, shuffle

from src.event.event_engine import EVT_NEW_HAND


MUST_UNDERCUT = False


class Round(object):

    def __init__(self, deck, players, events):
        # To be set by the user later
        self.max_pts = 2000
        # Deck to use in this roud
        self.deck = deck
        # Notification to send to event manager
        self.event = events
        self.players = players
        self.score = {'NS': 0, 'WE': 0}
        # TO MODIFY
        #self.dealer = choice(self.players)
        self.dealer = players[0]

    def next_player(self, p):
        return self.players[(p.id + 1) % len(self.players)]


    def deal(self):
        """
            Handle a whole deal from the distribution
            of cards to the last card played

        """
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
        # Annonces
        trump = None
        pass
        # Jeu
        p = self.dealer
        # Updating next dealer for next deal
        self.dealer = self.next_player(self.dealer)
        
        # To be removed
        self.score['NS'] = 2000

        while len(self.players[0].get_cards()) > 0:
            # p = self.next_player(p)
            p = self.trick(trump, p)
            

    
    def trick(self, trump, p):
        played = list()
        for i in xrange(len(self.players)):
            playable = self.compute_playable(played, p.get_cards(), trump)
            card = None
            while card is None or not card in playable:
                card = p.get_card(playable, played)
            # Add the card to played cards
            played.append(card)
            # Notify user that its card has been played
            p.played(card)
            p = self.next_player(p)    
        # todo return the player that wins the trick
        return 0


    def compute_playable(self, played, cards, trump):
        # If payer is the first to play, he can choose
        # any card in its hand
        if len(played) == 0:
            return cards
        else:
            # Color that has been played first
            asked = played[0][1]
            # Compute the highest card played so far
            highest = Card.highest(played, trump)
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
        return self.score['NS'] >= self.max_pts \
                or self.score['WE'] >= self.max_pts 
