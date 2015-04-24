#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.ui.ui_engine import UIEngine 
from src.game.game_engine import GameEngine
from src.event.event_engine import EventEngine
from src.adapter.event_ui_adapter import EventUIAdapter

from src.adapter.game_local_player_adapter import GameLocalPlayerAdapter 
from src.ui.ui_player import UIPlayer

import time

game = GameEngine()
evt = EventEngine(game)
ui = UIEngine()
ui_adapt = EventUIAdapter(ui)
evt.connect_adapter(ui_adapt)

ui_player = UIPlayer(ui, 0) 
adapt = GameLocalPlayerAdapter(game, ui_player) 
adapt.join()

game.new_round()

