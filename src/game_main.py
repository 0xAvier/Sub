#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.ui.ui_engine import UIEngine 
from src.game.game_engine import GameEngine
from src.event.event_engine import EventEngine
from src.adapter.local_ui_adapter import LocalUIAdapter

from src.adapter.local_player_adapter import LocalPlayerAdapter 

from src.player.player import Player
from src.player.mind.ui_player_mind import UIPlayerMind 
from src.player.render.ui_player_render import UIPlayerRender

def add_human_player(game, ui):
    player = Player(0)
    player.add_render(UIPlayerRender(0, ui)) 
    player.set_mind(UIPlayerMind(0, ui) )
    ui.add_player(0)
    ui.set_reference_player(0)
    padapt = LocalPlayerAdapter(player) 
    game.add_player(padapt)


def enable_view_all_hand(game, ui):
    players = [None]*5
    adapts = [None]*5
    for pid in xrange(0, 4):
        try:
            ui.add_player(pid)
            players[pid] = Player(pid)
            players[pid].add_render(UIPlayerRender(pid, ui)) 
            adapts[pid] = LocalPlayerAdapter(players[pid]) 
            game.add_player(adapts[pid])
        except IndexError:
            # This seat is already taken, too bad
            pass


def launch_game(play = False, cheat = True):
    game = GameEngine()
    evt = EventEngine()
    game.add_event_manager(evt)
    
    ui = UIEngine()
    ui_adapt = LocalUIAdapter(ui)
    evt.add_ui(ui_adapt)
    
    if play:
        add_human_player(game, ui)
    
    if cheat: 
        enable_view_all_hand(game, ui)
    
    game.new_round()
