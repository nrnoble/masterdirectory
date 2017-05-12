#!/usr/bin/env python
""" generated source for module GObject """
from __future__ import print_function

# JAVA: public abstract class GObject implements Cloneable, Serializable
class GObject():
    """ generated source for class GObject """
    #  Protected constructor: GObject() 
    # 
    #  * Constructs a new <code>GObject</code> and initializes its state.  This
    #  * constructor is never called explicitly, but is instead invoked by the
    #  * constructors of its subclasses.
    #  
    def __init__(self):
        """ generated source for method __init__ """
        super(GObject, self).__init__()
        isVisible = True
        mouseListenersEnabled = False

    #  Abstract method: paint(g) 
    # 
    #  * All subclasses of <code>GObject</code> must define a <code>paint</code>
    #  * method which allows the object to draw itself on the <code>Graphics</code>
    #  * context passed in as the parameter <code>g</code>.
    #  *
    #  * @usage gobj.paint(g);
    #  * @param g The graphics context into which the painting is done
    #  
    def paint(self, g):
        """ generated source for method paint """

    #  Abstract method: getBounds() 
    # 
    #  * Returns the bounding box of this object, which is defined to be the
    #  * smallest rectangle that covers everything drawn by the figure.  The
    #  * coordinates of this rectangle do not necessarily match the location
    #  * returned by <a href="#getLocation()"><code>getLocation</code></a>.
    #  * Given a <a href="GLabel.html"><code>GLabel</code></a> object, for
    #  * example, <a href="#getLocation()"><code>getLocation</code></a>
    #  * returns the coordinates of the point on the baseline at which the
    #  * string begins; <code>getBounds</code>, by contrast, returns a
    #  * rectangle that covers the entire window area occupied by the string.
    #  *
    #  * @usage GRectangle bounds = gobj.getBounds();
    #  * @return The bounding box for this object
    #  
    def getBounds(self):
        """ generated source for method getBounds """

    #  Method: setLocation(x, y) 
    # 
    #  * Sets the location of this object to the point (<code>x</code>, <code>y</code>).
    #  *
    #  * @usage gobj.setLocation(x, y);
    #  * @param x The new x-coordinate for the object
    #  * @param y The new y-coordinate for the object
    #  
    # @overloaded
    def setLocation(self, x, y):
        """ generated source for method setLocation """
        xc = x
        yc = y
        repaint()

    #  Method: setLocation(pt) 
    # 
    #  * Sets the location of this object to the specified point.
    #  *
    #  * @usage gobj.setLocation(pt);
    #  * @param pt The new location for this object
    #  * @noshow
    #  
    # @setLocation.register(object, GPoint)
    def setLocation(self, pt):
        """ generated source for method setLocation_0 """
        self.setLocation(pt.getX(), pt.getY())

    #  Method: getLocation() 
    # 
    #  * Returns the location of this object as a <code>GPoint</code>.
    #  *
    #  * @usage GPoint pt = gobj.getLocation();
    #  * @return The location of this object as a <code>GPoint</code>
    #  
    def getLocation(self):
        """ generated source for method getLocation """
        return GPoint(xc, yc)

    #  Method: getX() 
    # 
    #  * Returns the x-coordinate of the object.
    #  *
    #  * @usage double x = gobj.getX();
    #  * @return The x-coordinate of the object
    #  
    def getX(self):
        """ generated source for method getX """
        return xc

    #  Method: getY() 
    # 
    #  * Returns the y-coordinate of the object.
    #  *
    #  * @usage double y = gobj.getY();
    #  * @return The y-coordinate of the object
    #  
    def getY(self):
        """ generated source for method getY """
        return yc

    #  Method: move(dx, dy) 
    # 
    #  * Moves the object on the screen using the displacements <code>dx</code> and <code>dy</code>.
    #  *
    #  * @usage gobj.move(dx, dy);
    #  * @param dx The distance to move the object in the x direction (positive is rightward)
    #  * @param dy The distance to move the object in the y direction (positive is downward)
    #  
    def move(self, dx, dy):
        """ generated source for method move """
        self.setLocation(xc + dx, yc + dy)

    #  Method: movePolar(r, theta) 
    # 
    #  * Moves the object using displacements given in polar coordinates.  The
    #  * parameter <code>r</code> specifies the distance to move and <code>theta</code>
    #  * specifies the angle in which the motion occurs.  The angle is measured in
    #  * degrees increasing counterclockwise from the +x axis.
    #  *
    #  * @usage gobj.movePolar(r, theta);
    #  * @param r The distance to move
    #  * @param theta The angle in which to move, measured in degrees
    #  *              increasing counterclockwise from the +x axis
    #  
    def movePolar(self, r, theta):
        """ generated source for method movePolar """
        radians = theta * PI / 180
        self.move(r * cos(radians), -r * sin(radians))

    #  Method: getSize() 
    # 
    #  * Returns the size of the bounding box for this object.
    #  *
    #  * @usage GDimension size = gobj.getSize();
    #  * @return The size of this object
    #  
    def getSize(self):
        """ generated source for method getSize """
        bounds = self.getBounds()
        return GDimension(bounds.getWidth(), bounds.getHeight())

    #  Method: getWidth() 
    # 
    #  * Returns the width of this object, which is defined to be
    #  * the width of the bounding box.
    #  *
    #  * @usage double width = gobj.getWidth();
    #  * @return The width of this object on the screen
    #  
    def getWidth(self):
        """ generated source for method getWidth """
        return self.getBounds().getWidth()

    #  Method: getHeight() 
    # 
    #  * Returns the height of this object, which is defined to be
    #  * the height of the bounding box.
    #  *
    #  * @usage double height = gobj.getHeight();
    #  * @return The height of this object on the screen
    #  
    def getHeight(self):
        """ generated source for method getHeight """
        return self.getBounds().getHeight()

    #  Method: contains(x, y) 
    # 
    #  * Checks to see whether a point is inside the object.  By default, this
    #  * method simply checks to see if the point is inside the bounding box.
    #  * Many subclasses will need to override this to check whether the point
    #  * is contained in the shape.
    #  *
    #  * @usage if (gobj.contains(x, y)) . . .
    #  * @param x The x-coordinate of the point being tested
    #  * @param y The y-coordinate of the point being tested
    #  * @return <code>true</code> if the point (<code>x</code>,&nbsp;<code>y</code>) is inside
    #  *         the object, and <code>false</code> otherwise
    #  
    # @overloaded
    def contains(self, x, y):
        """ generated source for method contains """
        return self.getBounds().contains(Ground(x), Ground(y))

    #  Method: contains(pt) 
    # 
    #  * Checks to see whether a point is inside the object.
    #  *
    #  * @usage if (gobj.contains(pt)) . . .
    #  * @param pt The point being tested
    #  * @return <code>true</code> if the point is inside the object, and <code>false</code> otherwise
    #  
    # @contains.register(object, GPoint)
    def contains(self, pt):
        """ generated source for method contains_0 """
        return self.contains(pt.getX(), pt.getY())

    #  Method: sendToFront() 
    # 
    #  * Moves this object to the front of the display in the <i>z</i> dimension.  By
    #  * moving it to the front, this object will appear to be on top of the other graphical
    #  * objects on the display and may hide any objects that are further back.
    #  *
    #  * @usage gobj.sendToFront();
    #  
    def sendToFront(self):
         """ generated source for method sendToFront """
        # if compoundParent != None:
        #     compoundParent.sendToFront(self)
        # elif isinstance(transientParent, (GCanvas, )):
        #     (transientParent).sendToFront(self)
        # elif transientParent != None:
        #     try:
        #         parentClass = transientParent.__class__
        #         types = [Class.forName("acm.graphics.GObject")]
        #         args = [self]
        #         fn = parentClass.getMethod("sendToFront", types)
        #         if fn != None:
        #             fn.invoke(transientParent, args)
        #     except Exception as ex:
        #         pass
        #         #  Empty
        # if mouseListenersEnabled:
        #     updateEnabledList()

    #  Method: sendToBack() 
    # 
    #  * Moves this object to the back of the display in the <i>z</i> dimension.  By
    #  * moving it to the back, this object will appear to be behind the other graphical
    #  * objects on the display and may be obscured by other objects in front.
    #  *
    #  * @usage gobj.sendToBack();
    #  
    def sendToBack(self):
         """ generated source for method sendToBack """
        # if compoundParent != None:
        #     compoundParent.sendToBack(self)
        # elif isinstance(transientParent, (GCanvas, )):
        #     (transientParent).sendToBack(self)
        # elif transientParent != None:
        #     try:
        #         parentClass = transientParent.__class__
        #         types = [Class.forName("acm.graphics.GObject")]
        #         args = [self]
        #         fn = parentClass.getMethod("sendToBack", types)
        #         if fn != None:
        #             fn.invoke(transientParent, args)
        #     except Exception as ex:
        #         pass
        #         #  Empty
        # if mouseListenersEnabled:
        #     updateEnabledList()

    #  Method: sendForward() 
    # 
    #  * Moves this object one step toward the front in the <i>z</i> dimension.
    #  * If it was already at the front of the stack, nothing happens.
    #  *
    #  * @usage gobj.sendForward();
    #  
    def sendForward(self):
        """ generated source for method sendForward """
        # if compoundParent != None:
        #     compoundParent.sendForward(self)
        # elif isinstance(transientParent, (GCanvas, )):
        #     (transientParent).sendForward(self)
        # elif transientParent != None:
        #     try:
        #         parentClass = transientParent.__class__
        #         types = [Class.forName("acm.graphics.GObject")]
        #         args = [self]
        #         fn = parentClass.getMethod("sendForward", types)
        #         if fn != None:
        #             fn.invoke(transientParent, args)
        #     except Exception as ex:
        #         pass
        #         #  Empty
        # if mouseListenersEnabled:
        #     updateEnabledList()

    #  Method: sendBackward() 
    # 
    #  * Moves this object one step toward the back in the <i>z</i> dimension.
    #  * If it was already at the back of the stack, nothing happens.
    #  *
    #  * @usage gobj.sendBackward();
    #  
    def sendBackward(self):
        """ generated source for method sendBackward """
        # if compoundParent != None:
        #     compoundParent.sendBackward(self)
        # elif isinstance(transientParent, (GCanvas, )):
        #     (transientParent).sendBackward(self)
        # elif transientParent != None:
        #     try:
        #         parentClass = transientParent.__class__
        #         types = [Class.forName("acm.graphics.GObject")]
        #         args = [self]
        #         fn = parentClass.getMethod("sendBackward", types)
        #         if fn != None:
        #             fn.invoke(transientParent, args)
        #     except Exception as ex:
        #         pass
        #         #  Empty
        # if mouseListenersEnabled:
        #     updateEnabledList()

    #  Method: setColor(color) 
    # 
    #  * Sets the color used to display this object.
    #  *
    #  * @usage gobj.setColor(color);
    #  * @param color The color used to display this object
    #  
    def setColor(self, color):
        """ generated source for method setColor """
        # objectColor = color
        # repaint()

    #  Method: getColor() 
    # 
    #  * Returns the color used to display this object.
    #  *
    #  * @usage Color color = gobj.getColor();
    #  * @return The color used to display this object
    #  
    def getColor(self):
        """ generated source for method getColor """
        # obj = self
        # while obj.objectColor == None:
        #     parent = obj.getParent()
        #     if isinstance(parent, (GObject, )):
        #         obj = parent
        #     elif isinstance(parent, (Component, )):
        #         return (parent).getForeground()
        #     else:
        #         return Color.BLACK
        # return obj.objectColor

    #  Method: setVisible(visible) 
    # 
    #  * Sets whether this object is visible.
    #  *
    #  * @usage gobj.setVisible(visible);
    #  * @param visible <code>true</code> to make the object visible, <code>false</code> to hide it
    #  
    def setVisible(self, visible):
        """ generated source for method setVisible """
        isVisible = visible
        repaint()

    #  Method: isVisible() 
    # 
    #  * Checks to see whether this object is visible.
    #  *
    #  * @usage if (gobj.isVisible()) . . .
    #  * @return <code>true</code> if the object is visible, otherwise <code>false</code>
    #  
    def isVisible(self):
        """ generated source for method isVisible """
        return self.isVisible

    #  Method: toString() 
    # 
    #  * Overrides the <code>toString</code> method in <code>Object</code> to produce
    #  * more readable output.
    #  * @noshow
    #  
    def __str__(self):
         """ generated source for method toString """
        # name = getClass().__name__
        # if name.startsWith("acm.graphics."):
        #     name = name.substring(len(length))
        # return name + "[" + paramString() + "]"

    #  Method: getParent() 
    # 
    #  * Returns the parent of this object, which is the canvas or compound object in
    #  * which it is enclosed.
    #  *
    #  * @usage GContainer parent = gobj.getParent();
    #  * @return The parent of this object
    #  

    def getParent(self):
        """ generated source for method getParent """
    # return compoundParent if (compoundParent != None) else transientParent

    #  Method: pause(milliseconds) 
    # 
    #  * Delays the calling thread for the specified time, which is expressed in
    #  * milliseconds.  Unlike <code>Thread.sleep</code>, this method never throws an
    #  * exception.
    #  *
    #  * @usage gobj.pause(milliseconds);
    #  * @param milliseconds The sleep time in milliseconds
    #  
    def pause(self, milliseconds):
        """ generated source for method pause """
        # JTFTools.pause(milliseconds)

    #  Method: addMouseListener(listener) 
    # 
    #  * Adds a mouse listener to this graphical object.
    #  *
    #  * @usage gobj.addMouseListener(listener);
    #  * @param listener Any object that implements the <code>MouseListener</code> interface
    #  
    def addMouseListener(self, listener):
        """ generated source for method addMouseListener """
        # mouseListener = AWTEventMulticaster.add(mouseListener, listener)
        # mouseListenersEnabled = True
        # updateEnabledList()

    #  Method: removeMouseListener(listener) 
    # 
    #  * Removes a mouse listener from this graphical object.
    #  *
    #  * @usage gobj.removeMouseListener(listener);
    #  * @param listener The listener object to remove
    #  
    def removeMouseListener(self, listener):
        """ generated source for method removeMouseListener """
        # mouseListener = AWTEventMulticaster.remove(mouseListener, listener)

    #  Method: addMouseMotionListener(listener) 
    # 
    #  * Adds a mouse motion listener to this graphical object.
    #  *
    #  * @usage gobj.addMouseMotionListener(listener);
    #  * @param listener Any object that implements the <code>MouseMotionListener</code> interface
    #  
    def addMouseMotionListener(self, listener):
        """ generated source for method addMouseMotionListener """
        # mouseMotionListener = AWTEventMulticaster.add(mouseMotionListener, listener)
        # mouseListenersEnabled = True
        # updateEnabledList()

    #  Method: removeMouseMotionListener(listener) 
    # 
    #  * Removes a mouse motion listener from this graphical object.
    #  *
    #  * @usage gobj.removeMouseMotionListener(listener);
    #  * @param listener The listener object to remove
    #  
    def removeMouseMotionListener(self, listener):
        """ generated source for method removeMouseMotionListener 111"""
        # mouseMotionListener = AWTEventMulticaster.remove(mouseMotionListener, listener)

    #  Method: addActionListener(listener) 
    # 
    #  * Adds an action listener to this graphical object.
    #  *
    #  * @usage gobj.addActionListener(listener);
    #  * @param listener Any object that implements the <code>ActionListener</code> interface
    #  
    def addActionListener(self, listener):
        """ generated source for method addActionListener """
        actionListener = AWTEventMulticaster.add(actionListener, listener)

    #  Method: removeActionListener(listener) 
    # 
    #  * Removes an action listener from this graphical object.
    #  *
    #  * @usage gobj.removeActionListener(listener);
    #  * @param listener The listener object to remove
    #  
    def removeActionListener(self, listener):
        """ generated source for method removeActionListener """
        # actionListener = AWTEventMulticaster.remove(actionListener, listener)

    #  Method: fireActionEvent(actionCommand) 
    # 
    #  * Triggers an action event for this graphical object with the specified
    #  * action command.
    #  *
    #  * @usage gobj.fireActionEvent(actionCommand);
    #  * @param actionCommand The action command to include in the event
    #  
    # @overloaded
    def fireActionEvent(self, actionCommand):
        """ generated source for method fireActionEvent """
        self.fireActionEvent(ActionEvent(self, ActionEvent.ACTION_PERFORMED, actionCommand))

    #  Method: fireActionEvent(e) 
    # 
    #  * Triggers an action event for this graphical object.
    #  *
    #  * @usage gobj.fireActionEvent(e);
    #  * @param e The <code>ActionEvent</code> to fire
    #  
    # @fireActionEvent.register(object, ActionEvent)
    def fireActionEvent(self, e):
        """ generated source for method fireActionEvent_0 """
        # if actionListener != None:
        #     actionListener.actionPerformed(e)

    #  Unadvertised method: setParent(parent) 
    # 
    #  * Sets the parent of this object, which should be called only by the
    #  * <code>GContainer</code> in which this is installed.  The
    #  * serialization behavior of the parent data depends on the parent
    #  * type.  Because a <code>GCompound</code> is serializable, it
    #  * needs to be maintained in a nontransient variable; other parent
    #  * classes are transient, so that these parents are not recorded
    #  * in the serial form.
    #  * @noshow
    #  
    def setParent(self, parent):
        """ generated source for method setParent """
        # if isinstance(parent, (GCompound, )):
        #     compoundParent = parent
        # else:
        #     transientParent = parent

    #  Protected method: fireMouseListeners(e) 
    # 
    #  * Sends the event to the appropriate listener.
    #  *
    #  * @usage gobj.fireMouseListeners(e);
    #  * @param e The <code>MouseEvent</code> that triggered this response
    #  * @noshow
    #  
    def fireMouseListeners(self, e):
        """ generated source for method fireMouseListeners """
        # if e.getID() == MouseEvent.MOUSE_PRESSED:
        #     if mouseListener != None:
        #         mouseListener.mousePressed(e)
        # elif e.getID() == MouseEvent.MOUSE_RELEASED:
        #     if mouseListener != None:
        #         mouseListener.mouseReleased(e)
        # elif e.getID() == MouseEvent.MOUSE_CLICKED:
        #     if mouseListener != None:
        #         mouseListener.mouseClicked(e)
        # elif e.getID() == MouseEvent.MOUSE_EXITED:
        #     if mouseListener != None:
        #         mouseListener.mouseExited(e)
        # elif e.getID() == MouseEvent.MOUSE_ENTERED:
        #     if mouseListener != None:
        #         mouseListener.mouseEntered(e)
        # elif e.getID() == MouseEvent.MOUSE_MOVED:
        #     if mouseMotionListener != None:
        #         mouseMotionListener.mouseMoved(e)
        # elif e.getID() == MouseEvent.MOUSE_DRAGGED:
        #     if mouseMotionListener != None:
        #         mouseMotionListener.mouseDragged(e)

    #  Protected method: areMouseListenersEnabled() 
    # 
    #  * Returns <code>true</code> if mouse listeners have ever been assigned to
    #  * this object.
    #  *
    #  * @usage if (gobj.areMouseListenersEnabled()) . . .
    #  * @return <code>true</code> if mouse listeners have been enabled in this object
    #  * @noshow
    #  
    def areMouseListenersEnabled(self):
        """ generated source for method areMouseListenersEnabled """
        # return mouseListenersEnabled

    #  Protected method: start() 
    # 
    #  * Starts a <code>GraphicsProgram</code> containing this object.
    #  *
    #  * @usage gobj.start();
    #  * @noshow
    #  
    # @overloaded
    def start(self):
        """ generated source for method start """
        self.start(None)

    #  Protected method: start(args) 
    # 
    #  * Starts a <code>GraphicsProgram</code> containing this object, passing
    #  * it the specified arguments.
    #  *
    #  * @usage gobj.start();
    #  * @param args The array of arguments
    #  * @noshow
    #  
    # @start.register(object, str)
    def start_0(self, args):
        """ generated source for method start_0 """
        # try:
        #     programClass = Class.forName("acm.program.GraphicsProgram")
        #     gObjectClass = Class.forName("acm.graphics.GObject")
        #     types = [gObjectClass, args.__class__]
        #     params = [self, args]
        #     startGraphicsProgram = programClass.getMethod("startGraphicsProgram", types)
        #     startGraphicsProgram.invoke(None, params)
        # except Exception as ex:
        #     raise ErrorException(ex)

    #  Protected method: getObjectColor() 
    # 
    #  * This method returns the color set for this specific object, which may
    #  * be <code>null</code>.  It differs from <code>getColor</code> in that
    #  * it does not walk up the containment chain.
    #  * @noshow
    #  
    def getObjectColor(self):
        """ generated source for method getObjectColor """
        # return objectColor

    #  Protected method: paramString() 
    # 
    #  * Returns a string indicating the parameters of this object.
    #  * @noshow
    #  
    def paramString(self):
        """ generated source for method paramString """
        param = ""
        # if isinstance(self, GResizable):
        #     r = self.getBounds()
        #     param += "bounds=(" + r.getX() + ", " + r.getY() + ", " + r.getWidth() + ", " + r.getHeight() + ")"
        # else:
        #     pt = self.getLocation()
        #     param += "location=(" + pt.getX() + ", " + pt.getY() + ")"
        # if objectColor != None:
        #     param += ", color=" + colorName(objectColor)
        # if isinstance(self, GFillable):
        #     param += ", filled=" + (self).isFilled()
        #     fillColor = (self).getFillColor()
        #     if fillColor != None and fillColor != objectColor:
        #         param += ", fillColor=" + colorName(fillColor)
        return param

    #  Protected static method: colorName(color) 
    # 
    #  * Translates a color to a string representation.
    #  * @noshow
    #  
    @classmethod
    def colorName(cls, color):
        """ generated source for method colorName """
        # if color == Color.BLACK:
        #     return "BLACK"
        # if color == Color.BLUE:
        #     return "BLUE"
        # if color == Color.CYAN:
        #     return "CYAN"
        # if color == Color.DARK_GRAY:
        #     return "DARK_GRAY"
        # if color == Color.GRAY:
        #     return "GRAY"
        # if color == Color.GREEN:
        #     return "GREEN"
        # if color == Color.LIGHT_GRAY:
        #     return "LIGHT_GRAY"
        # if color == Color.MAGENTA:
        #     return "MAGENTA"
        # if color == Color.ORANGE:
        #     return "ORANGE"
        # if color == Color.PINK:
        #     return "PINK"
        # if color == Color.RED:
        #     return "RED"
        # if color == Color.WHITE:
        #     return "WHITE"
        # if color == Color.YELLOW:
        #     return "YELLOW"
        # return "0x" + Integer.toString(color.getRGB() & 0xFFFFFF, 16).toUpperCase()

    #  Protected method: paintObject(g) 
    # 
    #  * Paints the object by setting up the necessary parameters and then
    #  * dispatching to the <code>paint</code> procedure for this object.
    #  * @noshow
    #  
    def paintObject(self, g):
        """ generated source for method paintObject """
        # if not self.isVisible():
        #     return
        # oldColor = g.getColor()
        # if objectColor != None:
        #     g.setColor(objectColor)
        # self.paint(g)
        # if objectColor != None:
        #     g.setColor(oldColor)

    #  Protected method: getComponent() 
    # 
    #  * Returns the component in which this object is installed, or <code>null</code>
    #  * if none exists.
    #  *
    #  * @usage Component comp = gobj.getComponent();
    #  * @return The component in which this object is installed, or <code>null</code> if none exists
    #  * @noshow
    #  
    def getComponent(self):
        """ generated source for method getComponent """
        # parent = self.getParent()
        # while isinstance(parent, (GObject, )):
        #     parent = (parent).getParent()
        # return parent if (isinstance(parent, (Component, ))) else None

    #  Protected method: updateEnabledList() 
    # 
    #  * Tells the parent to update its list of enabled objects.
    #  * @noshow
    #  
    def updateEnabledList(self):
        """ generated source for method updateEnabledList """
        # comp = self.getComponent()
        # if isinstance(comp, (GCanvas, )):
        #     (comp).updateEnabledList()

    #  Protected method: repaint() 
    # 
    #  * Signals that the object needs to be repainted.
    #  * @noshow
    #  
    def repaint(self):
        """ generated source for method repaint """
        # parent = self.getParent()
        # while isinstance(parent, (GObject, )):
        #     parent = (parent).getParent()
        # if isinstance(parent, (GCanvas, )):
        #     (parent).conditionalRepaint()

    #  Private instance variables 
    compoundParent = None
    objectColor = None
    xc = float()
    yc = float()
    isVisible = bool()
    mouseListenersEnabled = bool()
    mouseListener = None
    mouseMotionListener = None
    actionListener = None
    transientParent = None

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

