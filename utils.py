from Tkinter import *

def subimage(src, coord):
    dst = PhotoImage()
    dst.tk.call(dst, 'copy', src, '-from', 
                coord[0], coord[1], coord[2], coord[3], 
                '-to', 0, 0)
    return dst
