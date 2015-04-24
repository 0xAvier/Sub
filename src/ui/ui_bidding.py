# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button, LEFT, BOTTOM, END, X, RIGHT
from ttk import Combobox 

from threading import Event 

from src.game.bidding import Bidding

class UIBidding(object):


    def __init__(self, root, x, y, size_x, size_y):
        # Memorise the frame
        self._root = root 

        self._frame = Frame(width = size_x, height = size_y) 
        # No resize
        self._frame.pack_propagate(0)
        # Style
        self._frame.config(borderwidth = 10)

        self._x = x
        self._y = y

        # Init the buttons
        self._init_buttons()

        # Will be used to notify the main thread when waiting for a call 
        self.need_bid_event = Event() 

        self.player_bidding = 0
        self.last_bid = None 

     
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
        colors = Bidding.colors 
        # The buttons need to have a fixed size
        h = 2
        w = 2

        for c in colors:
            self._buttons[c] = Button(self._buttons_frame, text=c, \
                                      height=h, width=w, \
                                      command=lambda c=c: self._click_color(c))
            self._buttons[c].pack(side = LEFT)

        # Pack the dedicated frame into the main frame
        self._buttons_frame.pack(in_ = self._frame)

        self._selected_color = Bidding.colors[0] 


    def _init_value_box(self):
        """
            Init the list box which select the value of the bid

        """
        availableValue = Bidding.values 
        # TODO: display "pass" instead of "0"
        #availableValue[0] = "pass"
        self._value_box = Combobox(self._frame, \
                                   values = availableValue, \
                                   # TODO
                                   # Only justify the selected value
                                   #justify = RIGHT, \
                                   state = 'readonly')
        self._value_box.set(availableValue[0])
        self._value_box.pack(fill = X)


    def _init_bid_button(self):
        self._bid_button = Button(self._frame, text = "Pass", \
                                  command = self._click_bidding)
        self._bid_button.pack(fill = X)


    def _init_buttons(self):
        """
            Init the buttons 

        """
        # Put the value box on top of the buttons
        self._init_value_box()
        self._init_color_buttons()
        self._init_bid_button() 


    def _click_color(self, color):
        self._selected_color = color 
        self._update_bid_button()


    def _click_bidding(self):
        """
            Callback function on bidding click  

        """
        c = self._selected_color
        v = int(self._value_box.get())
        self.last_bid = Bidding(self.player_bidding, v, c) 
        # Notify the consumer (main thread)
        self.need_bid_event.set()
        # Reset the event
        self.need_bid_event.clear()


    def _update_bid_button(self):
        self._bid_button.config(text = "Bid " + self._selected_value + " " + \
                                self._selected_color)
