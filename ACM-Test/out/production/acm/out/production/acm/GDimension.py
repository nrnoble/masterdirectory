#!/usr/bin/env python
""" generated source for module GDimension """
from __future__ import print_function
# 
#  * @(#)GDimension.java   1.99.1 08/12/08
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
#  Class: GDimension 
# 
#  * This class is a double-precision version of the <code>Dimension</code> class
#  * in <code>java.awt</code>.
#  
class GDimension(Serializable):
    """ generated source for class GDimension """
    #  Constructor: GDimension() 
    # 
    #  * Constructs a new dimension object with zero values for width and height.
    #  *
    #  * @usage dim = new GDimension();
    #  
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(GDimension, self).__init__()
        self.__init__(0, 0)

    #  Constructor: GDimension(width, height) 
    # 
    #  * Constructs a new dimension object with the specified components.
    #  *
    #  * @usage dim = new GDimension(width, height);
    #  * @param width The width of the dimension object
    #  * @param height The height of the dimension object
    #  
    @__init__.register(object, float, float)
    def __init___0(self, width, height):
        """ generated source for method __init___0 """
        super(GDimension, self).__init__()
        myWidth = width
        myHeight = height

    #  Constructor: GDimension(size) 
    # 
    #  * Constructs a new <code>GDimension</code> object from an existing one.
    #  *
    #  * @usage dim = new GDimension(size);
    #  * @param size An existing <code>GDimension</code> object specifying the size
    #  
    @__init__.register(object, GDimension)
    def __init___1(self, size):
        """ generated source for method __init___1 """
        super(GDimension, self).__init__()
        self.__init__(size.myWidth, size.myHeight)

    #  Constructor: GDimension(size) 
    # 
    #  * Constructs a new <code>GDimension</code> object from an AWT <code>Dimension</code>.
    #  *
    #  * @usage dim = new GDimension(size);
    #  * @param size An AWT <code>Dimension</code> object specifying the size
    #  
    @__init__.register(object, Dimension)
    def __init___2(self, size):
        """ generated source for method __init___2 """
        super(GDimension, self).__init__()
        self.__init__(size.width, size.height)

    #  Method: getWidth() 
    # 
    #  * Returns the width of this <code>GDimension</code>.
    #  *
    #  * @usage width = dim.getWidth();
    #  * @return The width of this <code>GDimension</code>
    #  
    def getWidth(self):
        """ generated source for method getWidth """
        return myWidth

    #  Method: getHeight() 
    # 
    #  * Returns the height of this <code>GDimension</code>.
    #  *
    #  * @usage height = dim.getHeight();
    #  * @return The height of this <code>GDimension</code>
    #  
    def getHeight(self):
        """ generated source for method getHeight """
        return myHeight

    #  Method: setSize(width, height) 
    # 
    #  * Sets the components of the dimension object from the specified parameters.
    #  *
    #  * @usage dim.setSize(width, height);
    #  * @param width The new width of the dimension object
    #  * @param height The new height of the dimension object
    #  
    @overloaded
    def setSize(self, width, height):
        """ generated source for method setSize """
        myWidth = width
        myHeight = height

    #  Method: setSize(size) 
    # 
    #  * Sets the width and height of one <code>GDimension</code> object equal to that of another.
    #  *
    #  * @usage dim.setSize(size);
    #  * @param size A <code>GDimension</code> object specifying the new size
    #  
    @setSize.register(object, GDimension)
    def setSize_0(self, size):
        """ generated source for method setSize_0 """
        self.setSize(size.myWidth, size.myHeight)

    #  Method: getSize() 
    # 
    #  * Returns a new <code>GDimension</code> object equal to this one.
    #  *
    #  * @usage size = dim.getSize();
    #  * @return A new <code>GDimension</code> object with the same size
    #  
    def getSize(self):
        """ generated source for method getSize """
        return GDimension(myWidth, myHeight)

    #  Method: toDimension() 
    # 
    #  * Converts this <code>GDimension</code> to the nearest integer-based
    #  * <code>Dimension</code>.
    #  *
    #  * @usage size = dim.toDimension();
    #  * @return The closest integer-based <code>Dimension</code> object
    #  
    def toDimension(self):
        """ generated source for method toDimension """
        return Dimension(int(round(myWidth)), int(round(myHeight)))

    #  Method: hashCode() 
    # 
    #  * Returns an integer hash code for the dimension object.  The hash code for a
    #  * <code>GDimension</code> is constructed from the hash codes from the
    #  * <code>float</code> values of the width and height, which are the ones used in the
    #  * <code>equals</code> method.
    #  *
    #  * @usage hash = dim.hashCode();
    #  * @return The hash code for this dimension object
    #  * @noshow
    #  
    def hashCode(self):
        """ generated source for method hashCode """
        return float(float(myWidth)).hashCode() ^ (37 * float(float(myHeight)).hashCode())

    #  Method: equals(obj) 
    # 
    #  * Tests whether two <code>GDimension</code> objects are equal.
    #  * Because floating-point values are inexact, this method checks for
    #  * equality by comparing the <code>float</code> values (rather than the
    #  * <code>double</code> values) of the coordinates.
    #  *
    #  * @usage if (dim == obj) . . .
    #  * @param obj Any object
    #  * @return <code>true</code> if the <code>obj</code> is a <code>GDimension</code>
    #  *         equal to this one, and <code>false</code> otherwise
    #  * @noshow
    #  
    def equals(self, obj):
        """ generated source for method equals """
        if not (isinstance(obj, (GDimension, ))):
            return False
        dim = obj
        return (float(myWidth) == float(dim.myWidth)) and (float(myHeight) == float(dim.myHeight))

    #  Method: toString() 
    # 
    #  * Converts this <code>GDimension</code> to its string representation.
    #  *
    #  * @usage str = dim.__str__();
    #  * @return A string representation of this dimension object
    #  * @noshow
    #  
    def __str__(self):
        """ generated source for method toString """
        return "(" + float(myWidth) + "x" + float(myHeight) + ")"

    #  Private instance variables 
    myWidth = float()
    myHeight = float()

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

