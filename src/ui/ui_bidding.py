# -*- coding:utf-8 -*-
# TODO
from Tkinter import Tk, Frame, Button, LEFT, BOTTOM, END, X, RIGHT
from ttk import Combobox 

from threading import Event 

class UIBidding(object):


    def __init__(self, root, x, y, size_x, size_y):
        # Memorise the frame
        self._root = root 

        self._frame = Frame(width = size_x, height = size_y) 
        self._x = x
        self._y = y

        # Init the buttons
        self._init_buttons()

        # Will be used to notify the main thread when waiting for a call 
        self.need_call_event = Event() 

     
    def display(self): 
        """
            Display the widget on the table

        """
        self._frame.place(in_ = self._root, x = self._x, y = self._y)


    def hide(self):
        """
            Hide the pannel when the biddings are closed for example

        """
        self._frame.place_forget()


    def _init_color_buttons(self):
        """
            Init the buttons to select the color

        """
        # Dedicated frame for buttons
        self._buttons_frame = Frame()
        # This dictionnary will contains all the color buttons
        self._buttons = dict()
        # Several colors are available
        colors = ["S", "H", "C", "D", "A-T", "N-T"]
        # The buttons need to have a fixed size
        h = 2
        w = 2

        for c in colors:
            self._buttons[c] = Button(self._buttons_frame, \
                                      text=c, height=h, width=w)
            self._buttons[c].pack(side = LEFT)

        # Pack the dedicated frame into the main frame
        self._buttons_frame.pack(in_ = self._frame)


    def _init_value_box(self):
        """
            Init the list box which select the value of the bid

        """
        availableValue = ('80', '90', '100', '250', '270') 
        # The value will be updated by the combobox
        self._selected_value = "" 
        self._value_box = Combobox(self._frame, \
                                   textvariable = self._selected_value, \
                                   values = availableValue, \
                                   # TODO
                                   # Only justify the selected value
                                   #justify = RIGHT, \
                                   state = 'readonly')
        self._value_box.set(availableValue[0])
        self._value_box.pack(fill = X)


    def _init_buttons(self):
        """
            Init the buttons 

        """
        # Put the value box on top of the buttons
        self._init_value_box()
        self._init_color_buttons()
