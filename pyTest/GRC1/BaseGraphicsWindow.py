# import time, os, sys
#
# try:  # import as appropriate for 2.x vs. 3.x
#     import tkinter as tk
# except:
#     import Tkinter as tk
#

from BaseGlobals import *
from BaseGraphicsError import *

from GRC1.BasePoint import *


class GraphicsWindow(tk.Canvas):
    """A GraphicsWindow is windows for drawing graphics objects"""

    def __init__(self, title="Graphics Window",
                 width=300,
                 height=300,
                 autoflush=True):
        assert type(title) == type(""), "Title must be a string"
        master = tk.Toplevel(root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master, width=width, height=height,
                           highlightthickness=0, bd=0)
        self.master.title(title)
        self.pack()
        master.resizable(0, 0)
        self.foreground = "black"
        self.items = []
        self.mouseX = None
        self.mouseY = None
        #self.bind("<Button-1>", self._onClick)
        #self.bind_all("<Key>", self._onKey)
        self.height = int(height)
        self.width = int(width)
        self.autoflush = autoflush
        self._mouseCallback = None
        self.trans = None
        self.closed = False
        master.lift()
        self.lastKey = ""
        if autoflush: root.update()

    def close(self):
        """Close the window"""

        if self.closed:
            return "closing Graphics Window"
        self.closed = True
        self.master.destroy()
        self.__autoflush()

    def isClosed(self):
        return self.closed

    def isOpen(self):
        return not self.closed

    def getMouseClick(self):
        """Pause for a mouse click then return Point object where
        the click occured"""
        self.update()  # clear clicks
        self.mouseX = None
        self.mouseY = None
        while self.mouseX == None or self.mouseY == None:
            self.update()
            if self.isClosed(): raise GraphicsError("getMouse in closed window")
            time.sleep(.1)
        x, y = self.toWorld(self.mouseX, self.mouseY)
        self.mouseX = None
        self.mouseY = None
        return Point(x, y)
