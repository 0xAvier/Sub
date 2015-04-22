# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button, RIGHT

from src.ui.ui_table import UITable 

from src.ui.ui_console import UIConsole
from src.ui.ui_controllers import UIControllers, EVT_CONTROL_QUIT 

class UISidePannel(object):
    """
        The side pannel is responsible for all action aside the deal 

    """

    def __init__(self, root):
        # Memorise the root
        self._root = root

        w = 100
        h = UITable.TABLE_HEIGHT
        self._frame = Frame(self._root, width = w, height = h, bd=10)
        # Add some controllers 
        self._init_controllers(self._root, self._frame)
        # Add a console
        self._init_console(self._root, self._frame)
        self._frame.pack(side = RIGHT)


    def _init_controllers(self, root, frame):
        """
            Init the controllers frame
            This part is responsible for all the non-game stuff

        """
        # Add the frame
        self._controllers = UIControllers(root, frame)
        # Initialize the quit callback
        quit_callback = lambda: self._event[EVT_UI_PLAYER_LEFT]( \
                                 self._table.interface_player)
        self._controllers.set_method(EVT_CONTROL_QUIT, quit_callback) 


    def _init_console(self, root, frame):
        """
            Init the console

        """
        self._console = UIConsole(root, frame)


    def add_message(self, msg):
        """
            Add a message to the UIConsole

        """
        self._console.add_message(msg)
