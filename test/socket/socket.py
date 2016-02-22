#-*- coding: utf-8 -*-

import thread
from time import sleep

from src.socket.server import Server
from src.socket.client import Client
from src.game.card import Card
from src.game.bidding import Bidding

def test_server():
    svr = Server("config/server.yaml")

def test_client():
    client = Client("config/client.yaml")

def test_remote_player():
    svr = Server("config/server.yaml")
    # Threading server idle
    thread.start_new_thread(svr.idle, ())
    while svr.nb_players < 1:
        sleep(1)
    print "YOLO"
    cards = [Card('A', 'H'), Card('7', 'S')]
    svr.player[0].give_cards(cards)
    bid = Bidding(0, 80, 'SA')
    svr.player[0].bidded(bid)
    cards = [Card('A', 'H'), Card('7', 'S')]
    svr.player[0].give_cards(cards)
    svr.player[0].played(0, cards[1])

def main_socket_test():
    # test_server()
    # test_client()
    test_remote_player()

