# -*- coding:utf-8 -*-
from Tkinter import Frame, Button, Pack, RIGHT, TOP, BOTTOM
import tkMessageBox

from src.utils.notify import Notify

EVT_CONTROL_QUIT = 0

class UIControllers(Notify):
    """
        Add buttons to control the game proceedings
        For the moment, only a "Quit" button is added.
       
    """


    def __init__(self, root, frame):
        # Init the base class
        Notify.__init__(self)
        # Memorise the root
        self._root = root  
        # Create a new frame only for controllers
        self._frame = Frame() 
        self._frame.pack(in_=frame, side = BOTTOM)
        # Bind the close action with our own callback 
        self._root.protocol("WM_DELETE_WINDOW", self._quit_root)
        self._add_quit_button()


    def _add_quit_button(self):
        """
            Add a button to quit the game

        """
        self._quit = Button(self._frame, text = "Quit",
                                command=self._quit_root)
        self._quit.pack(side = BOTTOM)


    def _quit_root(self):
        """ 
            Own callback to handle "close window" event 

        """
        # Double check the user intentions
        if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
            # If he's sure (at least twice in a row), quit
            self._root.destroy()
            # Notify the event_engine
            self._event[EVT_CONTROL_QUIT]()
            exit(0)
