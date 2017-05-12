#!/usr/bin/env python
""" generated source for module GContainer """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
from functools import wraps
from threading import RLock
from GObject import *
# from GFillable import *
# from  GScalable import *
from unresolved import *

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
#  * @(#)GContainer.java   1.99.1 08/12/08
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
#    1. Factored out common implementation of GObjectList.
#    2. Moved GIterator code to this module.
# package: acm.graphics
#  Interface: GContainer 
# 
#  * Defines the functionality of an object that can serve as the parent
#  * of a <a href="GObject.html"><code>GObject</code></a>.
#  
class GContainer(object):
    """ generated source for interface GContainer """
    __metaclass__ = ABCMeta
    #  Constant: BACK_TO_FRONT 
    #  Specifies that iterators should run from back to front 
    BACK_TO_FRONT = 0

    #  Constant: FRONT_TO_BACK 
    #  Specifies that iterators should run from front to back 
    FRONT_TO_BACK = 1

    #  Method: add(gobj) 
    # 
    #  * Adds a new graphical object to this container.
    #  *
    #  * @usage gc.add(gobj);
    #  * @param gobj The graphical object to add
    #  
    # @abstractmethod
    # @overloaded
    def add(self, gobj):
        """ generated source for method add """

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
    # @abstractmethod
    # @add.register(object, GObject, float, float)
    def add_0(self, gobj, x, y):
        """ generated source for method add_0 """

    #  Method: add(gobj, pt) 
    # 
    #  * Adds the graphical object to this canvas and sets its location to the specified point.
    #  *
    #  * @usage gc.add(gobj, pt);
    #  * @param gobj The graphical object to add
    #  * @param pt A <code>GPoint</code> object giving the coordinates of the point
    #  
    # @abstractmethod
    # @add.register(object, GObject, GPoint)
    def add_1(self, gobj, pt):
        """ generated source for method add_1 """

    #  Method: remove(gobj) 
    # 
    #  * Removes a graphical object from this container.
    #  *
    #  * @usage gc.remove(gobj);
    #  * @param gobj The graphical object to remove
    #  
    # @abstractmethod
    def remove(self, gobj):
        """ generated source for method remove """

    #  Method: removeAll() 
    # 
    #  * Removes all graphical objects from this container.
    #  *
    #  * @usage gc.removeAll();
    #  
    # @abstractmethod
    def removeAll(self):
        """ generated source for method removeAll """

    #  Method: getElementCount() 
    # 
    #  * Returns the number of graphical objects stored in this <code>GCanvas</code>.
    #  *
    #  * @usage int n = gc.getElementCount();
    #  * @return The number of graphical objects in this <code>GCanvas</code>
    #  
    # @abstractmethod
    def getElementCount(self):
        """ generated source for method getElementCount """

    #  Method: getElement(index) 
    # 
    #  * Returns the graphical object at the specified index, numbering from back
    #  * to front in the the <i>z</i> dimension.
    #  *
    #  * @usage GObject gobj = gc.getElement(index);
    #  * @param index The index of the component to return
    #  * @return The graphical object at the specified index
    #  
    # @abstractmethod
    def getElement(self, index):
        """ generated source for method getElement """

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
    #  *         if no such object exists.
    #  
    # @abstractmethod
    # @overloaded
    def getElementAt(self, x, y):
        """ generated source for method getElementAt """

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
    # @abstractmethod
    # @getElementAt.register(object, GPoint)
    def getElementAt_0(self, pt):
        """ generated source for method getElementAt_0 """

