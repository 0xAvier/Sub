# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Button, RIGHT

from src.ui.ui_table import UITable 
from src.utils.notify import Notify
from src.event.event_engine import EVT_UI_PLAYER_LEFT 

from src.ui.ui_console import UIConsole
from src.ui.ui_controllers import UIControllers, EVT_CONTROL_QUIT 

class UISidePannel(Notify):
    """
        The side pannel is responsible for all action aside the deal 

    """

    def __init__(self, root):
        Notify.__init__(self)
        # Memorise the root
        self._root = root

        w = 100
        h = UITable.TABLE_HEIGHT
        self._frame = Frame(self._root, width = w, height = h, bd=10)
        # Add some controllers 
        self._init_controllers(self._root, self._frame)
        # Add a call widget
        #self._init_call(self._root, self._frame)
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


    def set_method(self, evt_id, method):
        """
            Overwrite set_method
            Because SidePannel is only an entry-point, set_method need
                to be called on every child of SidePannel 

        """
        self._controllers.set_method(evt_id, method)
