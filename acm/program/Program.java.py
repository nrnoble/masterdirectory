#!/usr/bin/env python
""" generated source for module Program """
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
#  * @(#)Program.java   1.99.1 08/12/08
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
#  Bug fix 30-Jan-07 (ESR, JTFBug 2007-002)
#    1. Change default in getCommandLine to behave as if Linux.
#    2. If environment is headless, substitute a CommandLineProgram.
# 
#  Feature enhancement 2-Mar-07 (ESR)
#    1. Added menu option to export the program as an applet.
#    2. Added menu option to submit the program via email.
# 
#  Bug fix 8-May-07 (ESR, JTFBug 2007-007)
#    1. Fixed significant bug introduced by JDK 1.6 in which it is no
#       longer possible to display a JApplet as a component.
# 
#  Code cleanup 28-May-07 (ESR)
#    1. Added generic type tags.
#    2. Rewrote code for handling command-line arguments.
#    3. Repackaged the ButtonLike interface.
#    4. Added setInputModel, setOutputModel, and setDialog for symmetry
# 
#  Bug fix 10-Sep-07 (ESR, JTFBug 2007-012)
#    1. Fixed deadlock bug arising from change to thread handling in JDK 1.6.
# 
#  Code cleanup 10-May-08 (ESR)
#    1. Changed code to account for introduction of CommandLineProgram class.
# 
#  Bug fix 21-May-08 (ESR, JTFBug 2008-002)
#    1. Fixed the logic for isAppletMode.
# 
#  Code cleanup 21-May-08 (ESR)
#    1. Changed factory method for the menu bar to pass the program.
#    2. Redesigned other code features to account for redesign of the
#       ProgramMenuBar class.
# 
#  Bug fix 10-Jun-08 (ESR, JTFBug 2008-003)
#    1. Fixed serious bug caused by overriding the definitions of
#       getWidth and getHeight (which was, in retrospect, a poor design).
#       To avoid requiring changes to client code, the implementation now
#       checks to see whether these methods have been called from inside
#       the java package hierarchy and, if so, maintains their traditional
#       semantics.
# package: acm.program
#  Class: Program 
# 
#  * This class is the superclass for all executable
#  * programs in the <code>acm.program</code> package.  Its principal
#  * role is to unify the concepts of applets and applications in a single
#  * class, although it also provides applications with many other useful
#  * facilities not traditionally available in applications.
#  *
#  * <p>In many programming environments, objects that are specific instances
#  * of a <code>Program</code> subclass will run automatically without any
#  * special action on your part.  For maximum portability, you might want
#  * to define a static <code>main</code> method as described in the comments
#  * for the standard implementation of <a href="#main(String[])"><code>main</code></a>.
#  
class Program(JApplet, IOModel, Runnable, MouseListener, MouseMotionListener, KeyListener, ActionListener):
    """ generated source for class Program """
    #  Constant specifying the north edge of the container 
    NORTH = BorderLayout.NORTH

    #  Constant specifying the south edge of the container 
    SOUTH = BorderLayout.SOUTH

    #  Constant specifying the east edge of the container 
    EAST = BorderLayout.EAST

    #  Constant specifying the west edge of the container 
    WEST = BorderLayout.WEST

    #  Constant specifying the center of the container 
    CENTER = BorderLayout.CENTER

    #  Default constructor: Program 
    # 
    #  * This code initializes the program data structures.
    #  
    def __init__(self):
        """ generated source for method __init__ """
        super(Program, self).__init__()
        JTFTools.registerApplet(self)
        appletMode = checkForAppletMode()
        shown = False
        parameterTable = None
        finalizers = ArrayList()
        myTitle = getClass().__name__
        myTitle = myTitle.substring(myTitle.lastIndexOf(".") + 1)
        appletStub = ProgramAppletStub(self)
        setAppletStub(appletStub)
        initContentPane(getContentPane())
        setVisible(False)
        setConsole(createConsole())
        myDialog = createDialogIO()
        myDialog.setAssociatedConsole(myConsole)
        myMenuBar = createMenuBar()
        myConsole.setMenuBar(myMenuBar)

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

    #  Method: print(value) 
    # 
    #  * Displays the argument value on the console, leaving the cursor at the end of
    #  * the output.  The <code>print</code> method is overloaded so that
    #  * <code>value</code> can be of any type.
    #  *
    #  * @usage program.print(value);
    #  * @param value The value to be displayed
    #  
    @overloaded
    def print_(self, value):
        """ generated source for method print_ """
        getOutputModel().print_(value)

    # 
    #  * Makes sure that <code>print</code> can display a <code>boolean</code>.
    #  * @noshow
    #  
    @print_.register(object, bool)
    def print__0(self, x):
        """ generated source for method print__0 """
        self.print_("" + x)

    # 
    #  * Makes sure that <code>print</code> can display a <code>char</code>.
    #  * @noshow
    #  
    @print_.register(object, str)
    def print__1(self, x):
        """ generated source for method print__1 """
        self.print_("" + x)

    # 
    #  * Makes sure that <code>print</code> can display a <code>double</code>.
    #  * @noshow
    #  
    @print_.register(object, float)
    def print__2(self, x):
        """ generated source for method print__2 """
        self.print_("" + x)

    # 
    #  * Makes sure that <code>print</code> can display a <code>float</code>.
    #  * @noshow
    #  
    @print_.register(object, float)
    def print__3(self, x):
        """ generated source for method print__3 """
        self.print_("" + x)

    # 
    #  * Makes sure that <code>print</code> can display an <code>int</code>.
    #  * @noshow
    #  
    @print_.register(object, int)
    def print__4(self, x):
        """ generated source for method print__4 """
        self.print_("" + x)

    # 
    #  * Makes sure that <code>print</code> can display a <code>long</code>.
    #  * @noshow
    #  
    @print_.register(object, long)
    def print__5(self, x):
        """ generated source for method print__5 """
        self.print_("" + x)

    # 
    #  * Makes sure that <code>print</code> can display an <code>Object</code>.
    #  * @noshow
    #  
    @print_.register(object, object)
    def print__6(self, x):
        """ generated source for method print__6 """
        self.print_("" + x)

    #  Method: println() 
    # 
    #  * Advances the console cursor to the beginning of the next line.
    #  *
    #  * @usage program.println();
    #  
    @overloaded
    def println(self):
        """ generated source for method println """
        getOutputModel().println()

    #  Method: println(value) 
    # 
    #  * Displays the argument value on the console and then advances the cursor
    #  * to the beginning of the next line.  The <code>println</code> method is
    #  * overloaded so that <code>value</code> can be of any type.
    #  *
    #  * @usage program.println(value);
    #  * @param value The value to be displayed
    #  
    @println.register(object, str)
    def println_0(self, value):
        """ generated source for method println_0 """
        getOutputModel().println(value)

    # 
    #  * Makes sure that <code>println</code> can display a <code>boolean</code>.
    #  * @noshow
    #  
    @println.register(object, bool)
    def println_1(self, x):
        """ generated source for method println_1 """
        self.println("" + x)

    # 
    #  * Makes sure that <code>println</code> can display a <code>char</code>.
    #  * @noshow
    #  
    @println.register(object, str)
    def println_2(self, x):
        """ generated source for method println_2 """
        self.println("" + x)

    # 
    #  * Makes sure that <code>println</code> can display a <code>double</code>.
    #  * @noshow
    #  
    @println.register(object, float)
    def println_3(self, x):
        """ generated source for method println_3 """
        self.println("" + x)

    # 
    #  * Makes sure that <code>println</code> can display a <code>float</code>.
    #  * @noshow
    #  
    @println.register(object, float)
    def println_4(self, x):
        """ generated source for method println_4 """
        self.println("" + x)

    # 
    #  * Makes sure that <code>println</code> can display an <code>int</code>.
    #  * @noshow
    #  
    @println.register(object, int)
    def println_5(self, x):
        """ generated source for method println_5 """
        self.println("" + x)

    # 
    #  * Makes sure that <code>println</code> can display a <code>long</code>.
    #  * @noshow
    #  
    @println.register(object, long)
    def println_6(self, x):
        """ generated source for method println_6 """
        self.println("" + x)

    # 
    #  * Makes sure that <code>println</code> can display an <code>Object</code>.
    #  * @noshow
    #  
    @println.register(object, object)
    def println_7(self, x):
        """ generated source for method println_7 """
        self.println("" + x)

    #  Method: showErrorMessage(msg) 
    # 
    #  * Displays the error message in the standard output model.
    #  *
    #  * @usage showErrorMessage(msg);
    #  * @param msg The error msg to be displayed
    #  
    def showErrorMessage(self, msg):
        """ generated source for method showErrorMessage """
        getOutputModel().showErrorMessage(msg)

    #  Method: readLine() 
    # 
    #  * Reads and returns a line of input from the console.  The end-of-line
    #  * characters that terminate the input are not included in the returned
    #  * string.
    #  *
    #  * @usage String str = program.readLine();
    #  * @return The next line of input as a <code>String</code>
    #  
    @overloaded
    def readLine(self):
        """ generated source for method readLine """
        return self.readLine(None)

    #  Method: readLine(prompt) 
    # 
    #  * Prompts the user for a line of input.  The end-of-line characters
    #  * that terminate the input are not included in the returned string.
    #  *
    #  * @usage String str = program.readLine(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The next line of input as a <code>String</code>
    #  
    @readLine.register(object, str)
    def readLine_0(self, prompt):
        """ generated source for method readLine_0 """
        return getInputModel().readLine(prompt)

    #  Method: readInt() 
    # 
    #  * Reads and returns an integer value from the user.  If the user types
    #  * a value that is not a legal integer, the method ordinarily offers the
    #  * user a chance to reenter the data, although this behavior can be
    #  * changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage int n = program.readInt();
    #  * @return The value of the input interpreted as a decimal integer
    #  
    @overloaded
    def readInt(self):
        """ generated source for method readInt """
        return self.readInt(None, Integer.MIN_VALUE, Integer.MAX_VALUE)

    #  Method: readInt(low, high) 
    # 
    #  * Reads and returns an integer value from the user, which is constrained to
    #  * be within the specified inclusive range.  If the user types a value
    #  * that is not a legal integer, the method ordinarily offers the user a chance
    #  * to reenter the data, although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage int n = program.readInt(low, high);
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a decimal integer
    #  
    @readInt.register(object, int, int)
    def readInt_0(self, low, high):
        """ generated source for method readInt_0 """
        return self.readInt(None, low, high)

    #  Method: readInt(prompt) 
    # 
    #  * Prompts the user to enter an integer, which is then returned as the value
    #  * of this method.  If the user types a value that is not a legal integer,
    #  * the method ordinarily offers the user a chance to reenter the data,
    #  * although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage int n = program.readInt(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The value of the input interpreted as a decimal integer
    #  
    @readInt.register(object, str)
    def readInt_1(self, prompt):
        """ generated source for method readInt_1 """
        return self.readInt(prompt, Integer.MIN_VALUE, Integer.MAX_VALUE)

    #  Method: readInt(prompt, low, high) 
    # 
    #  * Prompts the user to enter an integer, which is then returned as the value
    #  * of this method.  The value must be within the inclusive range between
    #  * <code>low</code> and <code>high</code>.  If the user types a value that
    #  * is not a legal integer or is outside the specified range, the method
    #  * ordinarily offers the user a chance to reenter the data,
    #  * although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage int n = console.readInt(prompt, low, high);
    #  * @param prompt The prompt string to display to the user
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a decimal integer
    #  
    @readInt.register(object, str, int, int)
    def readInt_2(self, prompt, low, high):
        """ generated source for method readInt_2 """
        return getInputModel().readInt(prompt, low, high)

    #  Method: readDouble() 
    # 
    #  * Reads and returns a double-precision value from the user.  If the user
    #  * types a value that is not a legal number, the method ordinarily offers
    #  * the user a chance to reenter the data, although this behavior can be
    #  * changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage double d = program.readDouble();
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @overloaded
    def readDouble(self):
        """ generated source for method readDouble """
        return self.readDouble(None, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY)

    #  Method: readDouble(low, high) 
    # 
    #  * Reads and returns a double-precision value from the user, which is
    #  * constrained to be within the specified inclusive range.  If the user
    #  * types a value that is not a legal number, the method ordinarily offers
    #  * the user a chance to reenter the data, although this behavior can be
    #  * changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage double d = program.readDouble(low, high);
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @readDouble.register(object, float, float)
    def readDouble_0(self, low, high):
        """ generated source for method readDouble_0 """
        return self.readDouble(None, low, high)

    #  Method: readDouble(prompt) 
    # 
    #  * Prompts the user to enter an double-precision number, which is then
    #  * returned as the value of this method.  If the user types a value that
    #  * is not a legal number, the method ordinarily offers the user a chance to
    #  * reenter the data,  although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage double d = program.readDouble(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @readDouble.register(object, str)
    def readDouble_1(self, prompt):
        """ generated source for method readDouble_1 """
        return self.readDouble(prompt, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY)

    #  Method: readDouble(prompt, low, high) 
    # 
    #  * Prompts the user to enter an double-precision number, which is then returned
    #  * as the value of this method.  The value must be within the inclusive range
    #  * between <code>low</code> and <code>high</code>.  If the user types a value
    #  * that is not a legal number, the method ordinarily offers the user a chance
    #  * to reenter the data,  although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage d = program.readDouble(prompt, low, high);
    #  * @param prompt The prompt string to display to the user
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @readDouble.register(object, str, float, float)
    def readDouble_2(self, prompt, low, high):
        """ generated source for method readDouble_2 """
        return getInputModel().readDouble(prompt, low, high)

    #  Method: readBoolean() 
    # 
    #  * Reads and returns a boolean value (<code>true</code> or <code>false</code>).
    #  * The input must match one of these strings, ignoring case.  If the user
    #  * types a value that is not one of these possibilities, the method ordinarily
    #  * offers the user a chance to reenter the data, although this behavior
    #  * can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage boolean flag = program.readBoolean();
    #  * @return The value of the input interpreted as a boolean value
    #  
    @overloaded
    def readBoolean(self):
        """ generated source for method readBoolean """
        return self.readBoolean(None)

    #  Method: readBoolean(prompt) 
    # 
    #  * Prompts the user to enter a boolean value, which is returned as
    #  * the value of this method.  If the user types a value that is not a
    #  * legal boolean value, the method ordinarily offers the user a chance
    #  * to reenter the data, although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage boolean flag = program.readBoolean(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The value of the input interpreted as a boolean value
    #  
    @readBoolean.register(object, str)
    def readBoolean_0(self, prompt):
        """ generated source for method readBoolean_0 """
        return self.readBoolean(prompt, "true", "false")

    #  Method: readBoolean(prompt, trueLabel, falseLabel) 
    # 
    #  * Prompts the user to enter a boolean value, which is matched against the
    #  * labels provided.  If the user enters a value that is not one of the two
    #  * choices, <code>readBoolean</code> ordinarily offers the user a chance
    #  * to reenter the data, although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage boolean flag = program.readBoolean(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @param trueLabel The string used to indicate <code>true</code>
    #  * @param falseLabel The string used to indicate <code>false</code>
    #  * @return The value of the input interpreted as a boolean value
    #  
    @readBoolean.register(object, str, str, str)
    def readBoolean_1(self, prompt, trueLabel, falseLabel):
        """ generated source for method readBoolean_1 """
        return getInputModel().readBoolean(prompt, trueLabel, falseLabel)

    #  Method: isAppletMode() 
    # 
    #  * Returns <code>true</code> if this program is running as an applet in a browser.
    #  *
    #  * @usage if (isAppletMode()) . . .
    #  * @return <code>true</code> if this program is running as an applet, <code>false</code> otherwise
    #  * @noshow
    #  
    def isAppletMode(self):
        """ generated source for method isAppletMode """
        return appletMode

    #  Method: setConsole(console) 
    # 
    #  * Sets the console associated with this program.
    #  *
    #  * @usage program.setConsole(console);
    #  * @param console The <code>IOConsole</code> object used for this program
    #  
    def setConsole(self, console):
        """ generated source for method setConsole """
        myConsole = console

    #  Method: getConsole() 
    # 
    #  * Returns the console associated with this program.
    #  *
    #  * @usage IOConsole console = program.getConsole();
    #  * @return The <code>IOConsole</code> object used for this program
    #  
    def getConsole(self):
        """ generated source for method getConsole """
        return myConsole

    #  Method: setDialog(dialog) 
    # 
    #  * Sets the dialog associated with this program.
    #  *
    #  * @usage program.setDialog(dialog);
    #  * @param dialog The <code>IODialog</code> object used for this program
    #  
    def setDialog(self, dialog):
        """ generated source for method setDialog """
        myDialog = dialog

    #  Method: getDialog() 
    # 
    #  * Returns the dialog used for user interaction.
    #  *
    #  * @usage IODialog dialog = program.getDialog();
    #  * @return The <code>IODialog</code> object used for this program
    #  
    def getDialog(self):
        """ generated source for method getDialog """
        return myDialog

    #  Method: setInputModel(io) 
    # 
    #  * Sets the input model associated with this program.
    #  *
    #  * @usage program.setInputModel(io);
    #  * @param io The input model used for this program
    #  
    def setInputModel(self, io):
        """ generated source for method setInputModel """
        inputModel = io

    #  Method: setOutputModel(io) 
    # 
    #  * Sets the output model associated with this program.
    #  *
    #  * @usage program.setOutputModel(io);
    #  * @param io The <code>IOModel</code> object used as the output model
    #  
    def setOutputModel(self, io):
        """ generated source for method setOutputModel """
        outputModel = io

    #  Method: getInputModel() 
    # 
    #  * Returns the <code>IOModel</code> used for program input, which will
    #  * ordinarily be the console.
    #  *
    #  * @usage IOModel io = program.getInputModel();
    #  * @return The <code>IOModel</code> used for program input
    #  
    def getInputModel(self):
        """ generated source for method getInputModel """
        return myConsole if (inputModel == None) else inputModel

    #  Method: getOutputModel() 
    # 
    #  * Returns the <code>IOModel</code> used for program output, which will
    #  * ordinarily be the console.
    #  *
    #  * @usage IOModel io = program.getOutputModel();
    #  * @return The <code>IOModel</code> used for program output
    #  
    def getOutputModel(self):
        """ generated source for method getOutputModel """
        return myConsole if (outputModel == None) else outputModel

    #  Method: getReader() 
    # 
    #  * Returns a <code>BufferedReader</code> whose input comes from the console.
    #  *
    #  * @usage BufferedReader rd = getReader();
    #  * @return A <code>Reader</code> for use with this console
    #  
    def getReader(self):
        """ generated source for method getReader """
        return self.getConsole().getReader()

    #  Method: getWriter() 
    # 
    #  * Returns a <code>PrintWriter</code> whose output is directed to the console.
    #  *
    #  * @usage PrintWriter wr = getWriter();
    #  * @return A <code>PrintWriter</code> for use with this console
    #  
    def getWriter(self):
        """ generated source for method getWriter """
        return self.getConsole().getWriter()

    #  Method: getRegionPanel(region) 
    # 
    #  * Gets the <code>JPanel</code> for the specified region.
    #  *
    #  * @usage JPanel panel = getRegionPanel(region);
    #  * @param region The region of the window (<code>NORTH</code>, <code>SOUTH</code>,
    #  *               <code>EAST</code>, <code>WEST</code>, or <code>CENTER</code>)
    #  * @return The <code>JPanel</code> for that subregion
    #  * @noshow
    #  
    def getRegionPanel(self, region):
        """ generated source for method getRegionPanel """
        if region == self.NORTH:
            return northPanel
        elif region == self.SOUTH:
            return southPanel
        elif region == self.WEST:
            return westPanel
        elif region == self.EAST:
            return eastPanel
        elif region == self.CENTER:
            return centerPanel
        else:
            raise ErrorException("getRegionPanel: Illegal region " + region)

    #  Method: add(comp, region, constraints) 
    # 
    #  * Adds the component to the specified border region with the indicated
    #  * constraints object.
    #  *
    #  * @usage add(comp, region, constraints);
    #  * @param comp The component to be added
    #  * @param region The region of the window (<code>NORTH</code>, <code>SOUTH</code>,
    #  *               <code>EAST</code>, <code>WEST</code>, or <code>CENTER</code>)
    #  * @param constraints The constraints object
    #  * @noshow
    #  
    def add(self, comp, region, constraints):
        """ generated source for method add """
        if region == self.NORTH:
            northPanel.add(comp, constraints)
        elif region == self.SOUTH:
            southPanel.add(comp, constraints)
        elif region == self.WEST:
            westPanel.add(comp, constraints)
        elif region == self.EAST:
            eastPanel.add(comp, constraints)
        elif region == self.CENTER:
            centerPanel.add(comp, constraints)
        else:
            raise ErrorException("add: Illegal region " + region)

    #  Method: addActionListeners() 
    # 
    #  * Adds the program as an <code>ActionListener</code> to every button in
    #  * the structure that does not have a listener already.
    #  *
    #  * @usage addActionListeners();
    #  
    @overloaded
    def addActionListeners(self):
        """ generated source for method addActionListeners """
        self.addActionListeners(self)

    #  Method: addActionListeners(listener) 
    # 
    #  * Adds the specified listener to every button in
    #  * the structure that does not have a listener already.
    #  *
    #  * @usage addActionListeners(listener);
    #  * @param listener The <code>ActionListener</code> to be added
    #  
    @addActionListeners.register(object, ActionListener)
    def addActionListeners_0(self, listener):
        """ generated source for method addActionListeners_0 """
        self.addActionListeners(getContentPane(), listener)

    #  Method: setTitle(title) 
    # 
    #  * Sets the title of this program.  The title appears in the title bar
    #  * when the program is running as an application.
    #  *
    #  * @usage setTitle(title);
    #  * @param title The title for this program
    #  
    def setTitle(self, title):
        """ generated source for method setTitle """
        myTitle = title
        if programFrame != None:
            programFrame.setTitle(title)

    #  Method: getTitle() 
    # 
    #  * Gets the title of this program.
    #  *
    #  * @usage String title = getTitle();
    #  * @return The title in use for this program
    #  
    def getTitle(self):
        """ generated source for method getTitle """
        return myTitle

    #  Method: getMenuBar() 
    # 
    #  * Returns the menu bar associated with this program.  Note that this menu bar
    #  * cannot be set by clients, although it can be changed initially by overriding
    #  * the <code>createMenuBar</code> factory method.
    #  *
    #  * @usage ProgramMenuBar mbar = getMenuBar();
    #  * @return The menu bar in use for this program
    #  
    def getMenuBar(self):
        """ generated source for method getMenuBar """
        return myMenuBar

    #  Method: start(args) 
    # 
    #  * Starts the program using the specified argument list.
    #  *
    #  * @usage program.start(args);
    #  * @param args An array of strings passed to the program
    #  
    @overloaded
    def start(self, args):
        """ generated source for method start """
        if parameterTable == None:
            parameterTable = createParameterTable(args)
        if getParent() == None:
            initApplicationFrame()
        validate()
        setVisible(True)
        if programFrame != None:
            programFrame.validate()
            nComponents = centerPanel.getComponentCount()
            nComponents += northPanel.getComponentCount()
            nComponents += southPanel.getComponentCount()
            nComponents += westPanel.getComponentCount()
            nComponents += eastPanel.getComponentCount()
            if nComponents > 0:
                programFrame.setVisible(True)
                shown = True
            circumventFrameSizeBug(programFrame, programBounds.getSize())
        started = True
        self.init()
        if programFrame != None and myMenuBar != None:
            myMenuBar.install(programFrame)
        validate()
        startRun()

    #  Method: exit() 
    # 
    #  * Exits from the program.  Subclasses should override this method if they need
    #  * to perform any actions before shutting down the program, such as asking the
    #  * user to save any unsaved files.  Any clients that do override this method
    #  * should call <code>super.exit()</code> at the end of their processing.
    #  *
    #  * @usage program.exit();
    #  
    def exit(self):
        """ generated source for method exit """
        nFinalizers = len(finalizers)
        i = 0
        while i < nFinalizers:
            obj = finalizers.get(i)
            try:
                c = obj.__class__
                exit = c.getMethod("exit", [None] * 0)
                self.exit.invoke(obj, [None] * 0)
            except Exception as ex:
                raise ErrorException(ex)
            i += 1
        JTFTools.terminateAppletThreads(self)
        if not appletMode:
            System.exit(0)

    #  Method: addExitHook(obj) 
    # 
    #  * Requests that the program call the <code>exit</code> method in the
    #  * specified object before exiting.
    #  *
    #  * @usage program.addExitHook(obj);
    #  
    def addExitHook(self, obj):
        """ generated source for method addExitHook """
        finalizers.add(obj)

    #  Method: setParameter(name, value) 
    # 
    #  * Sets a new value for the named parameter.
    #  *
    #  * @usage setParameter(name, value);
    #  * @param name The name of the parameter
    #  * @param value The new value
    #  * @noshow
    #  
    def setParameter(self, name, value):
        """ generated source for method setParameter """
        if parameterTable == None:
            parameterTable = HashMap()
        parameterTable.put(name.lower(), value)

    #  Method: getMainThread() 
    # 
    #  * Returns the thread that is running the main program.
    #  *
    #  * @usage Thread mainThread = getMainThread();
    #  * @return The thread that is running the main program, if any
    #  * @noshow
    #  
    def getMainThread(self):
        """ generated source for method getMainThread """
        return None if (appletStarter == None) else appletStarter.getMainThread()

    #  Method: pause(milliseconds) 
    # 
    #  * Delays the calling thread for the specified time, which is expressed in
    #  * milliseconds.  Unlike <code>Thread.sleep</code>, this method never throws an
    #  * exception.
    #  *
    #  * @usage program.pause(milliseconds);
    #  * @param milliseconds The sleep time in milliseconds
    #  
    def pause(self, milliseconds):
        """ generated source for method pause """
        JTFTools.pause(milliseconds)

    #  Method: getCentralRegionSize() 
    # 
    #  * Returns the size of the central region.  If the content pane has
    #  * not been validated, this method computes its preferred size by
    #  * subtracting the sizes required for the side panels from the size
    #  * of the entire frame.
    #  *
    #  * @return The size of the central region
    #  
    def getCentralRegionSize(self):
        """ generated source for method getCentralRegionSize """
        if centerPanel == None:
            return super(Program, self).getSize()
        if initFinished:
            return centerPanel.getSize()
        size = super(Program, self).getSize() if (programFrame == None) else programFrame.getSize()
        insets = super(Program, self).getInsets() if (programFrame == None) else programFrame.getInsets()
        size.width -= westPanel.getPreferredSize().width + eastPanel.getPreferredSize().width
        size.width -= insets.left + insets.right
        size.height -= northPanel.getPreferredSize().height + southPanel.getPreferredSize().height
        size.height -= insets.top + insets.bottom
        return size

    # /
    #  Listener methods                                                   
    # /
    #  Method: mouseClicked (implements MouseListener) 
    # 
    #  * Called when the mouse is clicked.  A call to <code>mouseClicked</code>
    #  * is always preceded by both a <code>mousePressed</code> and a
    #  * <code>mouseReleased</code> event for the same source.
    #  
    def mouseClicked(self, e):
        """ generated source for method mouseClicked """

    #  Method: mousePressed (implements MouseListener) 
    # 
    #  * Called when the mouse button is pressed.
    #  
    def mousePressed(self, e):
        """ generated source for method mousePressed """

    #  Method: mouseReleased (implements MouseListener) 
    # 
    #  * Called when the mouse button is released.
    #  
    def mouseReleased(self, e):
        """ generated source for method mouseReleased """

    #  Method: mouseEntered (implements MouseListener) 
    # 
    #  * Called when the mouse enters the source (which may be
    #  * either a component or a <code>GObject</code>).
    #  
    def mouseEntered(self, e):
        """ generated source for method mouseEntered """

    #  Method: mouseExited (implements MouseListener) 
    # 
    #  * Called when the mouse exits the source (which may be
    #  * either a component or a <code>GObject</code>).
    #  
    def mouseExited(self, e):
        """ generated source for method mouseExited """

    #  Method: mouseMoved (implements MouseMotionListener) 
    # 
    #  * Called when the mouse is moved.
    #  
    def mouseMoved(self, e):
        """ generated source for method mouseMoved """

    #  Method: mouseDragged (implements MouseMotionListener) 
    # 
    #  * Called when the mouse is dragged with the button down.  Java
    #  * makes several guarantees about dragging.  First, a
    #  * <code>mouseDragged</code> call is always preceded by a
    #  * <code>mousePressed</code> call for the same source.  If the
    #  * mouse is pressed elsewhere and then enters a source with
    #  * the button down, no drag event occurs.  Moreover, once the
    #  * mouse button goes down in a particular source, only that
    #  * source will receive mouse events until the button goes up.
    #  * Those events, moreover, are reported even in the mouse
    #  * travels outside the domain of the object.
    #  
    def mouseDragged(self, e):
        """ generated source for method mouseDragged """

    #  Method: keyTyped (implements KeyListener) 
    # 
    #  * Called when a key is typed (i.e., pressed and released).
    #  
    def keyTyped(self, e):
        """ generated source for method keyTyped """

    #  Method: keyPressed (implements KeyListener) 
    # 
    #  * Called when a key is pressed.
    #  
    def keyPressed(self, e):
        """ generated source for method keyPressed """

    #  Method: keyReleased (implements KeyListener) 
    # 
    #  * Called when a key is released.
    #  
    def keyReleased(self, e):
        """ generated source for method keyReleased """

    #  Method: actionPerformed (implements ActionListener) 
    # 
    #  * Called when a component (typically a button) is activated.
    #  
    def actionPerformed(self, e):
        """ generated source for method actionPerformed """

    # /
    #  Factory methods                                                    
    # /
    #  Factory method: createProgramFrame() 
    # 
    #  * Creates the frame containing the program.
    #  *
    #  * @usage Frame frame = program.createProgramFrame();
    #  * @return The newly allocated <code>Frame</code> object
    #  
    def createProgramFrame(self):
        """ generated source for method createProgramFrame """
        return ProgramFrame(self.getTitle())

    #  Factory method: createConsole() 
    # 
    #  * Creates the console used by the <code>ConsoleProgram</code>.  Subclasses can
    #  * override this method to create their own console types.
    #  *
    #  * @usage IOConsole console = program.createConsole();
    #  * @return The console to be used by the program
    #  
    def createConsole(self):
        """ generated source for method createConsole """
        return IOConsole.SYSTEM_CONSOLE

    #  Factory method: createDialogIO() 
    # 
    #  * Creates the dialog used for interaction (primarily by the <code>DialogProgram</code>
    #  * class).  Subclasses can override this method to create their own dialog types.
    #  *
    #  * @usage IODialog dialog = program.createDialogIO();
    #  * @return The dialog to be used by the program
    #  
    def createDialogIO(self):
        """ generated source for method createDialogIO """
        return IODialog(getContentPane())

    #  Factory method: createMenuBar() 
    # 
    #  * Creates a menu bar for use with the program.
    #  *
    #  * @usage ProgramMenuBar menuBar = createMenuBar();
    #  * @return A menu bar for use with this <code>Program</code>
    #  * @noshow
    #  
    def createMenuBar(self):
        """ generated source for method createMenuBar """
        return ProgramMenuBar(self)

    # /
    #  Overrides of existing methods                                      
    # /
    #  Overridden method: getPreferredSize() 
    # 
    #  * Returns the preferred size of the content pane.
    #  *
    #  * @usage Dimension size = getPreferredSize();
    #  * @return The preferred size of the content pane
    #  * @noshow
    #  
    def getPreferredSize(self):
        """ generated source for method getPreferredSize """
        return computeProgramBounds().getSize()

    #  Overridden method: getWidth() 
    # 
    #  * Returns the width of the central region.
    #  *
    #  * @usage int width = getWidth();
    #  * @return The width of the central region
    #  * @noshow
    #  
    def getWidth(self):
        """ generated source for method getWidth """
        caller = getMyCaller()
        if caller.startsWith("java.") or caller.startsWith("javax."):
            return super(Program, self).getWidth()
        else:
            return self.getCentralRegionSize().width

    #  Overridden method: getHeight() 
    # 
    #  * Returns the height of the central region.
    #  *
    #  * @usage int height = getHeight();
    #  * @return The height of the central region
    #  * @noshow
    #  
    def getHeight(self):
        """ generated source for method getHeight """
        caller = getMyCaller()
        if caller.startsWith("java.") or caller.startsWith("javax."):
            return super(Program, self).getHeight()
        else:
            return self.getCentralRegionSize().height

    #  Overridden method: getParameter(name) 
    # 
    #  * Returns the parameter associated with name.
    #  *
    #  * @usage String value = getParameter(name);
    #  * @param name The name of the parameter
    #  * @return The value associated with the parameter, or <code>null</code> if none
    #  * @noshow
    #  
    def getParameter(self, name):
        """ generated source for method getParameter """
        value = None
        if parameterTable != None:
            value = parameterTable.get(name.lower())
        if value != None:
            return value
        return super(Program, self).getParameter(name)

    #  Overridden method: setLayout(layout) 
    # 
    #  * Sets the layout manager for the central region of the content pane.
    #  *
    #  * @usage setLayout(layout);
    #  * @param layout The layout manager to use
    #  * @noshow
    #  
    def setLayout(self, layout):
        """ generated source for method setLayout """
        if isRootPaneCheckingEnabled():
            centerPanel.setLayout(layout)
        else:
            super(Program, self).setLayout(layout)

    #  Overridden method: getLayout() 
    # 
    #  * Gets the layout manager for the central region of the content pane.
    #  *
    #  * @usage LayoutManager layout = setLayout();
    #  * @return The active layout manager
    #  * @noshow
    #  
    def getLayout(self):
        """ generated source for method getLayout """
        if isRootPaneCheckingEnabled():
            return centerPanel.getLayout()
        else:
            return super(Program, self).getLayout()

    #  Overridden method: setBackground(color) 
    # 
    #  * Sets the background for the central region of the content pane.
    #  *
    #  * @usage setBackground(color);
    #  * @param color The new background color
    #  * @noshow
    #  
    def setBackground(self, color):
        """ generated source for method setBackground """
        if isRootPaneCheckingEnabled():
            centerPanel.setBackground(color)
        super(Program, self).setBackground(color)

    #  Overridden method: addImpl(comp, constraints, index) 
    # 
    #  * Adds the specified component to the content pane using the specified constraints and index.
    #  
    def addImpl(self, comp, constraints, index):
        """ generated source for method addImpl """
        if isRootPaneCheckingEnabled():
            if constraints == None:
                centerPanel.add(comp, index)
            elif constraints == self.NORTH:
                northPanel.add(comp, index)
            elif constraints == self.SOUTH:
                southPanel.add(comp, index)
            elif constraints == self.WEST:
                westPanel.add(comp, index)
            elif constraints == self.EAST:
                eastPanel.add(comp, index)
            elif constraints == self.CENTER:
                centerPanel.add(comp, index)
            else:
                centerPanel.add(comp, constraints, index)
            if not shown and programFrame != None:
                programFrame.setVisible(True)
                shown = True
        else:
            super(Program, self).addImpl(comp, constraints, index)

    #  Overridden method: remove(index) 
    # 
    #  * Removes the component at the specified index from the central region.
    #  *
    #  * @usage remove(index);
    #  * @param index The index position of the component to remove
    #  * @noshow
    #  
    @overloaded
    def remove(self, index):
        """ generated source for method remove """
        if isRootPaneCheckingEnabled():
            centerPanel.remove(index)
        else:
            super(Program, self).remove(index)

    #  Overridden method: remove(comp) 
    # 
    #  * Removes the specified component from the central region.
    #  *
    #  * @usage remove(comp);
    #  * @param comp The component to remove
    #  * @noshow
    #  
    @remove.register(object, Component)
    def remove_0(self, comp):
        """ generated source for method remove_0 """
        if isRootPaneCheckingEnabled():
            centerPanel.remove(comp)
        else:
            super(Program, self).remove(comp)

    #  Overridden method: removeAll() 
    # 
    #  * Removes all components from the central region.
    #  *
    #  * @usage removeAll();
    #  * @noshow
    #  
    def removeAll(self):
        """ generated source for method removeAll """
        if isRootPaneCheckingEnabled():
            centerPanel.removeAll()
        else:
            super(Program, self).removeAll()

    #  Overridden method: validate() 
    # 
    #  * Forwards validate to the content pane.
    #  *
    #  * @usage validate();
    #  * @noshow
    #  
    def validate(self):
        """ generated source for method validate """
        if isRootPaneCheckingEnabled():
            getContentPane().validate()
        super(Program, self).validate()

    #  Overridden method: repaint() 
    # 
    #  * Forwards repaint to the content pane.
    #  *
    #  * @usage repaint();
    #  * @noshow
    #  
    def repaint(self):
        """ generated source for method repaint """
        if isRootPaneCheckingEnabled():
            getContentPane().repaint()
        super(Program, self).repaint()

    #  Overridden method: start() 
    # 
    #  * Starts the program when it is running in application mode.  Note that this
    #  * overloads the <code>start</code> method in <code>Applet</code> and therefore
    #  * will be called as part of applet startup.
    #  *
    #  * @usage program.start();
    #  * @noshow
    #  
    @start.register(object)
    def start_0(self):
        """ generated source for method start_0 """
        appletMode = getParent() != None
        if appletMode:
            if not started:
                started = True
                self.validate()
                setVisible(True)
                appletStarter = AppletStarter(self)
                appletStarter.start()
        else:
            self.start(None)

    #  Overridden method: destroy() 
    # 
    #  * Called when the program has been told to destroy itself.  The code here
    #  * stops the main thread and any animators that have been initiated by this
    #  * applet.
    #  *
    #  * @usage program.destroy();
    #  * @noshow
    #  
    def destroy(self):
        """ generated source for method destroy """
        Animator.shutdown(self)
        if appletStarter != None:
            appletStarter.stop()

    #  Static method: main(args) 
    # 
    #  * Every application must either contain a "Main-Class" entry in its
    #  * manifest file or include a main method that looks like this, where
    #  * <code>MyClass</code> is the name of the program class:
    #  *
    #  * <p><pre><code>
    #  * &nbsp;    public static void main(String[] args) {
    #  * &nbsp;       new MyClass().start();
    #  * &nbsp;    }
    #  * </code></pre>
    #  *
    #  * <p>If the program needs the command line arguments, the <code>args</code>
    #  * array can be passed to the <code>start</code> method and then retrieved
    #  * using the <code>getArgumentArray</code> method.
    #  *
    #  * @param args An array of string arguments
    #  
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        ht = createParameterTable(args)
        JTFTools.setDebugOptions(ht.get("debug"))
        className = ht.get("code")
        if className == None:
            className = JTFTools.getMainClass()
        mainClass = None
        program = None
        if className != None:
            if className.endsWith(".class"):
                className = className.substring(0, 6 - len(className))
            className = className.replace('/', '.')
            CommandLineProgram.checkIfHeadless(className)
            try:
                mainClass = Class.forName(className)
            except ClassNotFoundException as ex:
                pass
                #  Empty 
        if mainClass != None:
            try:
                obj = mainClass.newInstance()
                if isinstance(obj, (Program, )):
                    program = obj
                    program.setStartupObject(None)
                else:
                    className = ht.get("program")
                    if className == None:
                        raise ErrorException("Main class does not specify a program")
                    program = Class.forName(className).newInstance()
                    program.setStartupObject(obj)
            except IllegalAccessException as ex:
                pass
                #  Empty 
            except InstantiationException as ex:
                pass
                #  Empty 
            except ClassNotFoundException as ex:
                pass
                #  Empty 
        if program == None:
            raise ErrorException("Cannot determine the main class.")
        program.setParameterTable(ht)
        program.start()

    #  Method: menuAction(e) 
    # 
    #  * Called whenever a program action is detected in the menu bar.
    #  * Subclasses can override this method to extend the set of menu
    #  * commands recognized even in the absence of a component with
    #  * keyboard focus.
    #  
    def menuAction(self, e):
        """ generated source for method menuAction """
        cmd = e.getActionCommand()
        if cmd == "Quit":
            self.exit()
        elif cmd == "Print":
            frame_ = JTFTools.getEnclosingFrame(self)
            if frame_ == None:
                return True
            pj = frame_.getToolkit().getPrintJob(frame_, myTitle, None)
            if pj == None:
                return True
            pg = pj.getGraphics()
            pg.translate(PRINT_MARGIN, PRINT_MARGIN)
            frame_.printAll(pg)
            pj.end()
            return True
        elif cmd == "Export Applet" or cmd == "Submit Project":
            JTFTools.executeExportAction(self, cmd)
            return True
        return self.getConsole().menuAction(e)

    # /
    #  Protected methods                                                  
    # /
    #  Protected method: getBorder(side) 
    # 
    #  * Returns the component installed as a border on the specified side, which must
    #  * be one of the constants from <code>BorderLayout</code> (<code>NORTH</code>,
    #  * <code>SOUTH</code>, <code>EAST</code>, <code>WEST</code>).
    #  *
    #  * @usage getBorder(side, comp);
    #  * @param side The side (<code>NORTH</code>, <code>SOUTH</code>, <code>EAST</code>,
    #  *             or <code>WEST</code>)
    #  * @return The component used as a border on the specified side
    #  * @noshow
    #  
    def getBorder(self, side):
        """ generated source for method getBorder """
        if side == self.NORTH:
            return northBorder
        if side == self.SOUTH:
            return southBorder
        if side == self.EAST:
            return eastBorder
        if side == self.WEST:
            return westBorder
        raise ErrorException("Illegal border specification - " + side)

    #  Protected method: getArgumentArray() 
    # 
    #  * Retrieves the array of arguments passed in from the command line, or
    #  * <code>null</code> if no arguments are available.
    #  *
    #  * @usage String[] args = getArgumentArray();
    #  * @return The array of command-line arguments
    #  * @noshow
    #  
    def getArgumentArray(self):
        """ generated source for method getArgumentArray """
        if parameterTable == None:
            return None
        tokenizer = StringTokenizer(parameterTable.get("ARGS"), "\t", False)
        args = [None] * tokenizer.countTokens()
        i = 0
        while tokenizer.hasMoreTokens():
            args[i] = tokenizer.nextToken()
            i += 1
        return args

    #  Protected method: isStarted() 
    # 
    #  * Checks to see whether this program has started, usually by checking to see
    #  * whether some pane exists.  Subclasses can override this method to ensure
    #  * that their structures are visible before proceeding.
    #  * @noshow
    #  
    def isStarted(self):
        """ generated source for method isStarted """
        console = self.getConsole()
        if console == None:
            return False
        if console.getParent() == None:
            return True
        size = console.getSize()
        return (console.isShowing()) and (size.width != 0) and (size.height != 0)

    #  Protected method: startHook() 
    # 
    #  * Performs class-specific initialization for the program just before
    #  * it starts.
    #  * @noshow
    #  
    def startHook(self):
        """ generated source for method startHook """
        #  Empty 

    #  Protected method: endHook() 
    # 
    #  * Performs class-specific cleanup for the program just after
    #  * it finishes.
    #  * @noshow
    #  
    def endHook(self):
        """ generated source for method endHook """
        #  Empty 

    #  Protected method: setAppletStub(stub) 
    # 
    #  * Sets the applet stub for this program in a way that makes it possible for
    #  * clients to retrieve it.
    #  *
    #  * @usage setAppletStub(stub);
    #  * @param stub The applet stub
    #  
    def setAppletStub(self, stub):
        """ generated source for method setAppletStub """
        appletStub = stub
        setStub(stub)

    #  Protected method: getAppletStub() 
    # 
    #  * Retrieves the applet stub.
    #  *
    #  * @usage AppletStub stub = getAppletStub();
    #  * @return The applet stub
    #  
    def getAppletStub(self):
        """ generated source for method getAppletStub """
        return appletStub

    #  Protected method: setParameterTable(ht) 
    # 
    #  * Sets the parameter table for this program.
    #  *
    #  * @usage setParameterTable(ht);
    #  * @param ht The parameter table
    #  
    def setParameterTable(self, ht):
        """ generated source for method setParameterTable """
        parameterTable = ht

    #  Protected method: getParameterTable() 
    # 
    #  * Retrieves the parameter table.
    #  *
    #  * @usage ParameterTable ht = getParameterTable();
    #  * @return The parameter table
    #  
    def getParameterTable(self):
        """ generated source for method getParameterTable """
        return parameterTable

    #  Protected method: setStartupObject(obj) 
    # 
    #  * Sets the object that is created when the program is started so that
    #  * it can be retrieved later by <code>getStartupObject</code>.
    #  *
    #  * @usage setStartupObject(obj);
    #  * @param obj The startup object
    #  
    def setStartupObject(self, obj):
        """ generated source for method setStartupObject """
        startupObject = obj

    #  Protected method: getStartupObject() 
    # 
    #  * Retrieves the object that was created when this program was started
    #  * if that object is something other than a <code>Program</code>.  In
    #  * the normal case of running a <code>Program</code> object, this method
    #  * will return <code>null</code>.
    #  *
    #  * @usage Object obj = getStartupObject();
    #  * @return The startup object
    #  
    def getStartupObject(self):
        """ generated source for method getStartupObject """
        return startupObject

    #  Protected method: startRun() 
    # 
    #  * Initializes and runs the run method.
    #  
    def startRun(self):
        """ generated source for method startRun """
        listener = ProgramStartupListener()
        root = getRootPane()
        if root.isShowing():
            root.addComponentListener(listener)
            root.validate()
            listener.waitForStartup(self)
            root.update(root.getGraphics())
        root.setCursor(Cursor.getDefaultCursor())
        initFinished = True
        self.startHook()
        runHook()
        self.endHook()
        if not root.isShowing() and not getContentPane().isShowing():
            self.exit()

    #  Protected method: runHook() 
    # 
    #  * Calls the run method in the program.  Subclasses can override this
    #  * method to transfer control somewhere else.
    #  
    def runHook(self):
        """ generated source for method runHook """
        self.run()

    #  Protected static method: createParameterTable(args) 
    # 
    #  * Creates a hash table containing the parameters specified in the
    #  * argument list.  Parameters are taken to be any argument that matches
    #  * the template
    #  *
    #  * <p>   <i>name</i><code>=</code><i>value</i>
    #  *
    #  * All other arguments are collected as a tab-separated string and placed
    #  * in an entry under the key <code>"ARGS"</code>.  All named parameters
    #  * are converted to lower case to preserve the case-insensitive semantics
    #  * of <code>getParameter</code>.
    #  *
    #  * @usage HashMap<String,String> ht = createParameterTable(args);
    #  * @param args The array of strings passed to the application
    #  * @return A <code>HashMap</code> containing the parameter bindings
    #  
    @classmethod
    def createParameterTable(cls, args):
        """ generated source for method createParameterTable """
        if args == None:
            return None
        ht = HashMap()
        newArgs = ""
        i = 0
        while len(args):
            arg = args[i]
            equals = arg.indexOf('=')
            if equals > 0:
                name = arg.substring(0, equals).lower()
                value = arg.substring(equals + 1)
                ht.put(name, value)
            else:
                if 0 > len(newArgs):
                    newArgs += '\t'
                newArgs += arg
            i += 1
        ht.put("ARGS", newArgs)
        return ht

    # /
    #  Private methods                                                    
    # /
    #  Private method: initContentPane(contentPane) 
    # 
    #  * Initializes the content pane to contain its five regions.
    #  
    def initContentPane(self, contentPane):
        """ generated source for method initContentPane """
        contentPane.setLayout(ProgramContentPaneLayout(self))
        northPanel = JPanel()
        southPanel = JPanel()
        eastPanel = JPanel()
        westPanel = JPanel()
        centerPanel = JPanel()
        northPanel.setLayout(TableLayout(1, 0, 5, 5))
        southPanel.setLayout(TableLayout(1, 0, 5, 5))
        westPanel.setLayout(TableLayout(0, 1, 5, 5))
        eastPanel.setLayout(TableLayout(0, 1, 5, 5))
        centerPanel.setLayout(GridLayout(1, 0))
        contentPane.add(northPanel, self.NORTH)
        contentPane.add(southPanel, self.SOUTH)
        contentPane.add(eastPanel, self.EAST)
        contentPane.add(westPanel, self.WEST)
        contentPane.add(centerPanel, self.CENTER)

    #  Private method: addActionListeners(comp, listener) 
    # 
    #  * Recursively adds the specified listener as an <code>ActionListener</code> to
    #  * every button in the hierarchy.  Reflection is used because there are many
    #  * possible classes of button-like objects.
    #  
    @addActionListeners.register(object, Component, ActionListener)
    def addActionListeners_1(self, comp, listener):
        """ generated source for method addActionListeners_1 """
        if isButton(comp):
            if not hasActionListener(comp):
                try:
                    types = [Class.forName("java.awt.event.ActionListener")]
                    args = [listener]
                    addActionListener = comp.__class__.getMethod("addActionListener", types)
                    addActionListener.invoke(comp, args)
                except Exception as ex:
                    raise ErrorException(ex)
        elif isinstance(comp, (Container, )):
            container = comp
            nComponents = container.getComponentCount()
            i = 0
            while i < nComponents:
                self.addActionListeners(container.getComponent(i), listener)
                i += 1

    #  Private method: isButton(comp) 
    # 
    #  * Determines whether the component is a button.
    #  
    def isButton(self, comp):
        """ generated source for method isButton """
        return (isinstance(comp, (Button, )) or isinstance(comp, (JButton, )))

    #  Private method: hasActionListener(comp) 
    # 
    #  * Returns true if the component has at least one action listener.  The method
    #  * returns false if the Java runtime is too old to determine the answer.
    #  
    def hasActionListener(self, comp):
        """ generated source for method hasActionListener """
        try:
            getActionListeners = comp.__class__.getMethod("getActionListeners", [None] * 0)
            listeners = getActionListeners.invoke(comp, [None] * 0)
            return (len(listeners))
        except Exception as ex:
            return False

    #  Private method: initApplicationFrame() 
    # 
    #  * Creates the program frame and puts the program in it.
    #  
    def initApplicationFrame(self):
        """ generated source for method initApplicationFrame """
        programFrame = self.createProgramFrame()
        (appletStub).setFrame(programFrame)
        contents = programFrame.getContentPane()
        contents.setLayout(BorderLayout())
        contents.add(getContentPane(), BorderLayout.CENTER)
        programFrame.addWindowListener(ProgramWindowListener(self))
        programBounds = computeProgramBounds()
        insets = programFrame.getInsets()
        frameWidth = programBounds.width + insets.left + insets.right
        frameHeight = programBounds.height + insets.top + insets.bottom
        programFrame.setBounds(programBounds.x, programBounds.y, frameWidth, frameHeight)

    #  Private method: decodeSizeParameter(name, value, max) 
    # 
    #  * Decodes a size parameter.
    #  *
    #  * @usage int size = decodeSizeParameter(name, value, max);
    #  * @param name The name of the parameter
    #  * @param value The default value if the parameter is unspecified
    #  * @param max The maximum value if the parameter is specified as a percentage
    #  * @return The integer denoting the size
    #  
    def decodeSizeParameter(self, name, value, max):
        """ generated source for method decodeSizeParameter """
        str_ = self.getParameter(name)
        if str_ == None:
            try:
                mainClass = getClass()
                field = mainClass.getField("APPLICATION_" + name)
                obj = field.get(None)
                if isinstance(obj, (int, )):
                    return (int(obj)).intValue()
                if isinstance(obj, (str, )):
                    str_ = str(obj)
                else:
                    return value
            except Exception as ex:
                return value
        if str_ == "*":
            str_ = "100%"
        if str_.endsWith("%"):
            percent = Integer.parseInt(str_.substring(0, 1 - len(str_)))
            return int(round(percent / 100.0 * max))
        else:
            return Integer.parseInt(str_)

    #  Private method: computeProgramBounds() 
    # 
    #  * Sets the bounds for this program as specified in the parameters.
    #  
    def computeProgramBounds(self):
        """ generated source for method computeProgramBounds """
        size = Toolkit.getDefaultToolkit().getScreenSize()
        width = self.decodeSizeParameter("WIDTH", DEFAULT_WIDTH, size.width)
        height = self.decodeSizeParameter("HEIGHT", DEFAULT_HEIGHT, size.height)
        x = self.decodeSizeParameter("X", 0 if (width >= size.width) else DEFAULT_X, size.width)
        y = self.decodeSizeParameter("Y", 0 if (height >= size.height) else DEFAULT_Y, size.height)
        return Rectangle(x, y, width, height)

    #  Private method: checkForAppletMode() 
    # 
    #  * Determines whether this program has been invoked as an applet by scanning
    #  * the execution stack to see if the string <code>"Applet"</code> appears
    #  * in any method name up the calling chain.
    #  
    def checkForAppletMode(self):
        """ generated source for method checkForAppletMode """
        stack = Throwable().getStackTrace()
        i = 1
        while len(stack):
            if stack[i].getMethodName().indexOf("Applet") >= 0:
                return True
            i += 1
        return False

    def getMyCaller(self):
        """ generated source for method getMyCaller """
        stack = Throwable().getStackTrace()
        return stack[2].getClassName() + "." + stack[2].getMethodName()

    def circumventFrameSizeBug(self, frame_, size):
        """ generated source for method circumventFrameSizeBug """
        contentPane = getContentPane()
        actualSize = contentPane.getSize()
        if size == actualSize or actualSize.width == 0 or actualSize.height == 0:
            return
        frameSize = frame_.getSize()
        frameSize.width += size.width - actualSize.width
        frameSize.height += size.height - actualSize.height
        frame_.setSize(frameSize.width, frameSize.height)
        frame_.validate()

    DEFAULT_X = 16
    DEFAULT_Y = 40
    DEFAULT_WIDTH = 754
    DEFAULT_HEIGHT = 492
    PRINT_MARGIN = 36
    finalizers = None
    parameterTable = None
    programFrame = None
    appletStub = None
    myTitle = None
    myMenuBar = None
    northBorder = None
    southBorder = None
    eastBorder = None
    westBorder = None
    northPanel = None
    southPanel = None
    eastPanel = None
    westPanel = None
    centerPanel = None
    myConsole = None
    myDialog = None
    inputModel = None
    outputModel = None
    startupObject = None
    appletStarter = None
    programBounds = None
    started = bool()
    shown = bool()
    initFinished = bool()
    appletMode = bool()


