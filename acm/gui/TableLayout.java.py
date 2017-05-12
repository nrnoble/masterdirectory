#!/usr/bin/env python
""" generated source for module TableLayout """
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
#  * @(#)TableLayout.java   1.99.1 08/12/08
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
#  Bug fix 8-Jan-06 (ESR, JTFBug 2008-001)
#    1. Fixed bug in the layoutContainer failed to consider the gridwidth
#       and gridheight values in computing the width of a column.
# 
#  Code cleanup 28-May-07 (ESR)
#    1. Added generic type tags.
# 
#  Feature enhancement 26-May-08 (ESR)
#    1. Added support for serialization.
# package: acm.gui
#  Class: TableLayout 
# 
#  * This class implements a new <code>LayoutManager</code> that arranges
#  * components into a two-dimensional grid.  The capabilities are analogous
#  * to those provide by the <code>GridBagLayout</code> class, although
#  * <code>TableLayout</code> is considerably easier to use.
#  *
#  * The constructor for the <code>TableLayout</code> class takes the number
#  * of rows and columns.  Thus, the constructor call
#  *
#  * <p><pre><code>
#  * &nbsp;    new TableLayout(3, 5)
#  * <code></pre>
#  *
#  * <p>creates a new <code>TableLayout</code> manager with three rows in the
#  * vertical dimension and five columns across the page.  Components are added
#  * to the grid starting at the upper left, filling each horizontal row and
#  * then moving on to the next row down after the current one is filled.
#  *
#  * <p>The <code>TableLayout</code> manager also supports more fine-grained
#  * control over the formatting of tables by allowing you to specify
#  * constraints in the following form:
#  *
#  * <p><pre><code>
#  * &nbsp;    </code><i>constraint</i><code>=</code><i>value</i><code>
#  * </code></pre>
#  *
#  * <p>For example, if you want to specify that a component occupies two
#  * columns in the grid, you would use the constraint
#  *
#  * <p><pre><code>
#  * &nbsp;    "gridwidth=2"
#  * </code></pre>
#  *
#  * <p>Strings used as constraint objects can set several constraints at
#  * once by including multiple constraint/value pairs separated by spaces.
#  *
#  * <p>The <code>TableLayout</code> class accepts all constraints supported
#  * by <code>GridBagLayout</code>.  The most common constraints are shown
#  * in the following table:
#  *
#  * <p><table bgcolor=#FFFFFF border=1 cellspacing=0 width=750>
#  * <tr><td><table border=0 cellspacing=1 cellpadding=0><tr><td colspan=2><code>gridwidth=</code><font face=times><i>columns</i></font>&nbsp;&nbsp;<i><font size=-1>or</font></i>&nbsp;&nbsp;<code>gridheight=</code><font face=times><i>rows</i></font></td></tr>
#  * <tr><td width=25>&nbsp;</td><td width=720>Indicates that this table cell should span the indicated number of columns or rows.</td></tr></table></td></tr>
#  * <tr><td><table border=0 cellspacing=1 cellpadding=0><tr><td colspan=2><code>width=</code><font face=times><i>pixels</i></font>&nbsp;&nbsp;<i><font size=-1>or</font></i>&nbsp;&nbsp;<code>height=</code><font face=times><i>pixels</i></font></td></tr>
#  * <tr><td width=25>&nbsp;</td><td width=720>The <code>width</code> specification indicates that the width of this column should be the specified number of pixels.  If different widths are specified for cells in the same column, the column width is defined to be the maximum.  In the absence of any <code>width</code> specification, the column width is the largest of the preferred widths.  The <code>height</code> specification is interpreted symmetrically for row heights.</td></tr></table></td></tr>
#  * <tr><td><table border=0 cellspacing=1 cellpadding=0><tr><td colspan=2><code>weightx=</code><font face=times><i>weight</i></font>&nbsp;&nbsp;<i><font size=-1>or</font></i>&nbsp;&nbsp;<code>weighty=</code><font face=times><i>weight</i></font></td></tr>
#  * <tr><td width=25>&nbsp;</td><td width=720>If the total size of the table is less than the size of its enclosure, <code>TableLayout</code> will ordinarily center the table in the available space.  If any of the cells, however, are given nonzero <code>weightx</code> or <code>weighty</code> values, the extra space is distributed along that axis in proportion to the weights specified.  As in the <code>GridBagLayout</code> model, the weights are floating-point values and may therefore contain a decimal point.</td></tr></table></td></tr>
#  * <tr><td><table border=0 cellspacing=1 cellpadding=0><tr><td colspan=2><code>fill=</code><font face=times><i>fill</i></font></td></tr>
#  * <tr><td width=25>&nbsp;</td><td width=720>Indicates how the component in this cell should be resized if its preferred size is smaller than the cell size.  The legal values are <code>NONE</code>, <code>HORIZONTAL</code>, <code>VERTICAL</code>, and <code>BOTH</code>, indicating the axes along which stretching should occur.  The default is <code>BOTH</code>.</td></tr></table></td></tr>
#  * <tr><td><table border=0 cellspacing=1 cellpadding=0><tr><td colspan=2><code>anchor=</code><font face=times><i>anchor</i></font></td></tr>
#  * <tr><td width=25>&nbsp;</td><td width=720>If a component is not being filled along a particular axis, the <code>anchor</code> specification indicates where the component should be placed in its cell.  The default value is <code>CENTER</code>, but any of the standard compass directions (<code>NORTH</code>, <code>SOUTH</code>, <code>EAST</code>, <code>WEST</code>, <code>NORTHEAST</code>, <code>NORTHWEST</code>, <code>SOUTHEAST</code>, or <code>SOUTHWEST</code>) may also be used.</td></tr></table></td></tr>
#  * </table>
#  
class TableLayout(LayoutManager2, Serializable):
    """ generated source for class TableLayout """
    #  Do not resize component 
    NONE = GridBagConstraints.NONE

    #  Resize component in horizontal direction only 
    HORIZONTAL = GridBagConstraints.HORIZONTAL

    #  Resize component in vertical direction only 
    VERTICAL = GridBagConstraints.VERTICAL

    #  Resize component in both directions 
    BOTH = GridBagConstraints.BOTH

    #  Center table in the container 
    CENTER = 10

    #  Align table horizontally at the left of its container 
    LEFT = 11

    #  Align table horizontally at the right of its container 
    RIGHT = 12

    #  Align table vertically at the top of its container 
    TOP = 13

    #  Align table vertically at the bottom of its container 
    BOTTOM = 14

    #  Expand table to fill its container 
    FILL = BOTH

    #  Constructor: TableLayout() 
    # 
    #  * Creates a new <code>TableLayout</code> object with no limits
    #  * on the number of rows and columns.
    #  *
    #  * @usage TableLayout layout = new TableLayout();
    #  
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(TableLayout, self).__init__()
        self.__init__(0, 0)

    #  Constructor: TableLayout(rows, columns) 
    # 
    #  * Creates a new <code>TableLayout</code> object with the specified
    #  * number of rows and columns.
    #  *
    #  * @usage TableLayout layout = new TableLayout(rows, columns);
    #  * @param rows The number of rows, or 0 for no limit
    #  * @param columns The number of columns, or 0 for no limit
    #  
    @__init__.register(object, int, int)
    def __init___0(self, rows, columns):
        """ generated source for method __init___0 """
        super(TableLayout, self).__init__()
        self.__init__(rows, columns, 0, 0)

    #  Constructor: TableLayout(rows, columns, hgap, vgap) 
    # 
    #  * Creates a new <code>TableLayout</code> object with the specified
    #  * row count, column count, alignment, horizontal gap, and vertical gap.
    #  *
    #  * @usage TableLayout layout = new TableLayout(rows, columns, hgap, vgap);
    #  * @param rows The number of rows, or 0 for no limit
    #  * @param columns The number of columns, or 0 for no limit
    #  * @param hgap The horizontal gap between columns
    #  * @param vgap The vertical gap between rows
    #  
    @__init__.register(object, int, int, int, int)
    def __init___1(self, rows, columns, hgap, vgap):
        """ generated source for method __init___1 """
        super(TableLayout, self).__init__()
        nRows = rows
        nColumns = columns
        hGap = hgap
        vGap = vgap
        horizontalAlignment = self.CENTER
        verticalAlignment = self.CENTER
        defaultFill = self.BOTH
        constraintTable = HashMap()
        propertyTable = HashMap()
        layoutTable = None

    #  Method: setColumnCount(columns) 
    # 
    #  * Resets the number of columns in the table.
    #  *
    #  * @usage layout.setColumnCount(columns);
    #  * @param columns The new number of columns
    #  
    def setColumnCount(self, columns):
        """ generated source for method setColumnCount """
        nColumns = columns
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: getColumnCount() 
    # 
    #  * Returns the number of columns in the table.
    #  *
    #  * @usage int columns = layout.getColumnCount();
    #  * @return The  number of columns
    #  
    def getColumnCount(self):
        """ generated source for method getColumnCount """
        return nColumns

    #  Method: setRowCount(rows) 
    # 
    #  * Resets the number of rows in the table.
    #  *
    #  * @usage layout.setRowCount(rows);
    #  * @param rows The new number of rows
    #  
    def setRowCount(self, rows):
        """ generated source for method setRowCount """
        nRows = rows
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: getRowCount() 
    # 
    #  * Returns the number of rows in the table.
    #  *
    #  * @usage int rows = layout.getRowCount();
    #  * @return The  number of rows
    #  
    def getRowCount(self):
        """ generated source for method getRowCount """
        return nRows

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
        horizontalAlignment = align
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: getHorizontalAlignment() 
    # 
    #  * Returns the horizontal alignment for the table.
    #  *
    #  * @usage int align = layout.getHorizontalAlignment();
    #  * @return The horizontal alignment for the table
    #  
    def getHorizontalAlignment(self):
        """ generated source for method getHorizontalAlignment """
        return horizontalAlignment

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
        verticalAlignment = align
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: getVerticalAlignment() 
    # 
    #  * Returns the vertical alignment for the table.
    #  *
    #  * @usage int align = layout.getVerticalAlignment();
    #  * @return The vertical alignment for the table
    #  
    def getVerticalAlignment(self):
        """ generated source for method getVerticalAlignment """
        return verticalAlignment

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
        defaultFill = fill
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: getDefaultFill() 
    # 
    #  * Returns the default fill parameter for components in the table.
    #  *
    #  * @usage int fill = layout.getDefaultFill();
    #  * @return The default fill parameter for components in the table
    #  
    def getDefaultFill(self):
        """ generated source for method getDefaultFill """
        return defaultFill

    #  Method: setHgap(pixels) 
    # 
    #  * Sets the horizontal gap between components.
    #  *
    #  * @usage layout.setHgap(pixels);
    #  * @param pixels The gap between components in pixels
    #  
    def setHgap(self, pixels):
        """ generated source for method setHgap """
        hGap = pixels
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: getHgap() 
    # 
    #  * Returns the horizontal gap between components.
    #  *
    #  * @usage int hgap = layout.getHgap();
    #  * @return The horizontal gap between components
    #  
    def getHgap(self):
        """ generated source for method getHgap """
        return hGap

    #  Method: setVgap(pixels) 
    # 
    #  * Sets the vertical gap between components.
    #  *
    #  * @usage layout.setVgap(pixels);
    #  * @param pixels The gap between components in pixels
    #  
    def setVgap(self, pixels):
        """ generated source for method setVgap """
        vGap = pixels
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: getVgap() 
    # 
    #  * Returns the vertical gap between components.
    #  *
    #  * @usage int vgap = layout.getVgap();
    #  * @return The vertical gap between components
    #  
    def getVgap(self):
        """ generated source for method getVgap """
        return vGap

    #  Method: setStrictGridBagModel(flag) 
    # 
    #  * Sets a flag indicating whether the layout manager should match the
    #  * model used in <code>GridBagLayout</code> even when that interpretation
    #  * seems wrong.  The differences show up in the following areas:
    #  *
    #  * <ul>
    #  * <li><i>Calculation of cell size.</i>  <code>GridBagLayout</code> uses
    #  * the minimum layout size of the component to determine the size of each
    #  * cell; <code>TableLayout</code> uses the preferred size.  In practice,
    #  * these two values are often the same, but it seems that the preferred
    #  * size makes considerably more sense in terms of how this layout is used.
    #  *
    #  * <li><i>Treatment of cells spanning several rows.</i>  In
    #  * <code>GridBagLayout</code>, each new row begins after the last
    #  * multirow cell in that row, even if there is  space to its left.
    #  * By default, <code>TableLayout</code> uses the HTML model in which
    #  * the cells begin at the left margin unless that column is itself
    #  * already occupied.
    #  * </ul>
    #  *
    #  * @usage layout.setStrictGridBagModel(flag);
    #  * @param flag <code>true</code> to use a strict <code>GridBagLayout</code> model
    #  * @noshow
    #  
    def setStrictGridBagModel(self, flag):
        """ generated source for method setStrictGridBagModel """
        useStrictGridBagModel = flag
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: isStrictGridBagModel() 
    # 
    #  * Returns <code>true</code> if this layout manager is treating multirow
    #  * cells exactly as <code>GridBagLayout</code> does.
    #  *
    #  * @usage if (layout.isStrictGridBagModel()) . . .
    #  * @return <code>true</code> if this manager is using the strict <code>GridBagLayout</code> model
    #  * @noshow
    #  
    def isStrictGridBagModel(self):
        """ generated source for method isStrictGridBagModel """
        return useStrictGridBagModel

    #  Method: setConstraints(comp, constraints) 
    # 
    #  * Sets the constraints for the component to a copy of the supplied
    #  * constraints.
    #  *
    #  * @usage layout.setConstraints(comp, constraints);
    #  * @param comp The component to be constrained
    #  * @param constraints The constraints object used to specify the layout
    #  
    @overloaded
    def setConstraints(self, comp, constraints):
        """ generated source for method setConstraints """
        constraintTable.put(comp, constraints.clone())
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: setConstraints(comp, constraints) 
    # 
    #  * Sets the constraints for the component to the constraints
    #  * specified by the string.
    #  *
    #  * @usage layout.setConstraints(comp, constraints);
    #  * @param comp The component to be constrained
    #  * @param constraints A string specifying the constraints
    #  
    @setConstraints.register(object, Component, str)
    def setConstraints_0(self, comp, constraints):
        """ generated source for method setConstraints_0 """
        self.setConstraints(comp, TableConstraints(constraints))

    #  Method: getConstraints(comp) 
    # 
    #  * Returns a copy of the constraints requested for the specified component.  The
    #  * constraints value is always converted to a <code>TableConstraints</code> so that
    #  * clients can use this class in preference to <code>GridBagConstraints</code>
    #  * without needing a type cast.
    #  *
    #  * @usage TableConstraints tc = layout.getConstraints(comp);
    #  * @param comp The component whose constraints are requested
    #  * @return A copy of the constraints object used to specify the layout
    #  
    def getConstraints(self, comp):
        """ generated source for method getConstraints """
        gbc = lookupConstraints(comp)
        return None if (gbc == None) else TableConstraints(gbc)

    #  LayoutManager interface 
    #  Method: addLayoutComponent(constraints, comp) 
    # 
    #  * Adds a component to the layout.  Implements <code>LayoutManager</code>.
    #  *
    #  * @param constraints The constraint string
    #  * @param comp The component to be added
    #  * @noshow
    #  
    @overloaded
    def addLayoutComponent(self, constraints, comp):
        """ generated source for method addLayoutComponent """
        self.addLayoutComponent(comp, constraints)

    #  Method: removeLayoutComponent(comp) 
    # 
    #  * Removes the specified component from the layout.
    #  *
    #  * @param comp The component to be removed
    #  * @noshow
    #  
    def removeLayoutComponent(self, comp):
        """ generated source for method removeLayoutComponent """
        constraintTable.remove(comp)
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: preferredLayoutSize(target) 
    # 
    #  * Calculates the preferred size for the <code>FrameLayout</code> component
    #  * when laid out in the <code>target</code> container.
    #  *
    #  * @param target The container in which the layout is done
    #  * @return The preferred dimensions for the layout
    #  * @noshow
    #  
    def preferredLayoutSize(self, target):
        """ generated source for method preferredLayoutSize """
        if target.getComponentCount() == 0:
            return Dimension(0, 0)
        return processLayout(target, PREFERRED_LAYOUT_SIZE_MODE)

    #  Method: minimumLayoutSize(target) 
    # 
    #  * Calculates the minimum size for the <code>FrameLayout</code> component
    #  * when laid out in the <code>target</code> container.
    #  *
    #  * @param target The container in which the layout is done
    #  * @return The minimum dimensions for the layout
    #  * @noshow
    #  
    def minimumLayoutSize(self, target):
        """ generated source for method minimumLayoutSize """
        if target.getComponentCount() == 0:
            return Dimension(0, 0)
        return processLayout(target, MINIMUM_LAYOUT_SIZE_MODE)

    #  Method: layoutContainer(target) 
    # 
    #  * Lays out the components in the target container.
    #  *
    #  * @param target The container in which the layout is done
    #  * @noshow
    #  
    def layoutContainer(self, target):
        """ generated source for method layoutContainer """
        targetContainer = target
        processLayout(target, LAYOUT_CONTAINER_MODE)

    #  Method: addLayoutComponent(comp, constraints) 
    # 
    #  * Adds a component to the layout.  The <code>TableLayout</code>
    #  * class overrides this method to allow for string constraints.
    #  *
    #  * @param comp The component to be added
    #  * @param constraints The constraint object
    #  * @noshow
    #  
    @addLayoutComponent.register(object, Component, object)
    def addLayoutComponent_0(self, comp, constraints):
        """ generated source for method addLayoutComponent_0 """
        if constraints == None:
            constraints = TableConstraints("")
            (constraints).fill = defaultFill
        elif isinstance(constraints, (str, )):
            options = OptionTable((str(constraints)).lower(), TableConstraints.LEGAL_KEYS)
            constraints = TableConstraints(options.getMap())
            if not options.isSpecified("fill"):
                (constraints).fill = self.NONE if (options.isSpecified("anchor")) else defaultFill
        elif not (isinstance(constraints, (GridBagConstraints, ))):
            raise ErrorException("TableLayout: Illegal constraints")
        constraintTable.put(comp, constraints)
        if targetContainer != None:
            targetContainer.invalidate()

    #  Method: maximumLayoutSize(target) 
    # 
    #  * Calculates the maximum size for the <code>FrameLayout</code> component
    #  * when laid out in the <code>target</code> container.
    #  *
    #  * @param target The container in which the layout is done
    #  * @return The maximum dimensions for the layout
    #  * @noshow
    #  
    def maximumLayoutSize(self, target):
        """ generated source for method maximumLayoutSize """
        return Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE)

    #  Method: getLayoutAlignmentX(target) 
    # 
    #  * Returns the alignment along the <i>x</i>-axis as described in the
    #  * <code>LayoutManager2</code> interface.
    #  *
    #  * @param target The container in which the layout is done
    #  * @return A value between 0 and 1 indicating where this component should align
    #  * @noshow
    #  
    def getLayoutAlignmentX(self, target):
        """ generated source for method getLayoutAlignmentX """
        return 0.5

    #  Method: getLayoutAlignmentY(target) 
    # 
    #  * Returns the alignment along the <i>y</i>-axis as described in the
    #  * <code>LayoutManager2</code> interface.
    #  *
    #  * @param target The container in which the layout is done
    #  * @return A value between 0 and 1 indicating where this component should align
    #  * @noshow
    #  
    def getLayoutAlignmentY(self, target):
        """ generated source for method getLayoutAlignmentY """
        return 0.5

    #  Method: invalidateLayout(target) 
    # 
    #  * Indicates that the layout is no longer valid.
    #  *
    #  * @param target The container in which the layout is done
    #  * @noshow
    #  
    @synchronized
    def invalidateLayout(self, target):
        """ generated source for method invalidateLayout """
        layoutTable = None
        iterator = propertyTable.keySet().iterator()
        while iterator.hasNext():
            key = iterator.next()
            if key.startsWith("width") and not key == "width":
                propertyTable.put(key, int(0))
            if key.startsWith("height") and not key == "height":
                propertyTable.put(key, int(0))
            if key.startsWith("weightx") and not key == "weightx":
                propertyTable.put(key, float(0))
            if key.startsWith("weighty") and not key == "weighty":
                propertyTable.put(key, float(0))

    #  Override method: toString() 
    # 
    #  * Creates a printable representation of the layout.
    #  * @noshow
    #  
    def __str__(self):
        """ generated source for method toString """
        str_ = getClass().__name__
        str_ += "[rows=" + nRows + ",columns=" + nColumns
        if hGap != 0:
            str_ += ",hgap=" + hGap
        if vGap != 0:
            str_ += ",vgap=" + vGap
        str_ += "]"
        return str_

    #  Protected method: lookupConstraints(comp) 
    # 
    #  * Returns the constraints object for the specified component.
    #  *
    #  * @usage GridBagConstraints gbc = layout.lookupConstraints(comp);
    #  * @param comp The component to be constrained
    #  * @return The constraints object used to specify the layout
    #  
    @overloaded
    def lookupConstraints(self, comp):
        """ generated source for method lookupConstraints """
        return constraintTable.get(comp)

    #  Protected method: lookupConstraints(comp, target) 
    # 
    #  * Returns the <code>TableConstraints</code> object actually applied to the specified
    #  * component when it is laid out in the target container.  In the result of this method
    #  * the values of the <code>gridx</code>, <code>gridx</code>, <code>gridwidth</code>,
    #  * and <code>gridheight</code> fields are filled in according to the actual position
    #  * in the grid.
    #  *
    #  * @usage TableConstraints tc = layout.lookupConstraints(comp, target);
    #  * @param comp The component to be constrained
    #  * @param target The container in which the layout is done
    #  * @return The constraints object actually applied to the layout
    #  
    @lookupConstraints.register(object, Component, Container)
    def lookupConstraints_0(self, comp, target):
        """ generated source for method lookupConstraints_0 """
        with lock_for_object(target.getTreeLock()):
            if layoutTable == None:
                computeLayoutTable(target)
            return layoutTable.get(comp)

    #  Protected method: getMinimumComponentSize(comp) 
    # 
    #  * This method returns the minimum size of the component for this layout.  Subclasses
    #  * can override this methods to establish specific bounds for certain component
    #  * classes, such as the code for scrollbars given here.
    #  *
    #  * @usage Dimension size = layout.getMinimumComponentSize(comp);
    #  * @param comp The component whose size is being tested
    #  * @return The minimum size for that component
    #  
    def getMinimumComponentSize(self, comp):
        """ generated source for method getMinimumComponentSize """
        if isScrollbar(comp):
            return getMinimumScrollbarSize(comp)
        return comp.getMinimumSize()

    #  Protected method: getPreferredComponentSize(comp) 
    # 
    #  * This method returns the preferred size of the component for this layout.  Subclasses
    #  * can override this methods to establish specific bounds for certain component
    #  * classes, such as the code for scrollbars given here.
    #  *
    #  * @usage Dimension size = layout.getPreferredComponentSize(comp);
    #  * @param comp The component whose size is being tested
    #  * @return The preferred size for that component
    #  
    def getPreferredComponentSize(self, comp):
        """ generated source for method getPreferredComponentSize """
        if isScrollbar(comp):
            return getMinimumScrollbarSize(comp)
        return comp.getPreferredSize()

    #  Protected method: isScrollbar(comp) 
    # 
    #  * Determines whether the component is a scroll bar or slider.
    #  
    def isScrollbar(self, comp):
        """ generated source for method isScrollbar """
        return (isinstance(comp, (Scrollbar, )) or isinstance(comp, (JScrollBar, )) or isinstance(comp, (JSlider, )))

    #  Protected method: getMinimumScrollbarSize(comp) 
    # 
    #  * Determines the minimum dimensions for this scrollbar, making sure it has enough
    #  * space to be displayed with a nonzero slider area.
    #  
    def getMinimumScrollbarSize(self, comp):
        """ generated source for method getMinimumScrollbarSize """
        size = comp.getMinimumSize()
        try:
            scrollbarClass = comp.__class__
            getOrientation = scrollbarClass.getMethod("getOrientation", [None] * 0)
            orientation = (int(getOrientation.invoke(comp, [None] * 0))).intValue()
            if orientation == Scrollbar.HORIZONTAL:
                size.width = max(size.width, MINIMUM_SCROLLBAR_SIZE)
            else:
                size.height = max(size.height, MINIMUM_SCROLLBAR_SIZE)
        except Exception as ex:
            raise ErrorException(ex)
        return size

    #  Private method: processLayout(target, caller) 
    # 
    #  * Common code for the different methods requiring layout synchronization.
    #  * The <code>caller</code> argument is one of the three constants
    #  * LAYOUT_CONTAINER_MODE, PREFERRED_LAYOUT_SIZE_MODE, or MINIMUM_LAYOUT_SIZE_MODE,
    #  * depending on the caller.
    #  
    def processLayout(self, target, caller):
        """ generated source for method processLayout """
        with lock_for_object(target.getTreeLock()):
            return lockedProcessLayout(target, caller)

    #  Private method: lockedProcessLayout(target, caller) 
    # 
    #  * Method to do the work of <code>processLayout</code> after synchronization.
    #  
    @synchronized
    def lockedProcessLayout(self, target, caller):
        """ generated source for method lockedProcessLayout """
        result = None
        if layoutTable == None:
            computeLayoutTable(target)
        nr = getIntProperty("nRows")
        nc = getIntProperty("nColumns")
        heights = [None] * nr
        widths = [None] * nc
        nComponents = target.getComponentCount()
        i = 0
        while i < nComponents:
            comp = target.getComponent(i)
            tc = layoutTable.get(comp)
            column = tc.gridx
            row = tc.gridy
            width = getIntProperty("width" + column)
            height = getIntProperty("height" + row)
            if width == 0:
                if caller == MINIMUM_LAYOUT_SIZE_MODE or useStrictGridBagModel:
                    width = self.getMinimumComponentSize(comp).width
                else:
                    width = self.getPreferredComponentSize(comp).width
                width += 2 * tc.ipadx + tc.insets.left + tc.insets.right
            if height == 0:
                if caller == MINIMUM_LAYOUT_SIZE_MODE or useStrictGridBagModel:
                    height = self.getMinimumComponentSize(comp).height
                else:
                    height = self.getPreferredComponentSize(comp).height
                height += 2 * tc.ipady + tc.insets.top + tc.insets.bottom
            if tc.gridwidth <= 1:
                widths[column] = max(widths[column], width)
            if tc.gridheight <= 1:
                heights[row] = max(heights[row], height)
            i += 1
        width = hGap
        height = vGap
        weightX = [None] * nc
        weightY = [None] * nr
        totalX = 0
        totalY = 0
        column = 0
        while column < nc:
            width += widths[column] + hGap
            weightX[column] = getDoubleProperty("weightx" + column)
            totalX += weightX[column]
            column += 1
        row = 0
        while row < nr:
            height += heights[row] + vGap
            weightY[row] = getDoubleProperty("weighty" + row)
            totalY += weightY[row]
            row += 1
        if caller == LAYOUT_CONTAINER_MODE:
            size = target.getSize()
            insets = target.getInsets()
            size.width -= insets.left + insets.right
            size.height -= insets.top + insets.bottom
            extraX = size.width - width
            extraY = size.height - height
            startX = insets.left
            startY = insets.top
            if totalX == 0:
                if horizontalAlignment == self.LEFT:
                    extraX = 0
                elif horizontalAlignment == self.CENTER:
                    startX += extraX / 2
                    extraX = 0
                elif horizontalAlignment == self.RIGHT:
                    startX += extraX
                    extraX = 0
                elif horizontalAlignment == self.FILL:
                    totalX = nc
                    column = 0
                    while column < nc:
                        weightX[column] = 1
                        column += 1
            if totalY == 0:
                if verticalAlignment == self.TOP:
                    extraY = 0
                elif verticalAlignment == self.CENTER:
                    startY += extraY / 2
                    extraY = 0
                elif verticalAlignment == self.BOTTOM:
                    startY += extraY
                    extraY = 0
                elif verticalAlignment == self.FILL:
                    totalY = nr
                    row = 0
                    while row < nr:
                        weightY[row] = 1
                        row += 1
            xc = [None] * nc
            x = hGap + startX
            column = 0
            while column < nc:
                xc[column] = x
                if extraX > 0:
                    pad = int(round(extraX * weightX[column] / totalX))
                    widths[column] += pad
                    extraX -= pad
                    totalX -= weightX[column]
                x += widths[column] + hGap
                column += 1
            yc = [None] * nr
            y = vGap + startY
            row = 0
            while row < nr:
                yc[row] = y
                if extraY > 0:
                    pad = int(round(extraY * weightY[row] / totalY))
                    heights[row] += pad
                    extraY -= pad
                    totalY -= weightY[row]
                y += heights[row] + vGap
                row += 1
            i = 0
            while i < nComponents:
                comp = target.getComponent(i)
                tc = layoutTable.get(comp)
                column = tc.gridx
                row = tc.gridy
                bx = xc[column] + tc.insets.left
                by = yc[row] + tc.insets.top
                bw = widths[column]
                ix = 1
                while ix < tc.gridwidth and column + ix < nc:
                    bw += widths[column + ix] + hGap
                    ix += 1
                bw -= tc.insets.left + tc.insets.right
                bh = heights[row]
                iy = 1
                while iy < tc.gridheight and row + iy < nr:
                    bh += heights[row + iy] + vGap
                    iy += 1
                bh -= tc.insets.top + tc.insets.bottom
                pSize = self.getMinimumComponentSize(comp) if (useStrictGridBagModel) else self.getPreferredComponentSize(comp)
                bounds = computeCellBounds(Rectangle(bx, by, bw, bh), pSize, tc)
                comp.setBounds(bounds.x, bounds.y, bounds.width, bounds.height)
                i += 1
        else:
            result = Dimension(width, height)
        return result

    #  Private method: computeLayoutTable(target) 
    # 
    #  * Updates the layoutTable constraints for each component in <code>target</code>.
    #  * All elements whose <code>gridx</code> or <code>gridy</code> constraints
    #  * are <code>RELATIVE</code> are changed to explicit grid references by
    #  * interpreting the <code>gridwidth</code> and <code>gridheight</code>
    #  * constraints.
    #  *
    #  * @usage computeLayoutTable(target);
    #  * @param target The target container
    #  
    def computeLayoutTable(self, target):
        """ generated source for method computeLayoutTable """
        unfinishedSpans = None
        row = 0
        column = 0
        layoutColumns = nColumns
        nComponents = target.getComponentCount()
        nextEndRow = False
        layoutTable = HashMap()
        i = 0
        while i < nComponents:
            comp = target.getComponent(i)
            tc = self.getConstraints(comp)
            if tc.gridx != GridBagConstraints.RELATIVE:
                column = tc.gridx
            if tc.gridy != GridBagConstraints.RELATIVE:
                row = tc.gridy
            if nRows > 0 and row >= nRows:
                raise ErrorException("TableLayout: Too many rows specified")
            while unfinishedSpans != None and len(unfinishedSpans) and unfinishedSpans[column] > 0:
                column += 1
                if layoutColumns > 0 and column >= layoutColumns:
                    c = 0
                    while len(unfinishedSpans):
                        if unfinishedSpans[c] > 0:
                            unfinishedSpans[c] -= 1
                        c += 1
                    row += 1
                    column = getFirstAvailableColumn(unfinishedSpans)
            tc.gridx = column
            tc.gridy = row
            endrow = nextEndRow
            setMaxProperty("width" + column, tc.width)
            setMaxProperty("height" + row, tc.height)
            setMaxProperty("weightx" + column, tc.weightx)
            setMaxProperty("weighty" + row, tc.weighty)
            colspan = 1
            if tc.gridwidth == GridBagConstraints.REMAINDER:
                endrow = True
                if layoutColumns > 0:
                    colspan = layoutColumns - column
            elif tc.gridwidth == GridBagConstraints.RELATIVE:
                if layoutColumns <= 0:
                    raise ErrorException("TableLayout: Illegal to use gridwidth=RELATIVE in first row")
                colspan = layoutColumns - column - 1
                nextEndRow = True
            else:
                colspan = tc.gridwidth
                endrow = (nColumns > 0 and column + tc.gridwidth >= nColumns)
            if colspan > 1 and unfinishedSpans != None:
                c = column
                while c < min(column + colspan, ):
                    if unfinishedSpans[c] != 0:
                        raise ErrorException("TableLayout: Overlapping cells")
                    c += 1
            rowspan = 1
            if tc.gridheight == GridBagConstraints.REMAINDER:
                rowspan = Integer.MAX_VALUE
            elif tc.gridheight == GridBagConstraints.RELATIVE:
                raise ErrorException("TableLayout: Illegal to use gridheight=RELATIVE")
            else:
                rowspan = tc.gridheight
            if rowspan > 1:
                if unfinishedSpans == None:
                    unfinishedSpans = [None] * column + colspan
                elif len(unfinishedSpans):
                    oldSpans = unfinishedSpans
                    unfinishedSpans = [None] * column + colspan
                    System.arraycopy(oldSpans, 0, unfinishedSpans, 0, )
                c = column
                while c < column + colspan:
                    unfinishedSpans[c] = rowspan
                    c += 1
            tc.gridwidth = colspan
            tc.gridheight = rowspan
            layoutTable.put(comp, tc)
            column += colspan
            while endrow or (layoutColumns > 0 and column >= layoutColumns):
                if layoutColumns <= 0:
                    layoutColumns = column
                if unfinishedSpans != None:
                    c = 0
                    while len(unfinishedSpans):
                        if unfinishedSpans[c] > 0:
                            unfinishedSpans[c] -= 1
                        c += 1
                row += 1
                column = getFirstAvailableColumn(unfinishedSpans)
                endrow = False
            i += 1
        if layoutColumns <= 0:
            layoutColumns = column
        setIntProperty("nColumns", layoutColumns)
        setIntProperty("nRows", row + 1)

    def computeCellBounds(self, enclosure, psize, tc):
        """ generated source for method computeCellBounds """
        x = enclosure.x
        y = enclosure.y
        width = enclosure.width
        height = enclosure.height
        if tc.fill == TableConstraints.NONE or tc.fill == TableConstraints.VERTICAL:
            width = psize.width
        if tc.fill == TableConstraints.NONE or tc.fill == TableConstraints.HORIZONTAL:
            height = psize.height
        if width != enclosure.width:
            if tc.anchor == TableConstraints.NORTH:
                pass
            elif tc.anchor == TableConstraints.CENTER:
                pass
            elif tc.anchor == TableConstraints.SOUTH:
                x += (enclosure.width - width) / 2
            elif tc.anchor == TableConstraints.NORTHEAST:
                pass
            elif tc.anchor == TableConstraints.EAST:
                pass
            elif tc.anchor == TableConstraints.SOUTHEAST:
                x += enclosure.width - width
        if height != enclosure.height:
            if tc.anchor == TableConstraints.WEST:
                pass
            elif tc.anchor == TableConstraints.CENTER:
                pass
            elif tc.anchor == TableConstraints.EAST:
                y += (enclosure.height - height) / 2
            elif tc.anchor == TableConstraints.SOUTHWEST:
                pass
            elif tc.anchor == TableConstraints.SOUTH:
                pass
            elif tc.anchor == TableConstraints.SOUTHEAST:
                y += enclosure.height - height
        return Rectangle(x, y, width, height)

    @overloaded
    def setMaxProperty(self, key, value):
        """ generated source for method setMaxProperty """
        setIntProperty(key, max(value, getIntProperty(key)))

    @setMaxProperty.register(object, str, float)
    def setMaxProperty_0(self, key, value):
        """ generated source for method setMaxProperty_0 """
        setDoubleProperty(key, max(value, getDoubleProperty(key)))

    def setIntProperty(self, key, value):
        """ generated source for method setIntProperty """
        propertyTable.put(key, int(value))

    def getIntProperty(self, key):
        """ generated source for method getIntProperty """
        binding = propertyTable.get(key)
        if binding == None:
            return 0
        return (int(binding)).intValue()

    def setDoubleProperty(self, key, value):
        """ generated source for method setDoubleProperty """
        propertyTable.put(key, float(value))

    def getDoubleProperty(self, key):
        """ generated source for method getDoubleProperty """
        binding = propertyTable.get(key)
        if binding == None:
            return 0.0
        return (float(binding)).doubleValue()

    def getFirstAvailableColumn(self, unfinishedSpans):
        """ generated source for method getFirstAvailableColumn """
        if useStrictGridBagModel and unfinishedSpans != None:
            column = int()
            while column > 0:
                if unfinishedSpans[column - 1] > 0:
                    return column
                column -= 1
        return 0

    LAYOUT_CONTAINER_MODE = 0
    MINIMUM_LAYOUT_SIZE_MODE = 1
    PREFERRED_LAYOUT_SIZE_MODE = 2
    MINIMUM_SCROLLBAR_SIZE = 100
    targetContainer = None
    constraintTable = None
    layoutTable = None
    propertyTable = None
    useStrictGridBagModel = bool()
    nRows = int()
    nColumns = int()
    horizontalAlignment = int()
    verticalAlignment = int()
    defaultFill = int()
    hGap = int()
    vGap = int()
    serialVersionUID = 1

