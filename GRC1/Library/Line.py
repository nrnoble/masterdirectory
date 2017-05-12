from Library.Globals import *
from Library.GraphicsError import *
from Library.BBox import *


class Line(BBox):
    """Generic base class for creating a line"""
    def __init__(self, p1, p2):
        BBox.__init__(self, p1, p2, ["arrow", "fill", "width"])
        self.setFillColor(DEFAULT_CONFIG['outline'])
        self.setOutline = self.setFillColor

    def __repr__(self):
        return "Line({}, {})".format(str(self.p1), str(self.p2))

    def clone(self):
        """clone existing line"""
        other = Line(self.p1, self.p2)
        other.config = self.config.copy()
        return other

    def _draw(self, canvas, options):
        p1 = self.p1
        p2 = self.p2
        x1, y1 = canvas.toScreen(p1.x, p1.y)
        x2, y2 = canvas.toScreen(p2.x, p2.y)
        return canvas.create_line(x1, y1, x2, y2, options)

    def setArrow(self, option):
        """Assign arrow to  existing line ["first", "last", "both", "none"] """
        if not option in ["first", "last", "both", "none"]:
            raise GraphicsError(BAD_OPTION)
        self._reconfig("arrow", option)