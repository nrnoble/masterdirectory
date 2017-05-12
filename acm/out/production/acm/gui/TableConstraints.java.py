#!/usr/bin/env python
""" generated source for module TableConstraints """
from __future__ import print_function
# 
#  * @(#)TableConstraints.java   1.99.1 08/12/08
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
#  Feature enhancement 26-May-08 (ESR)
#    1. Added support for serialization.
# package: acm.gui
#  Class: TableConstraints 
# 
#  * This class specifies a set of constraints appropriate to a
#  * <code>TableLayout</code> or <code>GridBagLayout</code>.  It has
#  * the following advantages over the <code>GridBagConstraints</code>
#  * class on which it is based:
#  *
#  * <p><ul>
#  * <li>The constraints can be specified as an easily readable string
#  *     instead of by initializing the individual fields.
#  * <li>The class includes new <code>width</code> and <code>height</code>
#  *     fields that can be used with <code>TableLayout</code> to specify
#  *     minimum heights and widths for rows and columns.
#  * <li>The class provides accessor methods (<code>getGridX</code>
#  *     and so forth) so that clients can operate as if the fields
#  *     are private.
#  * <li>The class includes a <code>toString</code> method that
#  *     displays nondefault values of the fields in a readable way.
#  * </ul>
#  *
#  * <p>To create a <code>TableConstraints</code> object, use the
#  * constructor with a string argument to set the fields of the
#  * underlying <code>GridBagConstraints</code> object.  For example,
#  * suppose you wanted to achieve the effect of the traditional code
#  *
#  * <p><pre><code>
#  * &nbsp;    GridBagConstraints gbc = new GridBagConstraints();
#  * &nbsp;    gbc.gridx = 2;
#  * &nbsp;    gbc.gridy = 3;
#  * &nbsp;    gbc.fill = GridBagConstraints.BOTH;
#  * </code></pre>
#  *
#  * <p>Using <code>TableConstraints</code>, you can do all of this
#  * with the constructor, as follows:
#  *
#  * <p><pre><code>
#  * &nbsp;    new TableConstraints("gridx=2 gridy=3 fill=BOTH");
#  * </code></pre>
#  
class TableConstraints(GridBagConstraints):
    """ generated source for class TableConstraints """
    #  Field: width 
    # 
    #  * Specifies the desired width of this cell.  The width of a column
    #  * is taken to be the maximum of the specified cell widths.  If this
    #  * field has its default value of 0, the width is taken from the
    #  * preferred size of the component.
    #  
    width = int()

    #  Field: height 
    # 
    #  * Specifies the desired height of this cell.  The height of a row
    #  * is taken to be the maximum of the specified cell heights.  If this
    #  * field has its default value of 0, the height is taken from the
    #  * preferred size of the component.
    #  
    height = int()

    #  Constructor: TableConstraints() 
    # 
    #  * Creates a new <code>TableConstraints</code> object with default
    #  * values for each of the fields.
    #  *
    #  * @usage TableConstraints constraints = new TableConstraints();
    #  
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(TableConstraints, self).__init__()
        self.__init__("")

    #  Constructor: TableConstraints(str) 
    # 
    #  * Creates a new <code>TableConstraints</code> object whose components
    #  * are initialized according from the specified string.  Each field is
    #  * initialized by specifying a binding in the form
    #  *
    #  * <p><pre><code>
    #  * &nbsp;    <font face="serif;times"><i>key</i></font>=<font face="serif;times"><i>value</i></font>
    #  * </code></pre>
    #  *
    #  * <p>where <i>key</i> is the name of one of the public fields
    #  * in the <code>TableConstraints</code> class and <i>value</i> is the
    #  * corresponding value, which can be expressed either as an integer
    #  * or as one of the constant names appropriate to that field.  For
    #  * example, the string
    #  *
    #  * <p><pre><code>
    #  * &nbsp;    "width=20 fill=BOTH"
    #  * </code></pre>
    #  *
    #  * <p>would create a <code>TableConstraints</code> object whose
    #  * <code>width</code> field was set to 20 and whose <code>fill</code>
    #  * field was set the the constant <code>GridBagConstraints.BOTH</code>.
    #  *
    #  * <p>As a special case, the four elements of the <code>insets</code>
    #  * field can be set using the key names <code>left</code>, <code>right</code>,
    #  * <code>top</code>, and <code>bottom</code>.  Also, because the names
    #  * are more likely to indicate their purposes to novices, the HTML names
    #  * <code>rowspan</code> and <code>colspan</code> can be used in place
    #  * of <code>gridwidth</code> and <code>gridheight</code>.
    #  *
    #  * @usage TableConstraints constraints = new TableConstraints(str);
    #  * @param str The constraint string as a series of key/value pairs
    #  
    @__init__.register(object, str)
    def __init___0(self, str_):
        """ generated source for method __init___0 """
        super(TableConstraints, self).__init__()
        self.__init__(OptionTable(str_.lower(), LEGAL_KEYS).getMap())

    #  Constructor: TableConstraints(map) 
    # 
    #  * Creates a new <code>TableConstraints</code> object whose components
    #  * are the key/value pairs in the map.
    #  *
    #  * @usage TableConstraints constraints = new TableConstraints(map);
    #  * @param map A map containing the key/value pairs
    #  * @noshow
    #  
    @__init__.register(object, Map)
    def __init___1(self, map):
        """ generated source for method __init___1 """
        super(TableConstraints, self).__init__()
        constraintTable = OptionTable(map)
        gridx = parseXYConstraint(constraintTable.getOption("gridx"))
        gridy = parseXYConstraint(constraintTable.getOption("gridy"))
        rowSpan = constraintTable.getOption("gridwidth")
        if rowSpan == None:
            rowSpan = constraintTable.getOption("rowspan")
        colSpan = constraintTable.getOption("gridheight")
        if colSpan == None:
            colSpan = constraintTable.getOption("colspan")
        gridwidth = parseSpanConstraint(rowSpan)
        gridheight = parseSpanConstraint(colSpan)
        fill = parseFillConstraint(constraintTable.getOption("fill"))
        anchor = parseAnchorConstraint(constraintTable.getOption("anchor"))
        ipadx = constraintTable.getIntOption("ipadx", 0)
        ipady = constraintTable.getIntOption("ipady", 0)
        weightx = constraintTable.getDoubleOption("weightx", 0.0)
        weighty = constraintTable.getDoubleOption("weighty", 0.0)
        insets.left = constraintTable.getIntOption("left", 0)
        insets.right = constraintTable.getIntOption("right", 0)
        insets.top = constraintTable.getIntOption("top", 0)
        insets.bottom = constraintTable.getIntOption("bottom", 0)
        self.width = constraintTable.getIntOption("width", -1)
        if self.width == -1:
            self.width = 0
        else:
            self.width += insets.left + insets.right
        self.height = constraintTable.getIntOption("height", -1)
        if self.height == -1:
            self.height = 0
        else:
            self.height += insets.top + insets.bottom
        if gridwidth != 1 and self.width != 0:
            raise ErrorException("TableConstraints: Cannot specify both width and gridwidth")
        if gridheight != 1 and self.height != 0:
            raise ErrorException("TableConstraints: Cannot specify both height and gridheight")

    #  Constructor: TableConstraints(gbc) 
    # 
    #  * Creates a new <code>TableConstraints</code> object whose fields match those
    #  * of the specified <code>GridBagConstraints</code> object.  Clients will not
    #  * ordinarily need to call this version of the constructor.
    #  *
    #  * @usage TableConstraints constraints = new TableConstraints(gbc);
    #  * @param gbc The <code>GridBagConstraints</code> object to copy
    #  * @noshow
    #  
    @__init__.register(object, GridBagConstraints)
    def __init___2(self, gbc):
        """ generated source for method __init___2 """
        super(TableConstraints, self).__init__()
        gridx = gbc.gridx
        gridy = gbc.gridy
        gridwidth = gbc.gridwidth
        gridheight = gbc.gridheight
        fill = gbc.fill
        anchor = gbc.anchor
        ipadx = gbc.ipadx
        ipady = gbc.ipady
        weightx = gbc.weightx
        weighty = gbc.weighty
        insets.left = gbc.insets.left
        insets.right = gbc.insets.right
        insets.top = gbc.insets.top
        insets.bottom = gbc.insets.bottom
        if isinstance(gbc, (TableConstraints, )):
            tc = gbc
            self.width = tc.width
            self.height = tc.height

    #  Method: getAnchor() 
    # 
    #  * Returns the <code>anchor</code> field from the constraint.
    #  *
    #  * @usage int anchor = constraint.getAnchor();
    #  * @return The <code>anchor</code> field from the constraint
    #  
    def getAnchor(self):
        """ generated source for method getAnchor """
        return anchor

    #  Method: getFill() 
    # 
    #  * Returns the <code>fill</code> field from the constraint.
    #  *
    #  * @usage int fill = constraint.getFill();
    #  * @return The <code>fill</code> field from the constraint
    #  
    def getFill(self):
        """ generated source for method getFill """
        return fill

    #  Method: getGridX() 
    # 
    #  * Returns the <code>gridx</code> field from the constraint.
    #  *
    #  * @usage int gridx = constraint.getGridX();
    #  * @return The <code>gridx</code> field from the constraint
    #  
    def getGridX(self):
        """ generated source for method getGridX """
        return gridx

    #  Method: getGridY() 
    # 
    #  * Returns the <code>gridy</code> field from the constraint.
    #  *
    #  * @usage int gridy = constraint.getGridY();
    #  * @return The <code>gridy</code> field from the constraint
    #  
    def getGridY(self):
        """ generated source for method getGridY """
        return gridy

    #  Method: getGridWidth() 
    # 
    #  * Returns the <code>gridwidth</code> field from the constraint.
    #  *
    #  * @usage int gridwidth = constraint.getGridWidth();
    #  * @return The <code>gridwidth</code> field from the constraint
    #  
    def getGridWidth(self):
        """ generated source for method getGridWidth """
        return gridwidth

    #  Method: getGridHeight() 
    # 
    #  * Returns the <code>gridheight</code> field from the constraint.
    #  *
    #  * @usage int gridheight = constraint.getGridHeight();
    #  * @return The <code>gridheight</code> field from the constraint
    #  
    def getGridHeight(self):
        """ generated source for method getGridHeight """
        return gridheight

    #  Method: getIPadX() 
    # 
    #  * Returns the <code>ipadx</code> field from the constraint.
    #  *
    #  * @usage int ipadx = constraint.getIPadX();
    #  * @return The <code>ipadx</code> field from the constraint
    #  
    def getIPadX(self):
        """ generated source for method getIPadX """
        return ipadx

    #  Method: getIPadY() 
    # 
    #  * Returns the <code>ipady</code> field from the constraint.
    #  *
    #  * @usage int ipady = constraint.getIPadY();
    #  * @return The <code>ipady</code> field from the constraint
    #  
    def getIPadY(self):
        """ generated source for method getIPadY """
        return ipady

    #  Method: getInsets() 
    # 
    #  * Returns the <code>insets</code> field from the constraint.
    #  *
    #  * @usage Insets insets = constraint.getInsets();
    #  * @return The <code>insets</code> field from the constraint
    #  
    def getInsets(self):
        """ generated source for method getInsets """
        return insets

    #  Method: getWeightX() 
    # 
    #  * Returns the <code>weightx</code> field from the constraint.
    #  *
    #  * @usage double weightx = constraint.getWeightX();
    #  * @return The <code>weightx</code> field from the constraint
    #  
    def getWeightX(self):
        """ generated source for method getWeightX """
        return weightx

    #  Method: getWeightY() 
    # 
    #  * Returns the <code>weighty</code> field from the constraint.
    #  *
    #  * @usage double weighty = constraint.getWeightY();
    #  * @return The <code>weighty</code> field from the constraint
    #  
    def getWeightY(self):
        """ generated source for method getWeightY """
        return weighty

    #  Method: getWidth() 
    # 
    #  * Returns the <code>width</code> field from the constraint.
    #  *
    #  * @usage int width = constraint.getWidth();
    #  * @return The <code>width</code> field from the constraint
    #  
    def getWidth(self):
        """ generated source for method getWidth """
        return self.width

    #  Method: getHeight() 
    # 
    #  * Returns the <code>height</code> field from the constraint.
    #  *
    #  * @usage int height = constraint.getHeight();
    #  * @return The <code>height</code> field from the constraint
    #  
    def getHeight(self):
        """ generated source for method getHeight """
        return self.height

    #  Override method: toString() 
    # 
    #  * Converts the constraint into a readable string.
    #  *
    #  * @usage String str = constraint.__str__();
    #  * @return A readable string version of the constraint
    #  * @noshow
    #  
    def __str__(self):
        """ generated source for method toString """
        str_ = getClass().__name__
        str_ += "[gridx=" + gridx + ",gridy=" + gridy
        if fill == VERTICAL:
            str_ += ",fill=VERTICAL"
        elif fill == HORIZONTAL:
            str_ += ",fill=HORIZONTAL"
        elif fill == BOTH:
            str_ += ",fill=BOTH"
        if anchor == NORTH:
            str_ += ",anchor=NORTH"
        elif anchor == SOUTH:
            str_ += ",anchor=SOUTH"
        elif anchor == EAST:
            str_ += ",anchor=EAST"
        elif anchor == WEST:
            str_ += ",anchor=WEST"
        elif anchor == NORTHEAST:
            str_ += ",anchor=NORTHEAST"
        elif anchor == NORTHWEST:
            str_ += ",anchor=NORTHWEST"
        elif anchor == SOUTHEAST:
            str_ += ",anchor=SOUTHEAST"
        elif anchor == SOUTHWEST:
            str_ += ",anchor=SOUTHWEST"
        elif anchor == MY_PAGE_START:
            str_ += ",anchor=PAGE_START"
        elif anchor == MY_PAGE_END:
            str_ += ",anchor=PAGE_END"
        elif anchor == MY_LINE_START:
            str_ += ",anchor=LINE_START"
        elif anchor == MY_LINE_END:
            str_ += ",anchor=LINE_END"
        elif anchor == MY_FIRST_LINE_START:
            str_ += ",anchor=FIRST_LINE_START"
        elif anchor == MY_FIRST_LINE_END:
            str_ += ",anchor=FIRST_LINE_END"
        elif anchor == MY_LAST_LINE_START:
            str_ += ",anchor=LAST_LINE_START"
        elif anchor == MY_LAST_LINE_END:
            str_ += ",anchor=LAST_LINE_END"
        if gridwidth != 1:
            str_ += ",gridwidth=" + gridwidth
        if gridheight != 1:
            str_ += ",gridheight=" + gridheight
        if ipadx != 0:
            str_ += ",ipadx=" + ipadx
        if ipady != 0:
            str_ += ",ipady=" + ipady
        if insets.left != 0:
            str_ += ",left=" + insets.left
        if insets.right != 0:
            str_ += ",right=" + insets.right
        if insets.top != 0:
            str_ += ",top=" + insets.top
        if insets.bottom != 0:
            str_ += ",bottom=" + insets.bottom
        if self.width != 0:
            str_ += ",width=" + self.width
        if self.height != 0:
            str_ += ",height=" + self.height
        str_ += "]"
        return str_

    #  Private method: parseXYConstraint(str) 
    # 
    #  * Reads the <code>gridx</code> and <code>gridy</code> values.
    #  
    def parseXYConstraint(self, str_):
        """ generated source for method parseXYConstraint """
        if str_ == None:
            return RELATIVE
        if str_ == "relative":
            return RELATIVE
        try:
            return Integer.decode(str_).intValue()
        except NumberFormatException as ex:
            raise ErrorException("TableConstraints: Illegal grid coordinate")

    #  Private method: parseSpanConstraint(str) 
    # 
    #  * Reads the <code>gridwidth</code> and <code>gridheight</code> values.
    #  
    def parseSpanConstraint(self, str_):
        """ generated source for method parseSpanConstraint """
        if str_ == None:
            return 1
        if str_ == "relative":
            return RELATIVE
        if str_ == "remainder":
            return REMAINDER
        try:
            return Integer.decode(str_).intValue()
        except NumberFormatException as ex:
            raise ErrorException("TableConstraints: Illegal span constraint")

    #  Private method: parseAnchorConstraint(str) 
    # 
    #  * Reads the value of an <code>anchor</code> constraint.
    #  
    def parseAnchorConstraint(self, str_):
        """ generated source for method parseAnchorConstraint """
        if str_ == None:
            return CENTER
        if str_ == "center":
            return CENTER
        if str_ == "north":
            return NORTH
        if str_ == "south":
            return SOUTH
        if str_ == "east":
            return EAST
        if str_ == "west":
            return WEST
        if str_ == "northeast" or str_ == "ne":
            return NORTHEAST
        if str_ == "northwest" or str_ == "nw":
            return NORTHWEST
        if str_ == "southeast" or str_ == "se":
            return SOUTHEAST
        if str_ == "southwest" or str_ == "sw":
            return SOUTHWEST
        if str_ == "page_start":
            return MY_PAGE_START
        if str_ == "page_end":
            return MY_PAGE_END
        if str_ == "line_start":
            return MY_LINE_START
        if str_ == "line_end":
            return MY_LINE_END
        if str_ == "first_line_start":
            return MY_FIRST_LINE_START
        if str_ == "first_line_end":
            return MY_FIRST_LINE_END
        if str_ == "last_line_start":
            return MY_LAST_LINE_START
        if str_ == "last_line_end":
            return MY_LAST_LINE_END
        raise ErrorException("TableConstraints: Illegal anchor specification")

    #  Private method: parseFillConstraint(str) 
    # 
    #  * Reads the value of an <code>fill</code> constraint.
    #  
    def parseFillConstraint(self, str_):
        """ generated source for method parseFillConstraint """
        if str_ == None or str_ == "none":
            return NONE
        if str_ == "horizontal":
            return HORIZONTAL
        if str_ == "vertical":
            return VERTICAL
        if str_ == "both":
            return BOTH
        raise ErrorException("TableConstraints: Illegal fill specification")

    #  Constants that allow this file to be compiled with old libraries 
    MY_PAGE_START = 19
    MY_PAGE_END = 20
    MY_LINE_START = 21
    MY_LINE_END = 22
    MY_FIRST_LINE_START = 23
    MY_FIRST_LINE_END = 24
    MY_LAST_LINE_START = 25
    MY_LAST_LINE_END = 26

    #  Array of legal keys 
    LEGAL_KEYS = ["anchor", "bottom", "colspan", "fill", "gridwidth", "gridheight", "gridx", "gridy", "height", "ipadx", "ipady", "left", "right", "rowspan", "top", "weightx", "weighty", "width"]

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

