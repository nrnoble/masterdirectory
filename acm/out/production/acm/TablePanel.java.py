#!/usr/bin/env python
""" generated source for module TablePanel """
from __future__ import print_function
# 
#  * @(#)TablePanel.java   1.99.1 08/12/08
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
#  Feature enhancement 26-May-08 (ESR)
#    1. Added support for serialization.
# package: acm.gui
#  Class: TablePanel 
# 
#  * This class represents a simple <code>JPanel</code> that uses
#  * <a href="TableLayout.html"><code>TableLayout</code></a> as its layout manager.
#  * The purpose of <code>TablePanel</code> is to support tabular component
#  * structures without the complexity of the <code>GridBagLayout</code> class.
#  
class TablePanel(JPanel):
    """ generated source for class TablePanel """
    #  Do not resize component 
    NONE = TableLayout.NONE

    #  Resize component in horizontal direction only 
    HORIZONTAL = TableLayout.HORIZONTAL

    #  Resize component in vertical direction only 
    VERTICAL = TableLayout.VERTICAL

    #  Resize component in both directions 
    BOTH = TableLayout.BOTH

    #  Center table in the container 
    CENTER = TableLayout.CENTER

    #  Align table horizontally at the left of its container 
    LEFT = TableLayout.LEFT

    #  Align table horizontally at the right of its container 
    RIGHT = TableLayout.RIGHT

    #  Align table vertically at the top of its container 
    TOP = TableLayout.TOP

    #  Align table vertically at the bottom of its container 
    BOTTOM = TableLayout.BOTTOM

    #  Expand table to fill its container 
    FILL = TableLayout.FILL

    #  Package private constructor: TablePanel() 
    # 
    #  * Creates a new <code>TablePanel</code> without assigning a layout manager.
    #  * This constructor is used only within the <code>acm.gui</code> package.
    #  
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(TablePanel, self).__init__()
        #  Empty 

    #  Constructor: TablePanel(rows, columns) 
    # 
    #  * Creates a new <code>TablePanel</code> whose layout manager supports the
    #  * specified number of rows and columns.
    #  *
    #  * @usage TablePanel panel = new TablePanel(rows, columns);
    #  * @param rows The number of rows, or 0 for no limit
    #  * @param columns The number of columns, or 0 for no limit
    #  
    @__init__.register(object, int, int)
    def __init___0(self, rows, columns):
        """ generated source for method __init___0 """
        super(TablePanel, self).__init__()
        self.__init__(rows, columns, 0, 0)

    #  Constructor: TablePanel(rows, columns, hgap, vgap) 
    # 
    #  * Creates a new <code>TablePanel</code> with the  specified number
    #  * of rows and columns and the supplied values for the horizontal and
    #  * vertical gap.
    #  *
    #  * @usage TablePanel panel = new TablePanel(rows, columns, hgap, vgap);
    #  * @param rows The number of rows, or 0 for no limit
    #  * @param columns The number of columns, or 0 for no limit
    #  * @param hgap The gap between columns
    #  * @param vgap The gap between rows
    #  
    @__init__.register(object, int, int, int, int)
    def __init___1(self, rows, columns, hgap, vgap):
        """ generated source for method __init___1 """
        super(TablePanel, self).__init__()
        setLayout(TableLayout(rows, columns, hgap, vgap))

    #  Method: setHorizontalAlignment(align) 
    # 
    #  * Sets the horizontal alignment for the table.  The legal values
    #  * are <code>CENTER</code>, <code>LEFT</code>, <code>RIGHT</code>, and
    #  * <code>FILL</code>.
    #  *
    #  * @usage layout.setHorizontalAlignment(align);
    #  * @param align The horizontal alignment for the table
    #  
    def setHorizontalAlignment(self, align):
        """ generated source for method setHorizontalAlignment """
        (getLayout()).setHorizontalAlignment(align)

    #  Method: getHorizontalAlignment() 
    # 
    #  * Returns the horizontal alignment for the table.
    #  *
    #  * @usage align = layout.getHorizontalAlignment();
    #  * @return The horizontal alignment for the table
    #  
    def getHorizontalAlignment(self):
        """ generated source for method getHorizontalAlignment """
        return (getLayout()).getHorizontalAlignment()

    #  Method: setVerticalAlignment(align) 
    # 
    #  * Sets the vertical alignment for the table.  The legal values
    #  * are <code>CENTER</code>, <code>TOP</code>, <code>BOTTOM</code>, and
    #  * <code>FILL</code>.
    #  *
    #  * @usage layout.setVerticalAlignment(align);
    #  * @param align The vertical alignment for the table
    #  
    def setVerticalAlignment(self, align):
        """ generated source for method setVerticalAlignment """
        (getLayout()).setVerticalAlignment(align)

    #  Method: getVerticalAlignment() 
    # 
    #  * Returns the vertical alignment for the table.
    #  *
    #  * @usage align = layout.getVerticalAlignment();
    #  * @return The vertical alignment for the table
    #  
    def getVerticalAlignment(self):
        """ generated source for method getVerticalAlignment """
        return (getLayout()).getVerticalAlignment()

    #  Method: setDefaultFill(fill) 
    # 
    #  * Sets the default fill parameter for components in the table.  The legal values
    #  * are <code>NONE</code>, <code>HORIZONTAL</code>, <code>VERTICAL</code>, and
    #  * <code>BOTH</code>.
    #  *
    #  * @usage layout.setDefaultFill(fill);
    #  * @param fill The default fill parameter for components in the table
    #  
    def setDefaultFill(self, fill):
        """ generated source for method setDefaultFill """
        (getLayout()).setDefaultFill(fill)

    #  Method: getDefaultFill() 
    # 
    #  * Returns the default fill parameter for components in the table.
    #  *
    #  * @usage fill = layout.getDefaultFill();
    #  * @return The default fill parameter for components in the table
    #  
    def getDefaultFill(self):
        """ generated source for method getDefaultFill """
        return (getLayout()).getDefaultFill()

    #  Method: setHgap(pixels) 
    # 
    #  * Sets the horizontal gap between components.
    #  * @param pixels The gap between components in pixels
    #  
    def setHgap(self, pixels):
        """ generated source for method setHgap """
        (getLayout()).setHgap(pixels)

    #  Method: getHgap() 
    # 
    #  * Returns the horizontal gap between components.
    #  * @return The horizontal gap between components
    #  
    def getHgap(self):
        """ generated source for method getHgap """
        return (getLayout()).getHgap()

    #  Method: setVgap(pixels) 
    # 
    #  * Sets the vertical gap between components.
    #  * @param pixels The gap between components in pixels
    #  
    def setVgap(self, pixels):
        """ generated source for method setVgap """
        (getLayout()).setVgap(pixels)

    #  Method: getVgap() 
    # 
    #  * Returns the vertical gap between components.
    #  * @return The vertical gap between components
    #  
    def getVgap(self):
        """ generated source for method getVgap """
        return (getLayout()).getVgap()

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

