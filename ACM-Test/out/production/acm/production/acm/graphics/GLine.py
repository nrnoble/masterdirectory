#!/usr/bin/env python
""" generated source for module GLine """
from __future__ import print_function
# 
#  * @(#)GLine.java   1.1 1 08/08/01
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
#  Code cleanup 30-Sep-06 (ESR)
#    1. Removed vestigial inherited methods setFilled and isFilled.
# 
#  Feature enhancement 26-May-08 (ESR)
#    1. Added support for serialization.
# package: acm.graphics
#  Class: GLine 
# 
#  * The <code>GLine</code> class is a graphical object whose appearance consists
#  * of a line segment.
#  
class GLine(GObject, GScalable):
    """ generated source for class GLine """
    #  Field: LINE_TOLERANCE 
    # 
    #  * This constant defines how close (measured in pixel units) a point has
    #  * to be to a line before that point is considered to be "contained" within
    #  * the line.
    #  
    LINE_TOLERANCE = 1.5

    #  Constructor: GLine(x0, y0, x1, y1) 
    # 
    #  * Constructs a line segment from its endpoints.  The point
    #  * (<code>x0</code>,&nbsp;<code>y0</code>) defines the start of the
    #  * line and the point (<code>x1</code>,&nbsp;<code>y1</code>) defines
    #  * the end.
    #  *
    #  * @usage GLine gline = new GLine(x0, y0, x1, y1);
    #  * @param x0 The x-coordinate of the start of the line
    #  * @param y0 The y-coordinate of the start of the line
    #  * @param x1 The x-coordinate of the end of the line
    #  * @param y1 The y-coordinate of the end of the line
    #  
    def __init__(self, x0, y0, x1, y1):
        """ generated source for method __init__ """
        super(GLine, self).__init__()
        setLocation(x0, y0)
        dx = x1 - x0
        dy = y1 - y0

    #  Method: paint(g) 
    # 
    #  * Implements the <code>paint</code> operation for this graphical object.  This method
    #  * is not called directly by clients.
    #  * @noshow
    #  
    def paint(self, g):
        """ generated source for method paint """
        x = getX()
        y = getY()
        g.drawLine(Ground(x), Ground(y), Ground(x + dx), Ground(y + dy))

    #  Method: getBounds() 
    # 
    #  * Returns the bounding box for this object.
    #  *
    #  * @usage GRectangle bounds = gline.getBounds();
    #  * @return The bounding box for this object
    #  
    def getBounds(self):
        """ generated source for method getBounds """
        x = min(getX(), getX() + dx)
        y = min(getY(), getY() + dy)
        return GRectangle(x, y, abs(dx), abs(dy))

    #  Method: setStartPoint(x, y) 
    # 
    #  * Sets the initial point in the line to (<code>x</code>,&nbsp;<code>y</code>),
    #  * leaving the end point unchanged.  This method is therefore different from
    #  * <a href="#setLocation(double, double)"><code>setLocation</code></a>, which
    #  * moves both components of the line segment.
    #  *
    #  * @usage gline.setStartPoint(x, y);
    #  * @param x The new x-coordinate of the origin
    #  * @param y The new y-coordinate of the origin
    #  
    def setStartPoint(self, x, y):
        """ generated source for method setStartPoint """
        dx += getX() - x
        dy += getY() - y
        setLocation(x, y)

    #  Method: getStartPoint() 
    # 
    #  * Returns the coordinates of the initial point in the line.  This method is
    #  * identical to <a href="#getLocation()"><code>getLocation</code></a> and exists only to
    #  * provide symmetry with <a href="#setStartPoint(double, double)"><code>setStartPoint</code></a>.
    #  *
    #  * @usage GPoint pt = gline.getStartPoint();
    #  * @return The coordinates of the origin of the line
    #  
    def getStartPoint(self):
        """ generated source for method getStartPoint """
        return getLocation()

    #  Method: setEndPoint(x, y) 
    # 
    #  * Sets the end point of the line to the point (<code>x</code>,&nbsp;<code>y</code>).
    #  * The origin of the line remains unchanged.
    #  *
    #  * @usage gline.setEndPoint(x, y);
    #  * @param x The new x-coordinate of the end point
    #  * @param y The new y-coordinate of the end point
    #  
    def setEndPoint(self, x, y):
        """ generated source for method setEndPoint """
        dx = x - getX()
        dy = y - getY()
        repaint()

    #  Method: getEndPoint() 
    # 
    #  * Returns the end point of the line as a <code>GPoint</code> object.
    #  *
    #  * @usage GPoint pt = gline.getEndPoint();
    #  * @return The coordinates of the end point of the line
    #  
    def getEndPoint(self):
        """ generated source for method getEndPoint """
        return GPoint(getX() + dx, getY() + dy)

    #  Method: scale(sx, sy) 
    # 
    #  * Scales the line on the screen by the scale factors <code>sx</code> and <code>sy</code>.
    #  * This method changes only the end point of the line, leaving the start of the line fixed.
    #  *
    #  * @usage gline.scale(sx, sy);
    #  * @param sx The factor used to scale all coordinates in the x direction
    #  * @param sy The factor used to scale all coordinates in the y direction
    #  
    @overloaded
    def scale(self, sx, sy):
        """ generated source for method scale """
        dx *= sx
        dy *= sy
        repaint()

    #  Method: scale(sf) 
    # 
    #  * Scales the object on the screen by the scale factor <code>sf</code>, which applies
    #  * in both dimensions.
    #  *
    #  * @usage gobj.scale(sf);
    #  * @param sf The factor used to scale all coordinates in both dimensions
    #  
    @scale.register(object, float)
    def scale_0(self, sf):
        """ generated source for method scale_0 """
        self.scale(sf, sf)

    #  Method: contains(x, y) 
    # 
    #  * Checks to see whether a point is inside the object.  For the <code>GLine</code>
    #  * class, containment is defined to mean that the point is within
    #  * <a href="#LINE_TOLERANCE"><code>LINE_TOLERANCE</code></a> pixels of the
    #  * line.
    #  *
    #  * @usage if (gline.contains(x, y)) . . .
    #  * @param x The x-coordinate of the point being tested
    #  * @param y The y-coordinate of the point being tested
    #  * @return <code>true</code> if the point (<code>x</code>,&nbsp;<code>y</code>) is inside
    #  
    def contains(self, x, y):
        """ generated source for method contains """
        x0 = getX()
        y0 = getY()
        x1 = x0 + dx
        y1 = y0 + dy
        tSquared = self.LINE_TOLERANCE * self.LINE_TOLERANCE
        if distanceSquared(x, y, x0, y0) < tSquared:
            return True
        if distanceSquared(x, y, x1, y1) < tSquared:
            return True
        if x < min(x0, x1) - self.LINE_TOLERANCE:
            return False
        if x > max(x0, x1) + self.LINE_TOLERANCE:
            return False
        if y < min(y0, y1) - self.LINE_TOLERANCE:
            return False
        if y > max(y0, y1) + self.LINE_TOLERANCE:
            return False
        if float(x0) - float(x1) == 0 and float(y0) - float(y1) == 0:
            return False
        u = ((x - x0) * (x1 - x0) + (y - y0) * (y1 - y0)) / distanceSquared(x0, y0, x1, y1)
        return distanceSquared(x, y, x0 + u * (x1 - x0), y0 + u * (y1 - y0)) < tSquared

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
    #  Protected method: paramString() 
    # 
    #  * Returns a string indicating the parameters of this object.
    #  * @noshow
    #  
    def paramString(self):
        """ generated source for method paramString """
        tail = super(GLine, self).paramString()
        tail = tail.substring(tail.indexOf(')') + 1)
        pt = self.getStartPoint()
        param = "start=(" + pt.getX() + ", " + pt.getY() + ")"
        pt = self.getEndPoint()
        param += ", end=(" + pt.getX() + ", " + pt.getY() + ")"
        return param + tail

    #  Private method: distanceSquared(x0, y0, x1, y1) 
    # 
    #  * Returns the square of the distance between (<code>x0</code>,&nbsp;<code>y0</code>)
    #  * and (<code>x1</code>,&nbsp;<code>y1</code>).
    #  
    def distanceSquared(self, x0, y0, x1, y1):
        """ generated source for method distanceSquared """
        return (x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0)

    #  Private instance variables 
    dx = float()
    dy = float()

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

