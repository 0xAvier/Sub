#-*- coding: utf-8 -*-

from src.game.bidding import Bidding


class Score(object):

    value = {
                'SA': {
                    '7': 0,
                    '8': 0,
                    '9': 0,
                    'J': 2,
                    'Q': 3,
                    'K': 4,
                    'T': 10,
                    'A': 19,
                    'DER': 10,
                },

                'AS': {
                    '7': 0,
                    '8': 0,
                    '9': 0,
                    'J': 2,
                    'Q': 3,
                    'K': 4,
                    'T': 10,
                    'A': 11,
                    'DER': 10,
                },

                'AA': {
                    '7': 0,
                    '8': 0,
                    '9': 14,
                    'J': 20,
                    'Q': 3,
                    'K': 4,
                    'T': 10,
                    'A': 11,
                    'DER': 10,
                },
            }


    def __init__(self, log):
        # score[0] is the score of players 0-2
        # score[1] is the score of players 1-3
        self.__score = [0, 0]
        # Logger
        self.log = log


    @staticmethod
    def eval_card(card, trump=None):
        """
            Return the value of a card, with trump consideration
            if trump is not None

        """
        if trump is None:
            s = Score.value["SA"][card[0]]
        elif card[1] != trump:
            s = Score.value["AS"][card[0]]
        elif card[1] == trump:
            s = Score.value["AA"][card[0]]
        return s


    @staticmethod
    def evaluate(cards, trump=None):
        """
            Evaluate the value of a set of cards

            @param cards    the set of cards to evaluate
            @param trump    the trump to consider (if not None)

        """
        return sum([Score.eval_card(c, trump) for c in cards])


    def update_score(self, team, pts):
        self.__score[team] += pts


    def get_score(self, team):
        return self.__score[team]


    def deal_points(self, deal, trump, last):
        """

            @param deal     two lists of tuples (trick, player), where:
                                - trick is the set of played cards
                                - player is the winning player of the trick
            @param trump    color of trump for this deal
            @param last     team that won the last trick
                            
        """
        # Score of each team from tricks
        pts = [0] * len(deal)
        for team, tricks in enumerate(deal):
            for trick in tricks:
                pts[team] += self.evaluate(trick[0], trump)
        # todo belotte / rebelotte

        # 10-der ?
        if trump != "TA":
            pts[last] += 10
        return pts 


    def around(self, pts):
        """
            Round points to multiple of 10

        """
        return int(round(float(pts) / 10.) * 10)


    def deal_score(self, deal, last, bid):
        """
            @param deal     two lists of tuples (trick, player), where:
                                - trick is the set of played cards
                                - player is the winning player of the trick
            @param last     team that won the last trick
            @param bid      Object Bidding defining the contract to be done

        """
        trump = bid.col
        team_taker = bid.taker.team()
        #todo belotte/rebelotte
        pts = [0] * 2
        # Special case : the taker team did win all tricks
        if len(deal[1 - team_taker]) == 0:
            pts[team_taker] = 250
            pts[1 - team_taker] = 0
        else:
            pts = self.deal_points(deal, trump, last)
        score_inc = [0, 0]
        if pts[team_taker] >= bid.val:
            # Contract is done
            score_inc[team_taker] = bid.coef * bid.val + self.around(pts[team_taker])
            # If the contract was not "coinché"
            if not bid.is_coinched:
                # Then the defensive team scores its points
                score_inc[1 - team_taker] = self.around(pts[1 - team_taker])
            # Log score
            self.log("Contract is done by {0} points ({1} - {2})".format(pts[team_taker] - bid.val, 
                                                                            pts[team_taker],
                                                                            pts[1 - team_taker]))
        else:
            # Contract is not done
            score_inc[1 - team_taker] = bid.coef * bid.val + 160
            # Log score
            self.log("Contract came to grief by {0} points ({1} - {2})".format(- pts[team_taker] + bid.val, 
                                                                            pts[team_taker],
                                                                            pts[1 - team_taker]))
        for team in xrange(len(self.__score)):
            self.update_score(team, score_inc[team])
        self.log("Score: (02) {0} - {1} (13)".format(self.__score[0], self.__score[1]))
        #todo notify event manager

