from Library.GraphicObject import *
from Library.GraphicsWindow import *
from Library.Point import *


class Polygon(GraphicsObject):
    """Create Polygon object """
    def __init__(self, *points):
        # if points passed as a list, extract it
        if len(points) == 1 and type(points[0]) == type([]):
            points = points[0]
        self.points = list(map(Point.clone, points))
        GraphicsObject.__init__(self, ["outline", "width", "fill"])

    def __repr__(self):
        return "Polygon" + str(tuple(p for p in self.points))

    def clone(self):
        """Clone Polygon"""
        other = Polygon(*self.points)
        other.config = self.config.copy()
        return other

    def getPoints(self):
        """TODO: description needed"""
        return list(map(Point.clone, self.points))

    def _move(self, dx, dy):
        for p in self.points:
            p.move(dx, dy)

    def _draw(self, canvas, options):
        args = [canvas]
        for p in self.points:
            x, y = canvas.toScreen(p.x, p.y)
            args.append(x)
            args.append(y)
        args.append(options)
        return GraphicsWindow.create_polygon(*args)

