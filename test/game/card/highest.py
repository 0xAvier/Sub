#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.game.card import Card

def highest():
    try:
        Card.highest([], 'S', 'S')
    except:
        print "\"Card.highest([], 'S', 'S')\" raises exception"

    assert(Card('7', 'S') == Card.highest([Card('7', 'S')], 'S', 'S'))

    try:
        Card.highest([Card('7', 'D')], 'S', 'S')
    except:
        print "\"Card.highest([Card('7', 'D')], 'S', 'S')\" raises exception"

    assert(Card('A', 'S') == Card.highest([Card('Q', 'S'), Card('A', 'S')],
        'S', 'D'))

    assert(Card('A', 'S') == Card.highest([Card('Q', 'S'), Card('A', 'S')],
        'S', 'S'))

    assert(Card('J', 'S') == Card.highest([Card('Q', 'S'), Card('J', 'S')],
        'S', 'S'))

    assert(Card('Q', 'S') == Card.highest([Card('Q', 'S'), Card('J', 'S')],
        'S', 'D'))

    assert(Card('Q', 'S') == Card.highest([Card('Q', 'S'), Card('K', 'C')],
        'S', 'D'))

    assert(Card('K', 'C') == Card.highest([Card('Q', 'S'), Card('K', 'C')],
        'S', 'C'))

    assert(Card('Q', 'S') == Card.highest([Card('Q', 'S'), Card('K', 'C')],
        'S', 'S'))

    assert(Card('J', 'S') == Card.highest([Card('Q', 'S'), Card('J', 'S'), 
        Card('A', 'D')], 'D', 'S'))

    assert(Card('J', 'S') == Card.highest([Card('Q', 'S'), Card('J', 'S'), 
        Card('A', 'D')], 'S', 'S'))

    assert(Card('A', 'D') == Card.highest([Card('Q', 'S'), Card('J', 'S'), 
        Card('A', 'D')], 'D', 'D'))

