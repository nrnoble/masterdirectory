#!/usr/bin/env python
""" generated source for module Animator """
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
#  * @(#)Animator.java   1.99.1 08/12/08
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
#  Bug fix 12-Sep-07 (ESR, JTFBug 2007-013)
#    1. Fixed bug in handling of ChangeListener compatibility.
# package: acm.util
#  Class: Animator 
# 
#  * This class extends <code>Thread</code> to provide several features that make it
#  * easier to build animations.  These features include a <code>pause</code>
#  * method that does not raise an exception and a <code>requestTermination</code>
#  * method that signals that the execution of this thread should stop at its
#  * next opportunity.  It also includes hooks to support a start/stop/single-step
#  * model for algorithm animation.
#  
class Animator(Thread):
    """ generated source for class Animator """
    #  Constant: INITIAL 
    #  Constant indicating that the animator has not yet started. 
    INITIAL = 0

    #  Constant: RUNNING 
    #  Constant indicating that the animator is running. 
    RUNNING = 1

    #  Constant: STEPPING 
    #  Constant indicating that the animator is running in single-step mode. 
    STEPPING = 2

    #  Constant: CALLING 
    #  Constant indicating that the animator is running until the end of the current call. 
    CALLING = 3

    #  Constant: STOPPING 
    #  Constant indicating that the animator should stop at the next trace point. 
    STOPPING = 4

    #  Constant: STOPPED 
    #  Constant indicating that the animator is suspended waiting for restart. 
    STOPPED = 5

    #  Constant: FINISHED 
    #  Constant indicating that the animator has finished its <code>run</code> method. 
    FINISHED = 6

    #  Constant: TERMINATING 
    #  Constant indicating that the animator has been asked to terminate. 
    TERMINATING = 7

    #  Constructor: Animator() 
    # 
    #  * Creates a new <code>Animator</code> object.
    #  *
    #  * @usage Animator animator = new Animator();
    #  
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(Animator, self).__init__()
        initAnimator()

    #  Constructor: Animator(group) 
    # 
    #  * Creates a new <code>Animator</code> object and assigns it to the
    #  * specified thread group.
    #  *
    #  * @usage Animator animator = new Animator(group);
    #  * @param group The <code>ThreadGroup</code> to which the new thread is assigned
    #  * @noshow
    #  
    @__init__.register(object, ThreadGroup)
    def __init___0(self, group):
        """ generated source for method __init___0 """
        super(Animator, self).__init__(None)
        initAnimator()

    #  Constructor: Animator(runnable) 
    # 
    #  * Creates a new <code>Animator</code> object with the specified runnable object.
    #  *
    #  * @usage Animator animator = new Animator(runnable);
    #  * @param runnable Any object that implements the <code>Runnable</code> interface
    #  * @noshow
    #  
    @__init__.register(object, Runnable)
    def __init___1(self, runnable):
        """ generated source for method __init___1 """
        super(Animator, self).__init__(runnable)
        initAnimator()

    #  Constructor: Animator(group, runnable) 
    # 
    #  * Creates a new <code>Animator</code> object with the specified runnable object
    #  * and assigns it to the specified thread group.
    #  *
    #  * @usage Animator animator = new Animator(group, runnable);
    #  * @param group The <code>ThreadGroup</code> to which the new thread is assigned
    #  * @param runnable Any object that implements the <code>Runnable</code> interface
    #  * @noshow
    #  
    @__init__.register(object, ThreadGroup, Runnable)
    def __init___2(self, group, runnable):
        """ generated source for method __init___2 """
        super(Animator, self).__init__(runnable)
        initAnimator()

    #  Method: run() 
    # 
    #  * Specifies the code for the animator.  Subclasses should override this
    #  * method with the code they need to execute to implement the animator's
    #  * function.
    #  
    def run(self):
        """ generated source for method run """
        #  Empty 

    #  Method: getAnimatorState() 
    # 
    #  * Returns the state of the animator. This value will be one of the constants
    #  * <a href="#INITIAL"><code>INITIAL</code></a>,
    #  * <a href="#RUNNING"><code>RUNNING</code></a>,
    #  * <a href="#STEPPING"><code>STEPPING</code></a>,
    #  * <a href="#CALLING"><code>CALLING</code></a>,
    #  * <a href="#STOPPING"><code>STOPPING</code></a>,
    #  * <a href="#STOPPED"><code>STOPPED</code></a>,
    #  * <a href="#FINISHED"><code>FINISHED</code></a>, or
    #  * <a href="#TERMINATING"><code>TERMINATING</code></a>,
    #  * as defined in this class.
    #  *
    #  * @usage int state = animator.getAnimatorState();
    #  * @return The current state of the animator
    #  
    def getAnimatorState(self):
        """ generated source for method getAnimatorState """
        return animatorState

    #  Method: pause(milliseconds) 
    # 
    #  * Delays this thread for the specified time, which is expressed in
    #  * milliseconds.  Unlike <code>Thread.sleep</code>, this method never
    #  * throws an exception.
    #  *
    #  * @usage animator.pause(milliseconds);
    #  * @param milliseconds The sleep time in milliseconds
    #  
    def pause(self, milliseconds):
        """ generated source for method pause """
        if animatorState == self.TERMINATING:
            terminate()
        JTFTools.pause(milliseconds)

    #  Method: startAction() 
    # 
    #  * Triggers a <code>"start"</code> action, as if the <code>Start</code> button
    #  * is pushed.
    #  *
    #  * @usage animator.startAction();
    #  
    def startAction(self):
        """ generated source for method startAction """
        start(self.RUNNING)

    #  Method: stopAction() 
    # 
    #  * Triggers a <code>"stop"</code> action, as if the <code>Stop</code> button
    #  * is pushed.
    #  *
    #  * @usage animator.stopAction();
    #  
    def stopAction(self):
        """ generated source for method stopAction """
        if animatorState == self.RUNNING:
            pass
        elif animatorState == self.STEPPING:
            pass
        elif animatorState == self.CALLING:
            animatorState = self.STOPPING
        else:

    #  Method: stepAction() 
    # 
    #  * Triggers a <code>"step"</code> action, as if the <code>Step</code> button
    #  * is pushed.
    #  *
    #  * @usage animator.stepAction();
    #  
    def stepAction(self):
        """ generated source for method stepAction """
        start(self.STEPPING)

    #  Method: callAction() 
    # 
    #  * Triggers a <code>"call"</code> action, as if the <code>Call</code> button
    #  * is pushed.
    #  *
    #  * @usage animator.callAction();
    #  
    def callAction(self):
        """ generated source for method callAction """
        callDepth = currentDepth
        start(self.CALLING)

    #  Method: buttonAction(actionCommand) 
    # 
    #  * Triggers an action for the action specified by the
    #  * action command.
    #  *
    #  * @usage boolean ok = animator.buttonAction(actionCommand);
    #  * @param actionCommand The action command from the button
    #  * @return <code>true</code> if the action command is recognized
    #  
    def buttonAction(self, actionCommand):
        """ generated source for method buttonAction """
        if actionCommand == "Start":
            self.startAction()
        elif actionCommand == "Stop":
            self.stopAction()
        elif actionCommand == "Step":
            self.stepAction()
        elif actionCommand == "Call":
            self.callAction()
        else:
            return False
        return True

    #  Method: setSpeed(speed) 
    # 
    #  * Sets the speed parameter for the animator.  The speed is a <code>double</code>
    #  * between 0.0 and 1.0, for which 0.0 is very slow and 1.0 is as fast as the
    #  * system can manage.
    #  *
    #  * @usage animator.setSpeed(speed);
    #  * @param speed A double between 0.0 (slow) and 1.0 (fast)
    #  
    def setSpeed(self, speed):
        """ generated source for method setSpeed """
        animatorSpeed = speed
        if isinstance(speedBar, (JSlider, )):
            slider = speedBar
            min = slider.getMinimum()
            max = slider.getMaximum()
            slider.setValue(int(round(min + speed * (max - min))))
        elif isinstance(speedBar, (JScrollBar, )):
            scrollBar = speedBar
            min = scrollBar.getMinimum()
            max = scrollBar.getMaximum()
            scrollBar.setValue(int(round(min + speed * (max - min))))

    #  Method: getSpeed() 
    # 
    #  * Returns the speed parameter for the animator.  The speed is a <code>double</code>
    #  * between 0.0 and 1.0, for which 0.0 is very slow and 1.0 is as fast as the
    #  * system can manage.
    #  *
    #  * @usage double speed = animator.getSpeed();
    #  * @return A double between 0.0 (slow) and 1.0 (fast)
    #  
    def getSpeed(self):
        """ generated source for method getSpeed """
        return animatorSpeed

    #  Method: trace() 
    # 
    #  * Checks the state of the animator and executes any actions have been requested.
    #  *
    #  * @usage animator.trace();
    #  
    @overloaded
    def trace(self):
        """ generated source for method trace """
        self.trace(0)

    #  Method: trace(depth) 
    # 
    #  * Checks the state of the animator and executes any actions have been requested
    #  * to occur at the specified call stack depth.  This method is useful only to
    #  * clients who are making use of the <code>Call</code> button functionality.
    #  *
    #  * @usage animator.trace(depth);
    #  * @param depth The current call stack depth.
    #  
    @trace.register(object, int)
    def trace_0(self, depth):
        """ generated source for method trace_0 """
        if Thread.currentThread() != self:
            raise ErrorException("trace() can be called only by the animator thread itself")
        currentDepth = depth
        if animatorState == self.RUNNING:
            delay()
        elif animatorState == self.STOPPING:
            pass
        elif animatorState == self.STEPPING:
            breakpoint()
        elif animatorState == self.CALLING:
            if callDepth < currentDepth:
                delay()
            else:
                breakpoint()
        elif animatorState == self.TERMINATING:
            terminate()

    #  Method: breakpoint() 
    # 
    #  * Suspends the animator until one of the restart actions is triggered.
    #  *
    #  * @usage animator.breakpoint();
    #  
    def breakpoint(self):
        """ generated source for method breakpoint """
        if Thread.currentThread() != self:
            raise ErrorException("breakpoint() can be called only by the animator thread itself")
        animatorState = self.STOPPED
        breakHook()
        suspendAnimator()

    # /
    #  Implementation notes: delay()                                              
    #  -----------------------------                                              
    #  The delay method turns out to be tricky to code.  The intent is that the   
    #  speed value should suggest a smoothly varying speed.   Unfortunately,      
    #  implementing delay so that it "feels right" requires a nonlinear approach. 
    #  This implementation varies the speed steeply from 0.0 to 0.25 and then     
    #  quadratically from 0.25 to 0.8.  From there it interposes delays in only   
    #  a fraction of the calls to delay.                                          
    # /
    #  Method: delay() 
    # 
    #  * Delays the calling thread according to the speed.
    #  *
    #  * @usage animator.delay();
    #  
    def delay(self):
        """ generated source for method delay """
        yield_ = True
        delay = 0
        if animatorSpeed < 0.25:
            delay = SLOW_DELAY + animatorSpeed / 0.25 * (CLIP_DELAY - SLOW_DELAY)
        elif animatorSpeed < 0.9:
            delay = CLIP_DELAY + sqrt((animatorSpeed - 0.25) / 0.65) * (FAST_DELAY - CLIP_DELAY)
        else:
            if int((animatorSpeed * 99.99 - 90)) == 0:
                yield_ = True
            elif int((animatorSpeed * 99.99 - 90)) == 1:
                yield_ = delayCount % 10 != 0
            elif int((animatorSpeed * 99.99 - 90)) == 2:
                yield_ = delayCount % 7 != 0
            elif int((animatorSpeed * 99.99 - 90)) == 3:
                yield_ = delayCount % 5 != 0
            elif int((animatorSpeed * 99.99 - 90)) == 4:
                yield_ = delayCount % 3 != 0
            elif int((animatorSpeed * 99.99 - 90)) == 5:
                yield_ = delayCount % 2 == 0
            elif int((animatorSpeed * 99.99 - 90)) == 6:
                yield_ = delayCount % 3 == 0
            elif int((animatorSpeed * 99.99 - 90)) == 7:
                yield_ = delayCount % 4 == 0
            elif int((animatorSpeed * 99.99 - 90)) == 8:
                yield_ = delayCount % 6 == 0
            elif int((animatorSpeed * 99.99 - 90)) == 9:
                yield_ = False
            delayCount = (delayCount + 1) % (2 * 2 * 3 * 5 * 7)
        if yield_:
            delayHook()
            JTFTools.pause(delay)

    #  Public method: registerSpeedBar(slider) 
    # 
    #  * Registers the specified slider as the delay controller for the animator.
    #  *
    #  * @usage registerSpeedBar(slider);
    #  * @param slider The slider which will serve as the speed bar for this animator
    #  
    @overloaded
    def registerSpeedBar(self, slider):
        """ generated source for method registerSpeedBar """
        SpeedBarListener.register(self, slider)
        speedBar = slider

    #  Public method: registerSpeedBar(scrollBar) 
    # 
    #  * Registers the specified scroll bar as the delay controller for the animator.
    #  *
    #  * @usage registerSpeedBar(scrollBar);
    #  * @param scrollBar The scroll bar which will serve as the speed bar for this animator
    #  
    @registerSpeedBar.register(object, JScrollBar)
    def registerSpeedBar_0(self, scrollBar):
        """ generated source for method registerSpeedBar_0 """
        SpeedBarListener.register(self, scrollBar)
        speedBar = scrollBar

    #  Public method: getSpeedBar() 
    # 
    #  * Returns the speed bar for the animator, if any.  The speed bar can be a
    #  * <code>JSlider</code> or a <code>JScrollBar</code>; it is the caller's
    #  * responsibility to cast the result to the appropriate class.
    #  *
    #  * @return The speed bar, or <code>null</code> if none exists
    #  
    def getSpeedBar(self):
        """ generated source for method getSpeedBar """
        return speedBar

    #  Method: requestTermination() 
    # 
    #  * Signals the <code>Animator</code> that it should stop running at the
    #  * next available opportunity, which is when the client next calls
    #  * <code>pause</code> or <code>checkForTermination</code>.  Making this
    #  * check at well-managed times makes it possible for the client to
    #  * ensure that objects are left in a consistent state and thereby
    #  * avoids the problems that led Sun to deprecate <code>Thread.stop</code>.
    #  *
    #  * @usage requestTermination();
    #  
    def requestTermination(self):
        """ generated source for method requestTermination """
        animatorState = self.TERMINATING

    #  Method: checkForTermination() 
    # 
    #  * Checks to see whether this <code>Animator</code> has been asked
    #  * to terminate.  If so, the <code>Animator</code> stops running,
    #  * and the call never returns.  If not, other threads are given a
    #  * chance to run, after which this <code>Animator</code> will return
    #  * to the caller.
    #  *
    #  * @usage checkForTermination();
    #  
    def checkForTermination(self):
        """ generated source for method checkForTermination """
        if animatorState == self.TERMINATING:
            terminate()
        else:
            yield_()

    #  Static method: shutdown(applet) 
    # 
    #  * Destroys all animator threads started by the specified applet.  This method
    #  * ensures that applet cleanup occurs in browsers that refuse to terminate an
    #  * applet that still has threads running.
    #  *
    #  * @param applet The applet that is ending its execution
    #  * @noshow
    #  
    @classmethod
    def shutdown(cls, applet):
        """ generated source for method shutdown """
        try:
            threadClass = Class.forName("java.lang.Thread")
            stop = threadClass.getMethod("stop", [None] * 0)
            args = [None] * 0
            list_ = animatorTable.get(applet)
            if list_ != None:
                animatorTable.remove(applet)
                nThreads = len(list_)
                i = 0
                while i < nThreads:
                    t = list_.get(i)
                    stop.invoke(t, args)
                    i += 1
        except Exception as ex:
            pass
            #  Empty 

    #  Hook method: delayHook() 
    # 
    #  * This method is called before the animator enters a timing delay.
    #  * Subclasses should override this method if they need to perform some
    #  * kind of action at this point, such as updating the display.
    #  
    def delayHook(self):
        """ generated source for method delayHook """
        #  Empty 

    #  Hook method: breakHook() 
    # 
    #  * This method is called before the animator executes a breakpoint.
    #  * Subclasses should override this method if they need to perform
    #  * some kind of action at this point, such as updating the display.
    #  
    def breakHook(self):
        """ generated source for method breakHook """
        #  Empty 

    #  Hook method: resumeHook() 
    # 
    #  * This method is called before the animator starts or restarts after
    #  * a breakpoint.  Subclasses should override this method if they need
    #  * to perform some kind of action at this point.
    #  
    def resumeHook(self):
        """ generated source for method resumeHook """
        #  Empty 

    #  Hook method: controllerHook() 
    # 
    #  * This method is called before the animator changes state in a way
    #  * that might interest a controller.  Subclasses will typically override
    #  * this hook to update the enabled status of buttons and menu items.
    #  
    def controllerHook(self):
        """ generated source for method controllerHook """
        #  Empty 

    #  Overridden method: start() 
    # 
    #  * Starts the thread.  The only difference in this method is that it
    #  * also sets the state.
    #  *
    #  * @usage animator.start();
    #  
    @overloaded
    def start(self):
        """ generated source for method start """
        self.start(self.RUNNING)

    #  Private method: initAnimator() 
    # 
    #  * Makes sure that this thread inherits the applet identity of its creator, if any.
    #  
    def initAnimator(self):
        """ generated source for method initAnimator """
        applet = JTFTools.getApplet()
        if applet != None:
            JTFTools.registerApplet(applet, self)
            list_ = animatorTable.get(applet)
            if list_ == None:
                list_ = ArrayList()
                animatorTable.put(applet, list_)
            list_.add(self)

    #  Private method: start(state) 
    # 
    #  * Restarts the animator in the specified state.
    #  
    @start.register(object, int)
    def start_0(self, state):
        """ generated source for method start_0 """
        if animatorState == self.INITIAL:
            pass
        elif animatorState == self.FINISHED:
            animatorState = state
            self.resumeHook()
            self.controllerHook()
            super(Animator, self).start()
        elif animatorState == self.STOPPED:
            animatorState = state
            self.resumeHook()
            self.controllerHook()
            resumeAnimator()
        else:

    #  Private method: suspendAnimator() 
    # 
    #  * Suspends the animator thread pending a later restart.
    #  
    @synchronized
    def suspendAnimator(self):
        """ generated source for method suspendAnimator """
        resumed = False
        while not resumed:
            try:
                wait()
            except InterruptedException as e:
                pass
                #  Empty 

    #  Private method: resumeAnimator() 
    # 
    #  * Resumes the animator where it left off.
    #  
    @synchronized
    def resumeAnimator(self):
        """ generated source for method resumeAnimator """
        resumed = True
        notifyAll()

    #  Private method: terminate() 
    # 
    #  * Terminates the animator by throwing a <code>ThreadDeath</code> exception.
    #  
    def terminate(self):
        """ generated source for method terminate """
        if Thread.currentThread() == self:
            raise ThreadDeath()
        else:
            raise ErrorException("Illegal call to terminate")

    #  Private constants 
    SLOW_DELAY = 1000.0
    CLIP_DELAY = 200.0
    FAST_DELAY = 0.0

    #  Static table of animator threads stored by applet 
    animatorTable = HashMap()

    #  Private instance variables 
    animatorState = INITIAL
    currentDepth = 0
    callDepth = 0
    delayCount = 0
    animatorSpeed = 0.5
    speedBar = None
    resumed = bool()

