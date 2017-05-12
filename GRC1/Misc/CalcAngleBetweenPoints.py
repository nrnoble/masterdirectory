from Library import GRCGraphics as GRC
import math

win = GRC.GraphicsWindow("test", 500, 500)

def main():

    #win = GRC.GraphicsWindow("test", 500, 500)

    p1 = GRC.Point(10, 20)
    p2 = GRC.Point(10, 200)

    # myLine = GRC.Line(p1, p2)
    # myLine.draw(win)
    # calcPoints(p1,p2)
    points = get_line([10,10], [20,200])
    #print (points)
    for point in points:
        print (point)
        win.plot(point[0], round(point[1]), "Black")

    line = GRC.Line(p1,p2)
    win.addItem(line)
    win.redraw()
    win.waitForKeyPress()
    #ListOfPoints(p1,p2)

def calcPoints(P1,P2):
    x1 = P1.x
    y1 = P1.y

    x2 = P2.x
    y2 = P2.y

    xx = x2 - x1
    yy = y2 - y1

    xStep = 1
    if xx < 0:
        xStep = -1


    yStep = yy / xx

    if yy < 0:
        yStep = yStep * -1

    print ("P1.x: "  + str (P1.x) + " P1.y: " + str (P1.y) + " xx=" + str(xx))
    print ("P2.x: "  + str (P2.x) + " P2.y: " + str (P2.y) + " yy=" + str(yy))
    print ("xx: "  + str (xx) + " yy: " + str (yy))
    print ("yStep: " + str (yStep))
    print()

    win.waitForKeyPress()
    x = P1.x
    y = P1.y

    while x != P2.x:
        x = x + xStep
        y = y + yStep
        print(x, round(y))
        win.plot(x, round(y), "Black")


class bresenham:
    def __init__(self, start, end):
        self.start = list(start)
        self.end = list(end)
        self.path = []

        self.steep = abs(self.end[1] - self.start[1]) > abs(self.end[0] - self.start[0])

        if self.steep:
            print ('Steep')
            self.start = self.swap(self.start[0], self.start[1])
            self.end = self.swap(self.end[0], self.end[1])

        if self.start[0] > self.end[0]:
            print ('flippin and floppin')
            _x0 = int(self.start[0])
            _x1 = int(self.end[0])
            self.start[0] = _x1
            self.end[0] = _x0

            _y0 = int(self.start[1])
            _y1 = int(self.end[1])
            self.start[1] = _y1
            self.end[1] = _y0

        dx = self.end[0] - self.start[0]
        dy = abs(self.end[1] - self.start[1])
        error = 0
        derr = dy / float(dx)

        ystep = 0
        y = self.start[1]

        if self.start[1] < self.end[1]:
            ystep = 1
        else:
            ystep = -1

        for x in range(self.start[0], self.end[0] + 1):
            if self.steep:
                self.path.append((y, x))
            else:
                self.path.append((x, y))

            error += derr

            if error >= 0.5:
                y += ystep
                error -= 1.0

        print (start)
        print (end)
        print()
        print (self.start)
        print (self.end)

    def swap(self, n1, n2):
        return [n2, n1]

def get_line(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end

    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print (points1)
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print (points2)
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points


main()