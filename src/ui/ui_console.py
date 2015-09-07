# -*- coding:utf-8 -*-
from Tkinter import Tk, Frame, Text, TOP, LEFT, RIGHT, END, Scrollbar, Y

from src.console.i_console import IConsole

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

        # Add text
        self._console.insert(END, "Initialisation of the log")


    def write(self, msg, red = False):
        """
            Add a message to the UIConsole

        """
        # Memorize the index of the message beginning
        msg_index = self._console.index(END)

        self._console.insert(END, "\n")
        self._console.insert(END, msg)
        self._console.see(END)
        
        # Add a tag wrapping the whole message
        self._console.tag_add("crt_msg", msg_index, END)

        # If the text has to be display in red...
        if red:
            # ... pop a giant blue unicorn ofc
            self._console.tag_config("crt_msg", foreground = "red") 
        else:
            # Otherwise the tag can be removed
            self._console.tag_remove("crt_msg", msg_index, END)


    def clear(self):
        """
            I want a fair task sharing
            Screw you

        """
        for i in xrange(0, 1000):
            self.write("Screw you")
