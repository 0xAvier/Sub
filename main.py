#!/usr/bin/python
#-*- coding: utf-8 -*-

import time, sys

from src.ui.ui_engine import UIEngine 
from src.game.game_engine import GameEngine
from src.event.event_engine import EventEngine
from src.adapter.event_ui_adapter import EventUIAdapter

from src.adapter.game_local_player_adapter import GameLocalPlayerAdapter 
from src.ui.ui_player import UIPlayer


game = GameEngine()
evt = EventEngine(game)
ui = UIEngine()
ui_adapt = EventUIAdapter(ui)
evt.connect_adapter(ui_adapt)

if len(sys.argv) > 1 and sys.argv[1] == "-p":
    ui.add_player(0)
    ui.set_reference_player(0)
    ui_player = UIPlayer(ui, 0) 
    adapt = GameLocalPlayerAdapter(game, ui_player) 
    adapt.join()

game.new_round()

