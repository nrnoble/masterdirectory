#!/usr/bin/env python
""" generated source for module GArc """
from __future__ import print_function
from functools import wraps
from threading import RLock

def lock_for_object(obj, locks={}):
    return locks.setdefault(id(obj), RLock())

def synchronized(call):
    assert call.__code__.co_varnames[0] in ['self', 'cls']
    @wraps(call)
    def inner(*args, **kwds):
        with lock_for_object(args[0]):
            return call(*args, **kwds)
    return inner

#!/usr/bin/env python
""" generated source for module GArc """
from __future__ import print_function
from functools import wraps
from threading import RLock

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
#  * @(#)GArc.java   1.99.1 08/12/08
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
#  Bug fix 26-Apr-07 (ESR, JTFBug 2007-005, reported by Leland Beck)
#    1. Fixed problems with cross-file references to ArcRenderer.
# 
#  Bug fix 28-May-07 (ESR, JTFBug 2007-009)
#    1. Fixed synchronization problem in ArcRenderer.
# 
#  Code cleanup 28-May-07 (ESR)
#    1. Added generic type tags.
# 
#  Feature enhancement 26-May-08 (ESR)
#    1. Added support for serialization.
#    2. Revised bounding box calculation to conform to Java standard.
# package: acm.graphics
#  Class: GArc 
# 
#  * The <code>GArc</code> class is a graphical object whose appearance consists
#  * of an arc.  If unfilled, the arc is simply a portion of the circumference of
#  * an ellipse; if filled, the arc is a pie-shaped wedge connected to the center
#  * of the figure.
#  
class GArc(GObject, GFillable, GScalable, GObject, GFillable, GScalable):
    """ generated source for class GArc """
    """ generated source for class GArc """
    #  Field: ARC_TOLERANCE 
    # 
    #  * This constant defines how close (measured in pixel units) a point has
    #  * to be to an arc before that point is considered to be "contained" within
    #  * the arc.
    #  
    ARC_TOLERANCE = 2.5

    #  BUG?: THIS SEEMS TO REQUIRE HITTING THE ARC EXACTLY EVEN WITH 2.5
    #  Constructor: GArc(width, height, start, sweep) 
    # 
    #  * Creates a new <code>GArc</code> object consisting of an elliptical arc
    #  * located at the point (0,&nbsp;0).  For complete descriptions of the
    #  * other parameters, see the entry for the
    #  * <a href="#GArc(double, double, double, double, double, double)"><code>GArc</code></a>
    #  * constructor that includes explicit <code>x</code> and <code>y</code>
    #  * parameters.
    #  *
    #  * @usage GArc garc = new GArc(width, height, start, sweep);
    #  * @param width The width of the rectangle in which the arc is inscribed
    #  * @param height The height of the rectangle in which the arc is inscribed
    #  * @param start The angle at which the arc begins measured in degrees counterclockwise
    #  *              from the +x axis
    #  * @param sweep The extent of the arc, measured in degrees counterclockwise
    #  
    @overloaded
    def __init__(self, width, height, start, sweep, self, width, height, start, sweep):
        """ generated source for method __init__ """
        """ generated source for method __init__ """
        super(GArc, self).__init__()
        self.__init__(0, 0, width, height, start, sweep)

    #  Constructor: GArc(x, y, width, height, start, sweep) 
    # 
    #  * Creates a new <code>GArc</code> object consisting of an elliptical arc
    #  * inscribed in a rectangle located at the point (<code>x</code>,&nbsp;<code>y</code>)
    #  * with the specified width and height.  The <code>start</code> parameter indicates
    #  * the angle at which the arc begins and is measured in degrees counterclockwise
    #  * from the +x axis.  Thus, a <code>start</code> angle of 0 indicates an arc
    #  * that begins along the line running eastward from the center (the 3:00
    #  * o&#146;clock position), a <code>start</code> angle of 135
    #  * begins along the line running northwest, and a <code>start</code>
    #  * angle of -90 begins along the line running south (the 6:00
    #  * o&#146;clock position).  The <code>sweep</code> parameter indicates
    #  * the extent of the arc and is also measured in degrees counterclockwise.
    #  * A <code>sweep</code> angle of 90 defines a quarter circle extending
    #  * counterclockwise from the <code>start</code> angle, and a
    #  * <code>sweep</code> angle of -180 defines a semicircle extending
    #  * clockwise.
    #  *
    #  * @usage GArc garc = new GArc(x, y, width, height, start, sweep);
    #  * @param x The x-coordinate for the rectangle in which the arc is inscribed
    #  * @param y The y-coordinate for the rectangle in which the arc is inscribed
    #  * @param width The width of the rectangle in which the arc is inscribed
    #  * @param height The height of the rectangle in which the arc is inscribed
    #  * @param start The angle at which the arc begins measured in degrees counterclockwise
    #  *              from the +x axis
    #  * @param sweep The extent of the arc, measured in degrees counterclockwise
    #  
    @__init__.register(object, float, float, float, float, float, float)
    @__init__.register(object, float, float, float, float, float, float)
    def __init___0(self, x, y, width, height, start, sweep, self, x, y, width, height, start, sweep):
        """ generated source for method __init___0 """
        """ generated source for method __init___0 """
        super(GArc, self).__init__()
        frameWidth = width
        frameHeight = height
        arcStart = start
        arcSweep = sweep
        setLocation(x, y)
        renderer = ArcRenderer(self)

    #  Method: setStartAngle(start) 
    # 
    #  * Sets the starting angle for this <code>GArc</code> object.
    #  *
    #  * @usage garc.setStartAngle(start);
    #  * @param start The new starting angle
    #  
    def setStartAngle(self, start, self, start):
        """ generated source for method setStartAngle """
        """ generated source for method setStartAngle """
        arcStart = start
        repaint()

    #  Method: getStartAngle() 
    # 
    #  * Returns the starting angle for this <code>GArc</code> object.
    #  *
    #  * @usage double start = garc.getStartAngle();
    #  * @return The starting angle for this arc
    #  
    def getStartAngle(self, self):
        """ generated source for method getStartAngle """
        """ generated source for method getStartAngle """
        return arcStart

    #  Method: setSweepAngle(sweep) 
    # 
    #  * Sets the sweep angle for this <code>GArc</code> object.
    #  *
    #  * @usage garc.setSweepAngle(sweep);
    #  * @param sweep The new sweep angle
    #  
    def setSweepAngle(self, sweep, self, sweep):
        """ generated source for method setSweepAngle """
        """ generated source for method setSweepAngle """
        arcSweep = sweep
        repaint()

    #  Method: getSweepAngle() 
    # 
    #  * Returns the sweep angle for this <code>GArc</code> object.
    #  *
    #  * @usage double sweep = garc.getSweepAngle();
    #  * @return The sweep angle for this arc
    #  
    def getSweepAngle(self, self):
        """ generated source for method getSweepAngle """
        """ generated source for method getSweepAngle """
        return arcSweep

    #  Method: getStartPoint() 
    # 
    #  * Returns the point at which the arc starts.
    #  *
    #  * @usage GPoint pt = garc.getStartPoint();
    #  * @return The point at which the arc starts
    #  
    def getStartPoint(self, self):
        """ generated source for method getStartPoint """
        """ generated source for method getStartPoint """
        return getArcPoint(arcStart)

    #  Method: getEndPoint() 
    # 
    #  * Returns the point at which the arc ends.
    #  *
    #  * @usage GPoint pt = garc.getEndPoint();
    #  * @return The point at which the arc ends
    #  
    def getEndPoint(self, self):
        """ generated source for method getEndPoint """
        """ generated source for method getEndPoint """
        return getArcPoint(arcStart + arcSweep)

    #  Method: paint(g) 
    # 
    #  * Implements the <code>paint</code> operation for this graphical object.  This method
    #  * is not called directly by clients.
    #  * @noshow
    #  
    def paint(self, g, self, g):
        """ generated source for method paint """
        """ generated source for method paint """
        comp = getComponent()
        if isRenderer or ((isinstance(comp, (GCanvas, ))) and not (comp).getNativeArcFlag()):
            renderer.draw(g)
        else:
            r = getAWTBounds()
            cx = Ground(getX() + frameWidth / 2)
            cy = Ground(getY() + frameHeight / 2)
            iStart = Ground(arcStart)
            iSweep = Ground(arcSweep)
            if isFilled():
                g.setColor(getFillColor())
                g.fillArc(r.x, r.y, r.width, r.height, iStart, iSweep)
                g.setColor(getColor())
                g.drawArc(r.x, r.y, r.width, r.height, iStart, iSweep)
                start = getArcPoint(iStart).toPoint()
                g.drawLine(cx, cy, start.x, start.y)
                end = getArcPoint(iStart + iSweep).toPoint()
                g.drawLine(cx, cy, end.x, end.y)
            else:
                g.drawArc(r.x, r.y, r.width, r.height, iStart, iSweep)

    #  Method: getBounds() 
    # 
    #  * Returns the bounding box of the arc.  Note that this method returns the
    #  * bounds of the visible portion of the arc and will therefore not contain
    #  * the same values as specified in
    #  * <a href="#setFrameRectangle(double, double, double, double)"><code>setFrameRectangle</code></a>.
    #  * To obtain the bounds used to describe the Java arc, use
    #  * <a href="#getFrameRectangle()"><code>getFrameRectangle</code></a>.
    #  *
    #  * @usage GRectangle bounds = garc.getBounds();
    #  * @return The bounding box of this object
    #  
    def getBounds(self, self):
        """ generated source for method getBounds """
        """ generated source for method getBounds """
        rx = frameWidth / 2
        ry = frameHeight / 2
        cx = getX() + rx
        cy = getY() + ry
        p1x = cx + GcosDegrees(arcStart) * rx
        p1y = cy - GsinDegrees(arcStart) * ry
        p2x = cx + GcosDegrees(arcStart + arcSweep) * rx
        p2y = cy - GsinDegrees(arcStart + arcSweep) * ry
        xMin = min(p1x, p2x)
        xMax = max(p1x, p2x)
        yMin = min(p1y, p2y)
        yMax = max(p1y, p2y)
        if containsAngle(0):
            xMax = cx + rx
        if containsAngle(90):
            yMin = cy - ry
        if containsAngle(180):
            xMin = cx - rx
        if containsAngle(270):
            yMax = cy + ry
        if isFilled():
            xMin = min(xMin, cx)
            yMin = min(yMin, cy)
            xMax = max(xMax, cx)
            yMax = max(yMax, cy)
        return GRectangle(xMin, yMin, xMax - xMin, yMax - yMin)

    #  Method: contains(x, y) 
    # 
    #  * Checks to see whether a point is inside the object.  For the <code>GArc</code>
    #  * class, containment depends on whether the arc is filled.  Filled arcs are a
    #  * wedge in which containment can be defined in a natural way; unfilled arcs are
    #  * essentially lines, which means that containment is defined to mean that the
    #  * point is within <a href="#ARC_TOLERANCE"><code>ARC_TOLERANCE</code></a> pixels
    #  * of the arc.
    #  *
    #  * @usage if (garc.contains(x, y)) . . .
    #  * @param x The x-coordinate of the point being tested
    #  * @param y The y-coordinate of the point being tested
    #  * @return <code>true</code> if the point (<code>x</code>,&nbsp;<code>y</code>) is inside
    #  
    def contains(self, x, y, self, x, y):
        """ generated source for method contains """
        """ generated source for method contains """
        rx = frameWidth / 2
        ry = frameHeight / 2
        if rx == 0 or ry == 0:
            return False
        dx = x - (getX() + rx)
        dy = y - (getY() + ry)
        r = (dx * dx) / (rx * rx) + (dy * dy) / (ry * ry)
        if isFilled():
            if r > 1.0:
                return False
        else:
            t = self.ARC_TOLERANCE / ((rx + ry) / 2)
            if abs(1.0 - r) > t:
                return False
        return containsAngle(GtoDegrees(atan2(-dy, dx)))

    #  Method: setFrameRectangle(x, y, width, height) 
    # 
    #  * Changes the arc bounds to the specified values.
    #  *
    #  * @usage garc.setBounds(x, y, width, height);
    #  * @param x The x-coordinate for the rectangle in which the arc is inscribed
    #  * @param y The y-coordinate for the rectangle in which the arc is inscribed
    #  * @param width The width of the rectangle in which the arc is inscribed
    #  * @param height The height of the rectangle in which the arc is inscribed
    #  
    @overloaded
    def setFrameRectangle(self, x, y, width, height, self, x, y, width, height):
        """ generated source for method setFrameRectangle """
        """ generated source for method setFrameRectangle """
        frameWidth = width
        frameHeight = height
        setLocation(x, y)

    #  Method: setFrameRectangle(bounds) 
    # 
    #  * Changes the arc bounds to the values from the specified <code>GRectangle</code>.
    #  *
    #  * @usage garc.setFrameRectangle(bounds);
    #  * @param bounds A <code>GRectangle</code> specifying the new arc bounds
    #  
    @setFrameRectangle.register(object, GRectangle)
    @setFrameRectangle.register(object, GRectangle)
    def setFrameRectangle_0(self, bounds, self, bounds):
        """ generated source for method setFrameRectangle_0 """
        """ generated source for method setFrameRectangle_0 """
        self.setFrameRectangle(bounds.getX(), bounds.getY(), bounds.getWidth(), bounds.getHeight())

    #  Method: getFrameRectangle() 
    # 
    #  * Returns the bounds of the <code>GRectangle</code> in which this arc is inscribed.
    #  * Note that this is usually different from the bounding box returned by
    #  * <a href="#getBounds()"><code>getBounds</code></a>, which returns the bounding
    #  * box in which the displayed portion of the arc is contained.
    #  *
    #  * @usage GRectangle bounds = garc.getFrameRectangle();
    #  * @return The <code>GRectangle</code> in which this arc is inscribed
    #  
    def getFrameRectangle(self, self):
        """ generated source for method getFrameRectangle """
        """ generated source for method getFrameRectangle """
        return GRectangle(getX(), getY(), frameWidth, frameHeight)

    #  Method: scale(sx, sy) 
    # 
    #  * Scales the object on the screen by the scale factors <code>sx</code> and <code>sy</code>.
    #  *
    #  * @usage gobj.scale(sx, sy);
    #  * @param sx The factor used to scale all coordinates in the x direction
    #  * @param sy The factor used to scale all coordinates in the y direction
    #  
    @overloaded
    def scale(self, sx, sy, self, sx, sy):
        """ generated source for method scale """
        """ generated source for method scale """
        frameWidth *= sx
        frameHeight *= sy
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
    @scale.register(object, float)
    def scale_0(self, sf, self, sf):
        """ generated source for method scale_0 """
        """ generated source for method scale_0 """
        self.scale(sf, sf)

    #  Method: setFilled(fill) 
    # 
    #  * Sets whether this object is filled.
    #  *
    #  * @usage garc.setFilled(fill);
    #  * @param fill <code>true</code> if the object should be filled, <code>false</code> for an outline
    #  
    def setFilled(self, fill, self, fill):
        """ generated source for method setFilled """
        """ generated source for method setFilled """
        isFilled = fill
        repaint()

    #  Method: isFilled() 
    # 
    #  * Returns whether this object is filled.
    #  *
    #  * @usage if (garc.isFilled()) . . .
    #  * @return The color used to display the object
    #  
    def isFilled(self, self):
        """ generated source for method isFilled """
        """ generated source for method isFilled """
        return self.isFilled

    #  Method: setFillColor(color) 
    # 
    #  * Sets the color used to display the filled region of this object.
    #  *
    #  * @usage garc.setFillColor(color);
    #  * @param color The color used to display the filled region of this object
    #  
    def setFillColor(self, color, self, color):
        """ generated source for method setFillColor """
        """ generated source for method setFillColor """
        fillColor = color
        repaint()

    #  Method: getFillColor() 
    # 
    #  * Returns the color used to display the filled region of this object.  If
    #  * none has been set, <code>getFillColor</code> returns the color of the
    #  * object.
    #  *
    #  * @usage Color color = garc.getFillColor();
    #  * @return The color used to display the filled region of this object
    #  
    def getFillColor(self, self):
        """ generated source for method getFillColor """
        """ generated source for method getFillColor """
        return getColor() if (fillColor == None) else fillColor

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
    #  Protected method: getAWTBounds() 
    # 
    #  * Returns an AWT <code>Rectangle</code> that specifies the bounds of this object.
    #  *
    #  * @usage Rectangle r = garc.getAWTBounds();
    #  * @return A <code>Rectangle</code> that specifies the bounds of this object
    #  
    def getAWTBounds(self, self):
        """ generated source for method getAWTBounds """
        """ generated source for method getAWTBounds """
        return Rectangle(Ground(getX()), Ground(getY()), Ground(frameWidth), Ground(frameHeight))

    #  Protected method: paramString() 
    # 
    #  * Returns a string indicating the parameters of this object.
    #  * @noshow
    #  
    def paramString(self, self):
        """ generated source for method paramString """
        """ generated source for method paramString """
        tail = super(GArc, self).paramString()
        tail = tail.substring(tail.indexOf(')') + 1)
        r = self.getFrameRectangle()
        param = "frame=(" + r.getX() + ", " + r.getY() + ", " + r.getWidth() + ", " + r.getHeight() + ")"
        param += ", start=" + arcStart + ", sweep=" + arcSweep
        return param + tail

    #  Private method: getArcPoint(angle) 
    # 
    #  * Returns the point on the ellipse for the arc at the specified angle.
    #  
    def getArcPoint(self, angle, self, angle):
        """ generated source for method getArcPoint """
        """ generated source for method getArcPoint """
        rx = frameWidth / 2
        ry = frameHeight / 2
        cx = getX() + rx
        cy = getY() + ry
        return GPoint(cx + rx * GcosDegrees(angle), cy - ry * GsinDegrees(angle))

    #  Private method: containsAngle(theta) 
    # 
    #  * Returns <code>true</code> if the arc contains the specified angle.
    #  
    def containsAngle(self, theta, self, theta):
        """ generated source for method containsAngle """
        """ generated source for method containsAngle """
        start = min(self.getStartAngle(), self.getStartAngle() + self.getSweepAngle())
        sweep = abs(self.getSweepAngle())
        if sweep >= 360:
            return True
        theta = 360 - (-theta % 360) if (theta < 0) else theta % 360
        start = 360 - (-start % 360) if (start < 0) else start % 360
        if start + sweep > 360:
            return theta >= start or theta <= start + sweep - 360
        else:
            return theta >= start and theta <= start + sweep

    #  Package-private constructor: GArc(gobj) 
    # 
    #  * This constructor creates a <code>GArc</code> that exists only
    #  * to render the arcs on behalf some other object.
    #  
    @__init__.register(object, GObject)
    @__init__.register(object, GObject)
    def __init___1(self, gobj, self, gobj):
        """ generated source for method __init___1 """
        """ generated source for method __init___1 """
        super(GArc, self).__init__()
        isRenderer = True
        renderer = ArcRenderer(gobj)

    #  Private instance variables 
    frameWidth = float()
    frameHeight = float()
    arcStart = float()
    arcSweep = float()
    fillColor = None
    isFilled = bool()
    isRenderer = bool()
    renderer = None

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

