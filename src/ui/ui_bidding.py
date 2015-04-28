# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button, LEFT, BOTTOM, END, X, RIGHT,\
                    DISABLED, NORMAL 
from ttk import Combobox 
from threading import Event 

from src.utils.notify import Notify
from src.event.event_engine import EVT_UI_COINCHE 
from src.event.event_engine import CONSOLE, CONSOLE_RED
from src.game.bidding import Bidding


class UIBidding(Notify):


    class CoincheException(Exception):
        def __init__(self, pid):
            self.pid = pid


    def __init__(self, root, x, y, size_x, size_y):
        Notify.__init__(self)

        # Memorise the frame
        self._root = root 

        self._frame = Frame(width = size_x, height = size_y) 
        # No resize
        self._frame.pack_propagate(0)
        # Style
        self._frame.config(borderwidth = 5)

        self._x = x
        self._y = y

        # Init the buttons
        self._init_buttons()

        # Will be used to notify the main thread when waiting for a call 
        self.need_bid_event = Event() 
        # Will be used to notify the main thread when waiting for a coinche 
        self.coinche_event = Event() 

        self.pid = 0
        self._last_bid = None 
        
        self.enable()
     
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
        colors = list(Bidding.colors)
        colors.pop()
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

        self._selected_color = None 


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
        self._value_box.bind("<<ComboboxSelected>>", lambda x: self._update_bid_button())
        self._value_box.set(availableValue[0])
        self._value_box.pack(fill = X)


    @staticmethod
    def raise_(e):
        raise e


    def _init_bid_button(self):
        # To bid
        self._bid_button = Button(self._frame, text = "Pass", \
                                  command = self._click_bidding)
        self._bid_button.pack(fill = X)
        # To coinche
        self._coinche_button = Button(self._frame, text = "Coinche", \
                command = lambda: self._event[EVT_UI_COINCHE]()) 
        self._coinche_button.pack(fill = X)


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
        if self._bid_button.config('text')[-1] == "Pass":
            self._last_bid = Bidding(self.pid)
        else:
            if self._selected_color is None:
                self._event[CONSOLE_RED]("Choose a color!")
                return
            c = self._selected_color
            v = int(self._value_box.get())
            self._last_bid = Bidding(self.pid, v, c) 
        # Notify the consumer (main thread)
        self.need_bid_event.set()
        # Reset the event
        self.need_bid_event.clear()


    def _click_coinche(self):
        # Notify the consumer
        self.coinche_event.set()
        # Reset the event
        self.coinche_event.clear()

    def _update_bid_button(self):
        value = self._value_box.get()
        color = self._selected_color
        if value == "0" and color is None:
            self._bid_button.config(text = "Pass")
        elif value == "0":
            self._bid_button.config(text = "Bid " + color)
        elif color is None: 
            self._bid_button.config(text = "Bid " + value)
        else:
            self._bid_button.config(text = "Bid " + value + " " + color)


    @property
    def last_bid(self):
        return self._last_bid


    @last_bid.setter
    def last_bid(self, value):
        if value is None:
            self._bid_button.config(text = "Pass")
            self._last_bid = None 
        else:
            raise Exception("Should not be called")


    def disable(self):
        """
            Disable the bid button

        """
        self._bid_button.config(state = DISABLED)


    def enable(self):
        """
            Enable the bid button

        """
        self._bid_button.config(state = NORMAL)
