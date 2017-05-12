#!/usr/bin/env python
""" generated source for module GRectangle """
from __future__ import print_function
# 
#  * @(#)GRectangle.java   1.99.1 08/12/08
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
#  Performance improvement 23-Jan-07 (ESR)
#    1. Changed hashCode implementation for better performance.
# 
#  Feature enhancement 26-May-08 (ESR)
#    1. Added support for serialization.
# package: acm.graphics
#  Class: GRectangle 
# 
#  * This class is a double-precision version of the <code>Rectangle</code> class
#  * in <code>java.awt</code>.
#  
class GRectangle(Serializable):
    """ generated source for class GRectangle """
    #  Constructor: GRectangle() 
    # 
    #  * Constructs a new empty <code>GRectangle</code>.
    #  *
    #  * @usage rect = new GRectangle();
    #  
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(GRectangle, self).__init__()
        self.__init__(0, 0, 0, 0)

    #  Constructor: GRectangle(x, y, width, height) 
    # 
    #  * Constructs a new <code>GRectangle</code> with the specified coordinates and size.
    #  *
    #  * @usage rect = new GRectangle(x, y, width, height);
    #  * @param x The x-coordinate of the rectangle
    #  * @param y The y-coordinate of the rectangle
    #  * @param width The width of the rectangle
    #  * @param height The height of the rectangle
    #  
    @__init__.register(object, float, float, float, float)
    def __init___0(self, x, y, width, height):
        """ generated source for method __init___0 """
        super(GRectangle, self).__init__()
        xc = x
        yc = y
        myWidth = width
        myHeight = height

    #  Constructor: GRectangle(width, height) 
    # 
    #  * Constructs a <code>GRectangle</code> at the origin with the specified width and height.
    #  *
    #  * @usage rect = new GRectangle(width, height);
    #  * @param width The width of the rectangle
    #  * @param height The height of the rectangle
    #  
    @__init__.register(object, float, float)
    def __init___1(self, width, height):
        """ generated source for method __init___1 """
        super(GRectangle, self).__init__()
        self.__init__(0, 0, width, height)

    #  Constructor: GRectangle(pt, size) 
    # 
    #  * Constructs a new <code>GRectangle</code> with the specified location and size.
    #  *
    #  * @usage rect = new GRectangle(pt, size);
    #  * @param pt The location of the upper left corner of the rectangle
    #  * @param size The dimensions of the rectangle
    #  
    @__init__.register(object, GPoint, GDimension)
    def __init___2(self, pt, size):
        """ generated source for method __init___2 """
        super(GRectangle, self).__init__()
        self.__init__(pt.getX(), pt.getY(), size.getWidth(), size.getHeight())

    #  Constructor: GRectangle(pt) 
    # 
    #  * Constructs a new empty <code>GRectangle</code> at the specified location.
    #  *
    #  * @usage rect = new GRectangle(pt);
    #  * @param pt The location of the upper left corner of the rectangle
    #  
    @__init__.register(object, GPoint)
    def __init___3(self, pt):
        """ generated source for method __init___3 """
        super(GRectangle, self).__init__()
        self.__init__(pt.getX(), pt.getY(), 0, 0)

    #  Constructor: GRectangle(size) 
    # 
    #  * Constructs a new <code>GRectangle</code> at the origin with the specified size.
    #  *
    #  * @usage rect = new GRectangle(size);
    #  * @param size The dimensions of the rectangle
    #  
    @__init__.register(object, GDimension)
    def __init___4(self, size):
        """ generated source for method __init___4 """
        super(GRectangle, self).__init__()
        self.__init__(0, 0, size.getWidth(), size.getHeight())

    #  Constructor: GRectangle(r) 
    # 
    #  * Constructs a new <code>GRectangle</code> from an existing one.
    #  *
    #  * @usage rect = new GRectangle(r);
    #  * @param r The original rectangle
    #  
    @__init__.register(object, GRectangle)
    def __init___5(self, r):
        """ generated source for method __init___5 """
        super(GRectangle, self).__init__()
        self.__init__(r.xc, r.yc, r.myWidth, r.myHeight)

    #  Method: getX() 
    # 
    #  * Returns the x coordinate of this <code>GRectangle</code>.
    #  *
    #  * @usage x = rect.getX();
    #  * @return The x coordinate of this <code>GRectangle</code>
    #  
    def getX(self):
        """ generated source for method getX """
        return xc

    #  Method: getY() 
    # 
    #  * Returns the y coordinate of this <code>GRectangle</code>.
    #  *
    #  * @usage y = rect.getY();
    #  * @return The y coordinate of this <code>GRectangle</code>
    #  
    def getY(self):
        """ generated source for method getY """
        return yc

    #  Method: getWidth() 
    # 
    #  * Returns the width of this <code>GDimension</code>.
    #  *
    #  * @usage width = rect.getWidth();
    #  * @return The width of this <code>GDimension</code>
    #  
    def getWidth(self):
        """ generated source for method getWidth """
        return myWidth

    #  Method: getHeight() 
    # 
    #  * Returns the height of this <code>GDimension</code>.
    #  *
    #  * @usage height = rect.getHeight();
    #  * @return The height of this <code>GDimension</code>
    #  
    def getHeight(self):
        """ generated source for method getHeight """
        return myHeight

    #  Method: setBounds(x, y, width, height) 
    # 
    #  * Sets the components of a <code>GRectangle</code> from the specified values.
    #  *
    #  * @usage rect.setBounds(x, y, width, height);
    #  * @param x The x-coordinate of the rectangle
    #  * @param y The y-coordinate of the rectangle
    #  * @param width The width of the rectangle
    #  * @param height The height of the rectangle
    #  
    @overloaded
    def setBounds(self, x, y, width, height):
        """ generated source for method setBounds """
        xc = x
        yc = y
        myWidth = width
        myHeight = height

    #  Method: setBounds(pt, size) 
    # 
    #  * Sets the components of a <code>GRectangle</code> from the specified location and size.
    #  *
    #  * @usage rect.setBounds(pt, size);
    #  * @param pt The location of the upper left corner of the rectangle
    #  * @param size The dimensions of the rectangle
    #  
    @setBounds.register(object, GPoint, GDimension)
    def setBounds_0(self, pt, size):
        """ generated source for method setBounds_0 """
        self.setBounds(pt.getX(), pt.getY(), size.getWidth(), size.getHeight())

    #  Method: setBounds(bounds) 
    # 
    #  * Sets the bounds of one <code>GRectangle</code> equal to that of another.
    #  *
    #  * @usage rect.setBounds(bounds);
    #  * @param bounds A <code>GRectangle</code> specifying the new bounds
    #  
    @setBounds.register(object, GRectangle)
    def setBounds_1(self, bounds):
        """ generated source for method setBounds_1 """
        self.setBounds(bounds.xc, bounds.yc, bounds.myWidth, bounds.myHeight)

    #  Method: getBounds() 
    # 
    #  * Returns a new <code>GRectangle</code> whose bounds are the same as this one.
    #  *
    #  * @usage r = rect.getBounds();
    #  * @return A new rectangle with the same bounds
    #  
    def getBounds(self):
        """ generated source for method getBounds """
        return GRectangle(self)

    #  Method: setLocation(x, y) 
    # 
    #  * Sets the location of the <code>GRectangle</code> to the specified <code>x</code>
    #  * and <code>y</code> values.
    #  *
    #  * @usage rect.setLocation(x, y);
    #  * @param x The new x-coordinate for the rectangle
    #  * @param y The new y-coordinate for the rectangle
    #  
    @overloaded
    def setLocation(self, x, y):
        """ generated source for method setLocation """
        xc = x
        yc = y

    #  Method: setLocation(pt) 
    # 
    #  * Sets the location of the <code>GRectangle</code> to the specified point.
    #  *
    #  * @usage rect.setLocation(pt);
    #  * @param pt The new location for the rectangle
    #  
    @setLocation.register(object, GPoint)
    def setLocation_0(self, pt):
        """ generated source for method setLocation_0 """
        self.setLocation(pt.getX(), pt.getY())

    #  Method: getLocation() 
    # 
    #  * Returns a new <code>GPoint</code> with the location of the rectangle.
    #  *
    #  * @usage pt = rect.getLocation();
    #  * @return The location of the rectangle as a <code>GPoint</code>
    #  
    def getLocation(self):
        """ generated source for method getLocation """
        return GPoint(xc, yc)

    #  Method: translate(dx, dy) 
    # 
    #  * Adjusts the coordinates of a rectangle by the specified <code>dx</code> and
    #  * <code>dy</code> offsets.
    #  *
    #  * @usage rect.translate(dx, dy);
    #  * @param dx The change in the x direction (positive is rightward)
    #  * @param dy The change in the y direction (positive is downward)
    #  
    def translate(self, dx, dy):
        """ generated source for method translate """
        xc += dx
        yc += dy

    #  Method: setSize(width, height) 
    # 
    #  * Sets the size of the <code>GRectangle</code> to the specified values.
    #  *
    #  * @usage rect.setSize(width, height);
    #  * @param width The new width of the rectangle
    #  * @param height The new height of the rectangle
    #  
    @overloaded
    def setSize(self, width, height):
        """ generated source for method setSize """
        myWidth = width
        myHeight = height

    #  Method: setSize(size) 
    # 
    #  * Sets the size of the <code>GRectangle</code> to the specified dimension.
    #  *
    #  * @usage rect.setSize(size);
    #  * @param size The new dimensions of the rectangle
    #  
    @setSize.register(object, GDimension)
    def setSize_0(self, size):
        """ generated source for method setSize_0 """
        self.setSize(size.getWidth(), size.getHeight())

    #  Method: getSize() 
    # 
    #  * Returns a new <code>GDimension</code> object with the size of the <code>GRectangle</code>.
    #  * @usage size = rect.getSize();
    #  * @return The size of the rectangle as a <code>GDimension</code>
    #  
    def getSize(self):
        """ generated source for method getSize """
        return GDimension(myWidth, myHeight)

    #  Method: grow(dx, dy) 
    # 
    #  * Adjusts the edges of a rectangle by the specified <code>dx</code> and <code>dy</code>
    #  * offsets along each of its borders.
    #  *
    #  * @usage rect.grow(dx, dy);
    #  * @param dx The offset to extend each of the left and right borders
    #  * @param dy The offset to extend each of the top and bottom borders
    #  
    def grow(self, dx, dy):
        """ generated source for method grow """
        xc -= dx
        yc -= dy
        myWidth += 2 * dx
        myHeight += 2 * dy

    #  Method: isEmpty() 
    # 
    #  * Returns <code>true</code> if the rectangle is empty.
    #  *
    #  * @usage if (rect.isEmpty()) . . .
    #  * @return <code>true</code> if the rectangle is empty, and <code>false</code> otherwise
    #  
    def isEmpty(self):
        """ generated source for method isEmpty """
        return myWidth <= 0 or myHeight <= 0

    #  Method: contains(x, y) 
    # 
    #  * Returns <code>true</code> if the <code>GRectangle</code> contains the specified point.
    #  *
    #  * @usage if (rect.contains(x, y)) . . .
    #  * @param x The x-coordinate of the point being tested
    #  * @param y The y-coordinate of the point being tested
    #  * @return <code>true</code> if the rectangle contains (<code>x</code>,&nbsp;<code>y</code>),
    #  *         and <code>false</code> otherwise
    #  
    @overloaded
    def contains(self, x, y):
        """ generated source for method contains """
        return x >= xc and y >= yc and x < xc + myWidth and y < yc + myHeight

    #  Method: contains(pt) 
    # 
    #  * Returns <code>true</code> if the <code>GRectangle</code> contains the specified point.
    #  *
    #  * @usage if (rect.contains(pt)) . . .
    #  * @param pt The point being tested
    #  * @return <code>true</code> if the rectangle contains <code>pt</code>,
    #  *         and <code>false</code> otherwise
    #  
    @contains.register(object, GPoint)
    def contains_0(self, pt):
        """ generated source for method contains_0 """
        return self.contains(pt.getX(), pt.getY())

    #  Method: intersects(r2) 
    # 
    #  * Returns <code>true</code> if <code>r1</code> and <code>r2</code> have a nonempty
    #  * intersection.
    #  *
    #  * @usage if (r1.intersects(r2)) . . .
    #  * @param r2 A second rectangle
    #  * @return <code>true</code> if the two rectangles intersect, and <code>false</code> otherwise
    #  
    def intersects(self, r2):
        """ generated source for method intersects """
        r1 = self
        if r1.xc > r2.xc + r2.myWidth:
            return False
        if r1.yc > r2.yc + r2.myHeight:
            return False
        if r2.xc > r1.xc + r1.myWidth:
            return False
        if r2.yc > r1.yc + r1.myHeight:
            return False
        return True

    #  Method: intersection(r2) 
    # 
    #  * Returns the largest rectangle that is contained in both
    #  * <code>r1</code> and <code>r2</code>.
    #  *
    #  * @usage r3 = r1.intersection(r2);
    #  * @param r2 A second rectangle
    #  * @return The intersection of this rectangle and <code>r2</code>
    #  
    def intersection(self, r2):
        """ generated source for method intersection """
        r1 = self
        x1 = max(r1.xc, r2.xc)
        y1 = max(r1.yc, r2.yc)
        x2 = min(r1.xc + r1.myWidth, r2.xc + r2.myWidth)
        y2 = min(r1.yc + r1.myHeight, r2.yc + r2.myHeight)
        return GRectangle(x1, y1, x2 - x1, y2 - y1)

    #  Method: union(r) 
    # 
    #  * Returns the smallest rectangle that contains both
    #  * <code>r1</code> and <code>r2</code>.
    #  *
    #  * @usage r3 = r1.union(r2);
    #  * @param r2 A second rectangle
    #  * @return The union of this rectangle and <code>r2</code>
    #  
    def union(self, r2):
        """ generated source for method union """
        if self.isEmpty():
            return GRectangle(r2)
        if r2.isEmpty():
            return GRectangle(self)
        r1 = self
        x1 = min(r1.xc, r2.xc)
        y1 = min(r1.yc, r2.yc)
        x2 = max(r1.xc + r1.myWidth, r2.xc + r2.myWidth)
        y2 = max(r1.yc + r1.myHeight, r2.yc + r2.myHeight)
        return GRectangle(x1, y1, x2 - x1, y2 - y1)

    #  Method: add(r) 
    # 
    #  * Adjusts the bounds of the current <code>GRectangle</code> so that it contains
    #  * the rectangle represented by the argument.
    #  *
    #  * @usage rect.add(r);
    #  * @param r A new rectangle to include in this one
    #  
    @overloaded
    def add(self, r):
        """ generated source for method add """
        if r.isEmpty():
            return
        if self.isEmpty():
            self.setBounds(r)
            return
        x2 = max(xc + myWidth, r.xc + r.myWidth)
        y2 = max(yc + myHeight, r.yc + r.myHeight)
        xc = min(r.xc, xc)
        yc = min(r.yc, yc)
        myWidth = x2 - xc
        myHeight = y2 - yc

    #  Method: add(x, y) 
    # 
    #  * Adds the specified point to the rectangle.
    #  *
    #  * @usage rect.add(x, y);
    #  * @param x The x coordinate of the new point
    #  * @param y The y coordinate of the new point
    #  
    @add.register(object, float, float)
    def add_0(self, x, y):
        """ generated source for method add_0 """
        if self.isEmpty():
            self.setBounds(x, y, 0, 0)
            return
        x2 = max(x + myWidth, x)
        y2 = max(y + myHeight, y)
        xc = min(x, xc)
        yc = min(y, yc)
        myWidth = x2 - xc
        myHeight = y2 - yc

    #  Method: toRectangle() 
    # 
    #  * Converts this <code>GRectangle</code> to the nearest integer-based <code>Rectangle</code>.
    #  *
    #  * @usage size = dim.toRectangle();
    #  * @return The closest integer-based <code>Rectangle</code>
    #  
    def toRectangle(self):
        """ generated source for method toRectangle """
        return Rectangle(int(round(xc)), int(round(yc)), int(round(myWidth)), int(round(myHeight)))

    #  Method: hashCode() 
    # 
    #  * Returns an integer hash code for the rectangle.  The hash code for a
    #  * <code>GRectangle</code> is constructed from the hash codes from the
    #  * <code>float</code> values of the coordinates, which are the ones used in the
    #  * <code>equals</code> method.
    #  *
    #  * @usage hash = rect.hashCode();
    #  * @return The hash code for this rectangle
    #  * @noshow
    #  
    def hashCode(self):
        """ generated source for method hashCode """
        hash = float(float(xc)).hashCode()
        hash = (37 * hash) ^ float(float(yc)).hashCode()
        hash = (37 * hash) ^ float(float(myWidth)).hashCode()
        hash = (37 * hash) ^ float(float(myHeight)).hashCode()
        return hash

    #  Method: equals(obj) 
    # 
    #  * Tests whether two <code>GRectangle</code> objects are equal.
    #  * Because floating-point values are inexact, this method checks for
    #  * equality by comparing the <code>float</code> values (rather than the
    #  * <code>double</code> values) of the coordinates.
    #  *
    #  * @usage if (rect == obj) . . .
    #  * @param obj Any object
    #  * @return <code>true</code> if the <code>obj</code> is a <code>GRectangle</code>
    #  *         equal to this one, and <code>false</code> otherwise
    #  * @noshow
    #  
    def equals(self, obj):
        """ generated source for method equals """
        if not (isinstance(obj, (GRectangle, ))):
            return False
        r = obj
        if float(xc) != float(r.xc):
            return False
        if float(yc) != float(r.yc):
            return False
        if float(myWidth) != float(r.myWidth):
            return False
        if float(myHeight) != float(r.myHeight):
            return False
        return True

    #  Method: toString() 
    # 
    #  * Converts this <code>GRectangle</code> to its string representation.
    #  *
    #  * @usage str = rect.__str__();
    #  * @return A string representation of this rectangle
    #  * @noshow
    #  
    def __str__(self):
        """ generated source for method toString """
        return "[" + float(xc) + ", " + float(yc) + ", " + float(myWidth) + "x" + float(myHeight) + "]"

    #  Private instance variables 
    xc = float()
    yc = float()
    myWidth = float()
    myHeight = float()

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

