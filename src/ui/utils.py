# -*- coding:utf-8 -*-
from Tkinter import PhotoImage 

def subimage(src, coord):
    """
        Return the subimage of the image src 
        @param src      source image
        @param coord    coordinates of the square subimage 
        Coordinates format is (x, y, x + dx

    """
    # Create an image
    dst = PhotoImage()
    # Copy the subimage into the image
    dst.tk.call(dst, 'copy', src, '-from', 
                coord[0], coord[1], coord[2], coord[3], 
                '-to', 0, 0)
    # Return the result
    return dst
