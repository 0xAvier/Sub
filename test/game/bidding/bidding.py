#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.game.bidding import Bidding

def test_initialisation(pid, val = 0, col = 'N'):
    b = Bidding(pid, val, col)
    assert(b.taker == pid)
    assert(b.val == val)
    assert(b.col == col)

def bidding():
    test_initialisation(0)
    test_initialisation(1)
    test_initialisation(2)
    test_initialisation(3)
    test_initialisation(2, 0, 'SA')
    test_initialisation(2, 80, 'SA')
    test_initialisation(2, 90, 'SA')
    test_initialisation(2, 120, 'SA')
    test_initialisation(2, 120, 'SA')
    test_initialisation(2, 140, 'SA')
    test_initialisation(2, 150, 'SA')
    test_initialisation(2, 250, 'SA')

    test_initialisation(2, 0,   'TA')
    test_initialisation(2, 80,  'TA')
    test_initialisation(2, 90,  'TA')
    test_initialisation(2, 120, 'TA')
    test_initialisation(2, 120, 'TA')
    test_initialisation(2, 140, 'TA')
    test_initialisation(2, 150, 'TA')
    test_initialisation(2, 250, 'TA')

    test_initialisation(2, 0,   'S')
    test_initialisation(2, 80,  'S')
    test_initialisation(2, 90,  'S')
    test_initialisation(2, 120, 'S')
    test_initialisation(2, 120, 'S')
    test_initialisation(2, 140, 'S')
    test_initialisation(2, 150, 'S')
    test_initialisation(2, 250, 'S')

    try: 
        Bidding(-1)
        print "KO Bidding(-1) should throw an exception" 
    except:
        pass

    try: 
        Bidding('-1')
        print "KO Bidding('-1') should throw an exception" 
    except:
        pass

    try: 
        Bidding(1, '1')
        print "KO Bidding(1, '1') should throw an exception" 
    except:
        pass

    try: 
        Bidding(1, 'A')
        print "KO Bidding(1, 'A') should throw an exception" 
    except:
        pass

    try: 
        Bidding(1, 80, 1)
        print "KO Bidding(1, 80, 1) should throw an exception" 
    except:
        pass

    try: 
        Bidding(1, 80, 'A')
        print "KO Bidding(1, 80, 1) should throw an exception" 
    except:
        pass

    try: 
        Bidding(1, 85, 'C')
        print "KO Bidding(1, 85, 'C') should throw an exception" 
    except:
        pass

