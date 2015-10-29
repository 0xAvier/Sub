#!/usr/bin/python
#-*- coding: utf-8 -*-

from test.game.bidding.bidding import bidding
from test.game.bidding.coinche import coinche 
from test.game.bidding.is_coinched import is_coinched 
from test.game.bidding.is_done import is_done 
from test.game.bidding.is_pass import is_pass 

def main_bidding_test():
    bidding()
    coinche()
    is_done()
    is_pass()
