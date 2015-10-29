#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.game.card import Card

def lower_than(lv, lc, hv, hc, t = None):
    # low card
    l = Card(lv, lc)
    # hight card
    h = Card(hv, hc)

    assert(h.higher(l, t))
    assert(not l.higher(h, t))


def not_lower_than(lv, lc, hv, hc, t = None):
    # low card
    l = Card(lv, lc)
    # hight card
    h = Card(hv, hc)

    assert(not l.higher(h, t))

def higher(): 
    # no trump
    lower_than('7', 'S', '8', 'S')
    lower_than('7', 'S', '9', 'S')
    lower_than('7', 'S', 'J', 'S')
    lower_than('7', 'S', 'Q', 'S')
    lower_than('7', 'S', 'K', 'S')
    lower_than('7', 'S', 'T', 'S')
    lower_than('7', 'S', 'A', 'S')

    lower_than('7', 'C', '8', 'C')
    lower_than('7', 'C', '9', 'C')
    lower_than('7', 'C', 'J', 'C')
    lower_than('7', 'C', 'Q', 'C')
    lower_than('7', 'C', 'K', 'C')
    lower_than('7', 'C', 'T', 'C')
    lower_than('7', 'C', 'A', 'C')

    not_lower_than('7', 'H', '8', 'D')
    not_lower_than('7', 'H', '9', 'D')
    not_lower_than('7', 'H', 'J', 'D')
    not_lower_than('7', 'H', 'Q', 'D')
    not_lower_than('7', 'H', 'K', 'D')
    not_lower_than('7', 'H', 'T', 'D')
    not_lower_than('7', 'H', 'A', 'D')

    not_lower_than('7', 'S', '8', 'D')
    not_lower_than('7', 'S', '9', 'D')
    not_lower_than('7', 'S', 'J', 'D')
    not_lower_than('7', 'S', 'Q', 'D')
    not_lower_than('7', 'S', 'K', 'D')
    not_lower_than('7', 'S', 'T', 'D')
    not_lower_than('7', 'S', 'A', 'D')

    lower_than('8', 'S', '9', 'S')
    lower_than('8', 'S', 'J', 'S')
    lower_than('8', 'S', 'Q', 'S')
    lower_than('8', 'S', 'K', 'S')
    lower_than('8', 'S', 'T', 'S')
    lower_than('8', 'S', 'A', 'S')

    lower_than('8', 'C', '9', 'C')
    lower_than('8', 'C', 'J', 'C')
    lower_than('8', 'C', 'Q', 'C')
    lower_than('8', 'C', 'K', 'C')
    lower_than('8', 'C', 'T', 'C')
    lower_than('8', 'C', 'A', 'C')

    not_lower_than('7', 'H', '8', 'D')
    not_lower_than('8', 'H', '9', 'D')
    not_lower_than('8', 'H', 'J', 'D')
    not_lower_than('8', 'H', 'Q', 'D')
    not_lower_than('8', 'H', 'K', 'D')
    not_lower_than('8', 'H', 'T', 'D')
    not_lower_than('8', 'H', 'A', 'D')

    not_lower_than('7', 'S', '8', 'D')
    not_lower_than('8', 'S', '9', 'D')
    not_lower_than('8', 'S', 'J', 'D')
    not_lower_than('8', 'S', 'Q', 'D')
    not_lower_than('8', 'S', 'K', 'D')
    not_lower_than('8', 'S', 'T', 'D')
    not_lower_than('8', 'S', 'A', 'D')

    lower_than('T', 'C', 'A', 'C')
    lower_than('J', 'S', 'A', 'S')
    lower_than('9', 'H', 'J', 'H')
    lower_than('K', 'D', 'T', 'D')

    # trump
    lower_than('7', 'S', '8', 'S', 'S')
    lower_than('7', 'S', '9', 'S', 'S')
    lower_than('7', 'S', 'J', 'S', 'S')
    lower_than('7', 'S', 'Q', 'S', 'S')
    lower_than('7', 'S', 'K', 'S', 'S')
    lower_than('7', 'S', 'T', 'S', 'S')
    lower_than('7', 'S', 'A', 'S', 'S')

    lower_than('7', 'C', '8', 'C', 'C')
    lower_than('7', 'C', '9', 'C', 'C')
    lower_than('7', 'C', 'J', 'C', 'C')
    lower_than('7', 'C', 'Q', 'C', 'C')
    lower_than('7', 'C', 'K', 'C', 'C')
    lower_than('7', 'C', 'T', 'C', 'C')
    lower_than('7', 'C', 'A', 'C', 'C')
    
    lower_than('7', 'H', '8', 'S', 'S')
    lower_than('7', 'H', '9', 'S', 'S')
    lower_than('7', 'H', 'J', 'S', 'S')
    lower_than('7', 'H', 'Q', 'S', 'S')
    lower_than('7', 'H', 'K', 'S', 'S')
    lower_than('7', 'H', 'T', 'S', 'S')
    lower_than('7', 'H', 'A', 'S', 'S')

    lower_than('7', 'S', '8', 'C', 'C')
    lower_than('7', 'S', '9', 'C', 'C')
    lower_than('7', 'S', 'J', 'C', 'C')
    lower_than('7', 'S', 'Q', 'C', 'C')
    lower_than('7', 'S', 'K', 'C', 'C')
    lower_than('7', 'S', 'T', 'C', 'C')
    lower_than('7', 'S', 'A', 'C', 'C')
    
    lower_than('T', 'C', 'A', 'C', 'C')
    lower_than('J', 'S', 'A', 'S', 'D')
    lower_than('A', 'S', 'J', 'S', 'S')
    lower_than('9', 'H', 'J', 'H', 'H')
    lower_than('9', 'H', 'J', 'H', 'D')
    lower_than('K', 'D', 'T', 'D', 'S')
    lower_than('K', 'D', 'T', 'D', 'D')

    lower_than('7', 'S', '8', 'S', 'D')
    lower_than('7', 'S', '9', 'S', 'D')
    lower_than('7', 'S', 'J', 'S', 'D')
    lower_than('7', 'S', 'Q', 'S', 'D')
    lower_than('7', 'S', 'K', 'S', 'D')
    lower_than('7', 'S', 'T', 'S', 'D')
    lower_than('7', 'S', 'A', 'S', 'D')

    lower_than('7', 'C', '8', 'C', 'D')
    lower_than('7', 'C', '9', 'C', 'D')
    lower_than('7', 'C', 'J', 'C', 'D')
    lower_than('7', 'C', 'Q', 'C', 'D')
    lower_than('7', 'C', 'K', 'C', 'D')
    lower_than('7', 'C', 'T', 'C', 'D')
    lower_than('7', 'C', 'A', 'C', 'D')

    not_lower_than('7', 'H', '8', 'D', 'C')
    not_lower_than('7', 'H', '9', 'D', 'C')
    not_lower_than('7', 'H', 'J', 'D', 'C')
    not_lower_than('7', 'H', 'Q', 'D', 'C')
    not_lower_than('7', 'H', 'K', 'D', 'C')
    not_lower_than('7', 'H', 'T', 'D', 'C')
    not_lower_than('7', 'H', 'A', 'D', 'C')

    not_lower_than('7', 'S', '8', 'D', 'C')
    not_lower_than('7', 'S', '9', 'D', 'C')
    not_lower_than('7', 'S', 'J', 'D', 'C')
    not_lower_than('7', 'S', 'Q', 'D', 'C')
    not_lower_than('7', 'S', 'K', 'D', 'C')
    not_lower_than('7', 'S', 'T', 'D', 'C')
    not_lower_than('7', 'S', 'A', 'D', 'C')

    lower_than('8', 'S', '9', 'S', 'D')
    lower_than('8', 'S', 'J', 'S', 'D')
    lower_than('8', 'S', 'Q', 'S', 'D')
    lower_than('8', 'S', 'K', 'S', 'D')
    lower_than('8', 'S', 'T', 'S', 'D')
    lower_than('8', 'S', 'A', 'S', 'D')

    lower_than('8', 'C', '9', 'C', 'D')
    lower_than('8', 'C', 'J', 'C', 'D')