class AppletStarter(Runnable):
    """ generated source for class AppletStarter """
    def __init__(self, program):
        """ generated source for method __init__ """
        super(AppletStarter, self).__init__()
        myProgram = program

    def start(self):
        """ generated source for method start """
        try:
            mainThread = Thread(self)
            mainThread.start()
            if JTFTools.testDebugOption("startup"):
                print("Starting main thread using Thread package")
        except SecurityException as ex:
            if JTFTools.testDebugOption("startup"):
                print("Starting main thread using Executor because " + ex)
            forkUsingExecutor()

    def stop(self):
        """ generated source for method stop """
        try:
            if executor == None:
                threadClass = Class.forName("java.lang.Thread")
                stop = threadClass.getMethod("stop", [None] * 0)
                self.stop.invoke(mainThread, [None] * 0)
            else:
                shutdownNow = executor.__class__.getMethod("shutdownNow", [None] * 0)
                shutdownNow.invoke(executor, [None] * 0)
        except Exception as ex:
            pass

    def run(self):
        """ generated source for method run """
        myProgram.startRun()

    def getMainThread(self):
        """ generated source for method getMainThread """
        return mainThread

    def forkUsingExecutor(self):
        """ generated source for method forkUsingExecutor """
        try:
            scheduledExecutorClass = Class.forName("java.util.concurrent.ScheduledExecutor")
            types1 = [Integer.TYPE]
            args1 = [int(1)]
            constructor = scheduledExecutorClass.getConstructor(types1)
            executor = constructor.newInstance(args1)
            timeUnitClass = Class.forName("java.util.concurrent.TimeUnit")
            secondsField = timeUnitClass.getField("SECONDS")
            seconds = secondsField.get(None)
            types2 = [Class.forName("java.lang.Runnable"), Long.TYPE, Class.forName("java.util.concurrent.TimeUnit")]
            args2 = [self, long(0), seconds]
            schedule = executor.__class__.getMethod("schedule", types2)
            schedule.invoke(executor, args2)
        except Exception as ex:
            if JTFTools.testDebugOption("startup"):
                print("Executor failed because " + ex)
            executor = None
            mainThread = Thread.currentThread()
            myProgram.startRun()

    myProgram = None
    mainThread = None
    executor = None


