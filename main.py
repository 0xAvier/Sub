#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.ui.interface import App
from src.game.game_engine import GameEngine
from src.event.event_engine import EventEngine

import time

game = GameEngine()
evt = EventEngine(game)
app = App()
time.sleep(3)
evt.add_ui(app, [0, 1, 2, 3])
game.new_round()

