#!/usr/bin/env python
""" generated source for module GCanvas """
from __future__ import print_function
from GContainer import *
# from GObject import *
# from GFillable import *
# from  GScalable import *
# from unresolved import *


# 
#  * @(#)GCanvas.java   1.99.1 08/12/08
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
#  Bug fix 27-Jul-06 (ESR, JTFBug 2006-001, reported by Chris Nevison)
#    1. Fixed implementation of enabledList.
# 
#  Bug fix 26-Apr-07 (ESR, JTFBug 2007-005, reported by Leland Beck)
#    1. Removed cross-file reference to GMouseEvent.
# 
#  Code cleanup 28-May-07 (ESR)
#    1. Added generic type tags.
#    2. Substituted GObjectList for ArrayList.
#    3. Removed warnings about use of Iterator.
# 
#  Feature enhancement 26-May-08 (ESR)
#    1. Added support for serialization.
# package: acm.graphics
#  Class: GCanvas 
# 
#  * The <code>GCanvas</code> class is a lightweight component that also
#  * serves as a container for graphical objects.  As such, this class
#  * provides the link between graphical objects and the window system.
#  * Conceptually, the <code>GCanvas</code> provides a background canvas
#  * to which other graphical objects can be added.
#  class GCanvas(Container, GContainer):

