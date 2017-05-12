#!/usr/bin/env python
""" generated source for module GraphicsProgram """
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
#  * @(#)GraphicsProgram.java   1.99.1 08/12/08
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
#  Code cleanup 30-Jan-07 (ESR)
#    1. Renamed instance variable "listener" to "eventListener" to avoid
#       warning messages from some compilers.
#    2. Removed unnecessary startHook code.
# package: acm.program
# 
#  * This class is a standard subclass of <code><a href="Program.html">Program</a></code>
#  * whose principal window is used for drawing graphics.
#  
class GraphicsProgram(Program):
    """ generated source for class GraphicsProgram """
    #  Constructor: GraphicsProgram() 
    # 
    #  * Creates a new graphics program.
    #  *
    #  * @usage GraphicsProgram program = new GraphicsProgram();
    #  
    def __init__(self):
        """ generated source for method __init__ """
        super(GraphicsProgram, self).__init__()
        eventListener = GProgramListener(self)
        gc = createGCanvas()
        gc.addMouseListener(eventListener)
        if eventListener.needsMouseMotionListeners():
            gc.addMouseMotionListener(eventListener)
        add(gc, CENTER)
        validate()

    #  Method: run() 
    # 
    #  * Specifies the code to be executed as the program runs.
    #  * The <code>run</code> method is required for applications that have
    #  * a thread of control that runs even in the absence of user actions,
    #  * such as a program that uses console interation or that involves
    #  * animation.  GUI-based programs that operate by setting up an initial
    #  * configuration and then wait for user events usually do not specify a
    #  * <code>run</code> method and supply a new definition for <code>init</code>
    #  * instead.
    #  
    def run(self):
        """ generated source for method run """
        #  Empty 

    #  Method: init() 
    # 
    #  * Specifies the code to be executed as startup time before the
    #  * <code>run</code> method is called.  Subclasses can override this
    #  * method to perform any initialization code that would ordinarily
    #  * be included in an applet <code>init</code> method.  In general,
    #  * subclasses will override <code>init</code> in GUI-based programs
    #  * where the program simply sets up an initial state and then waits
    #  * for events from the user.  The <code>run</code> method is required
    #  * for applications in which there needs to be some control thread
    #  * while the program runs, as in a typical animation.
    #  *
    #  * @usage program.init();
    #  
    def init(self):
        """ generated source for method init """
        #  Empty 

    #  Method: getGCanvas() 
    # 
    #  * Returns the <code>GCanvas</code> object used by this program.
    #  *
    #  * @usage GCanvas gc = getGCanvas();
    #  * @return The <code>GCanvas</code> object used by the program
    #  
    def getGCanvas(self):
        """ generated source for method getGCanvas """
        return gc

    #  Method: add(gobj) 
    # 
    #  * Adds a new graphical object to this container.
    #  *
    #  * @usage add(gobj);
    #  * @param gobj The graphical object to add
    #  
    @overloaded
    def add(self, gobj):
        """ generated source for method add """
        gc.add(gobj)

    #  Method: add(gobj, x, y) 
    # 
    #  * Adds the graphical object to the canvas and sets its location
    #  * to the point (<code>x</code>,&nbsp;<code>y</code>).
    #  *
    #  * @usage add(gobj, x, y);
    #  * @param gobj The graphical object to add
    #  * @param x The new x-coordinate for the object
    #  * @param y The new y-coordinate for the object
    #  
    @add.register(object, GObject, float, float)
    def add_0(self, gobj, x, y):
        """ generated source for method add_0 """
        gobj.setLocation(x, y)
        self.add(gobj)

    #  Method: add(gobj, pt) 
    # 
    #  * Adds the graphical object to the canvas and sets its location to the specified point.
    #  *
    #  * @usage add(gobj, pt);
    #  * @param gobj The graphical object to add
    #  * @param pt The new coordinates of the point
    #  
    @add.register(object, GObject, GPoint)
    def add_1(self, gobj, pt):
        """ generated source for method add_1 """
        gobj.setLocation(pt)
        self.add(gobj)

    #  Method: add(comp, x, y) 
    # 
    #  * Adds the component to the canvas and sets its location
    #  * to the point (<code>x</code>,&nbsp;<code>y</code>).
    #  *
    #  * @usage add(comp, x, y);
    #  * @param comp The component to add
    #  * @param x The new x-coordinate for the object
    #  * @param y The new y-coordinate for the object
    #  
    @add.register(object, Component, float, float)
    def add_2(self, comp, x, y):
        """ generated source for method add_2 """
        comp.setLocation(Ground(x), Ground(y))
        gc.add(comp)

    #  Method: add(comp, pt) 
    # 
    #  * Adds the component to the canvas and sets its location to the specified point.
    #  *
    #  * @usage add(comp, pt);
    #  * @param comp The component to add
    #  * @param pt A <code>GPoint</code> object giving the coordinates of the point
    #  
    @add.register(object, Component, GPoint)
    def add_3(self, comp, pt):
        """ generated source for method add_3 """
        self.add(comp, pt.getX(), pt.getY())

    #  Method: remove(gobj) 
    # 
    #  * Removes a graphical object from this container.
    #  *
    #  * @usage remove(gobj);
    #  * @param gobj The graphical object to remove
    #  
    def remove(self, gobj):
        """ generated source for method remove """
        gc.remove(gobj)

    #  Method: removeAll() 
    # 
    #  * Removes all graphical objects from this container.  Note that this
    #  * definition overrides the <code>Container</code> version of
    #  * <code>removeAll</code>, which is replaced by
    #  * <a href="#removeAllComponents()"><code>removeAllComponents</code></a>.
    #  *
    #  * @usage removeAll();
    #  
    def removeAll(self):
        """ generated source for method removeAll """
        gc.removeAll()

    #  Method: getElementCount() 
    # 
    #  * Returns the number of graphical objects stored in this <code>GCanvas</code>.
    #  *
    #  * @usage int n = getElementCount();
    #  * @return The number of graphical objects in this <code>GCanvas</code>
    #  
    def getElementCount(self):
        """ generated source for method getElementCount """
        return gc.getElementCount()

    #  Method: getElement(index) 
    # 
    #  * Returns the graphical object at the specified index, numbering from back
    #  * to front in the the <i>z</i> dimension.
    #  *
    #  * @usage GObject gobj = getElement(index);
    #  * @param index The index of the component to return
    #  * @return The graphical object at the specified index
    #  
    def getElement(self, index):
        """ generated source for method getElement """
        return gc.getElement(index)

    #  Method: getElementAt(x, y) 
    # 
    #  * Returns the topmost graphical object that contains the point
    #  * (<code>x</code>, <code>y</code>), or <code>null</code> if no such
    #  * object exists.
    #  *
    #  * @usage GObject gobj = program.getElementAt(x, y);
    #  * @param x The x-coordinate of the point being tested
    #  * @param y The y-coordinate of the point being tested
    #  * @return The graphical object at the specified location, or <code>null</code>
    #  *         if no such object exists.
    #  
    @overloaded
    def getElementAt(self, x, y):
        """ generated source for method getElementAt """
        return gc.getElementAt(x, y)

    #  Method: getElementAt(pt) 
    # 
    #  * Returns the topmost graphical object that contains the specified point,
    #  * or <code>null</code> if no such object exists.
    #  *
    #  * @usage GObject gobj = program.getElementAt(pt);
    #  * @param pt The coordinates being tested
    #  * @return The graphical object at the specified location, or <code>null</code>
    #  *         if no such object exists
    #  
    @getElementAt.register(object, GPoint)
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
    #  * <p>Applets that want to run in browsers, however, should avoid using
    #  * this method, because <code>Iterator</code> is not supported on 1.1 browsers.
    #  * For maximum portability, you should rely instead on the
    #  * <a href="GContainer.html#getElementCount()"><code>getElementCount</code></a>
    #  * and <a href="GContainer.html#getElement(int)"><code>getElement</code></a> methods,
    #  * which provide the same functionality in a browser-compatible way.
    #  *
    #  * @usage Iterator<GObject> i = iterator();
    #  * @return An <code>Iterator</code> ranging over the elements of the
    #  *         container from back to front
    #  
    @overloaded
    def iterator(self):
        """ generated source for method iterator """
        return gc.iterator()

    #  Method: iterator(direction) 
    # 
    #  * Returns an <code>Iterator</code> that cycles through the elements
    #  * within this container in the specified direction, which must be one
    #  * of the constants <a href="../graphics/GContainer.html#FRONT_TO_BACK"><code>FRONT_TO_BACK</code></a>
    #  * or <a href="GContainer.html#BACK_TO_FRONT"><code>BACK_TO_FRONT</code></a>
    #  * from the <a href="../graphics/GContainer.html"><code>GContainer</code></a> interface.<p>
    #  *
    #  * <code>  for (Iterator&lt;GObject&gt; i = iterator(direction); i.hasNext(); )</code>
    #  *
    #  * <p>Applets that want to run in browsers, however, should avoid using
    #  * this method, because <code>Iterator</code> is not supported on 1.1 browsers.
    #  * For maximum portability, you should rely instead on the
    #  * <a href="GContainer.html#getElementCount()"><code>getElementCount</code></a>
    #  * and <a href="GContainer.html#getElement(int)"><code>getElement</code></a> methods,
    #  * which provide the same functionality in a browser-compatible way.
    #  *
    #  * @usage Iterator<GObject> i = iterator(direction);
    #  * @return An <code>Iterator</code> ranging over the elements of the
    #  *         container in the specified direction
    #  
    @iterator.register(object, int)
    def iterator_0(self, direction):
        """ generated source for method iterator_0 """
        return gc.iterator(direction)

    #  Method: addMouseListeners() 
    # 
    #  * Adds the program as both a <code>MouseListener</code> and <code>MouseMotionListener</code>
    #  * to the canvas.
    #  *
    #  * @usage addMouseListeners();
    #  
    @overloaded
    def addMouseListeners(self):
        """ generated source for method addMouseListeners """
        gc.addMouseListener(self)
        gc.addMouseMotionListener(self)

    #  Method: addMouseListeners(listener) 
    # 
    #  * Adds the specified listener as a <code>MouseListener</code> and/or
    #  * <code>MouseMotionListener</code>, as appropriate, to the canvas.
    #  *
    #  * @usage addMouseListeners(listener);
    #  * @param listener A listener object that is either a <code>MouseListener</code>, a
    #  *        <code>MouseMotionListener</code>, or both
    #  
    @addMouseListeners.register(object, EventListener)
    def addMouseListeners_0(self, listener):
        """ generated source for method addMouseListeners_0 """
        ok = False
        if isinstance(listener, (MouseListener, )):
            gc.addMouseListener(listener)
            ok = True
        if isinstance(listener, (MouseMotionListener, )):
            gc.addMouseMotionListener(listener)
            ok = True
        if not ok:
            raise ErrorException("addMouseListeners: Illegal listener")

    #  Method: addKeyListeners() 
    # 
    #  * Adds the program as a <code>KeyListener</code> to the canvas.
    #  *
    #  * @usage addKeyListeners();
    #  
    @overloaded
    def addKeyListeners(self):
        """ generated source for method addKeyListeners """
        gc.addKeyListener(self)

    #  Method: addKeyListeners(listener) 
    # 
    #  * Adds the specified listener as a <code>KeyListener</code> to the canvas.
    #  *
    #  * @usage addKeyListeners(listener);
    #  * @param listener A <code>KeyListener</code> object
    #  
    @addKeyListeners.register(object, KeyListener)
    def addKeyListeners_0(self, listener):
        """ generated source for method addKeyListeners_0 """
        gc.addKeyListener(listener)

    #  Method: waitForClick() 
    # 
    #  * Waits for a mouse click in the window before proceeding.
    #  *
    #  * @usage waitForClick();
    #  
    def waitForClick(self):
        """ generated source for method waitForClick """
        eventListener.waitForClick()

    #  Method: repaint() 
    # 
    #  * Signals a need to repaint this window.
    #  * @noshow
    #  
    def repaint(self):
        """ generated source for method repaint """
        gc.repaint()
        super(GraphicsProgram, self).repaint()

    #  Method: removeAllComponents() 
    # 
    #  * Removes all components from this container.
    #  *
    #  * @usage removeAllComponents();
    #  * @noshow
    #  
    def removeAllComponents(self):
        """ generated source for method removeAllComponents """
        super(GraphicsProgram, self).removeAll()

    #  Override method: setBackground(bg) 
    # 
    #  * Sets the background color of the <code>GCanvas</code>.
    #  *
    #  * @usage setBackground(bg);
    #  * @param bg The new background color
    #  * @noshow
    #  
    def setBackground(self, bg):
        """ generated source for method setBackground """
        super(GraphicsProgram, self).setBackground(bg)
        if gc != None:
            gc.setBackground(bg)

    #  Static method: startGraphicsProgram(gobj, args) 
    # 
    #  * Creates a <code>GraphicsProgram</code> containing the specified <code>GObject</code>
    #  * and then starts it.  This code is called only by the <code>start</code> method in
    #  * <code>GObject</code>.
    #  *
    #  * @usage startGraphicsProgram(gobj, args);
    #  * @param gobj The object to be inserted into the <code>GraphicsProgram</code>
    #  * @param args The array of arguments
    #  * @noshow
    #  
    @classmethod
    def startGraphicsProgram(cls, gobj, args):
        """ generated source for method startGraphicsProgram """
        program = GObjectProgram()
        program.setStartupObject(gobj)
        program.start(args)

    #  Inherited method: print(value) 
    # 
    #  * @inherited Program#void print(String value)
    #  * Displays the argument value on the console, leaving the cursor at the end of
    #  * the output.
    #  
    #  Inherited method: println() 
    # 
    #  * @inherited Program#void println()
    #  * Advances the console cursor to the beginning of the next line.
    #  
    #  Inherited method: println(value) 
    # 
    #  * @inherited Program#void println(String value)
    #  * Displays the argument value on the console and then advances the cursor
    #  * to the next line.
    #  
    #  Inherited method: readLine() 
    # 
    #  * @inherited Program#String readLine()
    #  * Reads and returns a line of input from the console.
    #  
    #  Inherited method: readLine(prompt) 
    # 
    #  * @inherited Program#String readLine(String prompt)
    #  * Prompts the user for a line of input.
    #  
    #  Inherited method: readInt() 
    # 
    #  * @inherited Program#int readInt()
    #  * Reads and returns an integer value from the user.
    #  
    #  Inherited method: readInt(prompt) 
    # 
    #  * @inherited Program#int readInt(String prompt)
    #  * Prompts the user to enter an integer.
    #  
    #  Inherited method: readDouble() 
    # 
    #  * @inherited Program#double readDouble()
    #  * Reads and returns a double-precision value from the user.
    #  
    #  Inherited method: readDouble(prompt) 
    # 
    #  * @inherited Program#double readDouble(String prompt)
    #  * Prompts the user to enter a double-precision number, which is
    #  * returned as the value of this method.
    #  
    #  Inherited method: readBoolean() 
    # 
    #  * @inherited Program#boolean readBoolean()
    #  * Reads and returns a boolean value (<code>true</code> or <code>false</code>).
    #  
    #  Inherited method: readBoolean(prompt) 
    # 
    #  * @inherited Program#boolean readBoolean(String prompt)
    #  * Prompts the user to enter a boolean value.
    #  
    #  Inherited method: readBoolean(prompt, trueLabel, falseLabel) 
    # 
    #  * @inherited Program#boolean readBoolean(String prompt, String trueLabel, String falseLabel)
    #  * Prompts the user to enter a boolean value, which is matched against the
    #  * labels provided.
    #  
    #  Inherited method: getConsole() 
    # 
    #  * @inherited Program#IOConsole getConsole()
    #  * Returns the console associated with this program.
    #  
    #  Inherited method: getDialog() 
    # 
    #  * @inherited Program#IODialog getDialog()
    #  * Returns the dialog used for user interaction.
    #  
    #  Inherited method: getReader() 
    # 
    #  * @inherited Program#BufferedReader getReader()
    #  * Returns a <code>BufferedReader</code> whose input comes from the console.
    #  
    #  Inherited method: getWriter() 
    # 
    #  * @inherited Program#PrintWriter getWriter()
    #  * Returns a <code>PrintWriter</code> whose output is directed to the console.
    #  
    #  Inherited method: setTitle(title) 
    # 
    #  * @inherited Program#void setTitle(String title)
    #  * Sets the title of this program.
    #  
    #  Inherited method: getTitle() 
    # 
    #  * @inherited Program#String getTitle()
    #  * Gets the title of this program.
    #  
    #  Inherited method: pause(milliseconds) 
    # 
    #  * @inherited Program#void pause(double milliseconds)
    #  * Delays the calling thread for the specified time, which is expressed in
    #  * milliseconds.
    #  
    #  Factory method: createGCanvas() 
    # 
    #  * Creates the <code>GCanvas</code> used by the <code>GraphicsProgram</code>.  Subclasses can
    #  * override this method to create their own <code>GCanvas</code> types.
    #  *
    #  * @usage GCanvas gc = program.createGCanvas();
    #  * @return The <code>GCanvas</code> to be inserted into the program
    #  * @noshow
    #  
    def createGCanvas(self):
        """ generated source for method createGCanvas """
        return GCanvas()

    #  Protected method: endHook() 
    # 
    #  * Ensures that the window is repainted at the end of the program.
    #  
    def endHook(self):
        """ generated source for method endHook """
        gc.repaint()

    #  Protected method: isStarted() 
    # 
    #  * Checks to see whether this program has started, usually by checking to see
    #  * whether some pane exists.  Subclasses can override this method to ensure
    #  * that their structures are visible before proceeding.
    #  * @noshow
    #  
    def isStarted(self):
        """ generated source for method isStarted """
        if gc == None or not super(GraphicsProgram, self).isStarted():
            return False
        size = gc.getSize()
        return (size != None) and (size.width != 0) and (size.height != 0)

    #  Private instance variables 
    gc = None
    eventListener = None