#  Package class: GObjectList 
# 
#  * This class implements a synchronized list of <code>GObject</code> values
#  * that is shared by both <code>GCompound</code> and <code>GCanvas</code>.
#  * The list includes two sets of objects: one for the ordered list in the
#  * container and another for objects that are enabled to receive mouse
#  * events.
#  
class GObjectList(Serializable):
    """ generated source for class GObjectList """
    #  Constructor: new GObjectList(container) 
    # 
    #  * Creates a new <code>GObjectList</code> with no elements.
    #  *
    #  * @param container The <code>GCanvas</code> or <code>GCompound</code> that owns this list.
    #  
    def __init__(self, container):
        """ generated source for method __init__ """
        super(GObjectList, self).__init__()
        parent = container
        contents = ArrayList()
        if isinstance(parent, (GCanvas, )):
            enabledList = ArrayList()

    #  Method: add(gobj) 
    # 
    #  * Adds the specified <code>GObject</code> to the end of the contents list,
    #  * and includes it in the enabled list if mouse events are enabled.
    #  
    @synchronized
    def add(self, gobj):
        """ generated source for method add """
        if gobj.getParent() != None:
            gobj.getParent().remove(gobj)
        gobj.setParent(parent)
        contents.add(gobj)
        if enabledList != None and gobj.areMouseListenersEnabled():
            enabledList.add(gobj)

    #  Method: remove(gobj) 
    # 
    #  * Removes the specified object from the list.
    #  
    @synchronized
    def remove(self, gobj):
        """ generated source for method remove """
        contents.remove(gobj)
        gobj.setParent(None)
        if enabledList != None:
            enabledList.remove(gobj)

    #  Method: removeAll() 
    # 
    #  * Removes all objects from the list.
    #  
    @synchronized
    def removeAll(self):
        """ generated source for method removeAll """
        contents.clear()
        if enabledList != None:
            enabledList.clear()

    #  Method: getElementCount() 
    # 
    #  * Returns the number of elements in the list.
    #  
    def getElementCount(self):
        """ generated source for method getElementCount """
        return len(contents)

    #  Method: getElement(index) 
    # 
    #  * Returns the graphical object at the specified index, numbering from back
    #  * to front in the the <i>z</i> dimension.
    #  
    def getElement(self, index):
        """ generated source for method getElement """
        return contents.get(index)

    #  Method: getElementAt(x, y, requireEnabled) 
    # 
    #  * Returns the topmost graphical object that contains the point
    #  * (<code>x</code>, <code>y</code>), or <code>null</code> if no such
    #  * object exists.
    #  
    @synchronized
    def getElementAt(self, x, y, requireEnabled):
        """ generated source for method getElementAt """
        list_ = enabledList if (requireEnabled) else contents
        i = len(list_) - 1
        while i >= 0:
            gobj = list_.get(i)
            if gobj.contains(x, y):
                return gobj
            i -= 1
        return None

    #  Method: sendToFront(gobj) 
    # 
    #  * Implements the <code>sendToFront</code> function from the <code>GContainer</code>
    #  * interface.
    #  
    @synchronized
    def sendToFront(self, gobj):
        """ generated source for method sendToFront """
        index = contents.indexOf(gobj)
        if index >= 0:
            contents.remove(index)
            contents.add(gobj)

    #  Method: sendToBack(gobj) 
    # 
    #  * Implements the <code>sendToBack</code> function from the <code>GContainer</code>
    #  * interface.
    #  
    @synchronized
    def sendToBack(self, gobj):
        """ generated source for method sendToBack """
        index = contents.indexOf(gobj)
        if index >= 0:
            contents.remove(index)
            contents.add(0, gobj)

    #  Method: sendForward(gobj) 
    # 
    #  * Implements the <code>sendForward</code> function from the <code>GContainer</code>
    #  * interface.
    #  
    @synchronized
    def sendForward(self, gobj):
        """ generated source for method sendForward """
        index = contents.indexOf(gobj)
        if index >= 0:
            contents.remove(index)
            contents.add(min(len(contents), index + 1), gobj)

    #  Method: sendBackward(gobj) 
    # 
    #  * Implements the <code>sendBackward</code> function from the <code>GContainer</code>
    #  * interface.
    #  
    @synchronized
    def sendBackward(self, gobj):
        """ generated source for method sendBackward """
        index = contents.indexOf(gobj)
        if index >= 0:
            contents.remove(index)
            contents.add(max(0, index - 1), gobj)

    #  Method: getBounds() 
    # 
    #  * Returns the bounding rectangle for the objects in the list.
    #  
    @synchronized
    def getBounds(self):
        """ generated source for method getBounds """
        bounds = GRectangle()
        nElements = len(contents)
        i = 0
        while i < nElements:
            if i == 0:
                bounds = GRectangle(contents.get(i).getBounds())
            else:
                bounds.add(contents.get(i).getBounds())
            i += 1
        return bounds

    #  Method: contains(x, y) 
    # 
    #  * Checks to see whether a point is "inside" one of the objects on the list.
    #  
    @synchronized
    def contains(self, x, y):
        """ generated source for method contains """
        nElements = len(contents)
        i = 0
        while i < nElements:
            if contents.get(i).contains(x, y):
                return True
            i += 1
        return False

    #  Method: mapPaint(g) 
    # 
    #  * Paints all the elements of this container using the graphics context <code>g</code>.
    #  
    @synchronized
    def mapPaint(self, g):
        """ generated source for method mapPaint """
        nElements = len(contents)
        i = 0
        while i < nElements:
            contents.get(i).paintObject(g)
            i += 1

    #  Method: areMouseListenersEnabled() 
    # 
    #  * Returns <code>true</code> if mouse listeners have ever been assigned to
    #  * this object or to any of the contained objects.
    #  
    @synchronized
    def areMouseListenersEnabled(self):
        """ generated source for method areMouseListenersEnabled """
        nElements = len(contents)
        i = 0
        while i < nElements:
            gobj = contents.get(i)
            if gobj.areMouseListenersEnabled():
                return True
            i += 1
        return False

    #  Method: updateEnabledList() 
    # 
    #  * Reconstructs the enabledList list in the correct order.
    #  
    @synchronized
    def updateEnabledList(self):
        """ generated source for method updateEnabledList """
        enabledList.clear()
        nElements = len(contents)
        i = 0
        while i < nElements:
            gobj = contents.get(i)
            if gobj.areMouseListenersEnabled():
                enabledList.add(gobj)
            i += 1

    #  Private instance variables 
    parent = None
    contents = None
    enabledList = None