class GCanvas(Container):
    """ generated source for class GCanvas """
    #  Constructor: GCanvas() 
    # 
    #  * Creates a new <code>GCanvas</code> that contains no objects.
    #  *
    #  * @usage GCanvas gc = new GCanvas();
    #  
    def __init__(self):
        """ generated source for method __init__ """
        super(GCanvas, self).__init__()
        contents = GObjectList(self)
        setBackground(Color.WHITE)
        setForeground(Color.BLACK)
        setOpaque(True)
        setAutoRepaintFlag(True)
        setNativeArcFlag(False)
        setLayout(None)
        gCanvasListener = GCanvasListener(self)
        addComponentListener(gCanvasListener)
        addMouseListener(gCanvasListener)
        addMouseMotionListener(gCanvasListener)

    #  Method: add(gobj) 
    # 
    #  * Adds the graphical object to this canvas.
    #  *
    #  * @usage gc.add(gobj);
    #  * @param gobj The graphical object to add
    #  
    # @overloaded
    def add(self, gobj):
        """ generated source for method add """
        contents.add(gobj)
        conditionalRepaint()

    #  Method: add(gobj, x, y) 
    # 
    #  * Adds the graphical object to this canvas and sets its location
    #  * to the point (<code>x</code>,&nbsp;<code>y</code>).
    #  *
    #  * @usage gc.add(gobj, x, y);
    #  * @param gobj The graphical object to add
    #  * @param x The new x-coordinate for the object
    #  * @param y The new y-coordinate for the object
    #  
    # @add.register(object, GObject, float, float)
    def add_0(self, gobj, x, y):
        """ generated source for method add_0 """
        gobj.setLocation(x, y)
        self.add(gobj)

    #  Method: add(gobj, pt) 
    # 
    #  * Adds the graphical object to this canvas and sets its location to the specified point.
    #  *
    #  * @usage gc.add(gobj, pt);
    #  * @param gobj The graphical object to add
    #  * @param pt A <code>GPoint</code> object giving the coordinates of the point
    #  
    # @add.register(object, GObject, GPoint)
    def add_1(self, gobj, pt):
        """ generated source for method add_1 """
        self.add(gobj, pt.getX(), pt.getY())

    #  Method: remove(gobj) 
    # 
    #  * Removes a graphical object from this <code>GCanvas</code>.
    #  *
    #  * @usage gc.remove(gobj);
    #  * @param gobj The graphical object to remove
    #  
    # @overloaded
    def remove(self, gobj):
        """ generated source for method remove """
        contents.remove(gobj)
        conditionalRepaint()

    #  Method: removeAll() 
    # 
    #  * Removes all graphical objects from this <code>GCanvas</code>.
    #  *
    #  * @usage gc.removeAll();
    #  
    def removeAll(self):
        """ generated source for method removeAll """
        contents.removeAll()
        super(GCanvas, self).removeAll()
        repaint()

    #  Method: add(comp) 
    # 
    #  * Adds the component to this canvas without changing its location.
    #  * If the component has no size, its size is set to its preferred size.
    #  * The return type is <code>Component</code> to match the method in
    #  * the <code>Container</code> class, but the result is typically
    #  * ignored.
    #  *
    #  * @usage gc.add(comp);
    #  * @param comp The component to add
    #  
    # @add.register(object, Component)
    def add_2(self, comp):
        """ generated source for method add_2 """
        super(GCanvas, self).add(comp)
        size = comp.getSize()
        if size.width == 0 or size.height == 0:
            preferredSize = comp.getPreferredSize()
            if size.width == 0:
                size.width = preferredSize.width
            if size.height == 0:
                size.height = preferredSize.height
            comp.setSize(size)
        return comp

    #  Method: add(comp, x, y) 
    # 
    #  * Adds the component to this canvas and sets its location
    #  * to the point (<code>x</code>,&nbsp;<code>y</code>).
    #  *
    #  * @usage gc.add(comp, x, y);
    #  * @param comp The component to add
    #  * @param x The new x-coordinate for the object
    #  * @param y The new y-coordinate for the object
    #  
    # @add.register(object, Component, float, float)
    def add_3(self, comp, x, y):
        """ generated source for method add_3 """
        comp.setLocation(Ground(x), Ground(y))
        self.add(comp)

    #  Method: add(comp, pt) 
    # 
    #  * Adds the component to this canvas and sets its location to the specified point.
    #  *
    #  * @usage gc.add(comp, pt);
    #  * @param comp The component to add
    #  * @param pt A <code>GPoint</code> object giving the coordinates of the point
    #  
    # @add.register(object, Component, GPoint)
    def add_4(self, comp, pt):
        """ generated source for method add_4 """
        self.add(comp, pt.getX(), pt.getY())

    #  Method: remove(comp) 
    # 
    #  * Removes the component from the canvas.
    #  *
    #  * @usage gc.remove(comp);
    #  * @param comp The component to remove
    #  
    # @remove.register(object, Component)
    def remove_0(self, comp):
        """ generated source for method remove_0 """
        super(GCanvas, self).remove(comp)
        conditionalRepaint()

    #  Method: getElementCount() 
    # 
    #  * Returns the number of graphical objects stored in this <code>GCanvas</code>.
    #  *
    #  * @usage int n = gc.getElementCount();
    #  * @return The number of graphical objects in this <code>GCanvas</code>
    #  
    def getElementCount(self):
        """ generated source for method getElementCount """
        return contents.getElementCount()

    #  Method: getElement(index) 
    # 
    #  * Returns the graphical object at the specified index, numbering from back
    #  * to front in the the <i>z</i> dimension.
    #  *
    #  * @usage GObject gobj = gc.getElement(index);
    #  * @param index The index of the component to return
    #  * @return The graphical object at the specified index
    #  
    def getElement(self, index):
        """ generated source for method getElement """
        return contents.getElement(index)

    #  Method: getElementAt(x, y) 
    # 
    #  * Returns the topmost graphical object that contains the point
    #  * (<code>x</code>, <code>y</code>), or <code>null</code> if no such
    #  * object exists.
    #  *
    #  * @usage GObject gobj = gc.getElementAt(x, y);
    #  * @param x The x-coordinate of the point being tested
    #  * @param y The y-coordinate of the point being tested
    #  * @return The graphical object at the specified location, or <code>null</code>
    #  *         if no such object exists
    #  
    # @overloaded
    def getElementAt(self, x, y):
        """ generated source for method getElementAt """
        return contents.getElementAt(x, y, False)

    #  Method: getElementAt(pt) 
    # 
    #  * Returns the topmost graphical object that contains the specified point,
    #  * or <code>null</code> if no such object exists.
    #  *
    #  * @usage GObject gobj = gc.getElementAt(pt);
    #  * @param pt The coordinates being tested
    #  * @return The graphical object at the specified location, or <code>null</code>
    #  *         if no such object exists
    #  
    # @getElementAt.register(object, GPoint)
    def getElementAt_0(self, pt):
        """ generated source for method getElementAt_0 """
        return self.getElementAt(pt.getX(), pt.getY())

    #  Method: iterator() 
    # 
    #  * Returns an <code>Iterator</code> that cycles through the elements within
    #  * this container in the default direction, which is from back to front.
    #  * You can also run the iterator in the opposite direction by using the
    #  * <a href="#iterator(int)"><code>iterator</code></a><code>(</code><font
    #  * size=-1><i>direction</i></font><code>)</code> form of this method.
    #  *
    #  * @usage Iterator<GObject> i = gc.iterator();
    #  * @return An <code>Iterator</code> ranging over the elements of the
    #  *         container from back to front
    #  
    # @overloaded
    def iterator(self):
        """ generated source for method iterator """
        return GIterator(self, GContainer.BACK_TO_FRONT)

    #  Method: iterator(direction) 
    # 
    #  * Returns an <code>Iterator</code> that cycles through the elements
    #  * within this container in the specified direction, which must be one
    #  * of the constants <a href="GContainer.html#FRONT_TO_BACK"><code>GContainer.FRONT_TO_BACK</code></a>
    #  * or <a href="GContainer.html#BACK_TO_FRONT"><code>GContainer.BACK_TO_FRONT</code></a>.<p>
    #  *
    #  * <p><pre><code>
    #  * &nbsp;    for (Iterator&lt;GObject&gt; i = gc.iterator(direction); i.hasNext(); )
    #  * </code></pre>
    #  *
    #  * @usage Iterator<GObject> i = gc.iterator(direction);
    #  * @return An <code>Iterator</code> ranging over the elements of the
    #  *         container in the specified direction
    #  
    # @iterator.register(object, int)
    def iterator_0(self, direction):
        """ generated source for method iterator_0 """
        return GIterator(self, direction)

    #  Method: setOpaque(flag) 
    # 
    #  * Sets a flag indicating whether this canvas is opaque, which means that it
    #  * obscures anything behind it.  Setting this flag to <code>false</code> makes
    #  * the <code>GCanvas</code> transparent, so that any other lightweight components
    #  * behind it show through.
    #  *
    #  * @usage gc.setOpaque(flag);
    #  * @param flag <code>true</code> to make this canvas opaque, and <code>false</code>
    #  *             to make it transparent
    #  * @noshow
    #  
    def setOpaque(self, flag):
        """ generated source for method setOpaque """
        opaque = flag
        conditionalRepaint()

    #  Method: isOpaque() 
    # 
    #  * Returns a boolean value indicating whether this canvas is opaque.
    #  *
    #  * @usage if (gc.isOpaque(flag)) . . .
    #  * @return <code>true</code> if this canvas is opaque, and <code>false</code>
    #  *          if it is transparent
    #  * @noshow
    #  
    def isOpaque(self):
        """ generated source for method isOpaque """
        return opaque

    #  Method: getWidth() 
    # 
    #  * Returns the width of this canvas in pixels.  This method is defined in JDK 1.2
    #  * components, but not in earlier ones.  Defining this method here makes this entry
    #  * available in all browsers.
    #  *
    #  * @usage int width = gc.getWidth();
    #  * @return The width of this canvas
    #  
    def getWidth(self):
        """ generated source for method getWidth """
        return getSize().width

    #  Method: getHeight() 
    # 
    #  * Returns the height of this canvas in pixels.  This method is defined in JDK 1.2
    #  * components, but not in earlier ones.  Defining this method here makes this entry
    #  * available in all browsers.
    #  *
    #  * @usage int height = gc.getHeight();
    #  * @return The height of this canvas in pixels
    #  
    def getHeight(self):
        """ generated source for method getHeight """
        return getSize().height

    #  Method: paint(g) 
    # 
    #  * Paints the canvas.  This method is not ordinarily called by clients.
    #  *
    #  * @usage gc.paint(g);
    #  * @param g The graphics context into which the canvas is painted
    #  * @noshow
    #  
    def paint(self, g):
        """ generated source for method paint """
        g0 = g
        if self.isOpaque():
            if offscreenImage == None:
                initOffscreenImage()
            if offscreenImage != None:
                g = offscreenImage.getGraphics()
            size = getSize()
            g.setColor(getBackground())
            g.fillRect(0, 0, size.width, size.height)
            g.setColor(getForeground())
        contents.mapPaint(g)
        if self.isOpaque() and offscreenImage != None:
            g0.drawImage(offscreenImage, 0, 0, self)
        super(GCanvas, self).paint(g0)

    #  Method: update(g) 
    # 
    #  * Updates the canvas.  This method is overridden here to support transparency
    #  * in the Swing style.
    #  *
    #  * @usage gc.update(g);
    #  * @param g The graphics context into which the canvas is painted
    #  * @noshow
    #  
    def update(self, g):
        """ generated source for method update """
        self.paint(g)

    #  Method: setAutoRepaintFlag(state) 
    # 
    #  * Changes the setting of the auto-repaint flag.  By default, any change to a
    #  * graphical object contained in this canvas automatically triggers a repaint
    #  * of the canvas as a whole.  While this behavior makes it much easier to use
    #  * the package, it has the disadvantage that repaint requests come much more
    #  * frequently than necessary.  You can disable this feature by calling
    #  * <code>setAutoRepaintFlag(false)</code>, but you must then make explicit
    #  * calls to <code>repaint()</code> whenever you want to update the display.
    #  * The advantage of this model is that you can then make many different changes
    #  * and have them all appear at once with a single <code>repaint</code> call.
    #  *
    #  * @usage gc.setAutoRepaintFlag(state);
    #  * @param state <code>true</code> to enable auto-repaint mode, and <code>false</code>
    #  *              to disable it
    #  
    def setAutoRepaintFlag(self, state):
        """ generated source for method setAutoRepaintFlag """
        autoRepaint = state

    #  Method: getAutoRepaintFlag() 
    # 
    #  * Returns the current setting of the auto-repaint flag as described in
    #  * <a href="#setAutoRepaintFlag(boolean)"><code>setAutoRepaintFlag</code></a>.
    #  *
    #  * @usage if (gc.getAutoRepaintFlag()) . . .
    #  * @return <code>true</code> if auto-repaint mode is enabled, and <code>false</code>
    #  *          otherwise
    #  
    def getAutoRepaintFlag(self):
        """ generated source for method getAutoRepaintFlag """
        return autoRepaint

    #  Method: setNativeArcFlag(state) 
    # 
    #  * Sets whether the redering code for <code>GArc</code> and <code>GOval</code> should use
    #  * Java arcs.  By default, arcs and ovals are rendered using polygons and polylines
    #  * to ensure that the same set of pixels is covered by the fill and frame.
    #  * If this value is set to <code>true</code>, the renderers will use the native
    #  * arc code, which is more efficient but less accurate.
    #  *
    #  * @usage gc.setNativeArcFlag(state);
    #  * @param state <code>true</code> to enable native arcs, <code>false</code> to use polygons
    #  
    def setNativeArcFlag(self, state):
        """ generated source for method setNativeArcFlag """
        nativeArcFlag = state

    #  Method: getNativeArcFlag() 
    # 
    #  * Returns the current setting of the native-arc flag as described in
    #  * <a href="#setNativeArcFlag(boolean)"><code>setNativeArcFlag</code></a>.
    #  *
    #  * @usage if (gc.getNativeArcFlag()) . . .
    #  * @return <code>true</code> if native arcs are enabled, and <code>false</code>
    #  *          otherwise
    #  
    def getNativeArcFlag(self):
        """ generated source for method getNativeArcFlag """
        return nativeArcFlag

    #  Protected method: sendToFront(gobj) 
    # 
    #  * Implements the <code>sendToFront</code> function from the <code>GContainer</code>
    #  * interface.  Clients should not be calling this method, but the semantics of
    #  * interfaces forces it to be exported.
    #  * @noshow
    #  
    def sendToFront(self, gobj):
        """ generated source for method sendToFront """
        contents.sendToFront(gobj)
        conditionalRepaint()

    #  Protected method: sendToBack(gobj) 
    # 
    #  * Implements the <code>sendToBack</code> function from the <code>GContainer</code>
    #  * interface.  Clients should not be calling this method, but the semantics of
    #  * interfaces forces it to be exported.
    #  * @noshow
    #  
    def sendToBack(self, gobj):
        """ generated source for method sendToBack """
        contents.sendToBack(gobj)
        conditionalRepaint()

    #  Protected method: sendForward(gobj) 
    # 
    #  * Implements the <code>sendForward</code> function from the <code>GContainer</code>
    #  * interface.  Clients should not be calling this method, but the semantics of
    #  * interfaces forces it to be exported.
    #  * @noshow
    #  
    def sendForward(self, gobj):
        """ generated source for method sendForward """
        contents.sendForward(gobj)
        conditionalRepaint()

    #  Protected method: sendBackward(gobj) 
    # 
    #  * Implements the <code>sendBackward</code> function from the <code>GContainer</code>
    #  * interface.  Clients should not be calling this method, but the semantics of
    #  * interfaces forces it to be exported.
    #  * @noshow
    #  
    def sendBackward(self, gobj):
        """ generated source for method sendBackward """
        contents.sendBackward(gobj)
        conditionalRepaint()

    #  Protected method: dispatchMouseEvent(e) 
    # 
    #  * Dispatches this mouse event to the uppermost graphical object for which
    #  * the active point is within the object bounds.
    #  *
    #  * @usage gc.dispatchMouseEvent(MouseEvent e);
    #  * @param e The event that triggered this response
    #  * @noshow
    #  
    def dispatchMouseEvent(self, e):
        """ generated source for method dispatchMouseEvent """
        gobj = contents.getElementAt(e.getX(), e.getY(), True)
        newEvent = None
        if gobj != lastObject:
            if lastObject != None:
                newEvent = GMouseEvent(lastObject, MouseEvent.MOUSE_EXITED, e)
                lastObject.fireMouseListeners(newEvent)
            if gobj != None:
                newEvent = GMouseEvent(gobj, MouseEvent.MOUSE_ENTERED, e)
                gobj.fireMouseListeners(newEvent)
        lastObject = gobj
        if dragObject != None:
            gobj = dragObject
        if gobj != None:
            id = e.getID()
            if id != MouseEvent.MOUSE_EXITED and id != MouseEvent.MOUSE_ENTERED:
                if id != MouseEvent.MOUSE_DRAGGED or dragObject != None:
                    if id == MouseEvent.MOUSE_PRESSED:
                        dragObject = gobj
                    elif id == MouseEvent.MOUSE_RELEASED:
                        dragObject = None
                    newEvent = GMouseEvent(gobj, id, e)
                    gobj.fireMouseListeners(newEvent)
        if newEvent != None and newEvent.isConsumed():
            e.consume()

    #  Protected method: initOffscreenImage() 
    # 
    #  * Initializes the offscreen memory image used for double buffering.
    #  *
    #  * @usage gc.initOffscreenImage();
    #  * @noshow
    #  
    def initOffscreenImage(self):
        """ generated source for method initOffscreenImage """
        size = getSize()
        if size.width <= 0 or size.height <= 0:
            return
        offscreenImage = createImage(size.width, size.height)

    #  Protected method: conditionalRepaint() 
    # 
    #  * Repaints the canvas if auto-repaint is in effect.  This method is called only
    #  * by the <a href="GObject.html#repaint()"><code>repaint</code></a> method in
    #  * <code>GObject</code> and is not accessible outside the package.
    #  *
    #  * @usage gc.conditionalRepaint();
    #  * @noshow
    #  
    def conditionalRepaint(self):
        """ generated source for method conditionalRepaint """
        if autoRepaint:
            repaint()

    #  Protected method: updateEnabledList() 
    # 
    #  * Reconstructs the enabledList list in the correct order.
    #  *
    #  * @usage gc.updateEnabledList();
    #  
    def updateEnabledList(self):
        """ generated source for method updateEnabledList """
        contents.updateEnabledList()

    #  Package-private static method: createMouseEvent(gobj, eventID, e) 
    # 
    #  * Creates a new <code>GMouseEvent</code> object with <code>gobj</code>
    #  * effective source and <code>eventID</code>; all other fields are
    #  * copied from the event <code>e</code>.  This method must be included
    #  * in this class to avoid cross-file references to GMouseEvent from
    #  * the GCompound class.
    #  
    # @classmethod
    def createMouseEvent(cls, gobj, eventID, e):
        """ generated source for method createMouseEvent """
        return GMouseEvent(gobj, eventID, e)

    #  Private instance variables 
    gCanvasListener = None
    lastObject = None
    dragObject = None
    contents = None
    offscreenImage = None
    autoRepaint = bool()
    nativeArcFlag = bool()
    opaque = bool()

