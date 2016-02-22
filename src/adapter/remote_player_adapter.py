#-*- coding: utf-8 -*-

from time import sleep

from src.adapter.i_player_adapter import IPlayerAdapter
from src.socket.client import Client
# from src.adapter.i_game_adapter import IGameAdapter
# from src.game.coinche import COINCHE_CODE
from src.game.round import BID_COINCHE, BID_BIDDING
from src.socket.code import SOCK_GIVE_CARDS, SOCK_BIDDED, SOCK_PLAYED

class RemotePlayerAdapter(IPlayerAdapter):


    def __init__(self, svr, pid):
        self.__svr = svr
        # TODO : remote coinche
        # self.player.set_method(COINCHE_CODE, self.coinche)
        self.__coinched = False
        self.__pid = pid


    @property
    def id(self):
        ## TODO player id
        return self.__pid


    def give_cards(self, cards):
        return self.__svr.send_to_player(self.__pid, SOCK_GIVE_CARDS, [cards])


    def get_card(self, played, playable):
        # return self.player.get_card(played, playable)
        # TODO
        pass


    def get_coinche(self, q):
        self.__coinched = False
        while True:
            if self.__coinched:
                q.put((BID_COINCHE, self.id))
                self.__coinched = False
            sleep(1)


    def get_bid(self, bidded, biddable, queue):
        queue.put((BID_BIDDING, self.player.get_bid(bidded, biddable)))
        return


    def bidded(self, bid):
        self.__coinched = False
        return self.__svr.send_to_player(self.__pid, SOCK_BIDDED, [bid])


    def played(self, pid, card):
        return self.__svr.send_to_player(self.__pid, SOCK_PLAYED, [pid, card])


    def is_removable(self):
        return self.player.is_removable()

    
    def reset_hand(self):
        self.player.reset_hand()


    def coinche(self):
        self.__coinched = True

