#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.game.hand import Hand
from src.game.card import Card
from src.game.belote import Belote

#TODO test belote.check also

# TESTS BELOTE
def test_belote():
    # Belote engine 
    belote = Belote()
    # Hand
    hand = Hand()

    # GLOBAL TESTS
    hand.add([Card('Q', 'S'), Card('K', 'S'), Card('A', 'D')])
    assert(Card('Q', 'S') in hand)
    assert(Card('K', 'S') in hand)
    assert(Card('A', 'D') in hand)
    assert(not Card('A', 'S') in hand)
    assert(not Card('Q', 'D') in hand)
    assert(not Card('A', 'S') in hand)

    ## BELOTE OK
    hand.clear()
    hand.add([Card('Q', 'S'), Card('K', 'S'), Card('A', 'D')])
    # Queen played first
    assert(belote.belote_is_valid(hand, Card('Q', 'S'), 'S'))
    # King played first
    assert(belote.belote_is_valid(hand, Card('K', 'S'), 'S'))
    # Same tests with another color
    hand.clear()
    hand.add([Card('Q', 'H'), Card('K', 'H'), Card('A', 'S')])
    # Queen played first
    assert(belote.belote_is_valid(hand, Card('Q', 'H'), 'H'))
    # King played first
    assert(belote.belote_is_valid(hand, Card('K', 'H'), 'H'))
    
    ## BELOTE KO
    # Queen only
    hand.clear()
    hand.add([Card('Q', 'S'), Card('9', 'S'), Card('A', 'D')])
    assert(not belote.belote_is_valid(hand, Card('Q', 'S'), 'S'))
    # King only
    hand.clear()
    hand.add([Card('K', 'S'), Card('9', 'S'), Card('A', 'D')])
    assert(not belote.belote_is_valid(hand, Card('K', 'S'), 'S'))
    # Color other than trump
    hand.clear()
    hand.add([Card('Q', 'S'), Card('K', 'S'), Card('A', 'D')])
    assert(not belote.belote_is_valid(hand, Card('K', 'S'), 'D'))
    # King and Queen from different colors
    hand.clear()
    hand.add([Card('Q', 'S'), Card('K', 'H'), Card('A', 'D')])
    assert(not belote.belote_is_valid(hand, Card('K', 'H'), 'H'))
    assert(not belote.belote_is_valid(hand, Card('Q', 'S'), 'S'))
    

# TESTS REBELOTE
def test_rebelote():
    # Belote engine 
    belote = Belote()

    # REBELOTE OK
    # Queen
    assert(belote.rebelote_is_valid(Card('Q', 'S'), 'S'))
    assert(belote.rebelote_is_valid(Card('Q', 'H'), 'H'))
    assert(belote.rebelote_is_valid(Card('Q', 'C'), 'C'))
    assert(belote.rebelote_is_valid(Card('Q', 'D'), 'D'))
    # King
    assert(belote.rebelote_is_valid(Card('K', 'S'), 'S'))
    assert(belote.rebelote_is_valid(Card('K', 'H'), 'H'))
    assert(belote.rebelote_is_valid(Card('K', 'C'), 'C'))
    assert(belote.rebelote_is_valid(Card('K', 'D'), 'D'))
    
    # REBELOTE KO
    # Card played neither K nor Q
    # Spread
    assert(not belote.rebelote_is_valid(Card('A', 'S'), 'S'))
    assert(not belote.rebelote_is_valid(Card('T', 'S'), 'S'))
    assert(not belote.rebelote_is_valid(Card('J', 'S'), 'S'))
    assert(not belote.rebelote_is_valid(Card('9', 'S'), 'S'))
    assert(not belote.rebelote_is_valid(Card('8', 'S'), 'S'))
    assert(not belote.rebelote_is_valid(Card('7', 'S'), 'S'))
    # Heart
    assert(not belote.rebelote_is_valid(Card('A', 'H'), 'H'))
    assert(not belote.rebelote_is_valid(Card('T', 'H'), 'H'))
    assert(not belote.rebelote_is_valid(Card('J', 'H'), 'H'))
    assert(not belote.rebelote_is_valid(Card('9', 'H'), 'H'))
    assert(not belote.rebelote_is_valid(Card('8', 'H'), 'H'))
    assert(not belote.rebelote_is_valid(Card('7', 'H'), 'H'))
    # Clubs
    assert(not belote.rebelote_is_valid(Card('A', 'C'), 'C'))
    assert(not belote.rebelote_is_valid(Card('T', 'C'), 'C'))
    assert(not belote.rebelote_is_valid(Card('J', 'C'), 'C'))
    assert(not belote.rebelote_is_valid(Card('9', 'C'), 'C'))
    assert(not belote.rebelote_is_valid(Card('8', 'C'), 'C'))
    assert(not belote.rebelote_is_valid(Card('7', 'C'), 'C'))
    # Diamond
    assert(not belote.rebelote_is_valid(Card('A', 'D'), 'D'))
    assert(not belote.rebelote_is_valid(Card('T', 'D'), 'D'))
    assert(not belote.rebelote_is_valid(Card('J', 'D'), 'D'))
    assert(not belote.rebelote_is_valid(Card('9', 'D'), 'D'))
    assert(not belote.rebelote_is_valid(Card('8', 'D'), 'D'))
    assert(not belote.rebelote_is_valid(Card('7', 'D'), 'D'))

    # Card playyed not trump
    # King
    assert(not belote.rebelote_is_valid(Card('K', 'S'), 'H'))
    assert(not belote.rebelote_is_valid(Card('K', 'S'), 'C'))
    assert(not belote.rebelote_is_valid(Card('K', 'S'), 'D'))
    assert(not belote.rebelote_is_valid(Card('K', 'D'), 'S'))
    # Queen
    assert(not belote.rebelote_is_valid(Card('Q', 'S'), 'H'))
    assert(not belote.rebelote_is_valid(Card('Q', 'S'), 'C'))
    assert(not belote.rebelote_is_valid(Card('Q', 'S'), 'D'))
    assert(not belote.rebelote_is_valid(Card('Q', 'D'), 'S'))

