#!/usr/bin/python
#-*- coding: utf-8 -*-

from Tkinter import Tk

from src.ui.interface import App
from src.game.game_engine import GameEngine
from src.event.event_engine import EventEngine

root = Tk()
root.geometry("1000x700+1510+30") 

game = GameEngine()
evt = EventEngine(game)
app = App(root)
evt.add_ui(app, [0, 1, 2, 3])
game.new_round()

root.mainloop()
