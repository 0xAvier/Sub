# -*- coding:utf-8 -*-
from Tkinter import Label

from src.game.card import Card

from src.ui.image_loader import ImageLoader  
from src.ui.ui_card import UICard
from src.ui.ui_hand import UIHand
from src.ui.ui_table import TABLE_WIDTH, TABLE_HEIGHT 

class UIHeap(object):
    """
       Interface object for a heap 

    """

    def __init__(self, frame, position):
        # Memorise the frame
        self.frame = frame

        # Translate to a more usable index
        pos_to_index = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
        self._position = pos_to_index[position]

        # Memorise the card in the heap
        self._heap = None
        # The image itself 
        self._heap_image = None 
        # The label index
        self._label_index = None
        self._init_label()


    def label_column(self):
        """ 
            Define the position for the heap

        """
        if self._position == 0 or self._position == 2:
            # Base
            column = TABLE_WIDTH / 2    
        elif self._position == 1 or self._position == 3:
            # Base 
            column = TABLE_WIDTH / 2 
            # Small shifting 
            h_shift = 60 
            if self._position == 1:
                # Shift it to the right 
                column += h_shift
            elif self._position == 3:
                # Shift it to the left
                column -= h_shift
            # Don't forget to center it
        column -= ImageLoader.CARD_WIDTH / 2
        return column 


    def label_row(self):
        """
            Return the row (pixel) of the heap according to its player position

        """
        row = UIHand.first_card_row[self._position] 
        vert_shift = 15 
        if self._position == 0:
            # Shift it down
            row += 1.5*ImageLoader.CARD_HEIGHT
            # A little higher
            row -= vert_shift
        elif self._position == 2:
            # Shift it up
            row -= 1.5 * ImageLoader.CARD_HEIGHT
            # Down down down
            row += vert_shift

        return row 
        

    def _place_label(self):
        """
            Place the label to its position

        """
        self._label.place(x = self.label_column(), y = self.label_row())


    def _init_label(self):
        """
            Init the label 
        """
        self._label = Label(self.frame)


    def _update_heap_image(self):
        """
            Update the card image 
        """
        # Remove or update the image ?
        if self.heap is None:
            # Remove the image
            self._label.place_forget()
            self._heap_image = None
        else:
            # Get a new card
            new_card = UICard.get_card_image(self.heap)
            # Save it
            self._heap_image = new_card
            # Configure the label
            self._label.configure(image = new_card)
            # Replace it
            self._place_label()


    @property
    def heap(self):
        return self._heap


    @heap.setter
    def heap(self, value):
        self._heap = value
        self._update_heap_image()
