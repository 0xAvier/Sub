# -*- coding:utf-8 -*-

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
        self._heap = []

        # The image itself 
        self.heap_image = None 
        # The label 
        self.label = None
        # The label index
        self.label_index = None

    def label_column(self):
        """ 
            Define the position for the heap
        """
        # magical formula
        hand_width = (GameEngine.MAX_CARD - 1) * COVERING  + 10
        column = [hand_width * 1.5, hand_width * 1.8, hand_width * 1.5, 
                  hand_width * 1.3]
        return column[self.position]

    def label_row(self):
        """
            
        """
        