class ProgramActionListener(ActionListener):
    """ generated source for class ProgramActionListener """
    def __init__(self, owner):
        """ generated source for method __init__ """
        super(ProgramActionListener, self).__init__()
        program = owner

    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        program.menuAction(e)

    program = None


class ProgramWindowListener(WindowListener):
    """ generated source for class ProgramWindowListener """
    def __init__(self, owner):
        """ generated source for method __init__ """
        super(ProgramWindowListener, self).__init__()
        program = owner

    def windowClosing(self, e):
        """ generated source for method windowClosing """
        (e.getSource()).setVisible(False)
        program.exit()

    def windowOpened(self, e):
        """ generated source for method windowOpened """

    def windowClosed(self, e):
        """ generated source for method windowClosed """

    def windowIconified(self, e):
        """ generated source for method windowIconified """

    def windowDeiconified(self, e):
        """ generated source for method windowDeiconified """

    def windowActivated(self, e):
        """ generated source for method windowActivated """

    def windowDeactivated(self, e):
        """ generated source for method windowDeactivated """

    program = None


class ProgramStartupListener(ComponentListener):
    """ generated source for class ProgramStartupListener """
    @synchronized
    def waitForStartup(self, program):
        """ generated source for method waitForStartup """
        JTFTools.pause(STARTUP_DELAY)
        while not program.isStarted():
            try:
                wait(STARTUP_CYCLE)
            except InterruptedException as ex:
                pass

    def componentHidden(self, e):
        """ generated source for method componentHidden """

    def componentMoved(self, e):
        """ generated source for method componentMoved """

    def componentResized(self, e):
        """ generated source for method componentResized """
        componentShown(e)

    @synchronized
    def componentShown(self, e):
        """ generated source for method componentShown """
        notifyAll()

    STARTUP_DELAY = 1000
    STARTUP_CYCLE = 300


