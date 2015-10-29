# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button, LEFT, BOTTOM, END, X, RIGHT,\
                    DISABLED, NORMAL 
from ttk import Combobox 
from threading import Event 

from src.utils.notify import Notify
from src.event.event_engine import EVT_UI_COINCHE 
from src.event.event_engine import CONSOLE, CONSOLE_RED
from src.game.bidding import Bidding


class UIBelote(Notify):
    """
        Initialise the belote widget

    """

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
        self._init_button()
        
        self.enable()
        self.clicked = False
     

    def set_position(self, x, y):
        self._x = x
        self._y = y


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


    def _init_button(self):
        """
            TODO

        """
        h = 2
        w = 2
        self._button = Button(self._frame, text="Belote", \
                                height=h, width=w, \
                                command= self._click_belote)
        self._button.pack(fill=X)
        self._button_clicked = False 

    
    def set_button_style(self, clicked):
        """
            TODO
    
        """
        fg = 'white' if clicked else 'black' 
        bg = 'black' if clicked else 'white' 
        self._button.config(foreground= fg, background= bg)


    def _click_belote(self):
        """
            TODO
    
        """
        self.clicked = not self.clicked 


    def disable(self):
        """
            Disable the bid button

        """
        self._button.config(state = DISABLED)


    def enable(self):
        """
            Enable the bid button

        """
        self._button.config(state = NORMAL)

    
    def belote_ack(self):
        """

        """
        self._button.config(text = "Rebelote")
    

    def rebelote_ack(self):
        """

        """
        self.disable()


    def re_init(self):
        self._button.clicked = False
        self._button.config(text = "Belote")


    @property
    def clicked(self):
        return self._button_clicked
    
    @clicked.setter
    def clicked(self, c):
        self._button_clicked = c 
        self.set_button_style(c)
