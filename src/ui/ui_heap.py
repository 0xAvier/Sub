# -*- coding:utf-8 -*-
from Tkinter import Label

from src.game.card import Card

from src.ui.image_loader import ImageLoader  
from src.ui.ui_cards import UICards
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
        self.position = pos_to_index[position]

        # Memorise the card in the heap
        self._heap = None
        # The image itself 
        self.heap_image = None 
        # The label index
        self._label_index = None
        self._init_label()


    def label_column(self):
        """ 
            Define the position for the heap
        """
        if self.position == 0 or self.position == 2:
            # base column
            column = UIHand.first_card_column[self.position];
            # base
            column = TABLE_WIDTH / 2    
        elif self.position == 1 or self.position == 3:
            # base 
            column = TABLE_WIDTH / 2 
            # small shifting 
            h_shift = 60 
            if self.position == 1:
                # shift it to the right 
                column -= h_shift
            elif self.position == 3:
                # shift it to the left
                column += h_shift
            # don't forget to center it
        column -= ImageLoader.card_width / 2
        return column 


    def label_row(self):
        """
            
        """
        row = UIHand.first_card_row[self.position] 
        vert_shift = 15 
        if self.position == 0:
            # shift it down
            row += 1.5*ImageLoader.card_height
            # a little higher
            row -= vert_shift
        elif self.position == 2:
            # shift it up
            row -= 1.5 * ImageLoader.card_height
            # down down down
            row += vert_shift

        return row 
        

    def _init_label(self):
        self.heap_image = UICards.get_card_image(Card('7', 'S'))
        self._label = Label(self.frame, image=self.heap_image) 
        self._label.place(x = self.label_column(), y = self.label_row())

    def updateHeapImage(self):
        """
        """
        if self.heap == None:
            self._label.place_forget()
            print("Bug")
        else:
            new_card = UICards.get_card_image(self.heap)
            self._label.configure(image = new_card)

    @property
    def heap(self):
        """
        """
        return self._heap

    @heap.setter
    def heap(self, value):
        """
        """
        self._heap = value
        self.updateHeapImage()
