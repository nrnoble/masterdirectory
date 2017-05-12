#!/usr/bin/env python
""" generated source for module COMPON~1 """
from __future__ import print_function
from functools import wraps
from threading import RLock
from unresolved import *
from ImageObserver import *
from MenuContainer import *


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
#  * Copyright (c) 1995, 2015, Oracle and/or its affiliates. All rights reserved.
#  * ORACLE PROPRIETARY/CONFIDENTIAL. Use is subject to license terms.
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  
# package: java.awt
# 
#  * A <em>component</em> is an object having a graphical representation
#  * that can be displayed on the screen and that can interact with the
#  * user. Examples of components are the buttons, checkboxes, and scrollbars
#  * of a typical graphical user interface. <p>
#  * The <code>Component</code> class is the abstract superclass of
#  * the nonmenu-related Abstract Window Toolkit components. Class
#  * <code>Component</code> can also be extended directly to create a
#  * lightweight component. A lightweight component is a component that is
#  * not associated with a native window. On the contrary, a heavyweight
#  * component is associated with a native window. The {@link #isLightweight()}
#  * method may be used to distinguish between the two kinds of the components.
#  * <p>
#  * Lightweight and heavyweight components may be mixed in a single component
#  * hierarchy. However, for correct operating of such a mixed hierarchy of
#  * components, the whole hierarchy must be valid. When the hierarchy gets
#  * invalidated, like after changing the bounds of components, or
#  * adding/removing components to/from containers, the whole hierarchy must be
#  * validated afterwards by means of the {@link Container#validate()} method
#  * invoked on the top-most invalid container of the hierarchy.
#  *
#  * <h3>Serialization</h3>
#  * It is important to note that only AWT listeners which conform
#  * to the <code>Serializable</code> protocol will be saved when
#  * the object is stored.  If an AWT object has listeners that
#  * aren't marked serializable, they will be dropped at
#  * <code>writeObject</code> time.  Developers will need, as always,
#  * to consider the implications of making an object serializable.
#  * One situation to watch out for is this:
#  * <pre>
#  *    import java.awt.*;
#  *    import java.awt.event.*;
#  *    import java.io.Serializable;
#  *
#  *    class MyApp implements ActionListener, Serializable
#  *    {
#  *        BigObjectThatShouldNotBeSerializedWithAButton bigOne;
#  *        Button aButton = new Button();
#  *
#  *        MyApp()
#  *        {
#  *            // Oops, now aButton has a listener with a reference
#  *            // to bigOne!
#  *            aButton.addActionListener(this);
#  *        }
#  *
#  *        public void actionPerformed(ActionEvent e)
#  *        {
#  *            print("Hello There");
#  *        }
#  *    }
#  * </pre>
#  * In this example, serializing <code>aButton</code> by itself
#  * will cause <code>MyApp</code> and everything it refers to
#  * to be serialized as well.  The problem is that the listener
#  * is serializable by coincidence, not by design.  To separate
#  * the decisions about <code>MyApp</code> and the
#  * <code>ActionListener</code> being serializable one can use a
#  * nested class, as in the following example:
#  * <pre>
#  *    import java.awt.*;
#  *    import java.awt.event.*;
#  *    import java.io.Serializable;
#  *
#  *    class MyApp implements java.io.Serializable
#  *    {
#  *         BigObjectThatShouldNotBeSerializedWithAButton bigOne;
#  *         Button aButton = new Button();
#  *
#  *         static class MyActionListener implements ActionListener
#  *         {
#  *             public void actionPerformed(ActionEvent e)
#  *             {
#  *                 print("Hello There");
#  *             }
#  *         }
#  *
#  *         MyApp()
#  *         {
#  *             aButton.addActionListener(new MyActionListener());
#  *         }
#  *    }
#  * </pre>
#  * <p>
#  * <b>Note</b>: For more information on the paint mechanisms utilitized
#  * by AWT and Swing, including information on how to write the most
#  * efficient painting code, see
#  * <a href="http://www.oracle.com/technetwork/java/painting-140037.html">Painting in AWT and Swing</a>.
#  * <p>
#  * For details on the focus subsystem, see
#  * <a href="https://docs.oracle.com/javase/tutorial/uiswing/misc/focus.html">
#  * How to Use the Focus Subsystem</a>,
#  * a section in <em>The Java Tutorial</em>, and the
#  * <a href="../../java/awt/doc-files/FocusSpec.html">Focus Specification</a>
#  * for more information.
#  *
#  * @author      Arthur van Hoff
#  * @author      Sami Shaio
#  
class Component(ImageObserver, MenuContainer, Serializable):
    """ generated source for class Component """
    log = PlatformLogger.getLogger("java.awt.Component")
    eventLog = PlatformLogger.getLogger("java.awt.event.Component")
    focusLog = PlatformLogger.getLogger("java.awt.focus.Component")
    mixingLog = PlatformLogger.getLogger("java.awt.mixing.Component")

    # 
    #      * The peer of the component. The peer implements the component's
    #      * behavior. The peer is set when the <code>Component</code> is
    #      * added to a container that also is a peer.
    #      * @see #addNotify
    #      * @see #removeNotify
    #      
    peer = None

    # 
    #      * The parent of the object. It may be <code>null</code>
    #      * for top-level components.
    #      * @see #getParent
    #      
    parent = None

    # 
    #      * The <code>AppContext</code> of the component. Applets/Plugin may
    #      * change the AppContext.
    #      
    appContext = None

    # 
    #      * The x position of the component in the parent's coordinate system.
    #      *
    #      * @serial
    #      * @see #getLocation
    #      
    x = int()

    # 
    #      * The y position of the component in the parent's coordinate system.
    #      *
    #      * @serial
    #      * @see #getLocation
    #      
    y = int()

    # 
    #      * The width of the component.
    #      *
    #      * @serial
    #      * @see #getSize
    #      
    width = int()

    # 
    #      * The height of the component.
    #      *
    #      * @serial
    #      * @see #getSize
    #      
    height = int()

    # 
    #      * The foreground color for this component.
    #      * <code>foreground</code> can be <code>null</code>.
    #      *
    #      * @serial
    #      * @see #getForeground
    #      * @see #setForeground
    #      
    foreground = None

    # 
    #      * The background color for this component.
    #      * <code>background</code> can be <code>null</code>.
    #      *
    #      * @serial
    #      * @see #getBackground
    #      * @see #setBackground
    #      
    background = None

    # 
    #      * The font used by this component.
    #      * The <code>font</code> can be <code>null</code>.
    #      *
    #      * @serial
    #      * @see #getFont
    #      * @see #setFont
    #      
    font = None

    # 
    #      * The font which the peer is currently using.
    #      * (<code>null</code> if no peer exists.)
    #      
    peerFont = None

    # 
    #      * The cursor displayed when pointer is over this component.
    #      * This value can be <code>null</code>.
    #      *
    #      * @serial
    #      * @see #getCursor
    #      * @see #setCursor
    #      
    cursor = None

    # 
    #      * The locale for the component.
    #      *
    #      * @serial
    #      * @see #getLocale
    #      * @see #setLocale
    #      
    locale = None

    # 
    #      * A reference to a <code>GraphicsConfiguration</code> object
    #      * used to describe the characteristics of a graphics
    #      * destination.
    #      * This value can be <code>null</code>.
    #      *
    #      * @since 1.3
    #      * @serial
    #      * @see GraphicsConfiguration
    #      * @see #getGraphicsConfiguration
    #      
    graphicsConfig = None

    # 
    #      * A reference to a <code>BufferStrategy</code> object
    #      * used to manipulate the buffers on this component.
    #      *
    #      * @since 1.4
    #      * @see java.awt.image.BufferStrategy
    #      * @see #getBufferStrategy()
    #      
    bufferStrategy = None

    # 
    #      * True when the object should ignore all repaint events.
    #      *
    #      * @since 1.4
    #      * @serial
    #      * @see #setIgnoreRepaint
    #      * @see #getIgnoreRepaint
    #      
    ignoreRepaint = False

    # 
    #      * True when the object is visible. An object that is not
    #      * visible is not drawn on the screen.
    #      *
    #      * @serial
    #      * @see #isVisible
    #      * @see #setVisible
    #      
    visible = True

    # 
    #      * True when the object is enabled. An object that is not
    #      * enabled does not interact with the user.
    #      *
    #      * @serial
    #      * @see #isEnabled
    #      * @see #setEnabled
    #      
    enabled = True

    # 
    #      * True when the object is valid. An invalid object needs to
    #      * be layed out. This flag is set to false when the object
    #      * size is changed.
    #      *
    #      * @serial
    #      * @see #isValid
    #      * @see #validate
    #      * @see #invalidate
    #      
    valid = False

    # 
    #      * The <code>DropTarget</code> associated with this component.
    #      *
    #      * @since 1.2
    #      * @serial
    #      * @see #setDropTarget
    #      * @see #getDropTarget
    #      
    dropTarget = None

    # 
    #      * @serial
    #      * @see #add
    #      
    popups = None

    # 
    #      * A component's name.
    #      * This field can be <code>null</code>.
    #      *
    #      * @serial
    #      * @see #getName
    #      * @see #setName(String)
    #      
    name = None

    # 
    #      * A bool to determine whether the name has
    #      * been set explicitly. <code>nameExplicitlySet</code> will
    #      * be false if the name has not been set and
    #      * true if it has.
    #      *
    #      * @serial
    #      * @see #getName
    #      * @see #setName(String)
    #      
    nameExplicitlySet = False

    # 
    #      * Indicates whether this Component can be focused.
    #      *
    #      * @serial
    #      * @see #setFocusable
    #      * @see #isFocusable
    #      * @since 1.4
    #      
    focusable = True
    FOCUS_TRAVERSABLE_UNKNOWN = 0
    FOCUS_TRAVERSABLE_DEFAULT = 1
    FOCUS_TRAVERSABLE_SET = 2

    # 
    #      * Tracks whether this Component is relying on default focus travesability.
    #      *
    #      * @serial
    #      * @since 1.4
    #      
    isFocusTraversableOverridden = FOCUS_TRAVERSABLE_UNKNOWN

    # 
    #      * The focus traversal keys. These keys will generate focus traversal
    #      * behavior for Components for which focus traversal keys are enabled. If a
    #      * value of null is specified for a traversal key, this Component inherits
    #      * that traversal key from its parent. If all ancestors of this Component
    #      * have null specified for that traversal key, then the current
    #      * KeyboardFocusManager's default traversal key is used.
    #      *
    #      * @serial
    #      * @see #setFocusTraversalKeys
    #      * @see #getFocusTraversalKeys
    #      * @since 1.4
    #      
    focusTraversalKeys = []
    focusTraversalKeyPropertyNames = ["forwardFocusTraversalKeys", "backwardFocusTraversalKeys", "upCycleFocusTraversalKeys", "downCycleFocusTraversalKeys"]

    # 
    #      * Components for which focus traversal keys are disabled receive key
    #      * events for focus traversal keys. Components for which focus traversal
    #      * keys are enabled do not see these events; instead, the events are
    #      * automatically converted to traversal operations.
    #      *
    #      * @serial
    #      * @see #setFocusTraversalKeysEnabled
    #      * @see #getFocusTraversalKeysEnabled
    #      * @since 1.4
    #      
    focusTraversalKeysEnabled = True

    # 
    #      * The locking object for AWT component-tree and layout operations.
    #      *
    #      * @see #getTreeLock
    #      
    LOCK = AWTTreeLock()

    class AWTTreeLock(object):
        """ generated source for class AWTTreeLock """

    # 
    #      * The component's AccessControlContext.
    #      
    acc = AccessController.getContext()

    # 
    #      * Minimum size.
    #      * (This field perhaps should have been transient).
    #      *
    #      * @serial
    #      
    minSize = None

    # 
    #      * Whether or not setMinimumSize has been invoked with a non-null value.
    #      
    minSizeSet = bool()

    # 
    #      * Preferred size.
    #      * (This field perhaps should have been transient).
    #      *
    #      * @serial
    #      
    prefSize = None

    # 
    #      * Whether or not setPreferredSize has been invoked with a non-null value.
    #      
    prefSizeSet = bool()

    # 
    #      * Maximum size
    #      *
    #      * @serial
    #      
    maxSize = None

    # 
    #      * Whether or not setMaximumSize has been invoked with a non-null value.
    #      
    maxSizeSet = bool()

    # 
    #      * The orientation for this component.
    #      * @see #getComponentOrientation
    #      * @see #setComponentOrientation
    #      
    componentOrientation = ComponentOrientation.UNKNOWN

    # 
    #      * <code>newEventsOnly</code> will be true if the event is
    #      * one of the event types enabled for the component.
    #      * It will then allow for normal processing to
    #      * continue.  If it is false the event is passed
    #      * to the component's parent and up the ancestor
    #      * tree until the event has been consumed.
    #      *
    #      * @serial
    #      * @see #dispatchEvent
    #      
    newEventsOnly = False
    componentListener = None
    focusListener = None
    hierarchyListener = None
    hierarchyBoundsListener = None
    keyListener = None
    mouseListener = None
    mouseMotionListener = None
    mouseWheelListener = None
    inputMethodListener = None
    windowClosingException = None

    #  Internal, constants for serialization 
    actionListenerK = "actionL"
    adjustmentListenerK = "adjustmentL"
    componentListenerK = "componentL"
    containerListenerK = "containerL"
    focusListenerK = "focusL"
    itemListenerK = "itemL"
    keyListenerK = "keyL"
    mouseListenerK = "mouseL"
    mouseMotionListenerK = "mouseMotionL"
    mouseWheelListenerK = "mouseWheelL"
    textListenerK = "textL"
    ownedWindowK = "ownedL"
    windowListenerK = "windowL"
    inputMethodListenerK = "inputMethodL"
    hierarchyListenerK = "hierarchyL"
    hierarchyBoundsListenerK = "hierarchyBoundsL"
    windowStateListenerK = "windowStateL"
    windowFocusListenerK = "windowFocusL"

    # 
    #      * The <code>eventMask</code> is ONLY set by subclasses via
    #      * <code>enableEvents</code>.
    #      * The mask should NOT be set when listeners are registered
    #      * so that we can distinguish the difference between when
    #      * listeners request events and subclasses request them.
    #      * One bit is used to indicate whether input methods are
    #      * enabled; this bit is set by <code>enableInputMethods</code> and is
    #      * on by default.
    #      *
    #      * @serial
    #      * @see #enableInputMethods
    #      * @see AWTEvent
    #      
    eventMask = AWTEvent.INPUT_METHODS_ENABLED_MASK

    # 
    #      * Static properties for incremental drawing.
    #      * @see #imageUpdate
    #      
    isInc = bool()
    incRate = int()

    #  ensure that the necessary native libraries are loaded 
    #  initialize JNI field and method ids 
    s = java.security.AccessController.doPrivileged(GetPropertyAction("awt.image.incrementaldraw"))

    # 
    #      * Ease-of-use constant for <code>getAlignmentY()</code>.
    #      * Specifies an alignment to the top of the component.
    #      * @see     #getAlignmentY
    #      
    TOP_ALIGNMENT = 0.0

    # 
    #      * Ease-of-use constant for <code>getAlignmentY</code> and
    #      * <code>getAlignmentX</code>. Specifies an alignment to
    #      * the center of the component
    #      * @see     #getAlignmentX
    #      * @see     #getAlignmentY
    #      
    CENTER_ALIGNMENT = 0.5

    # 
    #      * Ease-of-use constant for <code>getAlignmentY</code>.
    #      * Specifies an alignment to the bottom of the component.
    #      * @see     #getAlignmentY
    #      
    BOTTOM_ALIGNMENT = 1.0

    # 
    #      * Ease-of-use constant for <code>getAlignmentX</code>.
    #      * Specifies an alignment to the left side of the component.
    #      * @see     #getAlignmentX
    #      
    LEFT_ALIGNMENT = 0.0

    # 
    #      * Ease-of-use constant for <code>getAlignmentX</code>.
    #      * Specifies an alignment to the right side of the component.
    #      * @see     #getAlignmentX
    #      
    RIGHT_ALIGNMENT = 1.0

    # 
    #      * JDK 1.1 serialVersionUID
    #      
    serialVersionUID = -7644114512714619750

    # 
    #      * If any <code>PropertyChangeListeners</code> have been registered,
    #      * the <code>changeSupport</code> field describes them.
    #      *
    #      * @serial
    #      * @since 1.2
    #      * @see #addPropertyChangeListener
    #      * @see #removePropertyChangeListener
    #      * @see #firePropertyChange
    #      
    changeSupport = None

    # 
    #      * In some cases using "this" as an object to synchronize by
    #      * can lead to a deadlock if client code also uses synchronization
    #      * by a component object. For every such situation revealed we should
    #      * consider possibility of replacing "this" with the package private
    #      * objectLock object introduced below. So far there're 3 issues known:
    #      * - CR 6708322 (the getName/setName methods);
    #      * - CR 6608764 (the PropertyChangeListener machinery);
    #      * - CR 7108598 (the Container.paint/KeyboardFocusManager.clearMostRecentFocusOwner methods).
    #      *
    #      * Note: this field is considered final, though readObject() prohibits
    #      * initializing final fields.
    #      
    objectLock = object()

    def getObjectLock(self):
        """ generated source for method getObjectLock """
        return self.objectLock

    # 
    #      * Returns the acc this component was constructed with.
    #      
    @overloaded
    def getAccessControlContext(self):
        """ generated source for method getAccessControlContext """
        if self.acc == None:
            raise SecurityException("Component is missing AccessControlContext")
        return self.acc

    isPacked = False

    # 
    #      * Pseudoparameter for direct Geometry API (setLocation, setBounds setSize
    #      * to signal setBounds what's changing. Should be used under TreeLock.
    #      * This is only needed due to the inability to change the cross-calling
    #      * order of public and deprecated methods.
    #      
    boundsOp = ComponentPeer.DEFAULT_OPERATION

    # 
    #      * Enumeration of the common ways the baseline of a component can
    #      * change as the size changes.  The baseline resize behavior is
    #      * primarily for layout managers that need to know how the
    #      * position of the baseline changes as the component size changes.
    #      * In general the baseline resize behavior will be valid for sizes
    #      * greater than or equal to the minimum size (the actual minimum
    #      * size; not a developer specified minimum size).  For sizes
    #      * smaller than the minimum size the baseline may change in a way
    #      * other than the baseline resize behavior indicates.  Similarly,
    #      * as the size approaches <code>Integer.MAX_VALUE</code> and/or
    #      * <code>Short.MAX_VALUE</code> the baseline may change in a way
    #      * other than the baseline resize behavior indicates.
    #      *
    #      * @see #getBaselineResizeBehavior
    #      * @see #getBaseline(int,int)
    #      * @since 1.6
    #      
    class BaselineResizeBehavior:
        """ generated source for enum BaselineResizeBehavior """
        CONSTANT_ASCENT = u'CONSTANT_ASCENT'
        CONSTANT_DESCENT = u'CONSTANT_DESCENT'
        CENTER_OFFSET = u'CENTER_OFFSET'
        OTHER = u'OTHER'

        # 
        #          * Indicates the baseline remains fixed relative to the
        #          * y-origin.  That is, <code>getBaseline</code> returns
        #          * the same value regardless of the height or width.  For example, a
        #          * <code>JLabel</code> containing non-empty text with a
        #          * vertical alignment of <code>TOP</code> should have a
        #          * baseline type of <code>CONSTANT_ASCENT</code>.
        #          
        # 
        #          * Indicates the baseline remains fixed relative to the height
        #          * and does not change as the width is varied.  That is, for
        #          * any height H the difference between H and
        #          * <code>getBaseline(w, H)</code> is the same.  For example, a
        #          * <code>JLabel</code> containing non-empty text with a
        #          * vertical alignment of <code>BOTTOM</code> should have a
        #          * baseline type of <code>CONSTANT_DESCENT</code>.
        #          
        # 
        #          * Indicates the baseline remains a fixed distance from
        #          * the center of the component.  That is, for any height H the
        #          * difference between <code>getBaseline(w, H)</code> and
        #          * <code>H / 2</code> is the same (plus or minus one depending upon
        #          * rounding error).
        #          * <p>
        #          * Because of possible rounding errors it is recommended
        #          * you ask for the baseline with two consecutive heights and use
        #          * the return value to determine if you need to pad calculations
        #          * by 1.  The following shows how to calculate the baseline for
        #          * any height:
        #          * <pre>
        #          *   Dimension preferredSize = component.getPreferredSize();
        #          *   int baseline = getBaseline(preferredSize.width,
        #          *                              preferredSize.height);
        #          *   int nextBaseline = getBaseline(preferredSize.width,
        #          *                                  preferredSize.height + 1);
        #          *   // Amount to add to height when calculating where baseline
        #          *   // lands for a particular height:
        #          *   int padding = 0;
        #          *   // Where the baseline is relative to the mid point
        #          *   int baselineOffset = baseline - height / 2;
        #          *   if (preferredSize.height % 2 == 0 &amp;&amp;
        #          *       baseline != nextBaseline) {
        #          *       padding = 1;
        #          *   }
        #          *   else if (preferredSize.height % 2 == 1 &amp;&amp;
        #          *            baseline == nextBaseline) {
        #          *       baselineOffset--;
        #          *       padding = 1;
        #          *   }
        #          *   // The following calculates where the baseline lands for
        #          *   // the height z:
        #          *   int calculatedBaseline = (z + padding) / 2 + baselineOffset;
        #          * </pre>
        #          
        # 
        #          * Indicates the baseline resize behavior can not be expressed using
        #          * any of the other constants.  This may also indicate the baseline
        #          * varies with the width of the component.  This is also returned
        #          * by components that do not have a baseline.
        #          

    # 
    #      * The shape set with the applyCompoundShape() method. It uncludes the result
    #      * of the HW/LW mixing related shape computation. It may also include
    #      * the user-specified shape of the component.
    #      * The 'null' value means the component has normal shape (or has no shape at all)
    #      * and applyCompoundShape() will skip the following shape identical to normal.
    #      
    compoundShape = None

    # 
    #      * Represents the shape of this lightweight component to be cut out from
    #      * heavyweight components should they intersect. Possible values:
    #      *    1. null - consider the shape rectangular
    #      *    2. EMPTY_REGION - nothing gets cut out (children still get cut out)
    #      *    3. non-empty - this shape gets cut out.
    #      
    mixingCutoutRegion = None

    # 
    #      * Indicates whether addNotify() is complete
    #      * (i.e. the peer is created).
    #      
    isAddNotifyComplete = False

    # 
    #      * Should only be used in subclass getBounds to check that part of bounds
    #      * is actualy changing
    #      
    def getBoundsOp(self):
        """ generated source for method getBoundsOp """
        assert Thread.holdsLock(getTreeLock())
        return self.boundsOp

    def setBoundsOp(self, op):
        """ generated source for method setBoundsOp """
        assert Thread.holdsLock(getTreeLock())
        if op == ComponentPeer.RESET_OPERATION:
            self.boundsOp = ComponentPeer.DEFAULT_OPERATION
        elif self.boundsOp == ComponentPeer.DEFAULT_OPERATION:
            self.boundsOp = op

    #  Whether this Component has had the background erase flag
    #  specified via SunToolkit.disableBackgroundErase(). This is
    #  needed in order to make this function work on X11 platforms,
    #  where currently there is no chance to interpose on the creation
    #  of the peer and therefore the call to XSetBackground.
    backgroundEraseDisabled = bool()

    def setBackgroundEraseDisabled(self, comp, disabled):
        """ generated source for method setBackgroundEraseDisabled """
        comp.backgroundEraseDisabled = disabled

    def getBackgroundEraseDisabled(self, comp):
        """ generated source for method getBackgroundEraseDisabled """
        return comp.backgroundEraseDisabled

    @overloaded
    def getBounds(self, comp):
        """ generated source for method getBounds """
        return Rectangle(comp.x, comp.y, comp.width, comp.height)

    def setMixingCutoutShape(self, comp, shape):
        """ generated source for method setMixingCutoutShape """
        region = None if shape == None else Region.getInstance(shape, None)
        with lock_for_object(comp.getTreeLock()):
            needShowing = False
            needHiding = False
            if not comp.isNonOpaqueForMixing():
                needHiding = True
            comp.mixingCutoutRegion = region
            if not comp.isNonOpaqueForMixing():
                needShowing = True
            if comp.isMixingNeeded():
                if needHiding:
                    comp.mixOnHiding(comp.isLightweight())
                if needShowing:
                    comp.mixOnShowing()

    @overloaded
    def setGraphicsConfiguration(self, comp, gc):
        """ generated source for method setGraphicsConfiguration """
        comp.setGraphicsConfiguration(gc)

    @overloaded
    def requestFocus(self, comp, cause):
        """ generated source for method requestFocus """
        return comp.requestFocus(cause)

    @overloaded
    def canBeFocusOwner(self, comp):
        """ generated source for method canBeFocusOwner """
        return comp.canBeFocusOwner()

    @overloaded
    def isVisible(self, comp):
        """ generated source for method isVisible """
        return comp.isVisible_NoClientCode()

    @overloaded
    def setRequestFocusController(self, requestController):
        """ generated source for method setRequestFocusController """
        Component.setRequestFocusController(requestController)

    def getAppContext(self, comp):
        """ generated source for method getAppContext """
        return comp.appContext

    def setAppContext(self, comp, appContext):
        """ generated source for method setAppContext """
        comp.appContext = appContext

    @overloaded
    def getParent(self, comp):
        """ generated source for method getParent """
        return comp.getParent_NoClientCode()

    def setParent(self, comp, parent):
        """ generated source for method setParent """
        comp.parent = parent

    @overloaded
    def setSize(self, comp, width, height):
        """ generated source for method setSize """
        comp.width = width
        comp.height = height

    @overloaded
    def getLocation(self, comp):
        """ generated source for method getLocation """
        return comp.location_NoClientCode()

    @overloaded
    def setLocation(self, comp, x, y):
        """ generated source for method setLocation """
        comp.x = x
        comp.y = y

    @overloaded
    def isEnabled(self, comp):
        """ generated source for method isEnabled """
        return comp.isEnabledImpl()

    @overloaded
    def isDisplayable(self, comp):
        """ generated source for method isDisplayable """
        return comp.peer != None

    @overloaded
    def getCursor(self, comp):
        """ generated source for method getCursor """
        return comp.getCursor_NoClientCode()

    @overloaded
    def getPeer(self, comp):
        """ generated source for method getPeer """
        return comp.peer

    def setPeer(self, comp, peer):
        """ generated source for method setPeer """
        comp.peer = peer

    # @overloaded
    # def isLightweight(self, comp):
    #     """ generated source for method isLightweight """
    #     return (isinstance(, (LightweightPeer, )))

    @overloaded
    def getIgnoreRepaint(self, comp):
        """ generated source for method getIgnoreRepaint """
        return comp.ignoreRepaint

    @overloaded
    def getWidth(self, comp):
        """ generated source for method getWidth """
        return comp.width

    @overloaded
    def getHeight(self, comp):
        """ generated source for method getHeight """
        return comp.height

    @overloaded
    def getX(self, comp):
        """ generated source for method getX """
        return comp.x

    @overloaded
    def getY(self, comp):
        """ generated source for method getY """
        return comp.y

    @overloaded
    def getForeground(self, comp):
        """ generated source for method getForeground """
        return comp.foreground

    @overloaded
    def getBackground(self, comp):
        """ generated source for method getBackground """
        return comp.background

    @overloaded
    def setBackground(self, comp, background):
        """ generated source for method setBackground """
        comp.background = background

    @overloaded
    def getFont(self, comp):
        """ generated source for method getFont """
        return comp.getFont_NoClientCode()

    @overloaded
    def processEvent(self, comp, e):
        """ generated source for method processEvent """
        comp.processEvent(e)

    @getAccessControlContext.register(object, Component)
    def getAccessControlContext_0(self, comp):
        """ generated source for method getAccessControlContext_0 """
        return comp.getAccessControlContext()

    @overloaded
    def revalidateSynchronously(self, comp):
        """ generated source for method revalidateSynchronously """
        comp.revalidateSynchronously()

    # 
    #      * Constructs a new component. Class <code>Component</code> can be
    #      * extended directly to create a lightweight component that does not
    #      * utilize an opaque native window. A lightweight component must be
    #      * hosted by a native container somewhere higher up in the component
    #      * tree (for example, by a <code>Frame</code> object).
    #      
    def __init__(self):
        """ generated source for method __init__ """
        super(Component, self).__init__()
        self.appContext = AppContext.getAppContext()

    @SuppressWarnings("unchecked")
    def initializeFocusTraversalKeys(self):
        """ generated source for method initializeFocusTraversalKeys """
        self.focusTraversalKeys = [None] * 3

    # 
    #      * Constructs a name for this component.  Called by <code>getName</code>
    #      * when the name is <code>null</code>.
    #      
    def constructComponentName(self):
        """ generated source for method constructComponentName """
        return None
        #  For strict compliance with prior platform versions, a Component
        #  that doesn't set its name should return null from
        #  getName()

    # 
    #      * Gets the name of the component.
    #      * @return this component's name
    #      * @see    #setName
    #      * @since JDK1.1
    #      
    def getName(self):
        """ generated source for method getName """
        if self.name == None and not self.nameExplicitlySet:
            with lock_for_object(self.getObjectLock()):
                if self.name == None and not self.nameExplicitlySet:
                    self.name = self.constructComponentName()
        return self.name

    # 
    #      * Sets the name of the component to the specified string.
    #      * @param name  the string that is to be this
    #      *           component's name
    #      * @see #getName
    #      * @since JDK1.1
    #      
    def setName(self, name):
        """ generated source for method setName """
        oldName = None
        with lock_for_object(self.getObjectLock()):
            oldName = self.name
            self.name = name
            self.nameExplicitlySet = True
        firePropertyChange("name", oldName, name)

    # 
    #      * Gets the parent of this component.
    #      * @return the parent container of this component
    #      * @since JDK1.0
    #      
    @getParent.register(object)
    def getParent_0(self):
        """ generated source for method getParent_0 """
        return getParent_NoClientCode()

    #  NOTE: This method may be called by privileged threads.
    #        This functionality is implemented in a package-private method
    #        to insure that it cannot be overridden by client subclasses.
    #        DO NOT INVOKE CLIENT CODE ON THIS THREAD!
    def getParent_NoClientCode(self):
        """ generated source for method getParent_NoClientCode """
        return self.parent

    #  This method is overridden in the Window class to return null,
    #     because the parent field of the Window object contains
    #     the owner of the window, not its parent.
    def getContainer(self):
        """ generated source for method getContainer """
        return self.getParent_NoClientCode()

    # 
    #      * @deprecated As of JDK version 1.1,
    #      * programs should not directly manipulate peers;
    #      * replaced by <code>boolean isDisplayable()</code>.
    #      
    @getPeer.register(object)
    def getPeer_0(self):
        """ generated source for method getPeer_0 """
        return self.peer

    # 
    #      * Associate a <code>DropTarget</code> with this component.
    #      * The <code>Component</code> will receive drops only if it
    #      * is enabled.
    #      *
    #      * @see #isEnabled
    #      * @param dt The DropTarget
    #      
    @synchronized
    def setDropTarget(self, dt):
        """ generated source for method setDropTarget """
        if dt == self.dropTarget or (self.dropTarget != None and self.dropTarget == dt):
            return
        old = None
        if (old == self.dropTarget) != None:
            if self.peer != None:
                self.dropTarget.removeNotify(self.peer)
            t = self.dropTarget
            self.dropTarget = None
            try:
                t.setComponent(None)
            except IllegalArgumentException as iae:
                pass
                #  ignore it.
        #  if we have a new one, and we have a peer, add it!
        if (self.dropTarget == dt) != None:
            try:
                self.dropTarget.setComponent(self)
                if self.peer != None:
                    self.dropTarget.addNotify(self.peer)
            except IllegalArgumentException as iae:
                if old != None:
                    try:
                        old.setComponent(self)
                        if self.peer != None:
                            self.dropTarget.addNotify(self.peer)
                    except IllegalArgumentException as iae1:
                        pass
                        #  ignore it!

    # 
    #      * Gets the <code>DropTarget</code> associated with this
    #      * <code>Component</code>.
    #      
    @synchronized
    def getDropTarget(self):
        """ generated source for method getDropTarget """
        return self.dropTarget

    # 
    #      * Gets the <code>GraphicsConfiguration</code> associated with this
    #      * <code>Component</code>.
    #      * If the <code>Component</code> has not been assigned a specific
    #      * <code>GraphicsConfiguration</code>,
    #      * the <code>GraphicsConfiguration</code> of the
    #      * <code>Component</code> object's top-level container is
    #      * returned.
    #      * If the <code>Component</code> has been created, but not yet added
    #      * to a <code>Container</code>, this method returns <code>null</code>.
    #      *
    #      * @return the <code>GraphicsConfiguration</code> used by this
    #      *          <code>Component</code> or <code>null</code>
    #      * @since 1.3
    #      
    def getGraphicsConfiguration(self):
        """ generated source for method getGraphicsConfiguration """
        with lock_for_object(getTreeLock()):
            return getGraphicsConfiguration_NoClientCode()

    def getGraphicsConfiguration_NoClientCode(self):
        """ generated source for method getGraphicsConfiguration_NoClientCode """
        return self.graphicsConfig

    @setGraphicsConfiguration.register(object, GraphicsConfiguration)
    def setGraphicsConfiguration_0(self, gc):
        """ generated source for method setGraphicsConfiguration_0 """
        with lock_for_object(getTreeLock()):
            if updateGraphicsData(gc):
                removeNotify()
                addNotify()

    def updateGraphicsData(self, gc):
        """ generated source for method updateGraphicsData """
        checkTreeLock()
        if self.graphicsConfig == gc:
            return False
        self.graphicsConfig = gc
        peer = self.getPeer()
        if peer != None:
            return peer.updateGraphicsData(gc)
        return False

    # 
    #      * Checks that this component's <code>GraphicsDevice</code>
    #      * <code>idString</code> matches the string argument.
    #      
    def checkGD(self, stringID):
        """ generated source for method checkGD """
        if self.graphicsConfig != None:
            if not self.graphicsConfig.getDevice().getIDstring() == stringID:
                raise IllegalArgumentException("adding a container to a container on a different GraphicsDevice")

    def getTreeLock(self):
        """ generated source for method getTreeLock """
        return self.LOCK

    def checkTreeLock(self):
        """ generated source for method checkTreeLock """
        if not Thread.holdsLock(self.getTreeLock()):
            raise IllegalStateException("This function should be called while holding treeLock")

    def getToolkit(self):
        """ generated source for method getToolkit """
        return getToolkitImpl()

    def getToolkitImpl(self):
        """ generated source for method getToolkitImpl """
        parent = self.parent
        if parent != None:
            return parent.getToolkitImpl()
        return Toolkit.getDefaultToolkit()

    def isValid(self):
        """ generated source for method isValid """
        return (self.peer != None) and self.valid

    @isDisplayable.register(object)
    def isDisplayable_0(self):
        """ generated source for method isDisplayable_0 """
        return self.getPeer() != None

    @isVisible.register(object)
    def isVisible_0(self):
        """ generated source for method isVisible_0 """
        return isVisible_NoClientCode()

    def isVisible_NoClientCode(self):
        """ generated source for method isVisible_NoClientCode """
        return self.visible

    def isRecursivelyVisible(self):
        """ generated source for method isRecursivelyVisible """
        return self.visible and (self.parent == None or self.parent.isRecursivelyVisible())

    def getRecursivelyVisibleBounds(self):
        """ generated source for method getRecursivelyVisibleBounds """
        container = self.getContainer()
        bounds = self.getBounds()
        if container == None:
            return bounds
        parentsBounds = container.getRecursivelyVisibleBounds()
        parentsBounds.setLocation(0, 0)
        return parentsBounds.intersection(bounds)

    def pointRelativeToComponent(self, absolute):
        """ generated source for method pointRelativeToComponent """
        compCoords = getLocationOnScreen()
        return Point(absolute.x - compCoords.x, absolute.y - compCoords.y)

    def findUnderMouseInWindow(self, pi):
        """ generated source for method findUnderMouseInWindow """
        if not isShowing():
            return None
        win = getContainingWindow()
        if not Toolkit.getDefaultToolkit().getMouseInfoPeer().isWindowUnderMouse(win):
            return None
        INCLUDE_DISABLED = True
        relativeToWindow = win.pointRelativeToComponent(pi.getLocation())
        inTheSameWindow = win.findComponentAt(relativeToWindow.x, relativeToWindow.y, INCLUDE_DISABLED)
        return inTheSameWindow

    def getMousePosition(self):
        """ generated source for method getMousePosition """
        if GraphicsEnvironment.isHeadless():
            raise HeadlessException()
        pi = java.security.AccessController.doPrivileged(java.security.PrivilegedAction())
        with lock_for_object(self.getTreeLock()):
            inTheSameWindow = self.findUnderMouseInWindow(pi)
            if not isSameOrAncestorOf(inTheSameWindow, True):
                return None
            return self.pointRelativeToComponent(pi.getLocation())

    def isSameOrAncestorOf(self, comp, allowChildren):
        """ generated source for method isSameOrAncestorOf """
        return comp == self

    def isShowing(self):
        """ generated source for method isShowing """
        if self.visible and (self.peer != None):
            parent = self.parent
            return (self.parent == None) or self.parent.isShowing()
        return False

    @isEnabled.register(object)
    def isEnabled_0(self):
        """ generated source for method isEnabled_0 """
        return isEnabledImpl()

    def isEnabledImpl(self):
        """ generated source for method isEnabledImpl """
        return self.enabled

    def setEnabled(self, b):
        """ generated source for method setEnabled """
        enable(b)

    @overloaded
    def enable(self):
        """ generated source for method enable """
        if not self.enabled:
            with lock_for_object(self.getTreeLock()):
                self.enabled = True
                peer = self.peer
                if self.peer != None:
                    self.peer.setEnabled(True)
                    if self.visible and not self.getRecursivelyVisibleBounds().isEmpty():
                        updateCursorImmediately()
            if accessibleContext != None:
                accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, None, AccessibleState.ENABLED)

    @enable.register(object, bool)
    def enable_0(self, b):
        """ generated source for method enable_0 """
        if b:
            self.enable()
        else:
            disable()

    def disable(self):
        """ generated source for method disable """
        if self.enabled:
            KeyboardFocusManager.clearMostRecentFocusOwner(self)
            with lock_for_object(self.getTreeLock()):
                self.enabled = False
                if (isFocusOwner() or (containsFocus() and not self.isLightweight())) and KeyboardFocusManager.isAutoFocusTransferEnabled():
                    transferFocus(False)
                peer = self.peer
                if self.peer != None:
                    self.peer.setEnabled(False)
                    if self.visible and not self.getRecursivelyVisibleBounds().isEmpty():
                        updateCursorImmediately()
            if accessibleContext != None:
                accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, None, AccessibleState.ENABLED)

    def isDoubleBuffered(self):
        """ generated source for method isDoubleBuffered """
        return False

    def enableInputMethods(self, enable):
        """ generated source for method enableInputMethods """
        if enable:
            if (self.eventMask & AWTEvent.INPUT_METHODS_ENABLED_MASK) != 0:
                return
            if isFocusOwner():
                inputContext = getInputContext()
                if inputContext != None:
                    focusGainedEvent = FocusEvent(self, FocusEvent.FOCUS_GAINED)
                    inputContext.dispatchEvent(focusGainedEvent)
            self.eventMask |= AWTEvent.INPUT_METHODS_ENABLED_MASK
        else:
            if (self.eventMask & AWTEvent.INPUT_METHODS_ENABLED_MASK) != 0:
                inputContext = getInputContext()
                if inputContext != None:
                    inputContext.endComposition()
                    inputContext.removeNotify(self)
            self.eventMask &= ~AWTEvent.INPUT_METHODS_ENABLED_MASK

    def setVisible(self, b):
        """ generated source for method setVisible """
        show(b)

    @overloaded
    def show(self):
        """ generated source for method show """
        if not self.visible:
            with lock_for_object(self.getTreeLock()):
                self.visible = True
                mixOnShowing()
                peer = self.peer
                if self.peer != None:
                    self.peer.setVisible(True)
                    createHierarchyEvents(HierarchyEvent.HIERARCHY_CHANGED, self, self.parent, HierarchyEvent.SHOWING_CHANGED, Toolkit.enabledOnToolkit(AWTEvent.HIERARCHY_EVENT_MASK))
                    if isinstance(self.peer, (LightweightPeer, )):
                        repaint()
                    updateCursorImmediately()
                if self.componentListener != None or (self.eventMask & AWTEvent.COMPONENT_EVENT_MASK) != 0 or Toolkit.enabledOnToolkit(AWTEvent.COMPONENT_EVENT_MASK):
                    e = ComponentEvent(self, ComponentEvent.COMPONENT_SHOWN)
                    Toolkit.getEventQueue().postEvent(e)
            parent = self.parent
            if self.parent != None:
                self.parent.invalidate()

    @show.register(object, bool)
    def show_0(self, b):
        """ generated source for method show_0 """
        if b:
            self.show()
        else:
            hide()

    def containsFocus(self):
        """ generated source for method containsFocus """
        return isFocusOwner()

    def clearMostRecentFocusOwnerOnHide(self):
        """ generated source for method clearMostRecentFocusOwnerOnHide """
        KeyboardFocusManager.clearMostRecentFocusOwner(self)

    def clearCurrentFocusCycleRootOnHide(self):
        """ generated source for method clearCurrentFocusCycleRootOnHide """

    def hide(self):
        """ generated source for method hide """
        self.isPacked = False
        if self.visible:
            self.clearCurrentFocusCycleRootOnHide()
            self.clearMostRecentFocusOwnerOnHide()
            with lock_for_object(self.getTreeLock()):
                self.visible = False
                mixOnHiding(self.isLightweight())
                if self.containsFocus() and KeyboardFocusManager.isAutoFocusTransferEnabled():
                    transferFocus(True)
                peer = self.peer
                if self.peer != None:
                    self.peer.setVisible(False)
                    createHierarchyEvents(HierarchyEvent.HIERARCHY_CHANGED, self, self.parent, HierarchyEvent.SHOWING_CHANGED, Toolkit.enabledOnToolkit(AWTEvent.HIERARCHY_EVENT_MASK))
                    if isinstance(self.peer, (LightweightPeer, )):
                        repaint()
                    updateCursorImmediately()
                if self.componentListener != None or (self.eventMask & AWTEvent.COMPONENT_EVENT_MASK) != 0 or Toolkit.enabledOnToolkit(AWTEvent.COMPONENT_EVENT_MASK):
                    e = ComponentEvent(self, ComponentEvent.COMPONENT_HIDDEN)
                    Toolkit.getEventQueue().postEvent(e)
            parent = self.parent
            if self.parent != None:
                self.parent.invalidate()

    @getForeground.register(object)
    def getForeground_0(self):
        """ generated source for method getForeground_0 """
        foreground = self.foreground
        if foreground != None:
            return foreground
        parent = self.parent
        return parent.getForeground() if (parent != None) else None

    def setForeground(self, c):
        """ generated source for method setForeground """
        oldColor = self.foreground
        peer = self.peer
        self.foreground = c
        if peer != None:
            c = self.getForeground()
            if c != None:
                peer.setForeground(c)
        firePropertyChange("foreground", oldColor, c)

    def isForegroundSet(self):
        """ generated source for method isForegroundSet """
        return (self.foreground != None)

    @getBackground.register(object)
    def getBackground_0(self):
        """ generated source for method getBackground_0 """
        background = self.background
        if background != None:
            return background
        parent = self.parent
        return parent.getBackground() if (parent != None) else None

    @setBackground.register(object, Color)
    def setBackground_0(self, c):
        """ generated source for method setBackground_0 """
        oldColor = self.background
        peer = self.peer
        self.background = c
        if peer != None:
            c = self.getBackground()
            if c != None:
                peer.setBackground(c)
        firePropertyChange("background", oldColor, c)

    def isBackgroundSet(self):
        """ generated source for method isBackgroundSet """
        return (self.background != None)

    @getFont.register(object)
    def getFont_0(self):
        """ generated source for method getFont_0 """
        return getFont_NoClientCode()

    def getFont_NoClientCode(self):
        """ generated source for method getFont_NoClientCode """
        font = self.font
        if font != None:
            return font
        parent = self.parent
        return parent.getFont_NoClientCode() if (parent != None) else None

    def setFont(self, f):
        """ generated source for method setFont """
        oldFont = None
        newFont = None
        with lock_for_object(self.getTreeLock()):
            oldFont = self.font
            newFont = self.font = f
            peer = self.peer
            if self.peer != None:
                f = self.getFont()
                if f != None:
                    self.peer.setFont(f)
                    self.peerFont = f
        firePropertyChange("font", oldFont, newFont)
        if f != oldFont and (oldFont == None or not oldFont == f):
            invalidateIfValid()

    def isFontSet(self):
        """ generated source for method isFontSet """
        return (self.font != None)

    def getLocale(self):
        """ generated source for method getLocale """
        locale = self.locale
        if locale != None:
            return locale
        parent = self.parent
        if parent == None:
            raise IllegalComponentStateException("This component must have a parent in order to determine its locale")
        else:
            return parent.getLocale()

    def setLocale(self, l):
        """ generated source for method setLocale """
        oldValue = self.locale
        self.locale = l
        firePropertyChange("locale", oldValue, l)
        invalidateIfValid()

    def getColorModel(self):
        """ generated source for method getColorModel """
        peer = self.peer
        if (peer != None) and not (isinstance(peer, (LightweightPeer, ))):
            return peer.getColorModel()
        elif GraphicsEnvironment.isHeadless():
            return ColorModel.getRGBdefault()
        return self.getToolkit().getColorModel()

    @getLocation.register(object)
    def getLocation_0(self):
        """ generated source for method getLocation_0 """
        return location()

    def getLocationOnScreen(self):
        """ generated source for method getLocationOnScreen """
        with lock_for_object(self.getTreeLock()):
            return getLocationOnScreen_NoTreeLock()

    def getLocationOnScreen_NoTreeLock(self):
        """ generated source for method getLocationOnScreen_NoTreeLock """
        if self.peer != None and self.isShowing():
            if isinstance(self.peer, (LightweightPeer, )):
                host = getNativeContainer()
                pt = host.peer.getLocationOnScreen()
                c = self
                while c != host:
                    pt.x += c.x
                    pt.y += c.y
                    c = c.getParent()
                return pt
            else:
                pt = self.peer.getLocationOnScreen()
                return pt
        else:
            raise IllegalComponentStateException("component must be showing on the screen to determine its location")

    def location(self):
        """ generated source for method location """
        return location_NoClientCode()

    def location_NoClientCode(self):
        """ generated source for method location_NoClientCode """
        return Point(self.x, self.y)

    @setLocation.register(object, int, int)
    def setLocation_0(self, x, y):
        """ generated source for method setLocation_0 """
        move(x, y)

    def move(self, x, y):
        """ generated source for method move """
        with lock_for_object(self.getTreeLock()):
            self.setBoundsOp(ComponentPeer.SET_LOCATION)
            setBounds(x, y, self.width, self.height)

    @setLocation.register(object, Point)
    def setLocation_1(self, p):
        """ generated source for method setLocation_1 """
        self.setLocation(p.x, p.y)

    @overloaded
    def getSize(self):
        """ generated source for method getSize """
        return size()

    def size(self):
        """ generated source for method size """
        return Dimension(self.width, self.height)

    @setSize.register(object, int, int)
    def setSize_0(self, width, height):
        """ generated source for method setSize_0 """
        resize(width, height)

    @overloaded
    def resize(self, width, height):
        """ generated source for method resize """
        with lock_for_object(self.getTreeLock()):
            self.setBoundsOp(ComponentPeer.SET_SIZE)
            setBounds(self.x, self.y, width, height)

    @setSize.register(object, Dimension)
    def setSize_1(self, d):
        """ generated source for method setSize_1 """
        self.resize(d)

    @resize.register(object, Dimension)
    def resize_0(self, d):
        """ generated source for method resize_0 """
        self.setSize(d.width, d.height)

    @getBounds.register(object)
    def getBounds_0(self):
        """ generated source for method getBounds_0 """
        return bounds()

    def bounds(self):
        """ generated source for method bounds """
        return Rectangle(self.x, self.y, self.width, self.height)

    @overloaded
    def setBounds(self, x, y, width, height):
        """ generated source for method setBounds """
        reshape(x, y, width, height)

    # def reshape(self, x, y, width, height):
    #     """ generated source for method reshape """
    #     with lock_for_object(self.getTreeLock()):
    #         try:
    #             self.setBoundsOp(ComponentPeer.SET_BOUNDS)
    #             resized = (self.width != width) or (self.height != height)
    #             moved = (self.x != x) or (self.y != y)
    #             if not resized and not moved:
    #                 return
    #             oldX = self.x
    #             oldY = self.y
    #             oldWidth = self.width
    #             oldHeight = self.height
    #             self.x = x
    #             self.y = y
    #             self.width = width
    #             self.height = height
    #             if resized:
    #                 self.isPacked = False
    #             needNotify = True
    #             mixOnReshaping()
    #             if self.peer != None:
    #                 if not (isinstance(self.peer, (LightweightPeer, ))):
    #                     reshapeNativePeer(x, y, width, height, self.getBoundsOp())
    #                     resized = (oldWidth != self.width) or (oldHeight != self.height)
    #                     moved = (oldX != self.x) or (oldY != self.y)
    #                     if isinstance(, (Window, )):
    #                         needNotify = False
    #                 if resized:
    #                     invalidate()
    #                 if self.parent != None:
    #                     self.parent.invalidateIfValid()
    #             if needNotify:
    #                 notifyNewBounds(resized, moved)
    #             repaintParentIfNeeded(oldX, oldY, oldWidth, oldHeight)
    #         finally:
    #             self.setBoundsOp(ComponentPeer.RESET_OPERATION)

    def repaintParentIfNeeded(self, oldX, oldY, oldWidth, oldHeight):
        """ generated source for method repaintParentIfNeeded """
        if self.parent != None and isinstance(self.peer, (LightweightPeer, )) and self.isShowing():
            self.parent.repaint(oldX, oldY, oldWidth, oldHeight)
            repaint()

    # def reshapeNativePeer(self, x, y, width, height, op):
    #     """ generated source for method reshapeNativePeer """
    #     nativeX = x
    #     nativeY = y
    #     c = self.parent
    #     while (c != None) and (isinstance(, (LightweightPeer, ))):
    #         nativeX += c.x
    #         nativeY += c.y
    #         c = c.parent
    #     self.peer.setBounds(nativeX, nativeY, width, height, op)

    # @SuppressWarnings("deprecation")
    # def notifyNewBounds(self, resized, moved):
    #     """ generated source for method notifyNewBounds """
    #     if self.componentListener != None or (self.eventMask & AWTEvent.COMPONENT_EVENT_MASK) != 0 or Toolkit.enabledOnToolkit(AWTEvent.COMPONENT_EVENT_MASK):
    #         if resized:
    #             e = ComponentEvent(self, ComponentEvent.COMPONENT_RESIZED)
    #             Toolkit.getEventQueue().postEvent(e)
    #         if moved:
    #             e = ComponentEvent(self, ComponentEvent.COMPONENT_MOVED)
    #             Toolkit.getEventQueue().postEvent(e)
    #     else:
    #         if isinstance(, (Container, )) and (self).countComponents() > 0:
    #             enabledOnToolkit = Toolkit.enabledOnToolkit(AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK)
    #             if resized:
    #                 (self).createChildHierarchyEvents(HierarchyEvent.ANCESTOR_RESIZED, 0, enabledOnToolkit)
    #             if moved:
    #                 (self).createChildHierarchyEvents(HierarchyEvent.ANCESTOR_MOVED, 0, enabledOnToolkit)

    @setBounds.register(object, Rectangle)
    def setBounds_0(self, r):
        """ generated source for method setBounds_0 """
        self.setBounds(r.x, r.y, r.width, r.height)

    @getX.register(object)
    def getX_0(self):
        """ generated source for method getX_0 """
        return self.x

    @getY.register(object)
    def getY_0(self):
        """ generated source for method getY_0 """
        return self.y

    @getWidth.register(object)
    def getWidth_0(self):
        """ generated source for method getWidth_0 """
        return self.width

    @getHeight.register(object)
    def getHeight_0(self):
        """ generated source for method getHeight_0 """
        return self.height

    @getBounds.register(object, Rectangle)
    def getBounds_1(self, rv):
        """ generated source for method getBounds_1 """
        if rv == None:
            return Rectangle(self.getX(), self.getY(), self.getWidth(), self.getHeight())
        else:
            rv.setBounds(self.getX(), self.getY(), self.getWidth(), self.getHeight())
            return rv

    @getSize.register(object, Dimension)
    def getSize_0(self, rv):
        """ generated source for method getSize_0 """
        if rv == None:
            return Dimension(self.getWidth(), self.getHeight())
        else:
            rv.setSize(self.getWidth(), self.getHeight())
            return rv

    @getLocation.register(object, Point)
    def getLocation_1(self, rv):
        """ generated source for method getLocation_1 """
        if rv == None:
            return Point(self.getX(), self.getY())
        else:
            rv.setLocation(self.getX(), self.getY())
            return rv

    def isOpaque(self):
        """ generated source for method isOpaque """
        if self.getPeer() == None:
            return False
        else:
            return not self.isLightweight()

    # @isLightweight.register(object)
    # def isLightweight_0(self):
    #     """ generated source for method isLightweight_0 """
    #     return isinstance(, (LightweightPeer, ))

    # def setPreferredSize(self, preferredSize):
    #     """ generated source for method setPreferredSize """
    #     old = None
    #     if self.prefSizeSet:
    #         old = self.prefSize
    #     else:
    #         old = None
    #     self.prefSize = preferredSize
    #     self.prefSizeSet = (preferredSize != None)
    #     firePropertyChange("preferredSize", old, preferredSize)

    def isPreferredSizeSet(self):
        """ generated source for method isPreferredSizeSet """
        return self.prefSizeSet

    def getPreferredSize(self):
        """ generated source for method getPreferredSize """
        return preferredSize()

    def preferredSize(self):
        """ generated source for method preferredSize """
        dim = self.prefSize
        if dim == None or not (self.isPreferredSizeSet() or self.isValid()):
            with lock_for_object(self.getTreeLock()):
                self.prefSize = self.peer.getPreferredSize() if (self.peer != None) else getMinimumSize()
                dim = self.prefSize
        return Dimension(dim)

    def setMinimumSize(self, minimumSize):
        """ generated source for method setMinimumSize """
        old = None
        if self.minSizeSet:
            old = self.minSize
        else:
            old = None
        self.minSize = minimumSize
        self.minSizeSet = (minimumSize != None)
        firePropertyChange("minimumSize", old, minimumSize)

    def isMinimumSizeSet(self):
        """ generated source for method isMinimumSizeSet """
        return self.minSizeSet

    def getMinimumSize(self):
        """ generated source for method getMinimumSize """
        return minimumSize()

    def minimumSize(self):
        """ generated source for method minimumSize """
        dim = self.minSize
        if dim == None or not (self.isMinimumSizeSet() or self.isValid()):
            with lock_for_object(self.getTreeLock()):
                self.minSize = self.peer.getMinimumSize() if (self.peer != None) else len(self)
                dim = self.minSize
        return Dimension(dim)

    def setMaximumSize(self, maximumSize):
        """ generated source for method setMaximumSize """
        old = None
        if self.maxSizeSet:
            old = self.maxSize
        else:
            old = None
        self.maxSize = maximumSize
        self.maxSizeSet = (maximumSize != None)
        firePropertyChange("maximumSize", old, maximumSize)

    def isMaximumSizeSet(self):
        """ generated source for method isMaximumSizeSet """
        return self.maxSizeSet

    def getMaximumSize(self):
        """ generated source for method getMaximumSize """
        if self.isMaximumSizeSet():
            return Dimension(self.maxSize)
        return Dimension(Short.MAX_VALUE, Short.MAX_VALUE)

    def getAlignmentX(self):
        """ generated source for method getAlignmentX """
        return self.CENTER_ALIGNMENT

    def getAlignmentY(self):
        """ generated source for method getAlignmentY """
        return self.CENTER_ALIGNMENT

    def getBaseline(self, width, height):
        """ generated source for method getBaseline """
        if width < 0 or height < 0:
            raise IllegalArgumentException("Width and height must be >= 0")
        return -1

    def getBaselineResizeBehavior(self):
        """ generated source for method getBaselineResizeBehavior """
        return self.BaselineResizeBehavior.OTHER

    def doLayout(self):
        """ generated source for method doLayout """
        layout()

    def layout(self):
        """ generated source for method layout """

    def validate(self):
        """ generated source for method validate """
        with lock_for_object(self.getTreeLock()):
            peer = self.peer
            wasValid = self.isValid()
            if not wasValid and self.peer != None:
                newfont = self.getFont()
                oldfont = self.peerFont
                if newfont != oldfont and (oldfont == None or not oldfont == newfont):
                    self.peer.setFont(newfont)
                    self.peerFont = newfont
                self.peer.layout()
            self.valid = True
            if not wasValid:
                mixOnValidating()

    def invalidate(self):
        """ generated source for method invalidate """
        with lock_for_object(self.getTreeLock()):
            self.valid = False
            if not self.isPreferredSizeSet():
                self.prefSize = None
            if not self.isMinimumSizeSet():
                self.minSize = None
            if not self.isMaximumSizeSet():
                self.maxSize = None
            invalidateParent()

    def invalidateParent(self):
        """ generated source for method invalidateParent """
        if self.parent != None:
            self.parent.invalidateIfValid()

    def invalidateIfValid(self):
        """ generated source for method invalidateIfValid """
        if self.isValid():
            self.invalidate()

    def revalidate(self):
        """ generated source for method revalidate """
        self.revalidateSynchronously()

    @revalidateSynchronously.register(object)
    def revalidateSynchronously_0(self):
        """ generated source for method revalidateSynchronously_0 """
        with lock_for_object(self.getTreeLock()):
            self.invalidate()
            root = self.getContainer()
            if root == None:
                self.validate()
            else:
                while not root.isValidateRoot():
                    if root.getContainer() == None:
                        break
                    root = root.getContainer()
                root.validate()

    def getGraphics(self):
        """ generated source for method getGraphics """
        if isinstance(self.peer, (LightweightPeer, )):
            if self.parent == None:
                return None
            g = self.parent.getGraphics()
            if g == None:
                return None
            if isinstance(g, (ConstrainableGraphics, )):
                (g).constrain(self.x, self.y, self.width, self.height)
            else:
                g.translate(self.x, self.y)
                g.setClip(0, 0, self.width, self.height)
            g.setFont(self.getFont())
            return g
        else:
            peer = self.peer
            return self.peer.getGraphics() if (self.peer != None) else None

    def getGraphics_NoClientCode(self):
        """ generated source for method getGraphics_NoClientCode """
        peer = self.peer
        if isinstance(peer, (LightweightPeer, )):
            parent = self.parent
            if self.parent == None:
                return None
            g = self.parent.getGraphics_NoClientCode()
            if g == None:
                return None
            if isinstance(g, (ConstrainableGraphics, )):
                (g).constrain(self.x, self.y, self.width, self.height)
            else:
                g.translate(self.x, self.y)
                g.setClip(0, 0, self.width, self.height)
            g.setFont(self.getFont_NoClientCode())
            return g
        else:
            return peer.getGraphics() if (peer != None) else None

    def getFontMetrics(self, font):
        """ generated source for method getFontMetrics """
        fm = FontManagerFactory.getInstance()
        if isinstance(fm, (SunFontManager, )) and (fm).usePlatformFontMetrics():
            if self.peer != None and not (isinstance(self.peer, (LightweightPeer, ))):
                return self.peer.getFontMetrics(font)
        return sun.font.FontDesignMetrics.getMetrics(font)

    def setCursor(self, cursor):
        """ generated source for method setCursor """
        self.cursor = cursor
        updateCursorImmediately()

    def updateCursorImmediately(self):
        """ generated source for method updateCursorImmediately """
        if isinstance(self.peer, (LightweightPeer, )):
            nativeContainer = getNativeContainer()
            if nativeContainer == None:
                return
            cPeer = nativeContainer.getPeer()
            if cPeer != None:
                cPeer.updateCursorImmediately()
        elif self.peer != None:
            self.peer.updateCursorImmediately()

    @getCursor.register(object)
    def getCursor_0(self):
        """ generated source for method getCursor_0 """
        return getCursor_NoClientCode()

    def getCursor_NoClientCode(self):
        """ generated source for method getCursor_NoClientCode """
        cursor = self.cursor
        if cursor != None:
            return cursor
        parent = self.parent
        if parent != None:
            return parent.getCursor_NoClientCode()
        else:
            return Cursor.getPredefinedCursor(Cursor.DEFAULT_CURSOR)

    def isCursorSet(self):
        """ generated source for method isCursorSet """
        return (self.cursor != None)

    def paint(self, g):
        """ generated source for method paint """

    def update(self, g):
        """ generated source for method update """
        self.paint(g)

    def paintAll(self, g):
        """ generated source for method paintAll """
        if self.isShowing():
            GraphicsCallback.PeerPaintCallback.getInstance().runOneComponent(self, Rectangle(0, 0, self.width, self.height), g, g.getClip(), GraphicsCallback.LIGHTWEIGHTS | GraphicsCallback.HEAVYWEIGHTS)

    def lightweightPaint(self, g):
        """ generated source for method lightweightPaint """
        self.paint(g)

    def paintHeavyweightComponents(self, g):
        """ generated source for method paintHeavyweightComponents """

    @overloaded
    def repaint(self):
        """ generated source for method repaint """
        self.repaint(0, 0, 0, self.width, self.height)

    @repaint.register(object, long)
    def repaint_0(self, tm):
        """ generated source for method repaint_0 """
        self.repaint(tm, 0, 0, self.width, self.height)

    @repaint.register(object, int, int, int, int)
    def repaint_1(self, x, y, width, height):
        """ generated source for method repaint_1 """
        self.repaint(0, x, y, width, height)

    # @repaint.register(object, long, int, int, int, int)
    # def repaint_2(self, tm, x, y, width, height):
    #     """ generated source for method repaint_2 """
    #     if isinstance(, (LightweightPeer, )):
    #         if self.parent != None:
    #             if x < 0:
    #                 width += x
    #                 x = 0
    #             if y < 0:
    #                 height += y
    #                 y = 0
    #             pwidth = self.width if (width > self.width) else width
    #             pheight = self.height if (height > self.height) else height
    #             if pwidth <= 0 or pheight <= 0:
    #                 return
    #             px = self.x + x
    #             py = self.y + y
    #             self.parent.repaint(tm, px, py, pwidth, pheight)
    #     else:
    #         if self.isVisible() and (self.peer != None) and (width > 0) and (height > 0):
    #             e = PaintEvent(self, PaintEvent.UPDATE, Rectangle(x, y, width, height))
    #             SunToolkit.postEvent(SunToolkit.targetToAppContext(self), e)

    def print_(self, g):
        """ generated source for method print_ """
        self.paint(g)

    def printAll(self, g):
        """ generated source for method printAll """
        if self.isShowing():
            GraphicsCallback.PeerPrintCallback.getInstance().runOneComponent(self, Rectangle(0, 0, self.width, self.height), g, g.getClip(), GraphicsCallback.LIGHTWEIGHTS | GraphicsCallback.HEAVYWEIGHTS)

    def lightweightPrint(self, g):
        """ generated source for method lightweightPrint """
        self.print_(g)

    def printHeavyweightComponents(self, g):
        """ generated source for method printHeavyweightComponents """

    def getInsets_NoClientCode(self):
        """ generated source for method getInsets_NoClientCode """
        peer = self.peer
        if isinstance(peer, (ContainerPeer, )):
            return (peer).getInsets().clone()
        return Insets(0, 0, 0, 0)

    def imageUpdate(self, img, infoflags, x, y, w, h):
        """ generated source for method imageUpdate """
        rate = -1
        if (infoflags & (FRAMEBITS | ALLBITS)) != 0:
            rate = 0
        elif (infoflags & SOMEBITS) != 0:
            if self.isInc:
                rate = self.incRate
                if rate < 0:
                    rate = 0
        if rate >= 0:
            self.repaint(rate, 0, 0, self.width, self.height)
        return (infoflags & (ALLBITS | ABORT)) == 0

    @overloaded
    def createImage(self, producer):
        """ generated source for method createImage """
        peer = self.peer
        if (peer != None) and not (isinstance(peer, (LightweightPeer, ))):
            return peer.createImage(producer)
        return self.getToolkit().createImage(producer)

    @createImage.register(object, int, int)
    def createImage_0(self, width, height):
        """ generated source for method createImage_0 """
        peer = self.peer
        if isinstance(peer, (LightweightPeer, )):
            if self.parent != None:
                return self.parent.createImage(width, height)
            else:
                return None
        else:
            return peer.createImage(width, height) if (peer != None) else None

    @overloaded
    def createVolatileImage(self, width, height):
        """ generated source for method createVolatileImage """
        peer = self.peer
        if isinstance(peer, (LightweightPeer, )):
            if self.parent != None:
                return self.parent.createVolatileImage(width, height)
            else:
                return None
        else:
            return peer.createVolatileImage(width, height) if (peer != None) else None

    @createVolatileImage.register(object, int, int, ImageCapabilities)
    def createVolatileImage_0(self, width, height, caps):
        """ generated source for method createVolatileImage_0 """
        return self.createVolatileImage(width, height)

    @overloaded
    def prepareImage(self, image, observer):
        """ generated source for method prepareImage """
        return self.prepareImage(image, -1, -1, observer)

    @prepareImage.register(object, Image, int, int, ImageObserver)
    def prepareImage_0(self, image, width, height, observer):
        """ generated source for method prepareImage_0 """
        peer = self.peer
        if isinstance(peer, (LightweightPeer, )):
            return self.parent.prepareImage(image, width, height, observer) if (self.parent != None) else self.getToolkit().prepareImage(image, width, height, observer)
        else:
            return peer.prepareImage(image, width, height, observer) if (peer != None) else self.getToolkit().prepareImage(image, width, height, observer)

    @overloaded
    def checkImage(self, image, observer):
        """ generated source for method checkImage """
        return self.checkImage(image, -1, -1, observer)

    @checkImage.register(object, Image, int, int, ImageObserver)
    def checkImage_0(self, image, width, height, observer):
        """ generated source for method checkImage_0 """
        peer = self.peer
        if isinstance(peer, (LightweightPeer, )):
            return self.parent.checkImage(image, width, height, observer) if (self.parent != None) else self.getToolkit().checkImage(image, width, height, observer)
        else:
            return peer.checkImage(image, width, height, observer) if (peer != None) else self.getToolkit().checkImage(image, width, height, observer)

    @overloaded
    def createBufferStrategy(self, numBuffers):
        """ generated source for method createBufferStrategy """
        bufferCaps = None
        if numBuffers > 1:
            bufferCaps = BufferCapabilities(ImageCapabilities(True), ImageCapabilities(True), BufferCapabilities.FlipContents.UNDEFINED)
            try:
                self.createBufferStrategy(numBuffers, bufferCaps)
                return
            except AWTException as e:
                pass
        bufferCaps = BufferCapabilities(ImageCapabilities(True), ImageCapabilities(True), None)
        try:
            self.createBufferStrategy(numBuffers, bufferCaps)
            return
        except AWTException as e:
            pass
        bufferCaps = BufferCapabilities(ImageCapabilities(False), ImageCapabilities(False), None)
        try:
            self.createBufferStrategy(numBuffers, bufferCaps)
            return
        except AWTException as e:
            raise InternalError("Could not create a buffer strategy", e)

    @createBufferStrategy.register(object, int, BufferCapabilities)
    def createBufferStrategy_0(self, numBuffers, caps):
        """ generated source for method createBufferStrategy_0 """
        if numBuffers < 1:
            raise IllegalArgumentException("Number of buffers must be at least 1")
        if caps == None:
            raise IllegalArgumentException("No capabilities specified")
        if self.bufferStrategy != None:
            self.bufferStrategy.dispose()
        if numBuffers == 1:
            self.bufferStrategy = SingleBufferStrategy(caps)
        else:
            sge = GraphicsEnvironment.getLocalGraphicsEnvironment()
            if not caps.isPageFlipping() and sge.isFlipStrategyPreferred(self.peer):
                caps = ProxyCapabilities(caps)
            if caps.isPageFlipping():
                self.bufferStrategy = FlipSubRegionBufferStrategy(numBuffers, caps)
            else:
                self.bufferStrategy = BltSubRegionBufferStrategy(numBuffers, caps)

    class ProxyCapabilities(ExtendedBufferCapabilities):
        """ generated source for class ProxyCapabilities """
        orig = None

        def __init__(self, orig):
            """ generated source for method __init__ """
            super(ProxyCapabilities, self).__init__(BufferCapabilities.FlipContents.BACKGROUND if orig.getFlipContents() == BufferCapabilities.FlipContents.BACKGROUND else BufferCapabilities.FlipContents.COPIED)
            self.orig = orig

    def getBufferStrategy(self):
        """ generated source for method getBufferStrategy """
        return self.bufferStrategy

    def getBackBuffer(self):
        """ generated source for method getBackBuffer """
        if self.bufferStrategy != None:
            if isinstance(self.bufferStrategy, (BltBufferStrategy, )):
                bltBS = self.bufferStrategy
                return bltBS.getBackBuffer()
            elif isinstance(self.bufferStrategy, (FlipBufferStrategy, )):
                flipBS = self.bufferStrategy
                return flipBS.getBackBuffer()
        return None

    class FlipBufferStrategy(BufferStrategy):
        """ generated source for class FlipBufferStrategy """
        numBuffers = int()
        caps = None
        drawBuffer = None
        drawVBuffer = None
        validatedContents = bool()
        width = int()
        height = int()

        # def __init__(self, numBuffers, caps):
        #     """ generated source for method __init__ """
        #     super(FlipBufferStrategy, self).__init__()
        #     if not (isinstance(, (Window, ))) and not (isinstance(, (Canvas, ))):
        #         raise ClassCastException("Component must be a Canvas or Window")
        #     self.numBuffers = numBuffers
        #     self.caps = caps
        #     createBuffers(numBuffers, caps)

        def createBuffers(self, numBuffers, caps):
            """ generated source for method createBuffers """
            if numBuffers < 2:
                raise IllegalArgumentException("Number of buffers cannot be less than two")
            elif self.peer == None:
                raise IllegalStateException("Component must have a valid peer")
            elif caps == None or not caps.isPageFlipping():
                raise IllegalArgumentException("Page flipping capabilities must be specified")
            self.width = self.getWidth()
            self.height = self.getHeight()
            if self.drawBuffer != None:
                self.drawBuffer = None
                self.drawVBuffer = None
                destroyBuffers()
            if isinstance(caps, (ExtendedBufferCapabilities, )):
                ebc = caps
                if ebc.getVSync() == VSYNC_ON:
                    if not VSyncedBSManager.vsyncAllowed(self):
                        caps = ebc.derive(VSYNC_DEFAULT)
            self.peer.createBuffers(numBuffers, caps)
            updateInternalBuffers()

        def updateInternalBuffers(self):
            """ generated source for method updateInternalBuffers """
            self.drawBuffer = self.getBackBuffer()
            if isinstance(self.drawBuffer, (VolatileImage, )):
                self.drawVBuffer = self.drawBuffer
            else:
                self.drawVBuffer = None

        def getBackBuffer(self):
            """ generated source for method getBackBuffer """
            if self.peer != None:
                return self.peer.getBackBuffer()
            else:
                raise IllegalStateException("Component must have a valid peer")

        def flip(self, flipAction):
            """ generated source for method flip """
            if self.peer != None:
                backBuffer = self.getBackBuffer()
                if backBuffer != None:
                    self.peer.flip(0, 0, backBuffer.getWidth(None), backBuffer.getHeight(None), flipAction)
            else:
                raise IllegalStateException("Component must have a valid peer")

        def flipSubRegion(self, x1, y1, x2, y2, flipAction):
            """ generated source for method flipSubRegion """
            if self.peer != None:
                self.peer.flip(x1, y1, x2, y2, flipAction)
            else:
                raise IllegalStateException("Component must have a valid peer")

        def destroyBuffers(self):
            """ generated source for method destroyBuffers """
            VSyncedBSManager.releaseVsync(self)
            if self.peer != None:
                self.peer.destroyBuffers()
            else:
                raise IllegalStateException("Component must have a valid peer")

        def getCapabilities(self):
            """ generated source for method getCapabilities """
            if isinstance(self.caps, (self.ProxyCapabilities, )):
                return (self.caps).orig
            else:
                return self.caps

        def getDrawGraphics(self):
            """ generated source for method getDrawGraphics """
            self.revalidate()
            return self.drawBuffer.getGraphics()

        @overloaded
        def revalidate(self):
            """ generated source for method revalidate """
            self.revalidate(True)

        @revalidate.register(object, bool)
        def revalidate_0(self, checkSize):
            """ generated source for method revalidate_0 """
            self.validatedContents = False
            if checkSize and (self.getWidth() != self.width or self.getHeight() != self.height):
                try:
                    self.createBuffers(self.numBuffers, self.caps)
                except AWTException as e:
                    pass
                self.validatedContents = True
            self.updateInternalBuffers()
            if self.drawVBuffer != None:
                gc = self.getGraphicsConfiguration_NoClientCode()
                returnCode = self.drawVBuffer.validate(gc)
                if returnCode == VolatileImage.IMAGE_INCOMPATIBLE:
                    try:
                        self.createBuffers(self.numBuffers, self.caps)
                    except AWTException as e:
                        pass
                    if self.drawVBuffer != None:
                        self.drawVBuffer.validate(gc)
                    self.validatedContents = True
                elif returnCode == VolatileImage.IMAGE_RESTORED:
                    self.validatedContents = True

        def contentsLost(self):
            """ generated source for method contentsLost """
            if self.drawVBuffer == None:
                return False
            return self.drawVBuffer.contentsLost()

        def contentsRestored(self):
            """ generated source for method contentsRestored """
            return self.validatedContents

        def show(self):
            """ generated source for method show """
            self.flip(self.caps.getFlipContents())

        def showSubRegion(self, x1, y1, x2, y2):
            """ generated source for method showSubRegion """
            self.flipSubRegion(x1, y1, x2, y2, self.caps.getFlipContents())

        def dispose(self):
            """ generated source for method dispose """
            if Component.self.bufferStrategy == self:
                Component.self.bufferStrategy = None
                if self.peer != None:
                    self.destroyBuffers()

    class BltBufferStrategy(BufferStrategy):
        """ generated source for class BltBufferStrategy """
        caps = None
        backBuffers = []
        validatedContents = bool()
        width = int()
        height = int()
        insets = None

        def __init__(self, numBuffers, caps):
            """ generated source for method __init__ """
            super(BltBufferStrategy, self).__init__()
            self.caps = caps
            createBackBuffers(numBuffers - 1)

        def dispose(self):
            """ generated source for method dispose """
            if self.backBuffers != None:
                counter = len(backBuffers)
                while counter >= 0:
                    if self.backBuffers[counter] != None:
                        self.backBuffers[counter].flush()
                        self.backBuffers[counter] = None
                    counter -= 1
            if Component.self.bufferStrategy == self:
                Component.self.bufferStrategy = None

        def createBackBuffers(self, numBuffers):
            """ generated source for method createBackBuffers """
            if numBuffers == 0:
                self.backBuffers = None
            else:
                self.width = self.getWidth()
                self.height = self.getHeight()
                self.insets = self.getInsets_NoClientCode()
                iWidth = self.width - self.insets.left - self.insets.right
                iHeight = self.height - self.insets.top - self.insets.bottom
                iWidth = max(1, iWidth)
                iHeight = max(1, iHeight)
                if self.backBuffers == None:
                    self.backBuffers = [None] * numBuffers
                else:
                    i = 0
                    while i < numBuffers:
                        if self.backBuffers[i] != None:
                            self.backBuffers[i].flush()
                            self.backBuffers[i] = None
                        i += 1
                i = 0
                while i < numBuffers:
                    self.backBuffers[i] = self.createVolatileImage(iWidth, iHeight)
                    i += 1

        def getCapabilities(self):
            """ generated source for method getCapabilities """
            return self.caps

        def getDrawGraphics(self):
            """ generated source for method getDrawGraphics """
            self.revalidate()
            backBuffer = self.getBackBuffer()
            if backBuffer == None:
                return self.getGraphics()
            g = backBuffer.getGraphics()
            g.constrain(-self.insets.left, -self.insets.top, backBuffer.getWidth(None) + self.insets.left, backBuffer.getHeight(None) + self.insets.top)
            return g

        def getBackBuffer(self):
            """ generated source for method getBackBuffer """
            if self.backBuffers != None:
                return self.backBuffers[len(backBuffers)]
            else:
                return None

        def show(self):
            """ generated source for method show """
            showSubRegion(self.insets.left, self.insets.top, self.width - self.insets.right, self.height - self.insets.bottom)

        def showSubRegion(self, x1, y1, x2, y2):
            """ generated source for method showSubRegion """
            if self.backBuffers == None:
                return
            x1 -= self.insets.left
            x2 -= self.insets.left
            y1 -= self.insets.top
            y2 -= self.insets.top
            g = self.getGraphics_NoClientCode()
            if g == None:
                return
            try:
                g.translate(self.insets.left, self.insets.top)
                i = 0
                while len(backBuffers):
                    g.drawImage(self.backBuffers[i], x1, y1, x2, y2, x1, y1, x2, y2, None)
                    g.dispose()
                    g = None
                    g = self.backBuffers[i].getGraphics()
                    i += 1
            finally:
                if g != None:
                    g.dispose()

        @overloaded
        def revalidate(self):
            """ generated source for method revalidate """
            self.revalidate(True)

        @revalidate.register(object, bool)
        def revalidate_0(self, checkSize):
            """ generated source for method revalidate_0 """
            self.validatedContents = False
            if self.backBuffers == None:
                return
            if checkSize:
                insets = self.getInsets_NoClientCode()
                if self.getWidth() != self.width or self.getHeight() != self.height or not self.insets == self.insets:
                    self.createBackBuffers()
                    self.validatedContents = True
            gc = self.getGraphicsConfiguration_NoClientCode()
            returnCode = self.backBuffers[len(backBuffers)].validate(gc)
            if returnCode == VolatileImage.IMAGE_INCOMPATIBLE:
                if checkSize:
                    self.createBackBuffers()
                    self.backBuffers[len(backBuffers)].validate(gc)
                self.validatedContents = True
            elif returnCode == VolatileImage.IMAGE_RESTORED:
                self.validatedContents = True

        def contentsLost(self):
            """ generated source for method contentsLost """
            if self.backBuffers == None:
                return False
            else:
                return self.backBuffers[len(backBuffers)].contentsLost()

        def contentsRestored(self):
            """ generated source for method contentsRestored """
            return self.validatedContents

    class FlipSubRegionBufferStrategy(FlipBufferStrategy, SubRegionShowable):
        """ generated source for class FlipSubRegionBufferStrategy """
        def __init__(self, numBuffers, caps):
            """ generated source for method __init__ """
            super(FlipSubRegionBufferStrategy, self).__init__(caps)

        def show(self, x1, y1, x2, y2):
            """ generated source for method show """
            showSubRegion(x1, y1, x2, y2)

        def showIfNotLost(self, x1, y1, x2, y2):
            """ generated source for method showIfNotLost """
            if not contentsLost():
                showSubRegion(x1, y1, x2, y2)
                return not contentsLost()
            return False

    class BltSubRegionBufferStrategy(BltBufferStrategy, SubRegionShowable):
        """ generated source for class BltSubRegionBufferStrategy """
        def __init__(self, numBuffers, caps):
            """ generated source for method __init__ """
            super(BltSubRegionBufferStrategy, self).__init__(caps)

        def show(self, x1, y1, x2, y2):
            """ generated source for method show """
            showSubRegion(x1, y1, x2, y2)

        def showIfNotLost(self, x1, y1, x2, y2):
            """ generated source for method showIfNotLost """
            if not contentsLost():
                showSubRegion(x1, y1, x2, y2)
                return not contentsLost()
            return False

    class SingleBufferStrategy(BufferStrategy):
        """ generated source for class SingleBufferStrategy """
        caps = None

        def __init__(self, caps):
            """ generated source for method __init__ """
            super(SingleBufferStrategy, self).__init__()
            self.caps = caps

        def getCapabilities(self):
            """ generated source for method getCapabilities """
            return self.caps

        def getDrawGraphics(self):
            """ generated source for method getDrawGraphics """
            return self.getGraphics()

        def contentsLost(self):
            """ generated source for method contentsLost """
            return False

        def contentsRestored(self):
            """ generated source for method contentsRestored """
            return False

        def show(self):
            """ generated source for method show """

    def setIgnoreRepaint(self, ignoreRepaint):
        """ generated source for method setIgnoreRepaint """
        self.ignoreRepaint = ignoreRepaint

    @getIgnoreRepaint.register(object)
    def getIgnoreRepaint_0(self):
        """ generated source for method getIgnoreRepaint_0 """
        return self.ignoreRepaint

    @overloaded
    def contains(self, x, y):
        """ generated source for method contains """
        return inside(x, y)

    def inside(self, x, y):
        """ generated source for method inside """
        return (x >= 0) and (x < self.width) and (y >= 0) and (y < self.height)

    @contains.register(object, Point)
    def contains_0(self, p):
        """ generated source for method contains_0 """
        return self.contains(p.x, p.y)

    @overloaded
    def getComponentAt(self, x, y):
        """ generated source for method getComponentAt """
        return locate(x, y)

    def locate(self, x, y):
        """ generated source for method locate """
        return self if self.contains(x, y) else None

    @getComponentAt.register(object, Point)
    def getComponentAt_0(self, p):
        """ generated source for method getComponentAt_0 """
        return self.getComponentAt(p.x, p.y)

    def deliverEvent(self, e):
        """ generated source for method deliverEvent """
        postEvent(e)

    def dispatchEvent(self, e):
        """ generated source for method dispatchEvent """
        dispatchEventImpl(e)

    # @SuppressWarnings("deprecation")
    # def dispatchEventImpl(self, e):
    #     """ generated source for method dispatchEventImpl """
    #     id = e.getID()
    #     compContext = self.appContext
    #     if compContext != None and not compContext == AppContext.getAppContext():
    #         if self.eventLog.isLoggable(PlatformLogger.Level.FINE):
    #             self.eventLog.fine("Event " + e + " is being dispatched on the wrong AppContext")
    #     if self.eventLog.isLoggable(PlatformLogger.Level.FINEST):
    #         self.eventLog.finest("{0}", e)
    #     if not (isinstance(e, (KeyEvent, ))):
    #         EventQueue.setCurrentEventAndMostRecentTime(e)
    #     if isinstance(e, (SunDropTargetEvent, )):
    #         (e).dispatch()
    #         return
    #     if not e.focusManagerIsDispatching:
    #         if e.isPosted:
    #             e = KeyboardFocusManager.retargetFocusEvent(e)
    #             e.isPosted = True
    #         if KeyboardFocusManager.getCurrentKeyboardFocusManager().dispatchEvent(e):
    #             return
    #     if (isinstance(e, (FocusEvent, ))) and self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
    #         self.focusLog.finest("" + e)
    #     if id == MouseEvent.MOUSE_WHEEL and (not eventTypeEnabled(id)) and (self.peer != None and not self.peer.handlesWheelScrolling()) and (dispatchMouseWheelToAncestor(e)):
    #         return
    #     toolkit = Toolkit.getDefaultToolkit()
    #     toolkit.notifyAWTEventListeners(e)
    #     if not e.isConsumed():
    #         if isinstance(e, (KeyEvent, )):
    #             KeyboardFocusManager.getCurrentKeyboardFocusManager().processKeyEvent(self, e)
    #             if e.isConsumed():
    #                 return
    #     if areInputMethodsEnabled():
    #         if ((isinstance(e, (InputMethodEvent, ))) and not (isinstance(, (CompositionArea, )))) or (isinstance(e, (InputEvent, ))) or (isinstance(e, (FocusEvent, ))):
    #             inputContext = getInputContext()
    #             if inputContext != None:
    #                 inputContext.dispatchEvent(e)
    #                 if e.isConsumed():
    #                     if (isinstance(e, (FocusEvent, ))) and self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
    #                         self.focusLog.finest("3579: Skipping " + e)
    #                     return
    #     else:
    #         if id == FocusEvent.FOCUS_GAINED:
    #             inputContext = getInputContext()
    #             if inputContext != None and isinstance(inputContext, (InputContext, )):
    #                 (inputContext).disableNativeIM()
    #     if id == KeyEvent.KEY_PRESSED:
    #         pass
    #     elif id == KeyEvent.KEY_RELEASED:
    #         p = (self if (isinstance(, (Container, ))) else self.parent)
    #         if p != None:
    #             p.preProcessKeyEvent(e)
    #             if e.isConsumed():
    #                 if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
    #                     self.focusLog.finest("Pre-process consumed event")
    #                 return
    #     elif id == WindowEvent.WINDOW_CLOSING:
    #         if isinstance(toolkit, (WindowClosingListener, )):
    #             self.windowClosingException = (toolkit).windowClosingNotify(e)
    #             if checkWindowClosingException():
    #                 return
    #     else:
    #     if self.newEventsOnly:
    #         if eventEnabled(e):
    #             self.processEvent(e)
    #     elif id == MouseEvent.MOUSE_WHEEL:
    #         autoProcessMouseWheel(e)
    #     elif not (isinstance(e, (MouseEvent, )) and not postsOldMouseEvents()):
    #         olde = e.convertToOld()
    #         if olde != None:
    #             key = olde.key
    #             modifiers = olde.modifiers
    #             postEvent(olde)
    #             if olde.isConsumed():
    #                 e.consume()
    #             if olde.id == Event.KEY_PRESS:
    #                 pass
    #             elif olde.id == Event.KEY_RELEASE:
    #                 pass
    #             elif olde.id == Event.KEY_ACTION:
    #                 pass
    #             elif olde.id == Event.KEY_ACTION_RELEASE:
    #                 if olde.key != key:
    #                     (e).setKeyChar(olde.getKeyEventChar())
    #                 if olde.modifiers != modifiers:
    #                     (e).setModifiers(olde.modifiers)
    #             else:
    #     if id == WindowEvent.WINDOW_CLOSING and not e.isConsumed():
    #         if isinstance(toolkit, (WindowClosingListener, )):
    #             self.windowClosingException = (toolkit).windowClosingDelivered(e)
    #             if checkWindowClosingException():
    #                 return
    #     if not (isinstance(e, (KeyEvent, ))):
    #         tpeer = self.peer
    #         if isinstance(e, (FocusEvent, )) and (tpeer == None or isinstance(tpeer, (LightweightPeer, ))):
    #             source = e.getSource()
    #             if source != None:
    #                 target = source.getNativeContainer()
    #                 if target != None:
    #                     tpeer = target.getPeer()
    #         if tpeer != None:
    #             tpeer.handleEvent(e)

    def autoProcessMouseWheel(self, e):
        """ generated source for method autoProcessMouseWheel """

    def dispatchMouseWheelToAncestor(self, e):
        """ generated source for method dispatchMouseWheelToAncestor """
        newX = int()
        newY = int()
        newX = e.getX() + self.getX()
        newY = e.getY() + self.getY()
        newMWE = None
        if self.eventLog.isLoggable(PlatformLogger.Level.FINEST):
            self.eventLog.finest("dispatchMouseWheelToAncestor")
            self.eventLog.finest("orig event src is of " + e.getSource().__class__)
        with lock_for_object(self.getTreeLock()):
            anc = self.getParent()
            while anc != None and not anc.eventEnabled(e):
                newX += anc.getX()
                newY += anc.getY()
                if not (isinstance(anc, (Window, ))):
                    anc = anc.getParent()
                else:
                    break
            if self.eventLog.isLoggable(PlatformLogger.Level.FINEST):
                self.eventLog.finest("new event src is " + anc.__class__)
            if anc != None and anc.eventEnabled(e):
                newMWE = MouseWheelEvent(anc, e.getID(), e.getWhen(), e.getModifiers(), newX, newY, e.getXOnScreen(), e.getYOnScreen(), e.getClickCount(), e.isPopupTrigger(), e.getScrollType(), e.getScrollAmount(), e.getWheelRotation(), e.getPreciseWheelRotation())
                (e).copyPrivateDataInto(newMWE)
                anc.dispatchEventToSelf(newMWE)
                if newMWE.isConsumed():
                    e.consume()
                return True
        return False

    # def checkWindowClosingException(self):
    #     """ generated source for method checkWindowClosingException """
    #     if self.windowClosingException != None:
    #         if isinstance(, (Dialog, )):
    #             (self).interruptBlocking()
    #         else:
    #             self.windowClosingException.fillInStackTrace()
    #             self.windowClosingException.printStackTrace()
    #             self.windowClosingException = None
    #         return True
    #     return False

    def areInputMethodsEnabled(self):
        """ generated source for method areInputMethodsEnabled """
        return ((self.eventMask & AWTEvent.INPUT_METHODS_ENABLED_MASK) != 0) and ((self.eventMask & AWTEvent.KEY_EVENT_MASK) != 0 or self.keyListener != None)

    def eventEnabled(self, e):
        """ generated source for method eventEnabled """
        return eventTypeEnabled(e.id)

    def eventTypeEnabled(self, type_):
        """ generated source for method eventTypeEnabled """
        if type_ == ComponentEvent.COMPONENT_MOVED:
            pass
        elif type_ == ComponentEvent.COMPONENT_RESIZED:
            pass
        elif type_ == ComponentEvent.COMPONENT_SHOWN:
            pass
        elif type_ == ComponentEvent.COMPONENT_HIDDEN:
            if (self.eventMask & AWTEvent.COMPONENT_EVENT_MASK) != 0 or self.componentListener != None:
                return True
        elif type_ == FocusEvent.FOCUS_GAINED:
            pass
        elif type_ == FocusEvent.FOCUS_LOST:
            if (self.eventMask & AWTEvent.FOCUS_EVENT_MASK) != 0 or self.focusListener != None:
                return True
        elif type_ == KeyEvent.KEY_PRESSED:
            pass
        elif type_ == KeyEvent.KEY_RELEASED:
            pass
        elif type_ == KeyEvent.KEY_TYPED:
            if (self.eventMask & AWTEvent.KEY_EVENT_MASK) != 0 or self.keyListener != None:
                return True
        elif type_ == MouseEvent.MOUSE_PRESSED:
            pass
        elif type_ == MouseEvent.MOUSE_RELEASED:
            pass
        elif type_ == MouseEvent.MOUSE_ENTERED:
            pass
        elif type_ == MouseEvent.MOUSE_EXITED:
            pass
        elif type_ == MouseEvent.MOUSE_CLICKED:
            if (self.eventMask & AWTEvent.MOUSE_EVENT_MASK) != 0 or self.mouseListener != None:
                return True
        elif type_ == MouseEvent.MOUSE_MOVED:
            pass
        elif type_ == MouseEvent.MOUSE_DRAGGED:
            if (self.eventMask & AWTEvent.MOUSE_MOTION_EVENT_MASK) != 0 or self.mouseMotionListener != None:
                return True
        elif type_ == MouseEvent.MOUSE_WHEEL:
            if (self.eventMask & AWTEvent.MOUSE_WHEEL_EVENT_MASK) != 0 or self.mouseWheelListener != None:
                return True
        elif type_ == InputMethodEvent.INPUT_METHOD_TEXT_CHANGED:
            pass
        elif type_ == InputMethodEvent.CARET_POSITION_CHANGED:
            if (self.eventMask & AWTEvent.INPUT_METHOD_EVENT_MASK) != 0 or self.inputMethodListener != None:
                return True
        elif type_ == HierarchyEvent.HIERARCHY_CHANGED:
            if (self.eventMask & AWTEvent.HIERARCHY_EVENT_MASK) != 0 or self.hierarchyListener != None:
                return True
        elif type_ == HierarchyEvent.ANCESTOR_MOVED:
            pass
        elif type_ == HierarchyEvent.ANCESTOR_RESIZED:
            if (self.eventMask & AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK) != 0 or self.hierarchyBoundsListener != None:
                return True
        elif type_ == ActionEvent.ACTION_PERFORMED:
            if (self.eventMask & AWTEvent.ACTION_EVENT_MASK) != 0:
                return True
        elif type_ == TextEvent.TEXT_VALUE_CHANGED:
            if (self.eventMask & AWTEvent.TEXT_EVENT_MASK) != 0:
                return True
        elif type_ == ItemEvent.ITEM_STATE_CHANGED:
            if (self.eventMask & AWTEvent.ITEM_EVENT_MASK) != 0:
                return True
        elif type_ == AdjustmentEvent.ADJUSTMENT_VALUE_CHANGED:
            if (self.eventMask & AWTEvent.ADJUSTMENT_EVENT_MASK) != 0:
                return True
        else:
            if type_ > AWTEvent.RESERVED_ID_MAX:
                return True
        return False

    def postEvent(self, e):
        """ generated source for method postEvent """
        peer = self.peer
        if handleEvent(e):
            e.consume()
            return True
        parent = self.parent
        eventx = e.x
        eventy = e.y
        if parent != None:
            e.translate(self.x, self.y)
            if parent.postEvent(e):
                e.consume()
                return True
            e.x = eventx
            e.y = eventy
        return False

    @synchronized
    def addComponentListener(self, l):
        """ generated source for method addComponentListener """
        if l == None:
            return
        self.componentListener = AWTEventMulticaster.add(self.componentListener, l)
        self.newEventsOnly = True

    @synchronized
    def removeComponentListener(self, l):
        """ generated source for method removeComponentListener """
        if l == None:
            return
        self.componentListener = AWTEventMulticaster.remove(self.componentListener, l)

    @synchronized
    def getComponentListeners(self):
        """ generated source for method getComponentListeners """
        return getListeners(ComponentListener.__class__)

    @synchronized
    def addFocusListener(self, l):
        """ generated source for method addFocusListener """
        if l == None:
            return
        self.focusListener = AWTEventMulticaster.add(self.focusListener, l)
        self.newEventsOnly = True
        if isinstance(self.peer, (LightweightPeer, )):
            self.parent.proxyEnableEvents(AWTEvent.FOCUS_EVENT_MASK)

    @synchronized
    def removeFocusListener(self, l):
        """ generated source for method removeFocusListener """
        if l == None:
            return
        self.focusListener = AWTEventMulticaster.remove(self.focusListener, l)

    @synchronized
    def getFocusListeners(self):
        """ generated source for method getFocusListeners """
        return getListeners(FocusListener.__class__)

    def addHierarchyListener(self, l):
        """ generated source for method addHierarchyListener """
        if l == None:
            return
        notifyAncestors = bool()
        with lock_for_object(self):
            notifyAncestors = (self.hierarchyListener == None and (self.eventMask & AWTEvent.HIERARCHY_EVENT_MASK) == 0)
            self.hierarchyListener = AWTEventMulticaster.add(self.hierarchyListener, l)
            notifyAncestors = (notifyAncestors and self.hierarchyListener != None)
            self.newEventsOnly = True
        if notifyAncestors:
            with lock_for_object(self.getTreeLock()):
                adjustListeningChildrenOnParent(AWTEvent.HIERARCHY_EVENT_MASK, 1)

    def removeHierarchyListener(self, l):
        """ generated source for method removeHierarchyListener """
        if l == None:
            return
        notifyAncestors = bool()
        with lock_for_object(self):
            notifyAncestors = (self.hierarchyListener != None and (self.eventMask & AWTEvent.HIERARCHY_EVENT_MASK) == 0)
            self.hierarchyListener = AWTEventMulticaster.remove(self.hierarchyListener, l)
            notifyAncestors = (notifyAncestors and self.hierarchyListener == None)
        if notifyAncestors:
            with lock_for_object(self.getTreeLock()):
                adjustListeningChildrenOnParent(AWTEvent.HIERARCHY_EVENT_MASK, -1)

    @synchronized
    def getHierarchyListeners(self):
        """ generated source for method getHierarchyListeners """
        return getListeners(HierarchyListener.__class__)

    def addHierarchyBoundsListener(self, l):
        """ generated source for method addHierarchyBoundsListener """
        if l == None:
            return
        notifyAncestors = bool()
        with lock_for_object(self):
            notifyAncestors = (self.hierarchyBoundsListener == None and (self.eventMask & AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK) == 0)
            self.hierarchyBoundsListener = AWTEventMulticaster.add(self.hierarchyBoundsListener, l)
            notifyAncestors = (notifyAncestors and self.hierarchyBoundsListener != None)
            self.newEventsOnly = True
        if notifyAncestors:
            with lock_for_object(self.getTreeLock()):
                adjustListeningChildrenOnParent(AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK, 1)

    def removeHierarchyBoundsListener(self, l):
        """ generated source for method removeHierarchyBoundsListener """
        if l == None:
            return
        notifyAncestors = bool()
        with lock_for_object(self):
            notifyAncestors = (self.hierarchyBoundsListener != None and (self.eventMask & AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK) == 0)
            self.hierarchyBoundsListener = AWTEventMulticaster.remove(self.hierarchyBoundsListener, l)
            notifyAncestors = (notifyAncestors and self.hierarchyBoundsListener == None)
        if notifyAncestors:
            with lock_for_object(self.getTreeLock()):
                adjustListeningChildrenOnParent(AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK, -1)

    def numListening(self, mask):
        """ generated source for method numListening """
        if self.eventLog.isLoggable(PlatformLogger.Level.FINE):
            if (mask != AWTEvent.HIERARCHY_EVENT_MASK) and (mask != AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK):
                self.eventLog.fine("Assertion failed")
        if (mask == AWTEvent.HIERARCHY_EVENT_MASK and (self.hierarchyListener != None or (self.eventMask & AWTEvent.HIERARCHY_EVENT_MASK) != 0)) or (mask == AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK and (self.hierarchyBoundsListener != None or (self.eventMask & AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK) != 0)):
            return 1
        else:
            return 0

    def countHierarchyMembers(self):
        """ generated source for method countHierarchyMembers """
        return 1

    def createHierarchyEvents(self, id, changed, changedParent, changeFlags, enabledOnToolkit):
        """ generated source for method createHierarchyEvents """
        if id == HierarchyEvent.HIERARCHY_CHANGED:
            if self.hierarchyListener != None or (self.eventMask & AWTEvent.HIERARCHY_EVENT_MASK) != 0 or enabledOnToolkit:
                e = HierarchyEvent(self, id, changed, changedParent, changeFlags)
                self.dispatchEvent(e)
                return 1
        elif id == HierarchyEvent.ANCESTOR_MOVED:
            pass
        elif id == HierarchyEvent.ANCESTOR_RESIZED:
            if self.eventLog.isLoggable(PlatformLogger.Level.FINE):
                if changeFlags != 0:
                    self.eventLog.fine("Assertion (changeFlags == 0) failed")
            if self.hierarchyBoundsListener != None or (self.eventMask & AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK) != 0 or enabledOnToolkit:
                e = HierarchyEvent(self, id, changed, changedParent)
                self.dispatchEvent(e)
                return 1
        else:
            if self.eventLog.isLoggable(PlatformLogger.Level.FINE):
                self.eventLog.fine("This code must never be reached")
        return 0

    @synchronized
    def getHierarchyBoundsListeners(self):
        """ generated source for method getHierarchyBoundsListeners """
        return getListeners(HierarchyBoundsListener.__class__)

    def adjustListeningChildrenOnParent(self, mask, num):
        """ generated source for method adjustListeningChildrenOnParent """
        if self.parent != None:
            self.parent.adjustListeningChildren(mask, num)

    @synchronized
    def addKeyListener(self, l):
        """ generated source for method addKeyListener """
        if l == None:
            return
        self.keyListener = AWTEventMulticaster.add(self.keyListener, l)
        self.newEventsOnly = True
        if isinstance(self.peer, (LightweightPeer, )):
            self.parent.proxyEnableEvents(AWTEvent.KEY_EVENT_MASK)

    @synchronized
    def removeKeyListener(self, l):
        """ generated source for method removeKeyListener """
        if l == None:
            return
        self.keyListener = AWTEventMulticaster.remove(self.keyListener, l)

    @synchronized
    def getKeyListeners(self):
        """ generated source for method getKeyListeners """
        return getListeners(KeyListener.__class__)

    @synchronized
    def addMouseListener(self, l):
        """ generated source for method addMouseListener """
        if l == None:
            return
        self.mouseListener = AWTEventMulticaster.add(self.mouseListener, l)
        self.newEventsOnly = True
        if isinstance(self.peer, (LightweightPeer, )):
            self.parent.proxyEnableEvents(AWTEvent.MOUSE_EVENT_MASK)

    @synchronized
    def removeMouseListener(self, l):
        """ generated source for method removeMouseListener """
        if l == None:
            return
        self.mouseListener = AWTEventMulticaster.remove(self.mouseListener, l)

    @synchronized
    def getMouseListeners(self):
        """ generated source for method getMouseListeners """
        return getListeners(MouseListener.__class__)

    @synchronized
    def addMouseMotionListener(self, l):
        """ generated source for method addMouseMotionListener """
        if l == None:
            return
        self.mouseMotionListener = AWTEventMulticaster.add(self.mouseMotionListener, l)
        self.newEventsOnly = True
        if isinstance(self.peer, (LightweightPeer, )):
            self.parent.proxyEnableEvents(AWTEvent.MOUSE_MOTION_EVENT_MASK)

    @synchronized
    def removeMouseMotionListener(self, l):
        """ generated source for method removeMouseMotionListener """
        if l == None:
            return
        self.mouseMotionListener = AWTEventMulticaster.remove(self.mouseMotionListener, l)

    @synchronized
    def getMouseMotionListeners(self):
        """ generated source for method getMouseMotionListeners """
        return getListeners(MouseMotionListener.__class__)

    @synchronized
    def addMouseWheelListener(self, l):
        """ generated source for method addMouseWheelListener """
        if l == None:
            return
        self.mouseWheelListener = AWTEventMulticaster.add(self.mouseWheelListener, l)
        self.newEventsOnly = True
        if isinstance(self.peer, (LightweightPeer, )):
            self.parent.proxyEnableEvents(AWTEvent.MOUSE_WHEEL_EVENT_MASK)

    @synchronized
    def removeMouseWheelListener(self, l):
        """ generated source for method removeMouseWheelListener """
        if l == None:
            return
        self.mouseWheelListener = AWTEventMulticaster.remove(self.mouseWheelListener, l)

    @synchronized
    def getMouseWheelListeners(self):
        """ generated source for method getMouseWheelListeners """
        return getListeners(MouseWheelListener.__class__)

    @synchronized
    def addInputMethodListener(self, l):
        """ generated source for method addInputMethodListener """
        if l == None:
            return
        self.inputMethodListener = AWTEventMulticaster.add(self.inputMethodListener, l)
        self.newEventsOnly = True

    @synchronized
    def removeInputMethodListener(self, l):
        """ generated source for method removeInputMethodListener """
        if l == None:
            return
        self.inputMethodListener = AWTEventMulticaster.remove(self.inputMethodListener, l)

    @synchronized
    def getInputMethodListeners(self):
        """ generated source for method getInputMethodListeners """
        return getListeners(InputMethodListener.__class__)

    @SuppressWarnings("unchecked")
    def getListeners(self, listenerType):
        """ generated source for method getListeners """
        l = None
        if listenerType == ComponentListener.__class__:
            l = self.componentListener
        elif listenerType == FocusListener.__class__:
            l = self.focusListener
        elif listenerType == HierarchyListener.__class__:
            l = self.hierarchyListener
        elif listenerType == HierarchyBoundsListener.__class__:
            l = self.hierarchyBoundsListener
        elif listenerType == KeyListener.__class__:
            l = self.keyListener
        elif listenerType == MouseListener.__class__:
            l = self.mouseListener
        elif listenerType == MouseMotionListener.__class__:
            l = self.mouseMotionListener
        elif listenerType == MouseWheelListener.__class__:
            l = self.mouseWheelListener
        elif listenerType == InputMethodListener.__class__:
            l = self.inputMethodListener
        elif listenerType == PropertyChangeListener.__class__:
            return getPropertyChangeListeners()
        return AWTEventMulticaster.getListeners(l, listenerType)

    def getInputMethodRequests(self):
        """ generated source for method getInputMethodRequests """
        return None

    def getInputContext(self):
        """ generated source for method getInputContext """
        parent = self.parent
        if parent == None:
            return None
        else:
            return parent.getInputContext()

    def enableEvents(self, eventsToEnable):
        """ generated source for method enableEvents """
        notifyAncestors = 0
        with lock_for_object(self):
            if (eventsToEnable & AWTEvent.HIERARCHY_EVENT_MASK) != 0 and self.hierarchyListener == None and (self.eventMask & AWTEvent.HIERARCHY_EVENT_MASK) == 0:
                notifyAncestors |= AWTEvent.HIERARCHY_EVENT_MASK
            if (eventsToEnable & AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK) != 0 and self.hierarchyBoundsListener == None and (self.eventMask & AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK) == 0:
                notifyAncestors |= AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK
            self.eventMask |= eventsToEnable
            self.newEventsOnly = True
        if isinstance(self.peer, (LightweightPeer, )):
            self.parent.proxyEnableEvents(self.eventMask)
        if notifyAncestors != 0:
            with lock_for_object(self.getTreeLock()):
                self.adjustListeningChildrenOnParent(notifyAncestors, 1)

    def disableEvents(self, eventsToDisable):
        """ generated source for method disableEvents """
        notifyAncestors = 0
        with lock_for_object(self):
            if (eventsToDisable & AWTEvent.HIERARCHY_EVENT_MASK) != 0 and self.hierarchyListener == None and (self.eventMask & AWTEvent.HIERARCHY_EVENT_MASK) != 0:
                notifyAncestors |= AWTEvent.HIERARCHY_EVENT_MASK
            if (eventsToDisable & AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK) != 0 and self.hierarchyBoundsListener == None and (self.eventMask & AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK) != 0:
                notifyAncestors |= AWTEvent.HIERARCHY_BOUNDS_EVENT_MASK
            self.eventMask &= ~eventsToDisable
        if notifyAncestors != 0:
            with lock_for_object(self.getTreeLock()):
                self.adjustListeningChildrenOnParent(notifyAncestors, -1)

    eventCache = []
    coalescingEnabled = checkCoalescing()
    coalesceMap = java.util.WeakHashMap()

    def checkCoalescing(self):
        """ generated source for method checkCoalescing """
        if getClass().getClassLoader() == None:
            return False
        clazz = getClass()
        with lock_for_object(self.coalesceMap):
            value = self.coalesceMap.get(clazz)
            if value != None:
                return value
            enabled = java.security.AccessController.doPrivileged(java.security.PrivilegedAction())
            self.coalesceMap.put(clazz, self.enabled)
            return self.enabled

    coalesceEventsParams = [AWTEvent.__class__, AWTEvent.__class__]

    @classmethod
    def isCoalesceEventsOverriden(cls, clazz):
        """ generated source for method isCoalesceEventsOverriden """
        assert Thread.holdsLock(cls.coalesceMap)
        superclass = clazz.getSuperclass()
        if superclass == None:
            return False
        if superclass.getClassLoader() != None:
            value = cls.coalesceMap.get(superclass)
            if value == None:
                if cls.isCoalesceEventsOverriden(superclass):
                    cls.coalesceMap.put(superclass, True)
                    return True
            elif value:
                return True
        try:
            clazz.getDeclaredMethod("coalesceEvents", cls.coalesceEventsParams)
            return True
        except NoSuchMethodException as e:
            return False

    def isCoalescingEnabled(self):
        """ generated source for method isCoalescingEnabled """
        return self.coalescingEnabled

    def coalesceEvents(self, existingEvent, newEvent):
        """ generated source for method coalesceEvents """
        return None

    @processEvent.register(object, AWTEvent)
    def processEvent_0(self, e):
        """ generated source for method processEvent_0 """
        if isinstance(e, (FocusEvent, )):
            processFocusEvent(e)
        elif isinstance(e, (MouseEvent, )):
            if e.getID() == MouseEvent.MOUSE_PRESSED:
                pass
            elif e.getID() == MouseEvent.MOUSE_RELEASED:
                pass
            elif e.getID() == MouseEvent.MOUSE_CLICKED:
                pass
            elif e.getID() == MouseEvent.MOUSE_ENTERED:
                pass
            elif e.getID() == MouseEvent.MOUSE_EXITED:
                processMouseEvent(e)
            elif e.getID() == MouseEvent.MOUSE_MOVED:
                pass
            elif e.getID() == MouseEvent.MOUSE_DRAGGED:
                processMouseMotionEvent(e)
            elif e.getID() == MouseEvent.MOUSE_WHEEL:
                processMouseWheelEvent(e)
        elif isinstance(e, (KeyEvent, )):
            processKeyEvent(e)
        elif isinstance(e, (ComponentEvent, )):
            processComponentEvent(e)
        elif isinstance(e, (InputMethodEvent, )):
            processInputMethodEvent(e)
        elif isinstance(e, (HierarchyEvent, )):
            if e.getID() == HierarchyEvent.HIERARCHY_CHANGED:
                processHierarchyEvent(e)
            elif e.getID() == HierarchyEvent.ANCESTOR_MOVED:
                pass
            elif e.getID() == HierarchyEvent.ANCESTOR_RESIZED:
                processHierarchyBoundsEvent(e)

    def processComponentEvent(self, e):
        """ generated source for method processComponentEvent """
        listener = self.componentListener
        if listener != None:
            id = e.getID()
            if id == ComponentEvent.COMPONENT_RESIZED:
                listener.componentResized(e)
            elif id == ComponentEvent.COMPONENT_MOVED:
                listener.componentMoved(e)
            elif id == ComponentEvent.COMPONENT_SHOWN:
                listener.componentShown(e)
            elif id == ComponentEvent.COMPONENT_HIDDEN:
                listener.componentHidden(e)

    def processFocusEvent(self, e):
        """ generated source for method processFocusEvent """
        listener = self.focusListener
        if listener != None:
            id = e.getID()
            if id == FocusEvent.FOCUS_GAINED:
                listener.focusGained(e)
            elif id == FocusEvent.FOCUS_LOST:
                listener.focusLost(e)

    def processKeyEvent(self, e):
        """ generated source for method processKeyEvent """
        listener = self.keyListener
        if listener != None:
            id = e.getID()
            if id == KeyEvent.KEY_TYPED:
                listener.keyTyped(e)
            elif id == KeyEvent.KEY_PRESSED:
                listener.keyPressed(e)
            elif id == KeyEvent.KEY_RELEASED:
                listener.keyReleased(e)

    def processMouseEvent(self, e):
        """ generated source for method processMouseEvent """
        listener = self.mouseListener
        if listener != None:
            id = e.getID()
            if id == MouseEvent.MOUSE_PRESSED:
                listener.mousePressed(e)
            elif id == MouseEvent.MOUSE_RELEASED:
                listener.mouseReleased(e)
            elif id == MouseEvent.MOUSE_CLICKED:
                listener.mouseClicked(e)
            elif id == MouseEvent.MOUSE_EXITED:
                listener.mouseExited(e)
            elif id == MouseEvent.MOUSE_ENTERED:
                listener.mouseEntered(e)

    def processMouseMotionEvent(self, e):
        """ generated source for method processMouseMotionEvent """
        listener = self.mouseMotionListener
        if listener != None:
            id = e.getID()
            if id == MouseEvent.MOUSE_MOVED:
                listener.mouseMoved(e)
            elif id == MouseEvent.MOUSE_DRAGGED:
                listener.mouseDragged(e)

    def processMouseWheelEvent(self, e):
        """ generated source for method processMouseWheelEvent """
        listener = self.mouseWheelListener
        if listener != None:
            id = e.getID()
            if id == MouseEvent.MOUSE_WHEEL:
                listener.mouseWheelMoved(e)

    def postsOldMouseEvents(self):
        """ generated source for method postsOldMouseEvents """
        return False

    def processInputMethodEvent(self, e):
        """ generated source for method processInputMethodEvent """
        listener = self.inputMethodListener
        if listener != None:
            id = e.getID()
            if id == InputMethodEvent.INPUT_METHOD_TEXT_CHANGED:
                listener.inputMethodTextChanged(e)
            elif id == InputMethodEvent.CARET_POSITION_CHANGED:
                listener.caretPositionChanged(e)

    def processHierarchyEvent(self, e):
        """ generated source for method processHierarchyEvent """
        listener = self.hierarchyListener
        if listener != None:
            id = e.getID()
            if id == HierarchyEvent.HIERARCHY_CHANGED:
                listener.hierarchyChanged(e)

    def processHierarchyBoundsEvent(self, e):
        """ generated source for method processHierarchyBoundsEvent """
        listener = self.hierarchyBoundsListener
        if listener != None:
            id = e.getID()
            if id == HierarchyEvent.ANCESTOR_MOVED:
                listener.ancestorMoved(e)
            elif id == HierarchyEvent.ANCESTOR_RESIZED:
                listener.ancestorResized(e)

    def handleEvent(self, evt):
        """ generated source for method handleEvent """
        if evt.id == Event.MOUSE_ENTER:
            return mouseEnter(evt, evt.x, evt.y)
        elif evt.id == Event.MOUSE_EXIT:
            return mouseExit(evt, evt.x, evt.y)
        elif evt.id == Event.MOUSE_MOVE:
            return mouseMove(evt, evt.x, evt.y)
        elif evt.id == Event.MOUSE_DOWN:
            return mouseDown(evt, evt.x, evt.y)
        elif evt.id == Event.MOUSE_DRAG:
            return mouseDrag(evt, evt.x, evt.y)
        elif evt.id == Event.MOUSE_UP:
            return mouseUp(evt, evt.x, evt.y)
        elif evt.id == Event.KEY_PRESS:
            pass
        elif evt.id == Event.KEY_ACTION:
            return keyDown(evt, evt.key)
        elif evt.id == Event.KEY_RELEASE:
            pass
        elif evt.id == Event.KEY_ACTION_RELEASE:
            return keyUp(evt, evt.key)
        elif evt.id == Event.ACTION_EVENT:
            return action(evt, evt.arg)
        elif evt.id == Event.GOT_FOCUS:
            return gotFocus(evt, evt.arg)
        elif evt.id == Event.LOST_FOCUS:
            return lostFocus(evt, evt.arg)
        return False

    def mouseDown(self, evt, x, y):
        """ generated source for method mouseDown """
        return False

    def mouseDrag(self, evt, x, y):
        """ generated source for method mouseDrag """
        return False

    def mouseUp(self, evt, x, y):
        """ generated source for method mouseUp """
        return False

    def mouseMove(self, evt, x, y):
        """ generated source for method mouseMove """
        return False

    def mouseEnter(self, evt, x, y):
        """ generated source for method mouseEnter """
        return False

    def mouseExit(self, evt, x, y):
        """ generated source for method mouseExit """
        return False

    def keyDown(self, evt, key):
        """ generated source for method keyDown """
        return False

    def keyUp(self, evt, key):
        """ generated source for method keyUp """
        return False

    def action(self, evt, what):
        """ generated source for method action """
        return False

    def addNotify(self):
        """ generated source for method addNotify """
        with lock_for_object(self.getTreeLock()):
            peer = self.peer
            if self.peer == None or isinstance(self.peer, (LightweightPeer, )):
                if self.peer == None:
                    self.peer = self.peer = self.getToolkit().createComponent(self)
                if self.parent != None:
                    mask = 0
                    if (self.mouseListener != None) or ((self.eventMask & AWTEvent.MOUSE_EVENT_MASK) != 0):
                        mask |= AWTEvent.MOUSE_EVENT_MASK
                    if (self.mouseMotionListener != None) or ((self.eventMask & AWTEvent.MOUSE_MOTION_EVENT_MASK) != 0):
                        mask |= AWTEvent.MOUSE_MOTION_EVENT_MASK
                    if (self.mouseWheelListener != None) or ((self.eventMask & AWTEvent.MOUSE_WHEEL_EVENT_MASK) != 0):
                        mask |= AWTEvent.MOUSE_WHEEL_EVENT_MASK
                    if self.focusListener != None or (self.eventMask & AWTEvent.FOCUS_EVENT_MASK) != 0:
                        mask |= AWTEvent.FOCUS_EVENT_MASK
                    if self.keyListener != None or (self.eventMask & AWTEvent.KEY_EVENT_MASK) != 0:
                        mask |= AWTEvent.KEY_EVENT_MASK
                    if mask != 0:
                        self.parent.proxyEnableEvents(mask)
            else:
                parent = self.getContainer()
                if self.parent != None and self.parent.isLightweight():
                    relocateComponent()
                    if not self.parent.isRecursivelyVisibleUpToHeavyweightContainer():
                        self.peer.setVisible(False)
            self.invalidate()
            npopups = (len(self.popups) if self.popups != None else 0)
            i = 0
            while i < npopups:
                popup = self.popups.elementAt(i)
                popup.addNotify()
                i += 1
            if self.dropTarget != None:
                self.dropTarget.addNotify(self.peer)
            self.peerFont = self.getFont()
            if self.getContainer() != None and not self.isAddNotifyComplete:
                self.getContainer().increaseComponentCount(self)
            updateZOrder()
            if not self.isAddNotifyComplete:
                mixOnShowing()
            self.isAddNotifyComplete = True
            if self.hierarchyListener != None or (self.eventMask & AWTEvent.HIERARCHY_EVENT_MASK) != 0 or Toolkit.enabledOnToolkit(AWTEvent.HIERARCHY_EVENT_MASK):
                e = HierarchyEvent(self, HierarchyEvent.HIERARCHY_CHANGED, self, self.parent, HierarchyEvent.DISPLAYABILITY_CHANGED | (HierarchyEvent.SHOWING_CHANGED if (self.isRecursivelyVisible()) else 0))
                self.dispatchEvent(e)

    def removeNotify(self):
        """ generated source for method removeNotify """
        KeyboardFocusManager.clearMostRecentFocusOwner(self)
        if KeyboardFocusManager.getCurrentKeyboardFocusManager().getPermanentFocusOwner() == self:
            KeyboardFocusManager.getCurrentKeyboardFocusManager().setGlobalPermanentFocusOwner(None)
        with lock_for_object(self.getTreeLock()):
            if isFocusOwner() and KeyboardFocusManager.isAutoFocusTransferEnabledFor(self):
                transferFocus(True)
            if self.getContainer() != None and self.isAddNotifyComplete:
                self.getContainer().decreaseComponentCount(self)
            npopups = (len(self.popups) if self.popups != None else 0)
            i = 0
            while i < npopups:
                popup = self.popups.elementAt(i)
                popup.removeNotify()
                i += 1
            if (self.eventMask & AWTEvent.INPUT_METHODS_ENABLED_MASK) != 0:
                inputContext = self.getInputContext()
                if inputContext != None:
                    inputContext.removeNotify(self)
            p = self.peer
            if p != None:
                isLightweight = self.isLightweight()
                if isinstance(self.bufferStrategy, (self.FlipBufferStrategy, )):
                    (self.bufferStrategy).destroyBuffers()
                if self.dropTarget != None:
                    self.dropTarget.removeNotify(self.peer)
                if self.visible:
                    p.setVisible(False)
                self.peer = None
                self.peerFont = None
                Toolkit.getEventQueue().removeSourceEvents(self, False)
                KeyboardFocusManager.getCurrentKeyboardFocusManager().discardKeyEvents(self)
                p.dispose()
                mixOnHiding(self.isLightweight)
                self.isAddNotifyComplete = False
                self.compoundShape = None
            if self.hierarchyListener != None or (self.eventMask & AWTEvent.HIERARCHY_EVENT_MASK) != 0 or Toolkit.enabledOnToolkit(AWTEvent.HIERARCHY_EVENT_MASK):
                e = HierarchyEvent(self, HierarchyEvent.HIERARCHY_CHANGED, self, self.parent, HierarchyEvent.DISPLAYABILITY_CHANGED | (HierarchyEvent.SHOWING_CHANGED if (self.isRecursivelyVisible()) else 0))
                self.dispatchEvent(e)

    def gotFocus(self, evt, what):
        """ generated source for method gotFocus """
        return False

    def lostFocus(self, evt, what):
        """ generated source for method lostFocus """
        return False

    def isFocusTraversable(self):
        """ generated source for method isFocusTraversable """
        if self.isFocusTraversableOverridden == self.FOCUS_TRAVERSABLE_UNKNOWN:
            self.isFocusTraversableOverridden = self.FOCUS_TRAVERSABLE_DEFAULT
        return self.focusable

    def isFocusable(self):
        """ generated source for method isFocusable """
        return self.isFocusTraversable()

    def setFocusable(self, focusable):
        """ generated source for method setFocusable """
        oldFocusable = bool()
        with lock_for_object(self):
            oldFocusable = self.focusable
            self.focusable = focusable
        self.isFocusTraversableOverridden = self.FOCUS_TRAVERSABLE_SET
        firePropertyChange("focusable", oldFocusable, focusable)
        if oldFocusable and not focusable:
            if isFocusOwner() and KeyboardFocusManager.isAutoFocusTransferEnabled():
                transferFocus(True)
            KeyboardFocusManager.clearMostRecentFocusOwner(self)

    def isFocusTraversableOverridden(self):
        """ generated source for method isFocusTraversableOverridden """
        return (self.isFocusTraversableOverridden != self.FOCUS_TRAVERSABLE_DEFAULT)

    def setFocusTraversalKeys(self, id, keystrokes):
        """ generated source for method setFocusTraversalKeys """
        if id < 0 or id >= KeyboardFocusManager.TRAVERSAL_KEY_LENGTH - 1:
            raise IllegalArgumentException("invalid focus traversal key identifier")
        setFocusTraversalKeys_NoIDCheck(id, keystrokes)

    def getFocusTraversalKeys(self, id):
        """ generated source for method getFocusTraversalKeys """
        if id < 0 or id >= KeyboardFocusManager.TRAVERSAL_KEY_LENGTH - 1:
            raise IllegalArgumentException("invalid focus traversal key identifier")
        return getFocusTraversalKeys_NoIDCheck(id)

    def setFocusTraversalKeys_NoIDCheck(self, id, keystrokes):
        """ generated source for method setFocusTraversalKeys_NoIDCheck """
        oldKeys = None
        with lock_for_object(self):
            if self.focusTraversalKeys == None:
                self.initializeFocusTraversalKeys()
            if keystrokes != None:
                for keystroke in keystrokes:
                    if keystroke == None:
                        raise IllegalArgumentException("cannot set null focus traversal key")
                    if keystroke.getKeyChar() != KeyEvent.CHAR_UNDEFINED:
                        raise IllegalArgumentException("focus traversal keys cannot map to KEY_TYPED events")
                    i = 0
                    while len(focusTraversalKeys):
                        if i == id:
                            i += 1
                            continue 
                        if getFocusTraversalKeys_NoIDCheck(i).contains(keystroke):
                            raise IllegalArgumentException("focus traversal keys must be unique for a Component")
                        i += 1
            oldKeys = self.focusTraversalKeys[id]
            self.focusTraversalKeys[id] = Collections.unmodifiableSet(HashSet(keystrokes)) if (keystrokes != None) else None
        firePropertyChange(self.focusTraversalKeyPropertyNames[id], oldKeys, keystrokes)

    def getFocusTraversalKeys_NoIDCheck(self, id):
        """ generated source for method getFocusTraversalKeys_NoIDCheck """
        keystrokes = self.focusTraversalKeys[id] if (self.focusTraversalKeys != None) else None
        if keystrokes != None:
            return keystrokes
        else:
            parent = self.parent
            if self.parent != None:
                return self.parent.getFocusTraversalKeys(id)
            else:
                return KeyboardFocusManager.getCurrentKeyboardFocusManager().getDefaultFocusTraversalKeys(id)

    def areFocusTraversalKeysSet(self, id):
        """ generated source for method areFocusTraversalKeysSet """
        if id < 0 or id >= KeyboardFocusManager.TRAVERSAL_KEY_LENGTH - 1:
            raise IllegalArgumentException("invalid focus traversal key identifier")
        return (self.focusTraversalKeys != None and self.focusTraversalKeys[id] != None)

    def setFocusTraversalKeysEnabled(self, focusTraversalKeysEnabled):
        """ generated source for method setFocusTraversalKeysEnabled """
        oldFocusTraversalKeysEnabled = bool()
        with lock_for_object(self):
            oldFocusTraversalKeysEnabled = self.focusTraversalKeysEnabled
            self.focusTraversalKeysEnabled = focusTraversalKeysEnabled
        firePropertyChange("focusTraversalKeysEnabled", oldFocusTraversalKeysEnabled, focusTraversalKeysEnabled)

    def getFocusTraversalKeysEnabled(self):
        """ generated source for method getFocusTraversalKeysEnabled """
        return self.focusTraversalKeysEnabled

    @requestFocus.register(object)
    def requestFocus_0(self):
        """ generated source for method requestFocus_0 """
        requestFocusHelper(False, True)

    @requestFocus.register(object, CausedFocusEvent.Cause)
    def requestFocus_1(self, cause):
        """ generated source for method requestFocus_1 """
        return requestFocusHelper(False, True, cause)

    @requestFocus.register(object, bool)
    def requestFocus_2(self, temporary):
        """ generated source for method requestFocus_2 """
        return requestFocusHelper(temporary, True)

    @requestFocus.register(object, bool, CausedFocusEvent.Cause)
    def requestFocus_3(self, temporary, cause):
        """ generated source for method requestFocus_3 """
        return requestFocusHelper(temporary, True, cause)

    @overloaded
    def requestFocusInWindow(self):
        """ generated source for method requestFocusInWindow """
        return requestFocusHelper(False, False)

    @requestFocusInWindow.register(object, CausedFocusEvent.Cause)
    def requestFocusInWindow_0(self, cause):
        """ generated source for method requestFocusInWindow_0 """
        return requestFocusHelper(False, False, cause)

    @requestFocusInWindow.register(object, bool)
    def requestFocusInWindow_1(self, temporary):
        """ generated source for method requestFocusInWindow_1 """
        return requestFocusHelper(temporary, False)

    @requestFocusInWindow.register(object, bool, CausedFocusEvent.Cause)
    def requestFocusInWindow_2(self, temporary, cause):
        """ generated source for method requestFocusInWindow_2 """
        return requestFocusHelper(temporary, False, cause)

    @overloaded
    def requestFocusHelper(self, temporary, focusedWindowChangeAllowed):
        """ generated source for method requestFocusHelper """
        return self.requestFocusHelper(temporary, focusedWindowChangeAllowed, CausedFocusEvent.Cause.UNKNOWN)

    @requestFocusHelper.register(object, bool, bool, CausedFocusEvent.Cause)
    def requestFocusHelper_0(self, temporary, focusedWindowChangeAllowed, cause):
        """ generated source for method requestFocusHelper_0 """
        currentEvent = EventQueue.getCurrentEvent()
        if isinstance(currentEvent, (MouseEvent, )) and SunToolkit.isSystemGenerated(currentEvent):
            source = (currentEvent).getComponent()
            if source == None or source.getContainingWindow() == getContainingWindow():
                self.focusLog.finest("requesting focus by mouse event \"in window\"")
                focusedWindowChangeAllowed = False
        if not isRequestFocusAccepted(temporary, focusedWindowChangeAllowed, cause):
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("requestFocus is not accepted")
            return False
        KeyboardFocusManager.setMostRecentFocusOwner(self)
        window = self
        while (window != None) and not (isinstance(window, (Window, ))):
            if not window.isVisible():
                if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                    self.focusLog.finest("component is recurively invisible")
                return False
            window = window.parent
        peer = self.peer
        heavyweight = getNativeContainer() if (isinstance(peer, (LightweightPeer, ))) else self
        if heavyweight == None or not heavyweight.isVisible():
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("Component is not a part of visible hierarchy")
            return False
        peer = heavyweight.peer
        if peer == None:
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("Peer is null")
            return False
        time = 0
        if EventQueue.isDispatchThread():
            time = Toolkit.getEventQueue().getMostRecentKeyEventTime()
        else:
            time = System.currentTimeMillis()
        success = peer.requestFocus(self, temporary, focusedWindowChangeAllowed, time, cause)
        if not success:
            KeyboardFocusManager.getCurrentKeyboardFocusManager(self.appContext).dequeueKeyEvents(time, self)
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("Peer request failed")
        else:
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("Pass for " + self)
        return success

    def isRequestFocusAccepted(self, temporary, focusedWindowChangeAllowed, cause):
        """ generated source for method isRequestFocusAccepted """
        if not self.isFocusable() or not self.isVisible():
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("Not focusable or not visible")
            return False
        peer = self.peer
        if peer == None:
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("peer is null")
            return False
        window = getContainingWindow()
        if window == None or not window.isFocusableWindow():
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("Component doesn't have toplevel")
            return False
        focusOwner = KeyboardFocusManager.getMostRecentFocusOwner(window)
        if focusOwner == None:
            focusOwner = KeyboardFocusManager.getCurrentKeyboardFocusManager().getFocusOwner()
            if focusOwner != None and focusOwner.getContainingWindow() != window:
                focusOwner = None
        if focusOwner == self or focusOwner == None:
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("focus owner is null or this")
            return True
        if CausedFocusEvent.Cause.ACTIVATION == cause:
            if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
                self.focusLog.finest("cause is activation")
            return True
        ret = Component.requestFocusController.acceptRequestFocus(focusOwner, self, temporary, focusedWindowChangeAllowed, cause)
        if self.focusLog.isLoggable(PlatformLogger.Level.FINEST):
            self.focusLog.finest("RequestFocusController returns {0}", ret)
        return ret

    requestFocusController = DummyRequestFocusController()

    class DummyRequestFocusController(RequestFocusController):
        """ generated source for class DummyRequestFocusController """
        def acceptRequestFocus(self, from_, to, temporary, focusedWindowChangeAllowed, cause):
            """ generated source for method acceptRequestFocus """
            return True

    @classmethod
    @setRequestFocusController.register(object, RequestFocusController)
    @synchronized
    def setRequestFocusController_0(cls, requestController):
        """ generated source for method setRequestFocusController_0 """
        if requestController == None:
            cls.requestFocusController = cls.DummyRequestFocusController()
        else:
            cls.requestFocusController = requestController

    def getFocusCycleRootAncestor(self):
        """ generated source for method getFocusCycleRootAncestor """
        rootAncestor = self.parent
        while rootAncestor != None and not rootAncestor.isFocusCycleRoot():
            rootAncestor = rootAncestor.parent
        return rootAncestor

    def isFocusCycleRoot(self, container):
        """ generated source for method isFocusCycleRoot """
        rootAncestor = self.getFocusCycleRootAncestor()
        return (rootAncestor == container)

    def getTraversalRoot(self):
        """ generated source for method getTraversalRoot """
        return self.getFocusCycleRootAncestor()

    @overloaded
    def transferFocus(self):
        """ generated source for method transferFocus """
        nextFocus()

    def nextFocus(self):
        """ generated source for method nextFocus """
        self.transferFocus(False)

    @transferFocus.register(object, bool)
    def transferFocus_0(self, clearOnFailure):
        """ generated source for method transferFocus_0 """
        if self.focusLog.isLoggable(PlatformLogger.Level.FINER):
            self.focusLog.finer("clearOnFailure = " + clearOnFailure)
        toFocus = getNextFocusCandidate()
        res = False
        if toFocus != None and not toFocus.isFocusOwner() and toFocus != self:
            res = toFocus.requestFocusInWindow(CausedFocusEvent.Cause.TRAVERSAL_FORWARD)
        if clearOnFailure and not res:
            if self.focusLog.isLoggable(PlatformLogger.Level.FINER):
                self.focusLog.finer("clear global focus owner")
            KeyboardFocusManager.getCurrentKeyboardFocusManager().clearGlobalFocusOwnerPriv()
        if self.focusLog.isLoggable(PlatformLogger.Level.FINER):
            self.focusLog.finer("returning result: " + res)
        return res

    def getNextFocusCandidate(self):
        """ generated source for method getNextFocusCandidate """
        rootAncestor = self.getTraversalRoot()
        comp = self
        while rootAncestor != None and not (rootAncestor.isShowing() and rootAncestor.canBeFocusOwner()):
            comp = rootAncestor
            rootAncestor = comp.getFocusCycleRootAncestor()
        if self.focusLog.isLoggable(PlatformLogger.Level.FINER):
            self.focusLog.finer("comp = " + comp + ", root = " + rootAncestor)
        candidate = None
        if rootAncestor != None:
            policy = rootAncestor.getFocusTraversalPolicy()
            toFocus = policy.getComponentAfter(rootAncestor, comp)
            if self.focusLog.isLoggable(PlatformLogger.Level.FINER):
                self.focusLog.finer("component after is " + toFocus)
            if toFocus == None:
                toFocus = policy.getDefaultComponent(rootAncestor)
                if self.focusLog.isLoggable(PlatformLogger.Level.FINER):
                    self.focusLog.finer("default component is " + toFocus)
            if toFocus == None:
                applet = EmbeddedFrame.getAppletIfAncestorOf(self)
                if applet != None:
                    toFocus = applet
            candidate = toFocus
        if self.focusLog.isLoggable(PlatformLogger.Level.FINER):
            self.focusLog.finer("Focus transfer candidate: " + candidate)
        return candidate

    @overloaded
    def transferFocusBackward(self):
        """ generated source for method transferFocusBackward """
        self.transferFocusBackward(False)

    @transferFocusBackward.register(object, bool)
    def transferFocusBackward_0(self, clearOnFailure):
        """ generated source for method transferFocusBackward_0 """
        rootAncestor = self.getTraversalRoot()
        comp = self
        while rootAncestor != None and not (rootAncestor.isShowing() and rootAncestor.canBeFocusOwner()):
            comp = rootAncestor
            rootAncestor = comp.getFocusCycleRootAncestor()
        res = False
        if rootAncestor != None:
            policy = rootAncestor.getFocusTraversalPolicy()
            toFocus = policy.getComponentBefore(rootAncestor, comp)
            if toFocus == None:
                toFocus = policy.getDefaultComponent(rootAncestor)
            if toFocus != None:
                res = toFocus.requestFocusInWindow(CausedFocusEvent.Cause.TRAVERSAL_BACKWARD)
        if clearOnFailure and not res:
            if self.focusLog.isLoggable(PlatformLogger.Level.FINER):
                self.focusLog.finer("clear global focus owner")
            KeyboardFocusManager.getCurrentKeyboardFocusManager().clearGlobalFocusOwnerPriv()
        if self.focusLog.isLoggable(PlatformLogger.Level.FINER):
            self.focusLog.finer("returning result: " + res)
        return res

    def transferFocusUpCycle(self):
        """ generated source for method transferFocusUpCycle """
        rootAncestor = None
        while rootAncestor != None and not (rootAncestor.isShowing() and rootAncestor.isFocusable() and rootAncestor.isEnabled()):
            pass
            rootAncestor = rootAncestor.getFocusCycleRootAncestor()
        if rootAncestor != None:
            rootAncestorRootAncestor = rootAncestor.getFocusCycleRootAncestor()
            fcr = rootAncestorRootAncestor if (rootAncestorRootAncestor != None) else rootAncestor
            KeyboardFocusManager.getCurrentKeyboardFocusManager().setGlobalCurrentFocusCycleRootPriv(fcr)
            rootAncestor.requestFocus(CausedFocusEvent.Cause.TRAVERSAL_UP)
        else:
            window = getContainingWindow()
            if window != None:
                toFocus = window.getFocusTraversalPolicy().getDefaultComponent(window)
                if toFocus != None:
                    KeyboardFocusManager.getCurrentKeyboardFocusManager().setGlobalCurrentFocusCycleRootPriv(window)
                    toFocus.requestFocus(CausedFocusEvent.Cause.TRAVERSAL_UP)

    def hasFocus(self):
        """ generated source for method hasFocus """
        return (KeyboardFocusManager.getCurrentKeyboardFocusManager().getFocusOwner() == self)

    def isFocusOwner(self):
        """ generated source for method isFocusOwner """
        return self.hasFocus()

    autoFocusTransferOnDisposal = True

    def setAutoFocusTransferOnDisposal(self, value):
        """ generated source for method setAutoFocusTransferOnDisposal """
        self.autoFocusTransferOnDisposal = value

    def isAutoFocusTransferOnDisposal(self):
        """ generated source for method isAutoFocusTransferOnDisposal """
        return self.autoFocusTransferOnDisposal

    def add(self, popup):
        """ generated source for method add """
        with lock_for_object(self.getTreeLock()):
            if popup.parent != None:
                popup.parent.remove(popup)
            if self.popups == None:
                self.popups = Vector()
            self.popups.addElement(popup)
            popup.parent = self
            if self.peer != None:
                if popup.peer == None:
                    popup.addNotify()

    @SuppressWarnings("unchecked")
    def remove(self, popup):
        """ generated source for method remove """
        with lock_for_object(self.getTreeLock()):
            if self.popups == None:
                return
            index = self.popups.indexOf(popup)
            if index >= 0:
                pmenu = popup
                if pmenu.peer != None:
                    pmenu.removeNotify()
                pmenu.parent = None
                self.popups.removeElementAt(index)
                if len(self.popups) == 0:
                    self.popups = None

    def paramString(self):
        """ generated source for method paramString """
        thisName = Objects.toString(self.__name__, "")
        invalid = "" if self.isValid() else ",invalid"
        hidden = "" if self.visible else ",hidden"
        disabled = "" if self.enabled else ",disabled"
        return thisName + ',' + self.x + ',' + self.y + ',' + self.width + 'x' + self.height + invalid + hidden + disabled

    def __str__(self):
        """ generated source for method toString """
        return getClass().__name__ + '[' + self.paramString() + ']'

    @overloaded
    def list_(self):
        """ generated source for method list_ """
        self.list_(System.out, 0)

    @list_.register(object, PrintStream)
    def list__0(self, out):
        """ generated source for method list__0 """
        self.list_(out, 0)

    @list_.register(object, PrintStream, int)
    def list__1(self, out, indent):
        """ generated source for method list__1 """
        i = 0
        while i < indent:
            out.print_(" ")
            i += 1
        out.println(self)

    @list_.register(object, PrintWriter)
    def list__2(self, out):
        """ generated source for method list__2 """
        self.list_(out, 0)

    @list_.register(object, PrintWriter, int)
    def list__3(self, out, indent):
        """ generated source for method list__3 """
        i = 0
        while i < indent:
            out.print_(" ")
            i += 1
        out.println(self)

    # def getNativeContainer(self):
    #     """ generated source for method getNativeContainer """
    #     p = self.getContainer()
    #     while p != None and isinstance(, (LightweightPeer, )):
    #         p = p.getContainer()
    #     return p

    # @overloaded
    # def addPropertyChangeListener(self, listener):
    #     """ generated source for method addPropertyChangeListener """
    #     with lock_for_object(self.getObjectLock()):
    #         if listener == None:
    #             return
    #         if self.changeSupport == None:
    #             self.changeSupport = PropertyChangeSupport(self)
    #         self.changeSupport.addPropertyChangeListener(listener)

    @overloaded
    def removePropertyChangeListener(self, listener):
        """ generated source for method removePropertyChangeListener """
        with lock_for_object(self.getObjectLock()):
            if listener == None or self.changeSupport == None:
                return
            self.changeSupport.removePropertyChangeListener(listener)

    @overloaded
    def getPropertyChangeListeners(self):
        """ generated source for method getPropertyChangeListeners """
        with lock_for_object(self.getObjectLock()):
            if self.changeSupport == None:
                return [None] * 0
            return self.changeSupport.getPropertyChangeListeners()

    @addPropertyChangeListener.register(object, str, PropertyChangeListener)
    def addPropertyChangeListener_0(self, propertyName, listener):
        """ generated source for method addPropertyChangeListener_0 """
        with lock_for_object(self.getObjectLock()):
            if listener == None:
                return
            if self.changeSupport == None:
                self.changeSupport = PropertyChangeSupport(self)
            self.changeSupport.addPropertyChangeListener(propertyName, listener)

    @removePropertyChangeListener.register(object, str, PropertyChangeListener)
    def removePropertyChangeListener_0(self, propertyName, listener):
        """ generated source for method removePropertyChangeListener_0 """
        with lock_for_object(self.getObjectLock()):
            if listener == None or self.changeSupport == None:
                return
            self.changeSupport.removePropertyChangeListener(propertyName, listener)

    @getPropertyChangeListeners.register(object, str)
    def getPropertyChangeListeners_0(self, propertyName):
        """ generated source for method getPropertyChangeListeners_0 """
        with lock_for_object(self.getObjectLock()):
            if self.changeSupport == None:
                return [None] * 0
            return self.changeSupport.getPropertyChangeListeners(propertyName)

    @overloaded
    def firePropertyChange(self, propertyName, oldValue, newValue):
        """ generated source for method firePropertyChange """
        changeSupport = None
        with lock_for_object(self.getObjectLock()):
            changeSupport = self.changeSupport
        if changeSupport == None or (oldValue != None and newValue != None and oldValue == newValue):
            return
        changeSupport.firePropertyChange(propertyName, oldValue, newValue)

    @firePropertyChange.register(object, str, bool, bool)
    def firePropertyChange_0(self, propertyName, oldValue, newValue):
        """ generated source for method firePropertyChange_0 """
        changeSupport = self.changeSupport
        if changeSupport == None or oldValue == newValue:
            return
        changeSupport.firePropertyChange(propertyName, oldValue, newValue)

    @firePropertyChange.register(object, str, int, int)
    def firePropertyChange_1(self, propertyName, oldValue, newValue):
        """ generated source for method firePropertyChange_1 """
        changeSupport = self.changeSupport
        if changeSupport == None or oldValue == newValue:
            return
        changeSupport.firePropertyChange(propertyName, oldValue, newValue)

    @firePropertyChange.register(object, str, int, int)
    def firePropertyChange_2(self, propertyName, oldValue, newValue):
        """ generated source for method firePropertyChange_2 """
        if self.changeSupport == None or oldValue == newValue:
            return
        self.firePropertyChange(propertyName, Byte.valueOf(oldValue), Byte.valueOf(newValue))

    @firePropertyChange.register(object, str, str, str)
    def firePropertyChange_3(self, propertyName, oldValue, newValue):
        """ generated source for method firePropertyChange_3 """
        if self.changeSupport == None or oldValue == newValue:
            return
        self.firePropertyChange(propertyName, Character(oldValue), Character(newValue))

    @firePropertyChange.register(object, str, int, int)
    def firePropertyChange_4(self, propertyName, oldValue, newValue):
        """ generated source for method firePropertyChange_4 """
        if self.changeSupport == None or oldValue == newValue:
            return
        self.firePropertyChange(propertyName, Short.valueOf(oldValue), Short.valueOf(newValue))

    @firePropertyChange.register(object, str, long, long)
    def firePropertyChange_5(self, propertyName, oldValue, newValue):
        """ generated source for method firePropertyChange_5 """
        if self.changeSupport == None or oldValue == newValue:
            return
        self.firePropertyChange(propertyName, Long.valueOf(oldValue), Long.valueOf(newValue))

    @firePropertyChange.register(object, str, float, float)
    def firePropertyChange_6(self, propertyName, oldValue, newValue):
        """ generated source for method firePropertyChange_6 """
        if self.changeSupport == None or oldValue == newValue:
            return
        self.firePropertyChange(propertyName, Float.valueOf(oldValue), Float.valueOf(newValue))

    @firePropertyChange.register(object, str, float, float)
    def firePropertyChange_7(self, propertyName, oldValue, newValue):
        """ generated source for method firePropertyChange_7 """
        if self.changeSupport == None or oldValue == newValue:
            return
        self.firePropertyChange(propertyName, Double.valueOf(oldValue), Double.valueOf(newValue))

    componentSerializedDataVersion = 4

    def doSwingSerialization(self):
        """ generated source for method doSwingSerialization """
        swingPackage = Package.getPackage("javax.swing")
        klass = Component.self.__class__
        while klass != None:
            if klass.getPackage() == swingPackage and klass.getClassLoader() == None:
                swingClass = klass
                methods = AccessController.doPrivileged(PrivilegedAction())
                counter = len(methods)
                while counter >= 0:
                    method = methods[counter]
                    if method.__name__ == "compWriteObjectNotify":
                        AccessController.doPrivileged(PrivilegedAction())
                        try:
                            method.invoke(self, None)
                        except IllegalAccessException as iae:
                            pass
                        except InvocationTargetException as ite:
                            pass
                        return
                    counter -= 1
            klass = klass.getSuperclass()

    def writeObject(self, s):
        """ generated source for method writeObject """
        self.doSwingSerialization()
        s.defaultWriteObject()
        AWTEventMulticaster.save(s, self.componentListenerK, self.componentListener)
        AWTEventMulticaster.save(s, self.focusListenerK, self.focusListener)
        AWTEventMulticaster.save(s, self.keyListenerK, self.keyListener)
        AWTEventMulticaster.save(s, self.mouseListenerK, self.mouseListener)
        AWTEventMulticaster.save(s, self.mouseMotionListenerK, self.mouseMotionListener)
        AWTEventMulticaster.save(s, self.inputMethodListenerK, self.inputMethodListener)
        s.writeObject(None)
        s.writeObject(self.componentOrientation)
        AWTEventMulticaster.save(s, self.hierarchyListenerK, self.hierarchyListener)
        AWTEventMulticaster.save(s, self.hierarchyBoundsListenerK, self.hierarchyBoundsListener)
        s.writeObject(None)
        AWTEventMulticaster.save(s, self.mouseWheelListenerK, self.mouseWheelListener)
        s.writeObject(None)

    def readObject(self, s):
        """ generated source for method readObject """
        self.objectLock = object()
        self.acc = AccessController.getContext()
        s.defaultReadObject()
        self.appContext = AppContext.getAppContext()
        self.coalescingEnabled = self.checkCoalescing()
        if self.componentSerializedDataVersion < 4:
            self.focusable = True
            self.isFocusTraversableOverridden = self.FOCUS_TRAVERSABLE_UNKNOWN
            self.initializeFocusTraversalKeys()
            self.focusTraversalKeysEnabled = True
        keyOrNull = None
        while None != (keyOrNull == s.readObject()):
            key = (str(keyOrNull)).intern()
            if self.componentListenerK == key:
                self.addComponentListener((s.readObject()))
            elif self.focusListenerK == key:
                self.addFocusListener((s.readObject()))
            elif self.keyListenerK == key:
                self.addKeyListener((s.readObject()))
            elif self.mouseListenerK == key:
                self.addMouseListener((s.readObject()))
            elif self.mouseMotionListenerK == key:
                self.addMouseMotionListener((s.readObject()))
            elif self.inputMethodListenerK == key:
                self.addInputMethodListener((s.readObject()))
            else:
                s.readObject()
        orient = None
        try:
            orient = s.readObject()
        except java.io.OptionalDataException as e:
            if not e.eof:
                raise (e)
        if orient != None:
            self.componentOrientation = orient
        else:
            self.componentOrientation = ComponentOrientation.UNKNOWN
        try:
            while None != (keyOrNull == s.readObject()):
                key = (str(keyOrNull)).intern()
                if self.hierarchyListenerK == key:
                    self.addHierarchyListener((s.readObject()))
                elif self.hierarchyBoundsListenerK == key:
                    self.addHierarchyBoundsListener((s.readObject()))
                else:
                    s.readObject()
        except java.io.OptionalDataException as e:
            if not e.eof:
                raise (e)
        try:
            while None != (keyOrNull == s.readObject()):
                key = (str(keyOrNull)).intern()
                if self.mouseWheelListenerK == key:
                    self.addMouseWheelListener((s.readObject()))
                else:
                    s.readObject()
        except java.io.OptionalDataException as e:
            if not e.eof:
                raise (e)
        if self.popups != None:
            npopups = len(self.popups)
            i = 0
            while i < npopups:
                popup = self.popups.elementAt(i)
                popup.parent = self
                i += 1

    def setComponentOrientation(self, o):
        """ generated source for method setComponentOrientation """
        oldValue = self.componentOrientation
        self.componentOrientation = o
        self.firePropertyChange("componentOrientation", oldValue, o)
        self.invalidateIfValid()

    def getComponentOrientation(self):
        """ generated source for method getComponentOrientation """
        return self.componentOrientation

    def applyComponentOrientation(self, orientation):
        """ generated source for method applyComponentOrientation """
        if orientation == None:
            raise NullPointerException()
        self.setComponentOrientation(orientation)

    @canBeFocusOwner.register(object)
    def canBeFocusOwner_0(self):
        """ generated source for method canBeFocusOwner_0 """
        if self.isEnabled() and self.isDisplayable() and self.isVisible() and self.isFocusable():
            return True
        return False

    def canBeFocusOwnerRecursively(self):
        """ generated source for method canBeFocusOwnerRecursively """
        if not self.canBeFocusOwner():
            return False
        with lock_for_object(self.getTreeLock()):
            if self.parent != None:
                return self.parent.canContainFocusOwner(self)
        return True

    def relocateComponent(self):
        """ generated source for method relocateComponent """
        with lock_for_object(self.getTreeLock()):
            if self.peer == None:
                return
            nativeX = self.x
            nativeY = self.y
            cont = self.getContainer()
            while cont != None and cont.isLightweight():
                nativeX += cont.x
                nativeY += cont.y
                cont = cont.getContainer()
            self.peer.setBounds(nativeX, nativeY, self.width, self.height, ComponentPeer.SET_LOCATION)

    def getContainingWindow(self):
        """ generated source for method getContainingWindow """
        return SunToolkit.getContainingWindow(self)

    @classmethod
    def initIDs(cls):
        """ generated source for method initIDs """

    accessibleContext = None

    def getAccessibleContext(self):
        """ generated source for method getAccessibleContext """
        return self.accessibleContext

    class AccessibleAWTComponent(AccessibleContext, Serializable, AccessibleComponent):
        """ generated source for class AccessibleAWTComponent """
        serialVersionUID = 642321655757800191

        def __init__(self):
            """ generated source for method __init__ """
            super(AccessibleAWTComponent, self).__init__()

        propertyListenersCount = 0
        accessibleAWTComponentHandler = None
        accessibleAWTFocusHandler = None

        class AccessibleAWTComponentHandler(ComponentListener):
            """ generated source for class AccessibleAWTComponentHandler """
            def componentHidden(self, e):
                """ generated source for method componentHidden """
                if self.accessibleContext != None:
                    self.accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, AccessibleState.VISIBLE, None)

            def componentShown(self, e):
                """ generated source for method componentShown """
                if self.accessibleContext != None:
                    self.accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, None, AccessibleState.VISIBLE)

            def componentMoved(self, e):
                """ generated source for method componentMoved """

            def componentResized(self, e):
                """ generated source for method componentResized """

        class AccessibleAWTFocusHandler(FocusListener):
            """ generated source for class AccessibleAWTFocusHandler """
            def focusGained(self, event):
                """ generated source for method focusGained """
                if self.accessibleContext != None:
                    self.accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, None, AccessibleState.FOCUSED)

            def focusLost(self, event):
                """ generated source for method focusLost """
                if self.accessibleContext != None:
                    self.accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, AccessibleState.FOCUSED, None)

        def addPropertyChangeListener(self, listener):
            """ generated source for method addPropertyChangeListener """
            if self.accessibleAWTComponentHandler == None:
                self.accessibleAWTComponentHandler = self.AccessibleAWTComponentHandler()
            if self.accessibleAWTFocusHandler == None:
                self.accessibleAWTFocusHandler = self.AccessibleAWTFocusHandler()
            __propertyListenersCount_0 = propertyListenersCount
            propertyListenersCount += 1
            if __propertyListenersCount_0 == 0:
                Component.self.addComponentListener(self.accessibleAWTComponentHandler)
                Component.self.addFocusListener(self.accessibleAWTFocusHandler)
            super(AccessibleAWTComponent, self).addPropertyChangeListener(listener)

        def removePropertyChangeListener(self, listener):
            """ generated source for method removePropertyChangeListener """
            propertyListenersCount -= 1
            if propertyListenersCount == 0:
                Component.self.removeComponentListener(self.accessibleAWTComponentHandler)
                Component.self.removeFocusListener(self.accessibleAWTFocusHandler)
            super(AccessibleAWTComponent, self).removePropertyChangeListener(listener)

        def getAccessibleName(self):
            """ generated source for method getAccessibleName """
            return accessibleName

        def getAccessibleDescription(self):
            """ generated source for method getAccessibleDescription """
            return accessibleDescription

        def getAccessibleRole(self):
            """ generated source for method getAccessibleRole """
            return AccessibleRole.AWT_COMPONENT

        def getAccessibleStateSet(self):
            """ generated source for method getAccessibleStateSet """
            return Component.self.getAccessibleStateSet()

        def getAccessibleParent(self):
            """ generated source for method getAccessibleParent """
            if accessibleParent != None:
                return accessibleParent
            else:
                parent = self.getParent()
                if isinstance(self.parent, (Accessible, )):
                    return self.parent
            return None

        def getAccessibleIndexInParent(self):
            """ generated source for method getAccessibleIndexInParent """
            return Component.self.getAccessibleIndexInParent()

        def getAccessibleChildrenCount(self):
            """ generated source for method getAccessibleChildrenCount """
            return 0

        def getAccessibleChild(self, i):
            """ generated source for method getAccessibleChild """
            return None

        def getLocale(self):
            """ generated source for method getLocale """
            return Component.self.getLocale()

        def getAccessibleComponent(self):
            """ generated source for method getAccessibleComponent """
            return self

        def getBackground(self):
            """ generated source for method getBackground """
            return Component.self.getBackground()

        def setBackground(self, c):
            """ generated source for method setBackground """
            Component.self.setBackground(c)

        def getForeground(self):
            """ generated source for method getForeground """
            return Component.self.getForeground()

        def setForeground(self, c):
            """ generated source for method setForeground """
            Component.self.setForeground(c)

        def getCursor(self):
            """ generated source for method getCursor """
            return Component.self.getCursor()

        def setCursor(self, cursor):
            """ generated source for method setCursor """
            Component.self.setCursor(cursor)

        def getFont(self):
            """ generated source for method getFont """
            return Component.self.getFont()

        def setFont(self, f):
            """ generated source for method setFont """
            Component.self.setFont(f)

        def getFontMetrics(self, f):
            """ generated source for method getFontMetrics """
            if f == None:
                return None
            else:
                return Component.self.getFontMetrics(f)

        def isEnabled(self):
            """ generated source for method isEnabled """
            return Component.self.isEnabled()

        def setEnabled(self, b):
            """ generated source for method setEnabled """
            old = Component.self.isEnabled()
            Component.self.setEnabled(b)
            if b != old:
                if self.accessibleContext != None:
                    if b:
                        self.accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, None, AccessibleState.ENABLED)
                    else:
                        self.accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, AccessibleState.ENABLED, None)

        def isVisible(self):
            """ generated source for method isVisible """
            return Component.self.isVisible()

        def setVisible(self, b):
            """ generated source for method setVisible """
            old = Component.self.isVisible()
            Component.self.setVisible(b)
            if b != old:
                if self.accessibleContext != None:
                    if b:
                        self.accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, None, AccessibleState.VISIBLE)
                    else:
                        self.accessibleContext.firePropertyChange(AccessibleContext.ACCESSIBLE_STATE_PROPERTY, AccessibleState.VISIBLE, None)

        def isShowing(self):
            """ generated source for method isShowing """
            return Component.self.isShowing()

        def contains(self, p):
            """ generated source for method contains """
            return Component.self.contains(p)

        def getLocationOnScreen(self):
            """ generated source for method getLocationOnScreen """
            with lock_for_object(Component.self.getTreeLock()):
                if Component.self.isShowing():
                    return Component.self.getLocationOnScreen()
                else:
                    return None

        def getLocation(self):
            """ generated source for method getLocation """
            return Component.self.getLocation()

        def setLocation(self, p):
            """ generated source for method setLocation """
            Component.self.setLocation(p)

        def getBounds(self):
            """ generated source for method getBounds """
            return Component.self.getBounds()

        def setBounds(self, r):
            """ generated source for method setBounds """
            Component.self.setBounds(r)

        def getSize(self):
            """ generated source for method getSize """
            return Component.self.getSize()

        def setSize(self, d):
            """ generated source for method setSize """
            Component.self.setSize(d)

        def getAccessibleAt(self, p):
            """ generated source for method getAccessibleAt """
            return None

        def isFocusTraversable(self):
            """ generated source for method isFocusTraversable """
            return Component.self.isFocusTraversable()

        def requestFocus(self):
            """ generated source for method requestFocus """
            Component.self.requestFocus()

        def addFocusListener(self, l):
            """ generated source for method addFocusListener """
            Component.self.addFocusListener(l)

        def removeFocusListener(self, l):
            """ generated source for method removeFocusListener """
            Component.self.removeFocusListener(l)

    # def getAccessibleIndexInParent(self):
    #     """ generated source for method getAccessibleIndexInParent """
    #     with lock_for_object(self.getTreeLock()):
    #         index = -1
    #         parent = self.getParent()
    #         if self.parent != None and isinstance(self.parent, (Accessible, )):
    #             ca = self.parent.getComponents()
    #             i = 0
    #             while len(ca):
    #                 if isinstance(, (Accessible, )):
    #                     index += 1
    #                 if self == ca[i]:
    #                     return index
    #                 i += 1
    #         return -1

    # def getAccessibleStateSet(self):
    #     """ generated source for method getAccessibleStateSet """
    #     with lock_for_object(self.getTreeLock()):
    #         states = AccessibleStateSet()
    #         if self.isEnabled():
    #             states.add(AccessibleState.ENABLED)
    #         if self.isFocusTraversable():
    #             states.add(AccessibleState.FOCUSABLE)
    #         if self.isVisible():
    #             states.add(AccessibleState.VISIBLE)
    #         if self.isShowing():
    #             states.add(AccessibleState.SHOWING)
    #         if self.isFocusOwner():
    #             states.add(AccessibleState.FOCUSED)
    #         if isinstance(, (Accessible, )):
    #             ac = (self).getAccessibleContext()
    #             if ac != None:
    #                 ap = ac.getAccessibleParent()
    #                 if ap != None:
    #                     pac = ap.getAccessibleContext()
    #                     if pac != None:
    #                         as_ = pac.getAccessibleSelection()
    #                         if as_ != None:
    #                             states.add(AccessibleState.SELECTABLE)
    #                             i = ac.getAccessibleIndexInParent()
    #                             if i >= 0:
    #                                 if as_.isAccessibleChildSelected(i):
    #                                     states.add(AccessibleState.SELECTED)
    #         if Component.isInstanceOf(self, "javax.swing.JComponent"):
    #             if (self).isOpaque():
    #                 states.add(AccessibleState.OPAQUE)
    #         return states

    @classmethod
    def isInstanceOf(cls, obj, className):
        """ generated source for method isInstanceOf """
        if obj == None:
            return False
        if className == None:
            return False
        cls = obj.__class__
        while cls != None:
            if cls.__name__ == className:
                return True
            cls = cls.getSuperclass()
        return False

    def areBoundsValid(self):
        """ generated source for method areBoundsValid """
        cont = self.getContainer()
        return cont == None or cont.isValid() or cont.getLayout() == None

    def applyCompoundShape(self, shape):
        """ generated source for method applyCompoundShape """
        self.checkTreeLock()
        if not self.areBoundsValid():
            if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
                self.mixingLog.fine("this = " + self + "; areBoundsValid = " + self.areBoundsValid())
            return
        if not self.isLightweight():
            peer = self.getPeer()
            if self.peer != None:
                if shape.isEmpty():
                    shape = Region.EMPTY_REGION
                if shape == getNormalShape():
                    if self.compoundShape == None:
                        return
                    self.compoundShape = None
                    self.peer.applyShape(None)
                else:
                    if shape == getAppliedShape():
                        return
                    self.compoundShape = shape
                    compAbsolute = getLocationOnWindow()
                    if self.mixingLog.isLoggable(PlatformLogger.Level.FINER):
                        self.mixingLog.fine("this = " + self + "; compAbsolute=" + compAbsolute + "; shape=" + shape)
                    self.peer.applyShape(shape.getTranslatedRegion(-compAbsolute.x, -compAbsolute.y))

    def getAppliedShape(self):
        """ generated source for method getAppliedShape """
        self.checkTreeLock()
        return getNormalShape() if (self.compoundShape == None or self.isLightweight()) else self.compoundShape

    def getLocationOnWindow(self):
        """ generated source for method getLocationOnWindow """
        self.checkTreeLock()
        curLocation = self.getLocation()
        parent = self.getContainer()
        while parent != None and not (isinstance(parent, (Window, ))):
            curLocation.x += parent.getX()
            curLocation.y += parent.getY()
            parent = parent.getContainer()
        return curLocation

    def getNormalShape(self):
        """ generated source for method getNormalShape """
        self.checkTreeLock()
        compAbsolute = self.getLocationOnWindow()
        return Region.getInstanceXYWH(compAbsolute.x, compAbsolute.y, self.getWidth(), self.getHeight())

    def getOpaqueShape(self):
        """ generated source for method getOpaqueShape """
        self.checkTreeLock()
        if self.mixingCutoutRegion != None:
            return self.mixingCutoutRegion
        else:
            return self.getNormalShape()

    def getSiblingIndexAbove(self):
        """ generated source for method getSiblingIndexAbove """
        self.checkTreeLock()
        parent = self.getContainer()
        if parent == None:
            return -1
        nextAbove = parent.getComponentZOrder(self) - 1
        return -1 if nextAbove < 0 else nextAbove

    def getHWPeerAboveMe(self):
        """ generated source for method getHWPeerAboveMe """
        self.checkTreeLock()
        cont = self.getContainer()
        indexAbove = self.getSiblingIndexAbove()
        while cont != None:
            i = indexAbove
            while i > -1:
                comp = cont.getComponent(i)
                if comp != None and comp.isDisplayable() and not comp.isLightweight():
                    return comp.getPeer()
                i -= 1
            if not cont.isLightweight():
                break
            indexAbove = cont.getSiblingIndexAbove()
            cont = cont.getContainer()
        return None

    def getSiblingIndexBelow(self):
        """ generated source for method getSiblingIndexBelow """
        self.checkTreeLock()
        parent = self.getContainer()
        if parent == None:
            return -1
        nextBelow = parent.getComponentZOrder(self) + 1
        return -1 if nextBelow >= parent.getComponentCount() else nextBelow

    def isNonOpaqueForMixing(self):
        """ generated source for method isNonOpaqueForMixing """
        return self.mixingCutoutRegion != None and self.mixingCutoutRegion.isEmpty()

    def calculateCurrentShape(self):
        """ generated source for method calculateCurrentShape """
        self.checkTreeLock()
        s = self.getNormalShape()
        if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
            self.mixingLog.fine("this = " + self + "; normalShape=" + s)
        if self.getContainer() != None:
            comp = self
            cont = comp.getContainer()
            while cont != None:
                index = comp.getSiblingIndexAbove()
                while index != -1:
                    c = cont.getComponent(index)
                    if c.isLightweight() and c.isShowing():
                        s = s.getDifference(c.getOpaqueShape())
                    index -= 1
                if cont.isLightweight():
                    s = s.getIntersection(cont.getNormalShape())
                else:
                    break
                comp = cont
                cont = cont.getContainer()
        if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
            self.mixingLog.fine("currentShape=" + s)
        return s

    def applyCurrentShape(self):
        """ generated source for method applyCurrentShape """
        self.checkTreeLock()
        if not self.areBoundsValid():
            if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
                self.mixingLog.fine("this = " + self + "; areBoundsValid = " + self.areBoundsValid())
            return
        if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
            self.mixingLog.fine("this = " + self)
        self.applyCompoundShape(self.calculateCurrentShape())

    def subtractAndApplyShape(self, s):
        """ generated source for method subtractAndApplyShape """
        self.checkTreeLock()
        if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
            self.mixingLog.fine("this = " + self + "; s=" + s)
        self.applyCompoundShape(self.getAppliedShape().getDifference(s))

    def applyCurrentShapeBelowMe(self):
        """ generated source for method applyCurrentShapeBelowMe """
        self.checkTreeLock()
        parent = self.getContainer()
        if parent != None and parent.isShowing():
            parent.recursiveApplyCurrentShape(self.getSiblingIndexBelow())
            parent2 = parent.getContainer()
            while not parent.isOpaque() and parent2 != None:
                parent2.recursiveApplyCurrentShape(parent.getSiblingIndexBelow())
                parent = parent2
                parent2 = parent.getContainer()

    def subtractAndApplyShapeBelowMe(self):
        """ generated source for method subtractAndApplyShapeBelowMe """
        self.checkTreeLock()
        parent = self.getContainer()
        if parent != None and self.isShowing():
            opaqueShape = self.getOpaqueShape()
            parent.recursiveSubtractAndApplyShape(opaqueShape, self.getSiblingIndexBelow())
            parent2 = parent.getContainer()
            while not parent.isOpaque() and parent2 != None:
                parent2.recursiveSubtractAndApplyShape(opaqueShape, parent.getSiblingIndexBelow())
                parent = parent2
                parent2 = parent.getContainer()

    def mixOnShowing(self):
        """ generated source for method mixOnShowing """
        with lock_for_object(self.getTreeLock()):
            if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
                self.mixingLog.fine("this = " + self)
            if not isMixingNeeded():
                return
            if self.isLightweight():
                self.subtractAndApplyShapeBelowMe()
            else:
                self.applyCurrentShape()

    def mixOnHiding(self, isLightweight):
        """ generated source for method mixOnHiding """
        with lock_for_object(self.getTreeLock()):
            if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
                self.mixingLog.fine("this = " + self + "; isLightweight = " + isLightweight)
            if not isMixingNeeded():
                return
            if isLightweight:
                self.applyCurrentShapeBelowMe()

    def mixOnReshaping(self):
        """ generated source for method mixOnReshaping """
        with lock_for_object(self.getTreeLock()):
            if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
                self.mixingLog.fine("this = " + self)
            if not isMixingNeeded():
                return
            if self.isLightweight():
                self.applyCurrentShapeBelowMe()
            else:
                self.applyCurrentShape()

    def mixOnZOrderChanging(self, oldZorder, newZorder):
        """ generated source for method mixOnZOrderChanging """
        with lock_for_object(self.getTreeLock()):
            becameHigher = newZorder < oldZorder
            parent = self.getContainer()
            if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
                self.mixingLog.fine("this = " + self + "; oldZorder=" + oldZorder + "; newZorder=" + newZorder + "; parent=" + self.parent)
            if not isMixingNeeded():
                return
            if self.isLightweight():
                if becameHigher:
                    if self.parent != None and self.isShowing():
                        self.parent.recursiveSubtractAndApplyShape(self.getOpaqueShape(), self.getSiblingIndexBelow(), oldZorder)
                else:
                    if self.parent != None:
                        self.parent.recursiveApplyCurrentShape(oldZorder, newZorder)
            else:
                if becameHigher:
                    self.applyCurrentShape()
                else:
                    if self.parent != None:
                        shape = self.getAppliedShape()
                        index = oldZorder
                        while index < newZorder:
                            c = self.parent.getComponent(index)
                            if c.isLightweight() and c.isShowing():
                                shape = shape.getDifference(c.getOpaqueShape())
                            index += 1
                        self.applyCompoundShape(shape)

    def mixOnValidating(self):
        """ generated source for method mixOnValidating """

    def isMixingNeeded(self):
        """ generated source for method isMixingNeeded """
        if SunToolkit.getSunAwtDisableMixing():
            if self.mixingLog.isLoggable(PlatformLogger.Level.FINEST):
                self.mixingLog.finest("this = " + self + "; Mixing disabled via sun.awt.disableMixing")
            return False
        if not self.areBoundsValid():
            if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
                self.mixingLog.fine("this = " + self + "; areBoundsValid = " + self.areBoundsValid())
            return False
        window = self.getContainingWindow()
        if window != None:
            if not window.hasHeavyweightDescendants() or not window.hasLightweightDescendants() or window.isDisposing():
                if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
                    self.mixingLog.fine("containing window = " + window + "; has h/w descendants = " + window.hasHeavyweightDescendants() + "; has l/w descendants = " + window.hasLightweightDescendants() + "; disposing = " + window.isDisposing())
                return False
        else:
            if self.mixingLog.isLoggable(PlatformLogger.Level.FINE):
                self.mixingLog.fine("this = " + self + "; containing window is null")
            return False
        return True

    def updateZOrder(self):
        """ generated source for method updateZOrder """
        self.peer.setZOrder(self.getHWPeerAboveMe())

# Component.#      * Indicates whether focus traversal keys are enabled for this Component.

