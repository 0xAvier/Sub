#!/usr/bin/python
#-*- coding: utf-8 -*-

from test.game.belote import main_belote_test 
from test.game.card.main import main_card_test 
from test.game.bidding.main import main_bidding_test


def run_tests():
    main_belote_test()
    main_card_test() 
    main_bidding_test()


    exit()
