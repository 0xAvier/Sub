#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.game.card import Card


def test_initialisation(v, c):
    nc = Card(v, c)
    assert(nc.val == v)
    assert(nc.col == c)


def card():
    test_initialisation('7', 'S')
    test_initialisation('8', 'S')
    test_initialisation('9', 'S')
    test_initialisation('J', 'S')
    test_initialisation('Q', 'S')
    test_initialisation('K', 'S')
    test_initialisation('T', 'S')
    test_initialisation('A', 'S')

    test_initialisation('7', 'H')
    test_initialisation('8', 'H')
    test_initialisation('9', 'H')
    test_initialisation('J', 'H')
    test_initialisation('Q', 'H')
    test_initialisation('K', 'H')
    test_initialisation('T', 'H')
    test_initialisation('A', 'H')

    test_initialisation('7', 'C')
    test_initialisation('8', 'C')
    test_initialisation('9', 'C')
    test_initialisation('J', 'C')
    test_initialisation('Q', 'C')
    test_initialisation('K', 'C')
    test_initialisation('T', 'C')
    test_initialisation('A', 'C')

    test_initialisation('7', 'D')
    test_initialisation('8', 'D')
    test_initialisation('9', 'D')
    test_initialisation('J', 'D')
    test_initialisation('Q', 'D')
    test_initialisation('K', 'D')
    test_initialisation('T', 'D')
    test_initialisation('A', 'D')

