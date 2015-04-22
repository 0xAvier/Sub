#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.ui.ui_engine import UIEngine 
from src.game.game_engine import GameEngine
from src.event.event_engine import EventEngine

import time

game = GameEngine()
evt = EventEngine(game)
app = UIEngine()
evt.add_ui(app, [1])
game.new_round()