#  Package class: GProgramListener 
# 
#  * The <code>GProgramListener</code> class implements the waitForClick
#  * method and the objectdraw-style listener model.
#  
class GProgramListener(MouseListener, MouseMotionListener):
    """ generated source for class GProgramListener """
    #  Constructor: GProgramListener() 
    # 
    #  * Creates the <code>GProgramListener</code>.
    #  
    def __init__(self, program):
        """ generated source for method __init__ """
        super(GProgramListener, self).__init__()
        myProgram = program
        try:
            programClass = program.__class__
            types = [Class.forName("acm.graphics.GPoint")]
            try:
                mousePressedHook = programClass.getMethod("mousePressed", types)
            except NoSuchMethodException as ex:
                pass
                #  Empty 
            try:
                mouseReleasedHook = programClass.getMethod("mouseReleased", types)
            except NoSuchMethodException as ex:
                pass
                #  Empty 
            try:
                mouseClickedHook = programClass.getMethod("mouseClicked", types)
            except NoSuchMethodException as ex:
                pass
                #  Empty 
            try:
                mouseMovedHook = programClass.getMethod("mouseMoved", types)
            except NoSuchMethodException as ex:
                pass
                #  Empty 
            try:
                mouseDraggedHook = programClass.getMethod("mouseDragged", types)
            except NoSuchMethodException as ex:
                pass
                #  Empty 
        except Exception as ex:
            raise ErrorException(ex)

    #  Method: needsMouseMotionListeners() 
    # 
    #  * Returns true if this listener has to respond to mouse motion events as well.
    #  
    def needsMouseMotionListeners(self):
        """ generated source for method needsMouseMotionListeners """
        return mouseMovedHook != None or mouseDraggedHook != None

    #  Method: mouseClicked() 
    # 
    #  * Called by the event-handling system when the mouse is clicked in the canvas.
    #  
    def mouseClicked(self, e):
        """ generated source for method mouseClicked """
        if mouseClickedHook != None:
            args = [GPoint(e.getX(), e.getY())]
            try:
                mouseClickedHook.invoke(myProgram, args)
            except Exception as ex:
                raise ErrorException(ex)
        signalClickOccurred()

    #  Method: mousePressed() 
    # 
    #  * Called by the event-handling system when the mouse button is pressed.
    #  
    def mousePressed(self, e):
        """ generated source for method mousePressed """
        if mousePressedHook != None:
            args = [GPoint(e.getX(), e.getY())]
            try:
                mousePressedHook.invoke(myProgram, args)
            except Exception as ex:
                raise ErrorException(ex)

    #  Method: mouseReleased() 
    # 
    #  * Called by the event-handling system when the mouse button is released.
    #  
    def mouseReleased(self, e):
        """ generated source for method mouseReleased """
        if mouseReleasedHook != None:
            args = [GPoint(e.getX(), e.getY())]
            try:
                mouseReleasedHook.invoke(myProgram, args)
            except Exception as ex:
                raise ErrorException(ex)

    #  Method: mouseEntered() 
    # 
    #  * Called by the event-handling system when the mouse enters the component.
    #  
    def mouseEntered(self, e):
        """ generated source for method mouseEntered """
        #  Empty 

    #  Method: mouseExited() 
    # 
    #  * Called by the event-handling system when the mouse leaves the component.
    #  
    def mouseExited(self, e):
        """ generated source for method mouseExited """
        #  Empty 

    #  Method: mouseMoved() 
    # 
    #  * Called by the event-handling system when the mouse moves.
    #  
    def mouseMoved(self, e):
        """ generated source for method mouseMoved """
        if mouseMovedHook != None:
            args = [GPoint(e.getX(), e.getY())]
            try:
                mouseMovedHook.invoke(myProgram, args)
            except Exception as ex:
                raise ErrorException(ex)

    #  Method: mouseDragged() 
    # 
    #  * Called by the event-handling system when the mouse is dragged with the button down.
    #  
    def mouseDragged(self, e):
        """ generated source for method mouseDragged """
        if mouseDraggedHook != None:
            args = [GPoint(e.getX(), e.getY())]
            try:
                mouseDraggedHook.invoke(myProgram, args)
            except Exception as ex:
                raise ErrorException(ex)

    #  Method: waitForClick() 
    # 
    #  * Waits for a mouse click in the window before proceeding.
    #  *
    #  * @usage waitForClick();
    #  
    @synchronized
    def waitForClick(self):
        """ generated source for method waitForClick """
        clickFlag = False
        while not clickFlag:
            try:
                wait()
            except InterruptedException as ex:
                pass
                #  Empty 

    #  Private method: signalClickOccurred() 
    # 
    #  * Notifies any waiting objects that a click has occurred.
    #  
    @synchronized
    def signalClickOccurred(self):
        """ generated source for method signalClickOccurred """
        clickFlag = True
        notifyAll()

    #  Private instance variables 
    myProgram = None
    mousePressedHook = None
    mouseReleasedHook = None
    mouseClickedHook = None
    mouseMovedHook = None
    mouseDraggedHook = None
    clickFlag = bool()

#  Package class: GObjectProgram 
# 
#  * This class is used to launch a program containing a single <code>GObject</code>
#  * instance at its center.
#  
class GObjectProgram(GraphicsProgram):
    """ generated source for class GObjectProgram """
    #  Hook method: runHook() 
    # 
    #  * Calls the run method in the graphical object.
    #  
    def runHook(self):
        """ generated source for method runHook """
        gobj = getStartupObject()
        size = gobj.getSize()
        add(gobj, (getWidth() - size.getWidth()) / 2, (getHeight() - size.getHeight()) / 2)
        try:
            gobjClass = gobj.__class__
            className = gobjClass.__name__
            className = className.substring(className.lastIndexOf(".") + 1)
            setTitle(className)
            run = gobjClass.getMethod("run", [None] * 0)
            if run == None:
                raise ErrorException(className + " has no run method")
            run.invoke(gobj, [None] * 0)
        except Exception as ex:
            raise ErrorException(ex)

