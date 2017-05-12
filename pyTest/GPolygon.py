#!/usr/bin/env python
""" generated source for module GPolygon """
from __future__ import print_function
from functools import wraps
from threading import RLock
from GObject import *
from GFillable import *
from GScalable import *
from unresolved import *
from unresolved import *
def lock_for_object(obj, locks={}):
    return locks.setdefault(id(obj), RLock())

def synchronized(call):
    assert call.__code__.co_varnames[0] in ['self', 'cls']
    @wraps(call)
    def inner(*args, **kwds):
        with lock_for_object(args[0]):
            return call(*args, **kwds)
    return inner

# 
#  * @(#)GPolygon.java   1.99.1 08/12/08
#  
#  ************************************************************************
#  * Copyright (c) 2008 by the Association for Computing Machinery        *
#  *                                                                      *
#  * The Java Task Force seeks to impose few restrictions on the use of   *
#  * these packages so that users have as much freedom as possible to     *
#  * use this software in constructive ways and can make the benefits of  *
#  * that work available to others.  In view of the legal complexities    *
#  * of software development, however, it is essential for the ACM to     *
#  * maintain its copyright to guard against attempts by others to        *
#  * claim ownership rights.  The full text of the JTF Software License   *
#  * is available at the following URL:                                   *
#  *                                                                      *
#  *          http://www.acm.org/jtf/jtf-software-license.pdf             *
#  *                                                                      *
#  ************************************************************************
#  REVISION HISTORY
# 
#  -- V2.0 --
#  Code cleanup 28-May-07 (ESR)
#    1. Added generic type tags.
# 
#  Bug fix 6-Jul-07 (ESR, JTFBug 2007-010, reported by Steve Wolfman)
#    1. Fixed bug in recenter code.
# 
#  Feature enhancement 26-May-08 (ESR)
#    1. Added support for serialization.
# package: acm.graphics
#  Class: GPolygon 
# 
#  * The <code>GPolygon</code> class is a graphical object whose appearance consists
#  * of a polygon.
#  
class GPolygon(GObject, GFillable, GScalable):
    """ generated source for class GPolygon """
    #  Constructor: GPolygon() 
    # 
    #  * Constructs a new empty polygon at the origin.
    #  *
    #  * @usage GPolygon gpoly = new GPolygon();
    #  
    #@overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(GPolygon, self).__init__()
        vertices = VertexList()
        clear()

    #  Constructor: GPolygon(x, y) 
    # 
    #  * Constructs a new empty polygon at (<code>x</code>, <code>y</code>).
    #  *
    #  * @usage GPolygon gpoly = new GPolygon(x, y);
    #  * @param x The x-coordinate of the origin of the polygon
    #  * @param y The y-coordinate of the origin of the polygon
    #  
    # @__init__.register(object, float, float)
    def __init___0(self, x, y):
        """ generated source for method __init___0 """
        super(GPolygon, self).__init__()
        self.__init__()
        setLocation(x, y)

    #  Constructor: GPolygon(points) 
    # 
    #  * Constructs a new polygon from the specified array of <code>GPoint</code>
    #  * objects.  The polygon is automatically marked as complete.
    #  *
    #  * @usage GPolygon gpoly = new GPolygon(points);
    #  * @param points An array of <code>GPoint</code> objects specifying the vertices
    #  
    # @__init__.register(object, GPoint)
    def __init___1(self, points):
        """ generated source for method __init___1 """
        super(GPolygon, self).__init__()
        self.__init__()
        vertices.add(points)
        markAsComplete()

    #  Method: addVertex(x, y) 
    # 
    #  * Adds a vertex at (<code>x</code>, <code>y</code>) relative to the polygon origin.
    #  *
    #  * @usage gpoly.addVertex(x, y);
    #  * @param x The x-coordinate of the vertex relative to the polygon origin
    #  * @param y The y-coordinate of the vertex relative to the polygon origin
    #  
    def addVertex(self, x, y):
        """ generated source for method addVertex """
        if complete:
            raise ErrorException("You can't add vertices to a GPolygon that has been " + "marked as complete.")
        vertices.addVertex(x, y)

    #  Method: addEdge(dx, dy) 
    # 
    #  * Adds an edge to the polygon whose components are given by the displacements
    #  * <code>dx</code> and <code>dy</code> from the last vertex.
    #  *
    #  * @usage gpoly.addEdge(dx, dy);
    #  * @param dx The x displacement through which the edge moves
    #  * @param dy The y displacement through which the edge moves
    #  
    def addEdge(self, dx, dy):
        """ generated source for method addEdge """
        if complete:
            raise ErrorException("You can't add edges to a GPolygon that has been " + "marked as complete.")
        vertices.addEdge(dx, dy)

    #  Method: addPolarEdge(r, theta) 
    # 
    #  * Adds an edge to the polygon specified in polar coordinates.  The length of the
    #  * edge is given by <code>r</code>, and the edge extends in direction <code>theta</code>,
    #  * measured in degrees counterclockwise from the +x axis.
    #  *
    #  * @usage gpoly.addPolarEdge(r, theta);
    #  * @param r The length of the edge
    #  * @param theta The angle at which the edge extends measured in degrees
    #  
    def addPolarEdge(self, r, theta):
        """ generated source for method addPolarEdge """
        if complete:
            raise ErrorException("You can't add edges to a GPolygon that has been " + "marked as complete.")
        vertices.addEdge(r * GcosDegrees(theta), -r * GsinDegrees(theta))

    #  Method: addArc(arcWidth, arcHeight, start, sweep) 
    # 
    #  * Adds a series of edges to the polygon that simulates the arc specified by
    #  * the parameters.  The <i>x</i> and <i>y</i> parameters for the arc bounding
    #  * box are computed implicitly by figuring out what values would place the
    #  * current vertex at the starting position.
    #  *
    #  * @usage gpoly.addArc(arcWidth, arcHeight, start, sweep);
    #  * @param arcWidth The width of the oval from which the arc is taken
    #  * @param arcHeight The height of the oval from which the arc is taken
    #  * @param start The angle at which the arc begins
    #  * @param sweep The extent of the arc
    #  
    def addArc(self, arcWidth, arcHeight, start, sweep):
        """ generated source for method addArc """
        if complete:
            raise ErrorException("You can't add edges to a GPolygon that has been " + "marked as complete.")
        vertices.addArc(arcWidth, arcHeight, start, sweep)

    #  Method: getCurrentPoint() 
    # 
    #  * Returns the coordinates of the last vertex added to the polygon, or <code>null</code>
    #  * if the polygon is empty.
    #  *
    #  * @usage GPoint vertex = gpoly.getCurrentPoint();
    #  * @return The last vertex added to the polygon, or <code>null</code> if empty
    #  
    def getCurrentPoint(self):
        """ generated source for method getCurrentPoint """
        return vertices.getCurrentPoint()

    #  Method: scale(sx, sy) 
    # 
    #  * Scales the polygon by the scale factors <code>sx</code> and <code>sy</code>.
    #  *
    #  * @usage gpoly.scale(sx, sy);
    #  * @param sx The factor used to scale all coordinates in the x direction
    #  * @param sy The factor used to scale all coordinates in the y direction
    #  
    #@overloaded
    def scale(self, sx, sy):
        """ generated source for method scale """
        xScale *= sx
        yScale *= sy
        repaint()

    #  Method: scale(sf) 
    # 
    #  * Scales the object on the screen by the scale factor <code>sf</code>, which applies
    #  * in both dimensions.
    #  *
    #  * @usage gobj.scale(sf);
    #  * @param sf The factor used to scale all coordinates in both dimensions
    #  
    # @scale.register(object, float)
    def scale_0(self, sf):
        """ generated source for method scale_0 """
        self.scale(sf, sf)

    #  Method: rotate(theta) 
    # 
    #  * Rotates the polygon around its origin by the angle theta, measured in degrees.
    #  *
    #  * @usage gpoly.rotate(theta);
    #  * @param theta The angle of rotation in degrees counterclockwise
    #  
    def rotate(self, theta):
        """ generated source for method rotate """
        rotation += theta
        repaint()

    #  Method: setFilled(fill) 
    # 
    #  * Sets whether this object is filled.
    #  *
    #  * @usage gobj.setFilled(fill);
    #  * @param fill <code>true</code> if the object should be filled, <code>false</code> for an outline
    #  
    def setFilled(self, fill):
        """ generated source for method setFilled """
        isFilled = fill
        repaint()

    #  Method: isFilled() 
    # 
    #  * Returns whether this object is filled.
    #  *
    #  * @usage if (gobj.isFilled()) . . .
    #  * @return The color used to display the object
    #  
    def isFilled(self):
        """ generated source for method isFilled """
        return self.isFilled

    #  Method: setFillColor(color) 
    # 
    #  * Sets the color used to display the filled region of this object.
    #  *
    #  * @usage gobj.setFillColor(color);
    #  * @param color The color used to display the filled region of this object
    #  
    def setFillColor(self, color):
        """ generated source for method setFillColor """
        fillColor = color
        repaint()

    #  Method: getFillColor() 
    # 
    #  * Returns the color used to display the filled region of this object.  If
    #  * none has been set, <code>getFillColor</code> returns the color of the
    #  * object.
    #  *
    #  * @usage Color color = gobj.getFillColor();
    #  * @return The color used to display the filled region of this object
    #  
    def getFillColor(self):
        """ generated source for method getFillColor """
        return getColor() if (fillColor == None) else fillColor

    #  Method: getBounds() 
    # 
    #  * Returns the bounding box of this object, which is defined to be the
    #  * smallest rectangle that covers everything drawn by the figure.
    #  *
    #  * @usage GRectangle bounds = gpoly.getBounds();
    #  * @return The bounding box for this object
    #  
    def getBounds(self):
        """ generated source for method getBounds """
        return vertices.getBounds(getX(), getY(), xScale, yScale, rotation)

    #  Method: contains(x, y) 
    # 
    #  * Checks to see whether a point is inside the object.
    #  *
    #  * @usage if (gpoly.contains(x, y)) . . .
    #  * @param x The x-coordinate of the point being tested
    #  * @param y The y-coordinate of the point being tested
    #  * @return <code>true</code> if the point (<code>x</code>,&nbsp;<code>y</code>) is inside
    #  *         the object, and <code>false</code> otherwise
    #  
    def contains(self, x, y):
        """ generated source for method contains """
        return vertices.contains((x - getX()) / xScale, (y - getY()) / yScale)

    #  Method: paint(g) 
    # 
    #  * Implements the <code>paint</code> operation for this graphical object.  This method
    #  * is not called directly by clients.
    #  * @noshow
    #  
    def paint(self, g):
        """ generated source for method paint """
        if len(vertices) == 0:
            return
        p = getPolygon()
        if self.isFilled():
            g.setColor(self.getFillColor())
            g.fillPolygon(p.xpoints, p.ypoints, p.npoints)
            g.setColor(getColor())
        g.drawPolygon(p.xpoints, p.ypoints, p.npoints)

    #  Method: recenter() 
    # 
    #  * Recalculates the vertices of the polygon so that they are positioned
    #  * relative to the geometric center of the object.  This method allows
    #  * clients to take a polygon drawn using mouse clicks on the screen and
    #  * then to reformulate it so that it can be displayed relative to its center.
    #  *
    #  * @usage gpoly.recenter();
    #  
    def recenter(self):
        """ generated source for method recenter """
        vertices.recenter()
        cacheValid = False

    #  Method: clone() 
    # 
    #  * Overrides <code>clone</code> in <code>Object</code> to make sure
    #  * that the vertex list is copied rather than shared.
    #  * @noshow
    #  
    def clone(self):
        """ generated source for method clone """
        try:
            clone = super(GPolygon, self).clone()
            self.clone.vertices = VertexList(self.clone.vertices)
            return self.clone
        except Exception as CloneNotSupportedException:
            raise ErrorException("Impossible exception")

    #  Inherited method: setLocation(x, y) 
    # 
    #  * @inherited GObject#void setLocation(double x, double y)
    #  * Sets the location of this object to the point (<code>x</code>, <code>y</code>).
    #  
    #  Inherited method: setLocation(pt) 
    # 
    #  * @inherited GObject#void setLocation(GPoint pt)
    #  * Sets the location of this object to the specified point.
    #  
    #  Inherited method: getLocation() 
    # 
    #  * @inherited GObject#GPoint getLocation()
    #  * Returns the location of this object as a <code>GPoint</code>.
    #  
    #  Inherited method: getX() 
    # 
    #  * @inherited GObject#double getX()
    #  * Returns the x-coordinate of the object.
    #  
    #  Inherited method: getY() 
    # 
    #  * @inherited GObject#double getY()
    #  * Returns the y-coordinate of the object.
    #  
    #  Inherited method: move(dx, dy) 
    # 
    #  * @inherited GObject#void move(double dx, double dy)
    #  * Moves the object on the screen using the displacements <code>dx</code> and <code>dy</code>.
    #  
    #  Inherited method: movePolar(r, theta) 
    # 
    #  * @inherited GObject#void movePolar(double r, double theta)
    #  * Moves the object using displacements given in polar coordinates.
    #  
    #  Inherited method: getSize() 
    # 
    #  * @inherited GObject#GDimension getSize()
    #  * Returns the size of the bounding box for this object.
    #  
    #  Inherited method: getWidth() 
    # 
    #  * @inherited GObject#double getWidth()
    #  * Returns the width of this object, which is defined to be
    #  * the width of the bounding box.
    #  
    #  Inherited method: getHeight() 
    # 
    #  * @inherited GObject#double getHeight()
    #  * Returns the height of this object, which is defined to be
    #  * the height of the bounding box.
    #  
    #  Inherited method: contains(pt) 
    # 
    #  * @inherited GObject#boolean contains(GPoint pt)
    #  * Checks to see whether a point is inside the object.
    #  
    #  Inherited method: sendToFront() 
    # 
    #  * @inherited GObject#void sendToFront()
    #  * Moves this object to the front of the display in the <i>z</i> dimension.
    #  
    #  Inherited method: sendToBack() 
    # 
    #  * @inherited GObject#void sendToBack()
    #  * Moves this object to the back of the display in the <i>z</i> dimension.
    #  
    #  Inherited method: sendForward() 
    # 
    #  * @inherited GObject#void sendForward()
    #  * Moves this object one step toward the front in the <i>z</i> dimension.
    #  
    #  Inherited method: sendBackward() 
    # 
    #  * @inherited GObject#void sendBackward()
    #  * Moves this object one step toward the back in the <i>z</i> dimension.
    #  
    #  Inherited method: setColor(color) 
    # 
    #  * @inherited GObject#void setColor(Color color)
    #  * Sets the color used to display this object.
    #  
    #  Inherited method: getColor() 
    # 
    #  * @inherited GObject#Color getColor()
    #  * Returns the color used to display this object.
    #  
    #  Inherited method: setVisible(visible) 
    # 
    #  * @inherited GObject#void setVisible(boolean visible)
    #  * Sets whether this object is visible.
    #  
    #  Inherited method: isVisible() 
    # 
    #  * @inherited GObject#boolean isVisible()
    #  * Checks to see whether this object is visible.
    #  
    #  Inherited method: addMouseListener(listener) 
    # 
    #  * @inherited GObject#void addMouseListener(MouseListener listener)
    #  * Adds a mouse listener to this graphical object.
    #  
    #  Inherited method: removeMouseListener(listener) 
    # 
    #  * @inherited GObject#void removeMouseListener(MouseListener listener)
    #  * Removes a mouse listener from this graphical object.
    #  
    #  Inherited method: addMouseMotionListener(listener) 
    # 
    #  * @inherited GObject#void addMouseMotionListener(MouseMotionListener listener)
    #  * Adds a mouse motion listener to this graphical object.
    #  
    #  Inherited method: removeMouseMotionListener(listener) 
    # 
    #  * @inherited GObject#void removeMouseMotionListener(MouseMotionListener listener)
    #  * Removes a mouse motion listener from this graphical object.
    #  
    #  Protected method: repaint() 
    # 
    #  * Overrides <code>repaint</code> in <code>GObject</code> to invalidate the
    #  * cached polygon.
    #  * @noshow
    #  
    def repaint(self):
        """ generated source for method repaint """
        cacheValid = False
        super(GPolygon, self).repaint()

    #  Protected method: getPolygon() 
    # 
    #  * Returns an AWT <code>Polygon</code> whose points are as close as possible
    #  * to the ones in this <code>GPolygon</code>.
    #  *
    #  * @usage Polygon p = gpoly.getPolygon();
    #  * @return An AWT polygon corresponding to this object
    #  
    def getPolygon(self):
        """ generated source for method getPolygon """
        if cacheValid:
            return poly
        poly = vertices.createPolygon(getX(), getY(), xScale, yScale, rotation)
        cacheValid = True
        return poly

    #  Protected method: markAsComplete() 
    # 
    #  * Calling this method makes it illegal to add or remove vertices from the
    #  * polygon.  Subclasses can invoke this method to protect the integrity of
    #  * the structure from changes by the client.
    #  
    def markAsComplete(self):
        """ generated source for method markAsComplete """
        complete = True

    #  Protected method: clear() 
    # 
    #  * Calling this method deletes all vertices from the polygon and resets the
    #  * scale and rotation factors to the their default values.  Subclasses can
    #  * use this method to reconstruct a polygon.
    #  
    def clear(self):
        """ generated source for method clear """
        if complete:
            raise ErrorException("You can't clear a GPolygon that has been " + "marked as complete.")
        vertices.clear()
        rotation = 0
        xScale = 1.0
        yScale = 1.0
        cacheValid = False

    #  Private instance variables 
    xScale = float()
    yScale = float()
    rotation = float()
    vertices = None
    cacheValid = bool()
    complete = bool()
    poly = None
    isFilled = bool()
    fillColor = None

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

