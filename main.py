#!/usr/bin/python
#-*- coding: utf-8 -*-

import argparse

# Import tests
from test.test_main import run_tests

# Import game
from src.game_main import launch_game

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-t", "--test", action="store_true")
group.add_argument("-p", "--play", action="store_true")
group.add_argument("-w", "--watch", action="store_true")
group.add_argument("-f", "--full_test", action="store_true")
parser.add_argument("-c", "--cheat", action="store_true")

args = parser.parse_args()

if args.play:
    launch_game(play= True, cheat= args.cheat)
elif args.watch:
    launch_game(play= False, cheat= args.cheat)
elif args.test:
    run_tests()
elif args.full_test:
    print "Not implemented yet."
    print "Try again in 2016."
else:
    launch_game(play= False, cheat= args.cheat)


