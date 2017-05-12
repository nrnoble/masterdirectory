#!/usr/bin/env python
""" generated source for module GMath """
from __future__ import print_function
# 
#  * @(#)Gjava   1.99.1 08/12/08
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
#  Bug fix 15-Aug-07 (ESR, JTFBug 2007-011, reported by William Slough)
#    1. Fixed comments that referred to incorrect trigonometric functions.
# package: acm.graphics
#  Class: GMath 
# 
#  * This class defines a variety of static mathematical methods
#  * that are useful for the <code>acm.graphics</code> package.
#  
class GMath(object):
    """ generated source for class GMath """
    #  Private constructor: GMath() 
    # 
    #  * Prevents clients from instantiating this class.
    #  
    def __init__(self):
        """ generated source for method __init__ """
        #  Empty 

    #  Static method: round(x) 
    # 
    #  * Rounds a <code>double</code> value to the nearest <code>int</code>.
    #  *
    #  * @usage int n = round(x);
    #  * @param x A <code>double</code> value
    #  * @return The nearest <code>int</code> value
    #  
    @classmethod
    def round(cls, x):
        """ generated source for method round """
        return int(round(x))

    #  Static method: sinDegrees(angle) 
    # 
    #  * Returns the trigonometric sine of its argument where <code>angle</code>
    #  * is expressed in degrees.
    #  *
    #  * @usage double s = sinDegrees(angle);
    #  * @param angle An angle measured in degrees
    #  * @return The trigonometric sine of the angle
    #  
    @classmethod
    def sinDegrees(cls, angle):
        """ generated source for method sinDegrees """
        return sin(toRadians(angle))

    #  Static method: cosDegrees(angle) 
    # 
    #  * Returns the trigonometric cosine of its argument where <code>angle</code>
    #  * is expressed in degrees.
    #  *
    #  * @usage double c = cosDegrees(angle);
    #  * @param angle An angle measured in degrees
    #  * @return The trigonometric cosine of the angle
    #  
    @classmethod
    def cosDegrees(cls, angle):
        """ generated source for method cosDegrees """
        return cos(toRadians(angle))

    #  Static method: tanDegrees(angle) 
    # 
    #  * Returns the trigonometric tangent of its argument where <code>angle</code>
    #  * is expressed in degrees.
    #  *
    #  * @usage double t = tanDegrees(angle);
    #  * @param angle An angle measured in degrees
    #  * @return The trigonometric tangent of the angle
    #  
    @classmethod
    def tanDegrees(cls, angle):
        """ generated source for method tanDegrees """
        return cls.sinDegrees(angle) / cls.cosDegrees(angle)

    #  Static method: toDegrees(radians) 
    # 
    #  * Converts an angle from radians to degrees.  This method is defined in
    #  * the <code>Math</code> class, but was added only in JDK1.2, which is not
    #  * supported in all browsers.
    #  *
    #  * @usage double degrees = toDegrees(radians);
    #  * @param radians An angle measured in radians
    #  * @return The equivalent angle in degrees
    #  
    @classmethod
    def toDegrees(cls, radians):
        """ generated source for method toDegrees """
        return radians * 180 / PI

    #  Static method: toRadians(degrees) 
    # 
    #  * Converts an angle from degrees to radians.  This method is defined in
    #  * the <code>Math</code> class, but was added only in JDK1.2, which is not
    #  * supported in all browsers.
    #  *
    #  * @usage double radians = toRadians(degrees);
    #  * @param degrees An angle measured in degrees
    #  * @return The equivalent angle in radians
    #  
    @classmethod
    def toRadians(cls, degrees):
        """ generated source for method toRadians """
        return degrees * PI / 180

    #  Static method: distance(x, y) 
    # 
    #  * Computes the distance between the origin and the point
    #  * (<code>x</code>,&nbsp;<code>y</code>).
    #  *
    #  * @usage double d = distance(x, y);
    #  * @param x The x-coordinate of the point
    #  * @param y The y-coordinate of the point
    #  * @return The distance from the origin to the point (<code>x</code>,&nbsp;<code>y</code>)
    #  
    @classmethod
    @overloaded
    def distance(cls, x, y):
        """ generated source for method distance """
        return sqrt(x * x + y * y)

    #  Static method: distance(x0, y0, x1, y1) 
    # 
    #  * Computes the distance between the points (<code>x0</code>,&nbsp;<code>y0</code>)
    #  * and (<code>x1</code>,&nbsp;<code>y1</code>).
    #  *
    #  * @usage double d = distance(x0, y0, x1, y1);
    #  * @param x0 The x-coordinate of one point
    #  * @param y0 The y-coordinate of that point
    #  * @param x1 The x-coordinate of the other point
    #  * @param y1 The y-coordinate of that point
    #  * @return The distance between the points (<code>x0</code>,&nbsp;<code>y0</code>) and
    #  *         (<code>x1</code>,&nbsp;<code>y1</code>)
    #  
    @classmethod
    @distance.register(object, float, float, float, float)
    def distance_0(cls, x0, y0, x1, y1):
        """ generated source for method distance_0 """
        return cls.distance(x1 - x0, y1 - y0)

    #  Static method: angle(x, y) 
    # 
    #  * Returns the angle in degrees from the origin to the point
    #  * (<code>x</code>,&nbsp;<code>y</code>).  This method is easier to use than
    #  * <code>atan2</code> because it specifies the displacements in the usual
    #  * x/y order and because it takes care of the fact that the Java coordinate
    #  * system is flipped.  The point (0, 0) is arbitrarily defined to be at
    #  * angle 0.
    #  *
    #  * @usage double theta = angle(x, y);
    #  * @param x The x-coordinate of the point
    #  * @param y The y-coordinate of the point
    #  * @return The angle from the origin to the point (<code>x</code>,&nbsp;<code>y</code>)
    #  *         measured in degrees counterclockwise from the +x axis
    #  
    @classmethod
    @overloaded
    def angle(cls, x, y):
        """ generated source for method angle """
        if x == 0 and y == 0:
            return 0
        return cls.toDegrees(atan2(-y, x))

    #  Static method: angle(x0, y0, x1, y1) 
    # 
    #  * Computes the angle in degrees formed by a line segment from the
    #  * point (<code>x0</code>,&nbsp;<code>y0</code>) and
    #  * (<code>x1</code>,&nbsp;<code>y1</code>).
    #  *
    #  * @usage double theta = angle(x0, y0, x1, y1);
    #  * @param x0 The x-coordinate of one point
    #  * @param y0 The y-coordinate of that point
    #  * @param x1 The x-coordinate of the other point
    #  * @param y1 The y-coordinate of that point
    #  * @return The angle formed by the line segment from
    #  *         (<code>x0</code>,&nbsp;<code>y0</code>) to
    #  *         (<code>x1</code>,&nbsp;<code>y1</code>)
    #  
    @classmethod
    @angle.register(object, float, float, float, float)
    def angle_0(cls, x0, y0, x1, y1):
        """ generated source for method angle_0 """
        return cls.angle(x1 - x0, y1 - y0)