#  Private class: SpeedBarListener 
# 
#  * This class acts as a generic listener to any kind of speed bar.  The
#  * two principal models are <code>JSlider</code> or a <code>JScrollBar</code>,
#  * but the listener can be anything that implements the methods <code>getValue</code>,
#  * <code>getMinimum</code>, and <code>getMaximum</code> along with either
#  * <code>addChangeListener</code> or <code>addAdjustmentListener</code>.
#  * The extra generality is not really important here.  The key is to allow
#  * both scrollbars and sliders.
#  
class SpeedBarListener(AdjustmentListener, ChangeListener):
    """ generated source for class SpeedBarListener """
    #  Static method: register(animator, speedBar) 
    # 
    #  * Registers the speed bar as the delay controller for the animator.
    #  
    @classmethod
    def register(cls, animator, speedBar):
        """ generated source for method register """
        listener = SpeedBarListener()
        listener.animator = animator
        listener.speedBar = speedBar
        speedBarClass = speedBar.__class__
        addListener = lookForMethod(speedBarClass, "addAdjustmentListener")
        if addListener == None:
            addListener = lookForMethod(speedBarClass, "addChangeListener")
        if addListener == None:
            addListener = lookForMethod(speedBarClass, "addChangeListener")
        try:
            listener.getValue = speedBarClass.getMethod("getValue", [None] * 0)
            listener.getMinimum = speedBarClass.getMethod("getMinimum", [None] * 0)
            listener.getMaximum = speedBarClass.getMethod("getMaximum", [None] * 0)
            args = [listener]
            addListener.invoke(speedBar, args)
        except Exception as ex:
            raise ErrorException("Illegal speed bar object")
        listener.setSpeed()

    #  Method: adjustmentValueChanged(e) 
    # 
    #  * Indicates that an adjustment value has changed.  Implements AdjustmentListener.
    #  
    def adjustmentValueChanged(self, e):
        """ generated source for method adjustmentValueChanged """
        if e != e:
            #  Avoid unused parameter warning 
        setSpeed()

    #  Method: stateChanged(e) 
    # 
    #  * Indicates that a change has occurred in a slider.  Implements ChangeListener.
    #  
    def stateChanged(self, e):
        """ generated source for method stateChanged """
        if e != e:
            #  Avoid unused parameter warning 
        setSpeed()

    #  Method: setSpeed() 
    # 
    #  * Sets the speed of the animator according to the speed bar.
    #  
    def setSpeed(self):
        """ generated source for method setSpeed """
        try:
            min = (int(getMinimum.invoke(speedBar, [None] * 0))).intValue()
            max = (int(getMaximum.invoke(speedBar, [None] * 0))).intValue()
            value = (int(getValue.invoke(speedBar, [None] * 0))).intValue()
            fraction = float((value - min)) / (max - min)
            animator.setSpeed(fraction)
        except Exception as ex:
            raise ErrorException(ex)

    #  Private static method: lookForMethod(speedBarClass, methodName) 
    # 
    #  * Looks for a method in the class with the appropriate name.
    #  
    @classmethod
    def lookForMethod(cls, speedBarClass, methodName):
        """ generated source for method lookForMethod """
        methods = speedBarClass.getMethods()
        i = 0
        while len(methods):
            if methodName == methods[i].__name__:
                return methods[i]
            i += 1
        return None

    animator = None
    speedBar = None
    getValue = None
    getMinimum = None
    getMaximum = None

Animator.#  * @usage Animator.shutdown(applet);

