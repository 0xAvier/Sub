#!/usr/bin/python
#-*- coding: utf-8 -*-

import time, sys

from src.ui.ui_engine import UIEngine 
from src.game.game_engine import GameEngine
from src.event.event_engine import EventEngine
from src.adapter.event_ui_adapter import EventUIAdapter

from src.adapter.game_local_player_adapter import GameLocalPlayerAdapter 

from src.player.player import Player
from src.ui.ui_player_mind import UIPlayerMind 
from src.ui.ui_player_render import UIPlayerRender


game = GameEngine()
evt = EventEngine(game)
ui = UIEngine()
ui_adapt = EventUIAdapter(ui)
evt.connect_adapter(ui_adapt)

if len(sys.argv) > 1 and sys.argv[1] == "-p":
    ui.add_player(0)
    ui.set_reference_player(0)
    ui_player = Player(0) 
    ui_player.add_render(UIPlayerRender(0, ui)) 
    ui_player.set_mind(UIPlayerMind(0, ui) )
    adapt = GameLocalPlayerAdapter(game, ui_player) 
    adapt.join()

game.new_round()

