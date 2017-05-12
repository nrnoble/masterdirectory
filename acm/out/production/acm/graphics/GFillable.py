#!/usr/bin/env python
""" generated source for module GFillable """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
# 
#  * @(#)GFillable.java   1.99.1 08/12/08
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
# package: acm.graphics
#  Interface: GFillable 
# 
#  * Specifies the characteristics of a graphical object that supports filling.
#  
class GFillable(object):
    """ generated source for interface GFillable """
    __metaclass__ = ABCMeta
    #  Method: setFilled(fill) 
    # 
    #  * Sets whether this object is filled.
    #  *
    #  * @usage gobj.setFilled(fill);
    #  * @param fill <code>true</code> if the object should be filled, <code>false</code> for an outline
    #  
    @abstractmethod
    def setFilled(self, fill):
        """ generated source for method setFilled """

    #  Method: isFilled() 
    # 
    #  * Returns whether this object is filled.
    #  *
    #  * @usage if (gobj.isFilled()) . . .
    #  * @return The color used to display the object
    #  
    @abstractmethod
    def isFilled(self):
        """ generated source for method isFilled """

    #  Method: setFillColor(color) 
    # 
    #  * Sets the color used to display the filled region of this object.
    #  *
    #  * @usage gobj.setFillColor(color);
    #  * @param color The color used to display the filled region of this object
    #  
    @abstractmethod
    def setFillColor(self, color):
        """ generated source for method setFillColor """

    #  Method: getFillColor() 
    # 
    #  * Returns the color used to display the filled region of this object.  If
    #  * none has been set, <code>getFillColor</code> returns the color of the
    #  * object.
    #  *
    #  * @usage Color color = gobj.getFillColor();
    #  * @return The color used to display the filled region of this object
    #  
    @abstractmethod
    def getFillColor(self):
        """ generated source for method getFillColor """