#  Package class: GIterator 
# 
#  * Implements an iterator class for any object that implements
#  * <code>GContainer</code> (i.e., <a href="GCanvas.html"><code>GCanvas</code></a>
#  * and <a href="GCompound.html"><code>GCompound</code></a>).  The usual method
#  * for using this class is to write something like</p>
#  *
#  * <p><pre><code>
#  * &nbsp;    for (Iterator&lt;GObject&gt; i = gc.iterator(direction); i.hasNext(); )
#  * </code></pre>
#  *
#  * where <code>gc</code> is the graphic container.  The enumeration supports
#  * traversal in two directions.  By default, it starts with the front
#  * element and works toward the back (as would be appropriate, for
#  * example, when trying to find the topmost component for a mouse click).
#  * You can, however, also process the elements of the container from back
#  * to front (as would be useful when drawing elements of the container,
#  * when the front objects should be drawn last).  To specify the direction
#  * of the traversal, specify either <code>GContainer.FRONT_TO_BACK</code> or
#  * <code>GContainer.BACK_TO_FRONT</code> in the <code>iterator</code> call.
#  
class GIterator(Iterator, GObject):
    """ generated source for class GIterator """
    #  Constructor: GIterator(container, direction) 
    # 
    #  * Creates a new <code>GIterator</code> that runs through the
    #  * container in the specified direction (<code>GContainer.FRONT_TO_BACK</code>
    #  * or <code>GContainer.BACK_TO_FRONT</code>).
    #  *
    #  * @usage Iterator<GObject> i = new GIterator(container, direction);
    #  * @param container The <code>GContainer</code> whose elements the iterator should return
    #  * @param direction The direction in which to process the elements
    #  
    def __init__(self, container, direction):
        """ generated source for method __init__ """
        super(GIterator, self).__init__()
        if direction == GContainer.FRONT_TO_BACK:
            pass
        elif direction == GContainer.BACK_TO_FRONT:
            dir = direction
        else:
            raise ErrorException("Illegal direction for iterator")
        cont = container
        index = 0
        nElements = container.getElementCount()

    #  Method: hasNext() 
    # 
    #  * Returns <code>true</code> if the iterator has more elements.  Implements
    #  * the <code>hasNext</code> method for the <code>Iterator</code> interface.
    #  *
    #  * @usage while (i.hasNext()) . . .
    #  * @return <code>true</code> if the iterator has more elements, <code>false</code> otherwise
    #  
    def hasNext(self):
        """ generated source for method hasNext """
        return index < nElements

    #  Method: next() 
    # 
    #  * Returns the next element from the iterator.  Implements the <code>next</code>
    #  * method for the <code>Iterator</code> interface.
    #  *
    #  * @usage Object element = i.next();
    #  * @return The next element from the iterator
    #

    # public GObject next(){
    # if (dir == GContainer.FRONT_TO_BACK){
    #    return cont.getElement(nElements - index + + - 1);
    #   }
    #    else {
    #    return cont.getElement(index + +);
    #    }
    # }


    def next(self):
        """ generated source for method next """
        # public GObject next(){
        # if (dir == GContainer.FRONT_TO_BACK){
        #    return cont.getElement(nElements - index + + - 1);
        #   }
        #    else {
        #    return cont.getElement(index + +);
        #    }
        # }


        # if dir == GContainer.FRONT_TO_BACK:
        # __index_0 = index
        # index += 1
        # __index_1 = index
        # index += 1
        #     return cont.getElement(nElements - __index_1 - 1)
        # else:
        # __index_2 = index
        # index += 1
        # __index_3 = index
        # index += 1
        #     return cont.getElement(__index_3)
        pass


    #  Method: nextElement() 
    # 
    #  * Returns the next element from the iterator as a <code>GObject</code>.  This
    #  * method is callable only if the iterator is declared as a <code>GIterator</code>.
    #  *
    #  * @usage GObject element = i.nextElement();
    #  * @return The next element from the iterator as a <code>GObject</code>
    #  
    def nextElement(self):
        """ generated source for method nextElement """
        return self.next()

    #  Method: remove() 
    # 
    #  * Removes the current element from its container.  Implements the <code>remove</code>
    #  * method for the <code>Iterator</code> interface.
    #  *
    #  * @usage i.remove();
    #  
    def remove(self):
        """ generated source for method remove """
        # if dir == GContainer.FRONT_TO_BACK:
        # index -= 1
        #     cont.remove(cont.getElement(nElements - index - 1))
        # else:
        # index -= 1
        #     cont.remove(cont.getElement(index))
        # nElements -= 1
        #
        # public void remove()
        # {
        # if (dir == GContainer.FRONT_TO_BACK)
        # {
        #     cont.remove(cont.getElement(nElements - --index - 1));
        # } else {
        #     cont.remove(cont.getElement(--index));
        # }
        # nElements - -;
        # }
        pass

    #  Private instance variables
    cont = None
    dir = int()
    index = int()
    nElements = int()

