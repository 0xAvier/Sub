#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.ui.ui_engine import UIEngine 
from src.game.game_engine import GameEngine
from src.event.event_engine import EventEngine
from src.adapter.event_ui_adapter import EventUIAdapter

import time

game = GameEngine()
evt = EventEngine(game)
ui = UIEngine()
ui_adapt = EventUIAdapter(ui)
evt.connect_adapter(ui_adapt)
game.new_round()

