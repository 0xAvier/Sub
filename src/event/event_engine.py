# -*- coding:utf-8 -*-

# Import all event codes 
from src.event.event_code import *


class EventEngine(object):


    def __init__(self):
        # List of adapters to be notified
        self.__adapt = list()
        # List of consoles to log messages 
        self.__console = list()

    def notify(self, EVT_CODE, *args):
        if EVT_CODE == EVT_NEW_DEAL:
            self.__new_deal(*args)
        elif EVT_CODE == EVT_NEW_ROUND:
            self.__new_round(*args)
        elif EVT_CODE == EVT_CARD_PLAYED:
            self.__card_played(*args)
        elif EVT_CODE == EVT_END_OF_TRICK:
            self.__end_of_trick(*args)
        elif EVT_CODE == EVT_NEW_BID:
            self.__new_bid(*args)
        elif EVT_CODE == EVT_DEAL_SCORE:
            self.__deal_score(*args)
        elif EVT_CODE == EVT_END_BIDDING:
            self.__end_bidding(*args)
        elif EVT_CODE == EVT_UPDATE_SCORE:
            self.__update_score(*args)
        elif EVT_CODE == EVT_COINCHE:
            self.__coinche(*args)
        elif EVT_CODE == CONSOLE:
            self.log(*args)


    def connect_adapter(self, adapt, p = None):
        """
            Connect an adapter to the event manager
            The adapter should be notified when some events
            occur during the game (such as card_played)

            @param adapt    adapter to notify
            @param p        list of players handled by the adapter

        """
        if adapt not in self.__adapt:
            self.__adapt.append(adapt)
            # add consoles if any
            for c in adapt.get_consoles():
                self.add_console(c)


    def add_console(self, console):
        """
            Add a console to log information messages

        """
        if console not in self.__console:
            self.__console.append(console)


    def log(self, msg):
        """
            Display message in all console objects set

        """
        for con in self.__console:
            con.write(msg)
        print "[log] " + msg


    def __new_round(self):
        """
            Notify all interfaces that a new round has begun

        """
        self.log("New round")
        for adapt in self.__adapt:
            adapt.new_round()


    def __new_deal(self):
        """
            Notify all interfaces that a new deal has begun

        """
        self.log("New deal")
        for adapt in self.__adapt:
            adapt.new_deal()


    def __end_of_trick(self, pid):
        """
            Notify all interfaces that the current trick is over
            @param p    player that wins the trick

        """
        # Log trick
        self.log("-{0}- wins".format(pid))
        for adapt in self.__adapt:
            adapt.end_of_trick(pid)


    def __card_played(self, p, c):
        # Log played card
        self.log("-" + str(p) + "- played " + str(c))
        for adapt in self.__adapt:
            adapt.card_played(p, c)



    
    def __new_bid(self, bid):
        """
            Notify UIs that a new bid has been announced

        """
        self.log("[" + str(bid.taker) + "] " + str(bid))
        for adapt in self.__adapt:
            adapt.new_bid(bid)


    def __deal_score(self, bid, pts):
        team_taker = self.game.get_team(bid.taker)
        if bid.is_done():
            self.log("Contract is done by {0} points ({1} - {2})".format(pts[team_taker] - bid.val, 
                                                                            pts[team_taker],
                                                                            pts[1 - team_taker]))
        else:
            # Log score
            self.log("Contract came to grief by {0} points ({1} - {2})".format(- pts[team_taker] + bid.val, 
                                                                            pts[team_taker],
                                                                            pts[1 - team_taker]))


    def __update_score(self, score):
        self.log("Score: (02) {0} - {1} (13)".format(score[0], score[1]))
        for adapt in self.__adapt:
            adapt.update_score(score)


    def __end_bidding(self):
        for adapt in self.__adapt:
            adapt.end_bidding()


    def __coinche(self, pid):
        self.log("-{0}- has coinched !".format(pid))