#  Package class: GCanvasListener 
# 
#  * This class fields mouse events that occur in the <code>GCanvas</code>.
#  
class GCanvasListener(MouseListener, MouseMotionListener, ComponentListener):
    """ generated source for class GCanvasListener """
    #  Constructor: GCanvasListener(gc) 
    # 
    #  * Creates a new listener object that watches for mouse events in the
    #  * <code>GCanvas</code>.
    #  *
    #  * @usage GCanvasListener listener = new GCanvasListener(gc);
    #  * @param gc The <code>GCanvas</code> object to which this listens
    #  
    def __init__(self, gc):
        """ generated source for method __init__ """
        super(GCanvasListener, self).__init__()
        gCanvas = gc

    #  MouseListener interface 
    def mouseClicked(self, e):
        """ generated source for method mouseClicked """
        gCanvas.dispatchMouseEvent(e)

    def mousePressed(self, e):
        """ generated source for method mousePressed """
        gCanvas.requestFocus()
        gCanvas.dispatchMouseEvent(e)

    def mouseReleased(self, e):
        """ generated source for method mouseReleased """
        gCanvas.dispatchMouseEvent(e)

    def mouseEntered(self, e):
        """ generated source for method mouseEntered """
        gCanvas.dispatchMouseEvent(e)

    def mouseExited(self, e):
        """ generated source for method mouseExited """
        gCanvas.dispatchMouseEvent(e)

    #  MouseMotionListener interface 
    def mouseDragged(self, e):
        """ generated source for method mouseDragged """
        gCanvas.dispatchMouseEvent(e)

    def mouseMoved(self, e):
        """ generated source for method mouseMoved """
        gCanvas.dispatchMouseEvent(e)

    #  ComponentListener interface 
    def componentResized(self, e):
        """ generated source for method componentResized """
        gCanvas.initOffscreenImage()
        if gCanvas.isShowing():
            gCanvas.repaint()

    def componentHidden(self, e):
        """ generated source for method componentHidden """

    def componentMoved(self, e):
        """ generated source for method componentMoved """

    def componentShown(self, e):
        """ generated source for method componentShown """

    #  Private instance variables 
    gCanvas = None


