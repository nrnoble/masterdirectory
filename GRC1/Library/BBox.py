from Library.GraphicObject import *
from Library.Point import *


class BBox(GraphicsObject):
    # Internal base class for objects represented by bounding box
    # (opposite corners) Line segment is a degenerate case.

    def __init__(self, p1, p2, options=["outline", "width", "fill"]):
        GraphicsObject.__init__(self, options)
        self.p1 = p1.clone()
        self.p2 = p2.clone()

    def _move(self, dx, dy):
        self.p1.x = self.p1.x + dx
        self.p1.y = self.p1.y + dy
        self.p2.x = self.p2.x + dx
        self.p2.y = self.p2.y + dy

    def getP1(self):
        """TODO: description needed"""
        return self.p1.clone()


    def getP2(self):
        """TODO: description needed"""
        return self.p2.clone()


    def getCenter(self):
        """TODO: description needed"""
        p1 = self.p1
        p2 = self.p2
        return Point((p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0)

    def moveTo(self, p1):
        """TODO: description needed"""
        self.p1.x = p1
        #self.p2.y = p2

    # def jumpTo(self, P1):
    #     """move object specific coorinates x,y"""
    #     # x = self.p1.x
    #     # y = self.p1.y
    #     # p1x = P1.x
    #     # p1y = P1.y
    #
    #     dx = P1.x - self.p1.x
    #     dy = P1.y - self.p1.y
    #     self._move(dx, dy)