class ProgramFrame(JFrame):
    """ generated source for class ProgramFrame """
    def __init__(self, title):
        """ generated source for method __init__ """
        super(ProgramFrame, self).__init__(title)

    def update(self, g):
        """ generated source for method update """
        paint(g)


class ProgramContentPaneLayout(BorderLayout):
    """ generated source for class ProgramContentPaneLayout """
    def __init__(self, program):
        """ generated source for method __init__ """
        super(ProgramContentPaneLayout, self).__init__()
        myProgram = program

    def layoutContainer(self, parent):
        """ generated source for method layoutContainer """
        super(ProgramContentPaneLayout, self).layoutContainer(parent)
        if not myProgram.isAncestorOf(parent):
            psize = parent.getSize()
            insets = parent.getInsets()
            x = insets.left
            y = insets.top
            width = psize.width - insets.left - insets.right
            height = psize.height - insets.top - insets.bottom
            myProgram.setBounds(x, y, width, height)
            e = ComponentEvent(myProgram, ComponentEvent.COMPONENT_RESIZED)
            Toolkit.getDefaultToolkit().getSystemEventQueue().postEvent(e)

    myProgram = None


class ProgramAppletStub(AppletContext, AppletStub):
    """ generated source for class ProgramAppletStub """
    def __init__(self, program):
        """ generated source for method __init__ """
        super(ProgramAppletStub, self).__init__()
        applet = program

    def setFrame(self, frame_):
        """ generated source for method setFrame """
        enclosure = frame_

    def isActive(self):
        """ generated source for method isActive """
        return True

    def getDocumentBase(self):
        """ generated source for method getDocumentBase """
        return getCodeBase()

    def getCodeBase(self):
        """ generated source for method getCodeBase """
        try:
            return URL("file:" + getCanonicalPath("."))
        except MalformedURLException as ex:
            raise ErrorException("Error: Illegal document base URL")

    def getParameter(self, name):
        """ generated source for method getParameter """
        return None

    def getAppletContext(self):
        """ generated source for method getAppletContext """
        return self

    def appletResize(self, width, height):
        """ generated source for method appletResize """
        if enclosure == None:
            if not recursiveResizeCheck:
                recursiveResizeCheck = True
                applet.resize(width, height)
                applet.validate()
                recursiveResizeCheck = False
        else:
            enclosure.setSize(width, height)
            enclosure.validate()

    def getAudioClip(self, url):
        """ generated source for method getAudioClip """
        clip = None
        if clip == None:
            clip = getNewAudioClip(url)
        return clip

    def getImage(self, url):
        """ generated source for method getImage """
        try:
            content = url.getContent()
            if isinstance(content, (ImageProducer, )):
                return applet.createImage(content)
        except IOError as ex:
            pass
        return None

    def getApplet(self, name):
        """ generated source for method getApplet """
        return None

    def getApplets(self):
        """ generated source for method getApplets """
        return Vector().elements()

    @overloaded
    def showDocument(self, url):
        """ generated source for method showDocument """
        if applet != None:
            applet.getAppletContext().showDocument(url)

    @showDocument.register(object, URL, str)
    def showDocument_0(self, url, target):
        """ generated source for method showDocument_0 """
        if applet != None:
            applet.getAppletContext().showDocument(url, target)

    def showStatus(self, status):
        """ generated source for method showStatus """
        if applet == None:
            print(status)
        else:
            applet.showStatus(status)

    def setStream(self, key, stream):
        """ generated source for method setStream """
        raise ErrorException("setStream: unimplemented operation")

    def getStream(self, key):
        """ generated source for method getStream """
        raise ErrorException("getStream: unimplemented operation")

    def getStreamKeys(self):
        """ generated source for method getStreamKeys """
        raise ErrorException("getStreamKeys: unimplemented operation")

    def getCanonicalPath(self, start):
        """ generated source for method getCanonicalPath """
        path = File(start).getAbsolutePath()
        sp = int()
        while (sp = path.indexOf(' ')) != -1:
            path = path.substring(0, sp) + "%20" + path.substring(sp + 1)
        return path

    @synchronized
    def getNewAudioClip(self, url):
        """ generated source for method getNewAudioClip """
        try:
            type_ = Class.forName("java.applet.Applet")
            types = [Class.forName("java.net.URL")]
            args = [url]
            fn = type_.getMethod("newAudioClip", types)
            return fn.invoke(None, args)
        except Exception as ex:
            return None

    applet = None
    enclosure = None
    recursiveResizeCheck = bool()


