# -*- coding:utf-8 -*-

# Define global constants to identify events
EVT_NEW_ROUND = 0
EVT_NEW_HAND = 1
EVT_UI_GET_CARD = 2
EVT_CARD_PLAYED = 3
EVT_UI_PLAYER_LEFT = 4
EVT_END_OF_TRICK = 5
EVT_NEW_DEAL = 6
CONSOLE = 7
EVT_NEW_BID = 8
EVT_COINCHE = 9
EVT_SURCOINCHE = 10
EVT_UI_COINCHE = 11
EVT_UI_SURCOINCHE = 12
EVT_UI_GET_BID = 13
EVT_DEAL_SCORE = 14
EVT_UPDATE_SCORE = 15
EVT_END_BIDDING = 16
CONSOLE_RED = 17

class EventEngine(object):


    def __init__(self, game):
        self.game = game
        # List of adapters to be notified
        self.adapt = list()
        # List of consoles to log messages 
        self.console = list()
        # Define the function of the event manager that the 
        # game engine should call at each new round
        self.game.set_method(EVT_NEW_ROUND, self.new_round)
        self.game.set_method(EVT_NEW_DEAL, self.new_deal)
        self.game.set_method(EVT_CARD_PLAYED, self.card_played)
        self.game.set_method(EVT_END_OF_TRICK, self.end_of_trick)
        self.game.set_method(EVT_NEW_BID, self.new_bid)
        self.game.set_method(EVT_DEAL_SCORE, self.deal_score)
        self.game.set_method(EVT_END_BIDDING, self.end_bidding)

        self.game.set_method(CONSOLE, self.log)


    def connect_adapter(self, adapt, p = None):
        """
            Connect an adapter to the event manager
            The adapter should be notified when some events
            occur during the game (such as card_played)

            @param adapt    adapter to notify
            @param p        list of players handled by the adapter

        """
        if adapt not in self.adapt:
            self.adapt.append(adapt)
            # add consoles if any
            for c in adapt.get_consoles():
                self.add_console(c)


    def add_console(self, console):
        """
            Add a console to log information messages

        """
        if console not in self.console:
            self.console.append(console)


    def new_round(self):
        """
            Notify all interfaces that a new round has begun

        """
        self.log("New round")
        for adapt in self.adapt:
            adapt.new_round()


    def new_deal(self):
        """
            Notify all interfaces that a new deal has begun

        """
        self.log("New deal")
        for adapt in self.adapt:
            adapt.new_deal()


    def end_of_trick(self, pid):
        """
            Notify all interfaces that the current trick is over
            @param p    player that wins the trick

        """
        # Log trick
        self.log("-{0}- wins".format(pid))
        for adapt in self.adapt:
            adapt.end_of_trick(pid)


    def card_played(self, p, c):
        # Log played card
        self.log("-" + str(p) + "- played " + str(c))
        for adapt in self.adapt:
            adapt.card_played(p, c)


    def player_left(self, p):
        """
            Notify game that a player has left the game
            @param p    played who left

        """
        pass


    def log(self, msg):
        """
            Display message in all console objects set

        """
        for con in self.console:
            con.write(msg)
        print "[log] " + msg

    
    def new_bid(self, bid):
        """
            Notify UIs that a new bid has been announced

        """
        self.log("[" + str(bid.taker) + "] " + str(bid))
        for adapt in self.adapt:
            adapt.new_bid(bid)


    def deal_score(self, bid, pts):
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


    def update_score(self, score):
        self.log("Score: (02) {0} - {1} (13)".format(score[0], score[1]))
        # todo notify ui


    def end_bidding(self):
        for adapt in self.adapt:
            adapt.end_bidding()

