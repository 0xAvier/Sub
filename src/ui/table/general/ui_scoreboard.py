# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Label, BOTH, LEFT 

class UIScoreboard(object):
    """
        Display a scoreboard for the current game

    """


    def __init__(self, frame, h_size, v_size):
        # Define the size & position
        height, width, offset = 40, 100, 80
        x, y = h_size - width - offset, 0 + offset - height 

        # Make a dedicated frame 
        # This is usefull because label size is in text unit when
        #   it displays text (*gasp*)
        self._frame = Frame(frame, height = height, width = width) 
        # Avoid shrinking 
        self._frame.pack_propagate(0)
        self._frame.place(x = x, y = y)

        # Init the label
        self._label = Label(self._frame, text = "", justify = LEFT)
        # Pack it and make it fill the frame
        self._label.pack(fill = BOTH, expand = 1)

        self._score_02 = None
        self._score_13 = None

    
    @property
    def score_02(self):
        return self._score_02


    @property
    def score_13(self):
        return self._score_13


    @score_02.setter
    def score_02(self, value):
        self._score_02 = value
        self._update_score_text()


    @score_13.setter
    def score_13(self, value):
        self._score_13 = value
        self._update_score_text()


    def _update_score_text(self):
        name_02 = "Team 0_2"
        name_13 = "Team 1_3"
        text_02 = str(self._score_02)
        text_13 = str(self._score_13)
        self._label.config(text = name_02 + ": " + text_02 + "\n" + \
                                  name_13 + ": " + text_13)
