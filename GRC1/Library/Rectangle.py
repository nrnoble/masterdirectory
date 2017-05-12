from Library.BBox import *

class Rectangle(BBox):
    def __init__(self, p1, p2):
        BBox.__init__(self, p1, p2)

    def __repr__(self):
        return "Rectangle({}, {})".format(str(self.p1), str(self.p2))

    def _draw(self, canvas, options):
        p1 = self.p1
        p2 = self.p2
        x1, y1 = canvas.toScreen(p1.x, p1.y)
        x2, y2 = canvas.toScreen(p2.x, p2.y)
        return canvas.create_rectangle(x1, y1, x2, y2, options)

    def clone(self):
        other = Rectangle(self.p1, self.p2)
        other.config = self.config.copy()
        return other


    # def jumpTo(self, P1):
    #     """ move object specific coorinates x,y """
    #     # x = self.p1.x
    #     # y = self.p1.y
    #     # p1x = P1.x
    #     # p1y = P1.y
    #
    #     # dx = self.p1.x + P1.x
    #     # dy = self.p1.y + P1.y
    #
    #     dx = P1.x - self.p1.x
    #     dy = P1.y - self.p1.y
    #
    #     self.move(dx, dy)