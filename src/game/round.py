#-*- coding: utf-8 -*-

import Queue as queue
from threading import Thread

from random import choice, shuffle, randint

from src.utils.notify import Notify
from src.event.event_engine import EVT_NEW_HAND, EVT_END_OF_TRICK, EVT_NEW_BID, EVT_CARD_PLAYED, EVT_END_BIDDING, EVT_COINCHE
from src.game.coinche import COINCHE_CODE, CoincheException
from src.game.card import Card
from src.game.score import Score
from src.game.bidding import Bidding
from src.game.hand import Hand


MUST_UNDERCUT = False

BID_COINCHE = 1
BID_BIDDING = 2


class Round(Notify):


    def __init__(self, deck, players, events, team):
        """
            @param deck     deck object to be used to get cards
            @param players  list of participating players
            @param events   list of events (to notify event manager)
            @param team     list of len(players) int, where team[i]
                            is the id of the team of player i

        """
        # Call parent constructor
        super(Round, self).__init__(events)
        # To be set by the user later
        self.max_pts = 2000
        # Deck to use in this round
        self.deck = deck
        # Notification to send to event manager
        self.event = events
        self.__players = [(p, Hand()) for p in players]
        self.score = Score(self.event, [0, 1, 0, 1])
        # Dealer of the round
        # todo: for now, player 0 always starts to deal
        self.dealer = self.__players[0]
        # List of played cards by trick and by team
        self.__tricks = [list(), list()]
        # List of team for each player
        self.team = team


    def next_player(self, p):
        """
            Compute the player who plays just after p
            in the game

            @param p    current player

            @ret        player after the current player

        """
        return self.__players[(p[0].id + 1) % len(self.__players)]


    def compute_biddable(self, p, bidded):
        """
            Compute the list of possible biddings for player p
            given the current state of biddings 

            @param p        player to bid (used to construct bids
                            with player id)
            @param bidded   list of the four previous bids

            @ret            list of possible biddings for player p

        """
        # Add the "pass" bid to biddable
        biddable = [Bidding(p[0].id)]
        # Get max bid so far
        highest_bid = max(bidded)
        # For each possible value of bidding
        for val in Bidding.values:
            # If value is lower than current bidding, we ignore it
            if val <= highest_bid.val:
                continue
            # Else, for each possible color
            for col in Bidding.colors:
                # If the player to bid hold the last bidding, he must change color
                if len([b for b in bidded if b.is_pass()]) == len(bidded) - 1 and col == highest_bid.col:
                    continue
                # Else, append the bid to possible biddings
                biddable.append(Bidding(p[0].id, val, col))
        # Return the list of biddings
        return biddable


    def handle_biddings(self):
        """
            Handle the rounds of biddings, from 
            the first one to the final one.
            Return the highest bid.


            ret     bid object corresponding to the highest bid
                    Possibly a "Pass" bidding if all players
                    have passed

        """
        # Initialize the biddings to "Pass" for each player
        bid = [Bidding(p[0].id) for p in self.__players]
        # Last bid at this point
        last_bid = None
        # Number of players that successively passed
        passed = 0
        # Queue to get thread answers
        q = queue.Queue()
        # Create threads to get a coinche from any player
        # at anytime
        bid_coinche = list()
        for pl, h in self.__players:
            bid_coinche.append(Thread(target=pl.get_coinche, args=(q,)))
            # We set the thread as a daemon in order to be able to terminate
            # even if it has not returned yet
            bid_coinche[-1].daemon = True
            bid_coinche[-1].start()
        # Starting player is the one after the dealer
        p = self.next_player(self.dealer)

        # We stop biddings when the four players have passed succesively
        while passed != 4:
            # Compute list of possible biddings
            biddable = self.compute_biddable(p, bid)
            # Create a thread to get bid from current player
            bid_th = Thread(target=p[0].get_bid, args=((bid, biddable, q)))
            bid_th.daemon = True
            bid_th.start()
            # Wait for p to return a bidding, or for any player to coinche
            while True:
                # Passive wait until a thread has returned
                tmp_bid = q.get()
                # If a thread notified a coinche and there was a bidding
                # from a player of another team than the one that coinched
                if (tmp_bid[0] == BID_COINCHE
                            and last_bid is not None 
                            and (tmp_bid[1] + last_bid.taker) % 2 == 1):
                    # We stop biddings right now by throwing an exception
                    # This exception will be handled by the calling function 
                    # (ie self.deal)
                    raise CoincheException(last_bid, tmp_bid[1])
                # Else if a thread notified a valid bid
                elif tmp_bid[0] == BID_BIDDING and tmp_bid[1] in biddable:
                    # We stop the wait loop for now
                    break

            # TODO: kill threads

            # Get the bid 
            bid[p[0].id] = tmp_bid[1]
            # Notify players for the new bid
            for pl in self.__players:
                pl[0].bidded(bid[p[0].id])
            # Notify event manager 
            self.notify(EVT_NEW_BID, bid[p[0].id])
            # If bid is "Pass", increment counter
            if bid[p[0].id].is_pass():
                passed += 1
            else:
                # Last not "pass" bid
                last_bid = bid[p[0].id]
                # Reset pass counter
                passed = 0
            # Next player
            p = self.next_player(p)
        return last_bid


    def deal(self):
        """
            Handle a whole deal from the distribution
            of cards to the last card played
            Update scores

        """
        # Reset deal cards
        self.__deal_cards = list()

        # Distribution
        # Distribution sequence generation
        npr = [2, 3, 3]
        # Shuffle the distribution sequence
        shuffle(npr)
        # For each round of distribution
        for n in npr:
            # For each player in the game
            for p in self.__players:
                # Pop n (2 or 3) cards from the deck
                cards  = [self.deck.pop() for i in xrange(n)]
                # Add card to the user's hand
                p[1].add(cards)
                # Notify user that he has a new hand
                p[0].give_cards(cards)
        # Check that all cards have been given
        assert self.deck.empty()

        # Starting player is the one after the dealer
        p = self.next_player(self.dealer)

        # Biddings
        try:
            # Ask for bids
            bid = self.handle_biddings()
        # If a player has coinched
        except CoincheException as e:
            # We get the bid through the exception
            bid = e.bid
            # We double its value
            bid.coinche()
            # Nofity event manager
            self.notify(EVT_COINCHE, e.by)
        # Notify end of biddings
        self.notify(EVT_END_BIDDING)
        # If bid is None, it means that the four players passed
        if bid is None:
            # So we end the deal without playing cards
            self.end_of_deal(False)
            return

        # Updating next dealer for next deal
        self.dealer = self.next_player(self.dealer)

        # Game
        while len(self.__players[0][1].get_cards()) > 0:
            # Handle one trick (ie four cards played)
            p = self.trick(bid.col, p)
            # Notify the event manager that the trick is over
            self.notify(EVT_END_OF_TRICK, p[0].id) 
        # Update scores
        self.score.deal_score(self.__tricks, self.team[p[0].id], bid)
        # End of deal
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
            # List of players whose hand is to get
            pid = range(4)
            # Shuffle order of recuperation
            shuffle(pid)
            # For each player
            while len(pid) != 0:
                p = self.__players[pid.pop()]
                # Get its cards one by one 
                while not p[1].is_empty():
                    # And put them on the deck
                    self.deck.push(p[1].pop())
                # Notify the user that its hand has
                # been reset
                p[0].reset_hand()


    def trick(self, trump, p):
        """
            Handle one trick, ie four cards played
            (one by each player)

            @param trump    color of the trump during this deal
            @param p        player who starts the trick

            @ret            the player that wins the trick

        """
        # List of cards played
        played = list()
        # Best card played so far
        best_card = None
        # Player that wins the trick
        wins = None
        # For each player
        for i in xrange(len(self.__players)):
            # Compute the cards that can be played by the player
            playable = self.compute_playable(played, p[1].get_cards(), trump)
            # Init the played card
            card = None
            # Get a valid card from the player
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
            self.notify(EVT_CARD_PLAYED, p[0].id, card)
            # Check if the card is the best played until now
            if best_card is None or Card.highest([card, best_card], 
                    played[0][1], trump) == card:
                # Update best card
                best_card = card
                # Update the winning player
                wins = p
            p = self.next_player(p)    
        self.__tricks[self.team[wins[0].id]].append((played, wins[0]))
        # return the player that wins the trick
        return wins


    def compute_playable(self, played, cards, trump):
        """
            Compute cards that a given player can play, 
            among its hand and relatively to cards already
            played and trump

            @param played   list of cards previously played
            @param cards    list of cards handed
            @param trump    color of trump in current game

            @ret            a subset of the list 'cards' corresponding
                            to cards that can be played

        """
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
        """
            Is the round over ? ie Have one team reached 
            the number of points needed to win the round ?

            @ret    True iif at least one team reached self.max_pts 

        """
        return self.score.get_score(0) >= self.max_pts \
                or self.score.get_score(1) >= self.max_pts 

