# -*- coding:utf-8 -*-

from Tkinter import Tk, Frame, Text, RIGHT, END, TOP, Scrollbar, Y

from src.console.console import IConsole

class UIConsole(IConsole):
    """
        Add a console for login and discussion

    """


    def __init__(self, root, frame):
        # Memorise the root
        self._root = root
        # Create a dedicated frame
        self._frame = Frame()
        self._frame.pack(in_=frame, side = TOP)
        
        # Init the text widget
        self._console = Text(self._frame, height = 100)
        self._console.pack()
        self._console.insert(END, "Initialisation of log console")
        
        # Add a scrollbar
        self._scrollbar = Scrollbar(self._frame)
        self._scrollbar.pack(side = RIGHT, fill = Y)
        self._scrollbar.config(command=self._console.yview)


    def write(self, msg):
        """
            Add a message to the UIConsole

        """
        self._console.insert(END, "\n")
        self._console.insert(END, msg)


    def clear(self):
        """
            I want a fair task sharing
            Screw you

        """
        for i in xrange(0, 1000):
            self.write("Screw you")
