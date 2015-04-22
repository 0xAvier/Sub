# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Text, TOP, LEFT, RIGHT, END, Scrollbar, Y

class UIConsole(object):
    """
        Add a console for login and discussion

    """


    def __init__(self, root, frame):
        # Memorise the root
        self._root = root
        # Create a dedicated frame
        self._frame = Frame()
        self._frame.pack(in_=frame, side = TOP)
        
        # Add a text widget
        self._console = Text(self._frame, height = 100)
        # Add a scrollbar
        self._scrollbar = Scrollbar(self._frame)

        # Init the scrollbar 
        self._scrollbar.pack(side = RIGHT, fill = Y)
        self._scrollbar.config(command=self._console.yview)
        # Init the text widget
        self._console.pack(side = LEFT)
        self._console.config(yscrollcommand=self._scrollbar.set)

        # Some noise to test
        for i in xrange(0, 1000):
            self.write(str(i))
    

    def write(self, msg):
        """
            Add a message to the UIConsole

        """
        self._console.insert(END, "\n")
        self._console.insert(END, msg)
        self._console.see(END)


    def clean(self):
        """
            I want a fair task sharing
            Screw you

        """
        for i in xrange(0, 1000):
            self.write("Screw you")
