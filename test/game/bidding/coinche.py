#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.game.bidding import Bidding


def coinche():
    # coinche OK announce
    # coinche pass
    # coinche coinched
    # coinche surcoinched
    try:
        Bidding('0').coinche()
        print "KO Bidding('0').coinche() should throw an exception" 
    except:
        pass

    b = Bidding(0, 80, 'S')
    b.coinche()
    assert(b.is_coinched())
    
