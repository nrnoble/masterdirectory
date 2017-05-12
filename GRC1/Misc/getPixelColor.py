from ctypes import windll
from tkinter import *

from Library import GRCGraphics as GRC

background2 = GRC.Image(GRC.Point(251, 134), ".\\Content\\randomPixelsbackground3.png")


root = Tk()

def click(event):
    dc = windll.user32.GetDC(0)dw
    rgb = windll.gdi32.GetPixel(dc,event.x_root,event.y_root)
    r = rgb & 0xff
    g = (rgb >> 8) & 0xff
    b = (rgb >> 16) & 0xff
    print (r,g,b)

for i in ['red', 'green', 'blue', 'black', 'white']:
    Label(root, width=30, background=i).pack()

root.bind('<Button-1>', click)

root.mainloop()