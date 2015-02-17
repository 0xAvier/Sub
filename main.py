#!/usr/bin/python
#-*- coding: utf-8 -*-

from Tkinter import Tk

from src.ui.interface import App

root = Tk()
root.geometry("1000x1000+30+30") 

app = App(root)

root.mainloop()
