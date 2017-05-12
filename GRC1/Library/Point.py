from Library.GraphicObject import *

class Point(GraphicsObject):
    """ create a single point """

    def __init__(self, x, y):
        GraphicsObject.__init__(self, ["outline", "fill"])
        self.setFill = self.setBoarderColor
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def _draw(self, canvas, options):
        x, y = canvas.toScreen(self.x, self.y)
        return canvas.create_rectangle(x, y, x + 1, y + 1, options)

    def _move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def clone(self):
        """Clone point"""
        other = Point(self.x, self.y)
        other.config = self.config.copy()
        return other

    def getX(self):
        """Get x coordenate"""
        return self.x


    def getY(self):
        """Get y coordenate"""
        return self.y



    def setAbsoluteX(self, x):
        """Set x coordenate"""
        self.x = x

    def setAbsoluteY(self,y):
        """Get y coordenate"""
        self.y = y