class DefaultActionListener(ActionListener):
    """ generated source for class DefaultActionListener """
    def __init__(self):
        """ generated source for method __init__ """
        super(DefaultActionListener, self).__init__()

    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        comp = e.getSource()
        program = findProgram(comp)
        if program != None and countActionListeners(comp) > 1:
            try:
                types = [Class.forName("java.awt.event.ActionListener")]
                args = [self]
                removeActionListener = comp.__class__.getMethod("removeActionListener", types)
                removeActionListener.invoke(comp, args)
                return
            except Exception as ex:
                raise ErrorException(ex)
        message = "No ActionListener is attached"
        if isinstance(comp, (Button, )):
            message += " to button " + (comp).getLabel()
        else:
            try:
                getText = comp.__class__.getMethod("getText", [None] * 0)
                message += " to button " + str(getText.invoke(comp, [None] * 0))
            except Exception as ex:
                raise ErrorException(ex)
        if program == None:
            raise ErrorException(message)
        else:
            program.getDialog().showErrorMessage(message)

    @classmethod
    def countActionListeners(cls, comp):
        """ generated source for method countActionListeners """
        try:
            getActionListeners = comp.__class__.getMethod("getActionListeners", [None] * 0)
            listeners = getActionListeners.invoke(comp, [None] * 0)
            len(listeners) len(listeners)
        except Exception as ex:
            return -1

    def findProgram(self, comp):
        """ generated source for method findProgram """
        if isinstance(comp, (Program, )):
            return comp
        elif comp != None:
            return self.findProgram(comp.getParent())
        else:
            return None


if __name__ == '__main__':
    import sys
    Program.main(sys.argv)