#  Package class: VertexList 
# 
#  * The <code>VertexList<code> class represents a list of vertices.
#  
class VertexList(Serializable):
    """ generated source for class VertexList """
    #  Constructor: new VertexList() 
    # 
    #  * Creates a new <code>VertexList</code> with no elements.
    #  
    # @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(VertexList, self).__init__()
        vertices = ArrayList()
        cx = 0
        cy = 0

    #  Constructor: new VertexList(oldList) 
    # 
    #  * Creates a new <code>VertexList</code> that is a clone of the old one.
    #  
    # @__init__.register(object, VertexList)
    def __init___(self, oldList):
        """ generated source for method __init___0 """
        super(VertexList, self).__init__()
        self.__init__()
        i = 0
        while i < len(oldList.vertices):
            vertices.add(oldList.vertices.get(i))
            i += 1

    #  Method: addVertex(x, y) 
    # 
    #  * Adds the specified vertex to the end of the list.
    #  
    # @synchronized
    def addVertex(self, x, y):
        """ generated source for method addVertex """
        cx = x
        cy = y
        vertices.add(GPoint(cx, cy))

    #  Method: addEdge(dx, dy) 
    # 
    #  * Adds the specified edge to the end of the list.
    #  
    #@synchronized
    def addEdge(self, dx, dy):
        """ generated source for method addEdge """
        cx += dx
        cy += dy
        vertices.add(GPoint(cx, cy))

    #  Method: addArc(arcWidth, arcHeight, start, sweep) 
    # 
    #  * Adds a series of edges to the polygon that simulates the arc specified by
    #  * the parameters.  The <i>x</i> and <i>y</i> parameters for the arc bounding
    #  * box are computed implicitly by figuring out what values would place the
    #  * current vertex at the starting position.
    #  
    def addArc(self, arcWidth, arcHeight, start, sweep):
        """ generated source for method addArc """
        aspectRatio = arcHeight / arcWidth
        rx = arcWidth / 2.0
        ry = arcHeight / 2.0
        x0 = cx - rx * GcosDegrees(start)
        y0 = cy + ry * GsinDegrees(start)
        if sweep > 359.99:
            sweep = 360
        if sweep < -359.99:
            sweep = -360
        dt = atan2(1, max(arcWidth, arcHeight))
        nSteps = int((GtoRadians(abs(sweep)) / dt))
        dt = GtoRadians(sweep) / nSteps
        theta = GtoRadians(start)
        i = 0
        while i < nSteps:
            theta += dt
            px = x0 + rx * cos(theta)
            py = y0 - rx * sin(theta) * aspectRatio
            self.addVertex(px, py)
            i += 1

    #  Method: add(array) 
    # 
    #  * Adds copies of the points to the end of the vertex list.
    #  
    # @synchronized
    def add(self, array):
        """ generated source for method add """
        i = 0
        while len(array):
            vertices.add(GPoint(array[i].getX(), array[i].getY()))
            i += 1

   #synchronized
    def remove(self, vertex):
        """ generated source for method remove """
        vertices.remove(vertex)

    #@synchronized
    def clear(self):
        """ generated source for method clear """
        vertices.clear()

    def size(self):
        """ generated source for method size """
        return len(vertices)

    def getCurrentPoint(self):
        """ generated source for method getCurrentPoint """
        return None if (len(vertices) == 0) else GPoint(cx, cy)

    #@synchronized
    def getBounds(self, x0, y0, xScale, yScale, rotation):
        """ generated source for method getBounds """
        nPoints = len(vertices)
        if nPoints == 0:
            return GRectangle()
        xMin = 0
        xMax = 0
        yMin = 0
        yMax = 0
        sinTheta = GsinDegrees(rotation)
        cosTheta = GcosDegrees(rotation)
        first = True
        i = 0
        while i < len(vertices):
            vertex = vertices.get(i)
            x = x0 + xScale * (cosTheta * vertex.getX() + sinTheta * vertex.getY())
            y = y0 + yScale * (cosTheta * vertex.getY() - sinTheta * vertex.getX())
            if first:
                xMin = x
                xMax = x
                yMin = y
                yMax = y
                first = False
            else:
                xMin = min(xMin, x)
                xMax = max(xMax, x)
                yMin = min(yMin, y)
                yMax = max(yMax, y)
            i += 1
        return GRectangle(xMin, yMin, xMax - xMin, yMax - yMin)

    #@synchronized
    def contains(self, x, y):
        """ generated source for method contains """
        nPoints = len(vertices)
        isContained = False
        i = 0
        while i < nPoints:
            v1 = vertices.get(i)
            v2 = vertices.get((i + 1) % nPoints)
            if ((v1.getY() < y) and (v2.getY() >= y)) or ((v2.getY() < y) and (v1.getY() >= y)):
                if v1.getX() + (y - v1.getY()) / (v2.getY() - v1.getY()) * (v2.getX() - v1.getX()) < x:
                    isContained = not isContained
            i += 1
        return isContained

    #@synchronized
    def createPolygon(self, x0, y0, xScale, yScale, rotation):
        """ generated source for method createPolygon """
        sinTheta = GsinDegrees(rotation)
        cosTheta = GcosDegrees(rotation)
        poly = Polygon()
        i = 0
        while i < len(vertices):
            vertex = vertices.get(i)
            x = x0 + xScale * (cosTheta * vertex.getX() + sinTheta * vertex.getY())
            y = y0 + yScale * (cosTheta * vertex.getY() - sinTheta * vertex.getX())
            poly.addPoint(Ground(x), Ground(y))
            i += 1
        return poly

    def recenter(self):
        """ generated source for method recenter """
        xMin = 0
        xMax = 0
        yMin = 0
        yMax = 0
        first = True
        i = 0
        while i < len(vertices):
            vertex = vertices.get(i)
            if first:
                xMin = vertex.getX()
                xMax = vertex.getX()
                yMin = vertex.getY()
                yMax = vertex.getY()
                first = False
            else:
                xMin = min(xMin, vertex.getX())
                xMax = max(xMax, vertex.getX())
                yMin = min(yMin, vertex.getY())
                yMax = max(yMax, vertex.getY())
            i += 1
        xc = (xMin + xMax) / 2
        yc = (yMin + yMax) / 2
        i = 0
        while i < len(vertices):
            vertex = vertices.get(i)
            vertex.translate(-xc, -yc)
            i += 1

    vertices = None
    cx = float()
    cy = float()