class GMouseEvent(MouseEvent):
    """ generated source for class GMouseEvent """
    #  Constructor: GMouseEvent(gobj, eventID, e) 
    # 
    #  * Creates a new <code>GMouseEvent</code> object with <code>gobj</code>
    #  * effective source and <code>eventID</code>; all other fields are
    #  * copied from the event <code>e</code>.
    #  
    def __init__(self, gobj, eventID, e):
        """ generated source for method __init__ """
        super(GMouseEvent, self).__init__(e.isPopupTrigger())
        effectiveSource = gobj

    #  Method: getSource() 
    # 
    #  * Overrides <code>getSource</code> to return the effective source of this event,
    #  * which will typically be a <code>GObject</code> rather than the <code>GCanvas</code>
    #  * that triggered the event.
    #  
    def getSource(self):
        """ generated source for method getSource """
        return effectiveSource

    #  Method: getComponent() 
    # 
    #  * Overrides <code>getComponent</code> to return the <code>GCanvas</code>
    #  * that triggered the event.
    #  
    def getComponent(self):
        """ generated source for method getComponent """
        return super(GMouseEvent, self).getSource()

    #  Method: toString() 
    # 
    #  * Overrides <code>toString</code> to display the correct source for this event.
    #  
    def __str__(self):
        """ generated source for method toString """
        return getClass().__name__ + "[" + paramString() + "] on " + self.getSource()

    #  Private instance variables 
    effectiveSource = None