#  Package class: ArcRenderer 
# 
#  * This class supports the implementation of rendered arcs, which are
#  * used by default for arcs and ovals.  The class maintains an internal
#  * polygon that stores the approximate points.  The methods that draw
#  * the object automatically update the cached version if any of the
#  * parameters have changed.
#  
class ArcRenderer(Serializable, Serializable):
    """ generated source for class ArcRenderer """
    """ generated source for class ArcRenderer """
    #  Constructor: ArcRenderer(gobj) 
    # 
    #  * Creates a new renderer object to draw the parent object.
    #  
    def __init__(self, gobj, self, gobj):
        """ generated source for method __init__ """
        """ generated source for method __init__ """
        super(ArcRenderer, self).__init__()
        target = gobj
        poly = Polygon()
        cacheValid = False

    #  Method: draw(g) 
    # 
    #  * Draws the object given the specified graphics context, filling
    #  * it if appropriate.
    #  
    @synchronized
    @synchronized
    def draw(self, g, self, g):
        """ generated source for method draw """
        """ generated source for method draw """
        validateCache()
        if (target).isFilled():
            g.setColor((target).getFillColor())
            g.fillPolygon(poly.xpoints, poly.ypoints, poly.npoints)
            g.setColor(target.getColor())
            g.drawPolygon(poly.xpoints, poly.ypoints, poly.npoints)
        elif isinstance(target, (GArc, )):
            g.drawPolyline(poly.xpoints, poly.ypoints, poly.npoints - 1)
        else:
            g.drawPolygon(poly.xpoints, poly.ypoints, poly.npoints)

    #  Private method: validateCache() 
    # 
    #  * Makes sure that the internal polygon is up to date.
    #  
    def validateCache(self, self):
        """ generated source for method validateCache """
        """ generated source for method validateCache """
        bounds = None
        start = 0
        sweep = 360
        if isinstance(target, (GOval, )) or isinstance(target, (GRoundRect, )):
            bounds = target.getBounds()
        else:
            arc = target
            bounds = arc.getFrameRectangle()
            start = arc.getStartAngle()
            sweep = arc.getSweepAngle()
            if start != oldStart or sweep != oldSweep:
                cacheValid = False
        if bounds == None:
            return
        x = bounds.getX()
        y = bounds.getY()
        width = bounds.getWidth()
        height = bounds.getHeight()
        if width <= 0 or height <= 0:
            return
        if not cacheValid or width != oldBounds.getWidth() or height != oldBounds.getHeight():
            poly.npoints = 0
            if isinstance(target, (GRoundRect, )):
                rr = target
                arcWidth = Ground(rr.getArcWidth())
                arcHeight = Ground(rr.getArcHeight())
                poly.addPoint(Ground(x + arcWidth / 2 + EPSILON), Ground(y + EPSILON))
                addArc(x, y, arcWidth, arcHeight, 90, 90)
                addArc(x, y + height - arcHeight, arcWidth, arcHeight, 180, 90)
                addArc(x + width - arcWidth, y + height - arcHeight, arcWidth, arcHeight, 270, 90)
                addArc(x + width - arcWidth, y, arcWidth, arcHeight, 0, 90)
            else:
                addArc(x, y, width, height, start, sweep)
                if isinstance(target, (GArc, )):
                    poly.addPoint(Ground(x + width / 2 + EPSILON), Ground(y + height / 2 + EPSILON))
                    oldStart = start
                    oldSweep = sweep
            x0 = Ground(poly.xpoints[0] - x)
            y0 = Ground(poly.ypoints[0] - y)
            oldBounds = bounds
        if x != oldBounds.getX() or y != oldBounds.getY():
            movePoly(Ground(x + EPSILON), Ground(y + EPSILON))
            oldBounds = bounds
        cacheValid = True

    #  Private method: addArc(x, y, width, height, start, sweep) 
    # 
    #  * Adds the points for an elliptical arc as specified by the parameters, which
    #  * have the same interpretation as in the <code>GArc</code> class.
    #  
    @synchronized
    @synchronized
    def addArc(self, x, y, width, height, start, sweep, self, x, y, width, height, start, sweep):
        """ generated source for method addArc """
        """ generated source for method addArc """
        aspectRatio = height / width
        rx = width / 2.0
        ry = height / 2.0
        xc = x + rx
        yc = y + ry
        if sweep < 0:
            start += sweep
            sweep = -sweep
        if sweep > 359.99:
            sweep = 360
        dt = atan2(1, max(width, height))
        nSteps = int((GtoRadians(sweep) / dt))
        dt = GtoRadians(sweep) / nSteps
        theta = GtoRadians(start)
        i = 0
        while i <= nSteps:
            px = xc + rx * cos(theta)
            py = yc - rx * sin(theta) * aspectRatio
            poly.addPoint(Ground(px + EPSILON), Ground(py + EPSILON))
            theta += dt
            i += 1

    #  Private method: movePoly(x, y) 
    # 
    #  * Shifts the polygon so that its origin is now at (x, y).
    #  
    @synchronized
    @synchronized
    def movePoly(self, x, y, self, x, y):
        """ generated source for method movePoly """
        """ generated source for method movePoly """
        dx = x - (poly.xpoints[0] - x0)
        dy = y - (poly.ypoints[0] - y0)
        i = 0
        while i < poly.npoints:
            poly.xpoints[i] += dx
            poly.ypoints[i] += dy
            i += 1

    #  Private constants 
    EPSILON = 0.00001

    #  Private instance variables 
    target = None
    poly = None
    x0 = int()
    y0 = int()
    oldBounds = None
    oldStart = float()
    oldSweep = float()
    cacheValid = bool()

