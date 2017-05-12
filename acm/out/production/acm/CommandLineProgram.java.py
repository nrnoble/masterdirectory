#!/usr/bin/env python
""" generated source for module CommandLineProgram """
from __future__ import print_function
# 
#  * @(#)CommandLineProgram.java   1.99.1 08/12/08
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
#  Class introduced in V1.1
# package: acm.program
# 
#  * This class simulates the functionality of a <code>ConsoleProgram</code>
#  * in an environment that lacks a graphics context. As of JDK 1.4, it is
#  * illegal even to instantiate an applet in a non-graphics environment
#  * (called "headless" in the Java terminology), which means that the program
#  * can no longer extend <code>Applet</code> or <code>JApplet</code>.  This
#  * class creates a stripped-down program class that duplicates the operation
#  * of a <code>ConsoleProgram</code> using the standard I/O streams.
#  
class CommandLineProgram(IOModel, Runnable, MouseListener, MouseMotionListener, KeyListener, ActionListener):
    """ generated source for class CommandLineProgram """
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

    #  Default constructor: CommandLineProgram 
    # 
    #  * This code initializes the program data structures.
    #  
    def __init__(self):
        """ generated source for method __init__ """
        super(CommandLineProgram, self).__init__()
        parameterTable = None
        finalizers = ArrayList()
        myTitle = getClass().__name__
        myTitle = myTitle.substring(myTitle.lastIndexOf(".") + 1)
        setConsole(createConsole())

    #  Static method: checkIfHeadless(className) 
    # 
    #  * Checks to see if the program is running in a headless environment and, if so,
    #  * runs it in that form.  If the environment is indeed headless, this call never
    #  * returns.
    #  *
    #  * @param className The name of the main class
    #  
    @classmethod
    def checkIfHeadless(cls, className):
        """ generated source for method checkIfHeadless """
        if not JTFTools.testDebugOption("headless"):
            try:
                graphicsEnvironmentClass = Class.forName("java.awt.GraphicsEnvironment")
                isHeadless = graphicsEnvironmentClass.getMethod("isHeadless", [None] * 0)
                if not Boolean.TRUE == isHeadless.invoke(None, [None] * 0):
                    return
            except Exception as ex:
                return
        try:
            loader = CommandLineProgramLoader(className)
            mainClass = loader.loadClass(className)
            program = mainClass.newInstance()
            program.init()
            program.run()
            program.exit()
        except Exception as ex:
            raise ErrorException(ex)

    #  Method: run() 
    # 
    #  * Contains the code to be executed for each specific program subclass.  If
    #  * you are defining your own program, you need to override the definition of
    #  * <code>run</code> so that it contains the code for your application.
    #  
    def run(self):
        """ generated source for method run """
        #  Empty 

    #  Method: init() 
    # 
    #  * The init method is called at startup time before the run method is
    #  * called.  Subclasses can override this method to perform any
    #  * initialization code that would ordinarily be included in an applet
    #  * <code>init</code> method.  This method is used only for certain styles
    #  * of application development that have their roots in the applet world;
    #  * other styles will not ordinarily use or override this method.
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
        return False

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

    #  Method: getDialog() 
    # 
    #  * Returns the dialog used for user interaction.
    #  *
    #  * @usage IODialog dialog = program.getDialog();
    #  * @return The <code>IODialog</code> object used for this program
    #  
    def getDialog(self):
        """ generated source for method getDialog """
        return None

    #  Method: getInputModel() 
    # 
    #  * Returns the <code>IOModel</code> used for program input, which will
    #  * typically be either the default <code>IOConsole</code> or <code>IODialog</code> object.
    #  *
    #  * @usage IOModel io = program.getInputModel();
    #  * @return The <code>IOModel</code> used for program input
    #  
    def getInputModel(self):
        """ generated source for method getInputModel """
        return self.getConsole()

    #  Method: getOutputModel() 
    # 
    #  * Returns the <code>IOModel</code> used for program output, which will
    #  * typically be either the default <code>IOConsole</code> or <code>IODialog</code> object.
    #  *
    #  * @usage IOModel io = program.getOutputModel();
    #  * @return The <code>IOModel</code> used for program output
    #  
    def getOutputModel(self):
        """ generated source for method getOutputModel """
        return self.getConsole()

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
        if region != region:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

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
        if comp != comp:
            #  Avoid unused parameter warning 
        if region != region:
            #  Avoid unused parameter warning 
        if constraints != constraints:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

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
        raise ErrorException("No graphics environment")

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
        if listener != listener:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

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

    #  Method: start(args) 
    # 
    #  * Starts the program using the specified argument list.
    #  *
    #  * @usage program.start(args);
    #  * @param args An array of strings passed to the program
    #  
    def start(self, args):
        """ generated source for method start """
        if parameterTable == None and args != None:
            parameterTable = createParameterTable(args)
        self.init()
        self.run()

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
        raise ErrorException("No graphics environment")

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
        return Dimension(0, 0)

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
        return 0

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
        return 0

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
        return value

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
        if layout != layout:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

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
        raise ErrorException("No graphics environment")

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
        if color != color:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

    #  Overridden method: addImpl(comp, constraints, index) 
    # 
    #  * Adds the specified component to the content pane using the specified constraints and index.
    #  
    def addImpl(self, comp, constraints, index):
        """ generated source for method addImpl """
        if comp != comp:
            #  Avoid unused parameter warning 
        if constraints != constraints:
            #  Avoid unused parameter warning 
        if index != index:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

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
        if index != index:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

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
        if comp != comp:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

    #  Overridden method: removeAll() 
    # 
    #  * Removes all components from the central region.
    #  *
    #  * @usage removeAll();
    #  * @noshow
    #  
    def removeAll(self):
        """ generated source for method removeAll """
        raise ErrorException("No graphics environment")

    #  Overridden method: validate() 
    # 
    #  * Forwards validate to the content pane.
    #  *
    #  * @usage validate();
    #  * @noshow
    #  
    def validate(self):
        """ generated source for method validate """
        raise ErrorException("No graphics environment")

    #  Overridden method: repaint() 
    # 
    #  * Forwards repaint to the content pane.
    #  *
    #  * @usage repaint();
    #  * @noshow
    #  
    def repaint(self):
        """ generated source for method repaint """
        raise ErrorException("No graphics environment")

    #  Overridden method: destroy() 
    # 
    #  * Called when the program has been told to destroy itself.
    #  *
    #  * @usage program.destroy();
    #  * @noshow
    #  
    def destroy(self):
        """ generated source for method destroy """
        #  Empty 

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
            try:
                mainClass = Class.forName(className)
            except ClassNotFoundException as ex:
                pass
                #  Empty 
        if mainClass != None:
            try:
                obj = mainClass.newInstance()
                if isinstance(obj, (CommandLineProgram, )):
                    program = obj
                else:
                    raise ErrorException("Main class does not specify a program")
            except IllegalAccessException as ex:
                pass
                #  Empty 
            except InstantiationException as ex:
                pass
                #  Empty 
        if program == None:
            raise ErrorException("Cannot determine the main class.")
        program.setParameterTable(ht)
        program.start(None)

    # /
    #  Menu handling methods                                              
    # /
    #  Method: menuAction(cmd) 
    # 
    #  * Called whenever an action event is detected in the menu bar.  Most of
    #  * these actions are simply passed on to the appropriate console.
    #  
    def menuAction(self, cmd):
        """ generated source for method menuAction """
        if cmd != cmd:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

    #  Protected method: setMacMenuBarFlag(flag) 
    # 
    #  * Sets a flag indicating whether applications running on the Macintosh
    #  * should use standard Mac menus.  The default is <code>true</code>.
    #  * Setting this value to <code>false</code> means that Mac programs
    #  * use the same in-window <code>JMenuBar</code> approach used on other
    #  * platforms.
    #  *
    #  * @usage setMacMenuBarFlag(flag);
    #  * @param flag <code>true</code> to use Mac menu style; <code>false</code> otherwise
    #  
    def setMacMenuBarFlag(self, flag):
        """ generated source for method setMacMenuBarFlag """
        if flag != flag:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

    #  Protected method: getMacMenuBarFlag() 
    # 
    #  * Retrieves the setting of the Mac menu bar flag.
    #  *
    #  * @usage boolean flag = getMacMenuBarFlag();
    #  * @return <code>true</code> if Mac menu style is supported; <code>false</code> otherwise
    #  
    def getMacMenuBarFlag(self):
        """ generated source for method getMacMenuBarFlag """
        raise ErrorException("No graphics environment")

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
        if side != side:
            #  Avoid unused parameter warning 
        raise ErrorException("No graphics environment")

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
        raise ErrorException("No graphics environment")

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

    #  Private instance variables 
    parameterTable = None
    finalizers = None
    appletStub = None
    myTitle = None
    myConsole = None


class CommandLineProgramLoader(ClassLoader):
    """ generated source for class CommandLineProgramLoader """
    def __init__(self, name):
        """ generated source for method __init__ """
        super(CommandLineProgramLoader, self).__init__()
        targetName = name
        try:
            classLoader = Class.forName("java.lang.ClassLoader")
            getSystemClassLoader = classLoader.getMethod("getSystemClassLoader", [None] * 0)
            realLoader = getSystemClassLoader.invoke(None, [None] * 0)
        except Exception as ex:
            raise ErrorException(ex)

    def loadClass(self, name, resolve):
        """ generated source for method loadClass """
        if name == targetName:
            in_ = getResourceAsStream(name + ".class")
            superclassOffset = findSuperclassOffset(in_)
            in_ = getResourceAsStream(name + ".class")
            code_ = patchClassData(in_)
            return defineClass(name, code_, 0, )
        else:
            return realLoader.loadClass(name)

    def getResourceAsStream(self, name):
        """ generated source for method getResourceAsStream """
        return realLoader.getResourceAsStream(name)

    def getResource(self, name):
        """ generated source for method getResource """
        return realLoader.getResource(name)

    def patchClassData(self, in_):
        """ generated source for method patchClassData """
        try:
            out = ByteArrayOutputStream()
            JTFTools.copyBytes(in_, out, 8)
            nConstants = in_.read() << 8 | in_.read()
            out.write(nConstants >> 8)
            out.write(nConstants & 0xFF)
            index = 1
            while index < nConstants:
                type_ = in_.read()
                out.write(type_)
                if JTFTools.testDebugOption("constants"):
                    print(index + ": " + getConstantTypeName(type_))
                if type_ == CONSTANT_Integer:
                    JTFTools.copyBytes(in_, out, 4)
                elif type_ == CONSTANT_Float:
                    JTFTools.copyBytes(in_, out, 4)
                elif type_ == CONSTANT_Long:
                    JTFTools.copyBytes(in_, out, 8)
                    index += 1
                elif type_ == CONSTANT_Double:
                    JTFTools.copyBytes(in_, out, 8)
                    index += 1
                elif type_ == CONSTANT_Class:
                    JTFTools.copyBytes(in_, out, 2)
                elif type_ == CONSTANT_String:
                    JTFTools.copyBytes(in_, out, 2)
                elif type_ == CONSTANT_Fieldref:
                    JTFTools.copyBytes(in_, out, 4)
                elif type_ == CONSTANT_Methodref:
                    JTFTools.copyBytes(in_, out, 4)
                elif type_ == CONSTANT_InterfaceMethodref:
                    JTFTools.copyBytes(in_, out, 4)
                elif type_ == CONSTANT_NameAndType:
                    JTFTools.copyBytes(in_, out, 4)
                elif type_ == CONSTANT_Utf8:
                    if index == superclassOffset:
                        nChars = in_.read() << 8 | in_.read()
                        in_.skip(nChars)
                        superclass = "acm/program/CommandLineProgram"
                        nChars = len(superclass)
                        out.write(nChars >> 8)
                        out.write(nChars & 0xFF)
                        j = 0
                        while j < nChars:
                            out.write(int(superclass.charAt(j)))
                            j += 1
                    else:
                        nChars = in_.read() << 8 | in_.read()
                        out.write(nChars >> 8)
                        out.write(nChars & 0xFF)
                        JTFTools.copyBytes(in_, out, nChars)
                index += 1
            while True:
                ch = in_.read()
                if ch == -1:
                    break
                out.write(ch)
            return out.toByteArray()
        except IOError as ex:
            raise ErrorException(ex)

    def findSuperclassOffset(self, in_):
        """ generated source for method findSuperclassOffset """
        classTable = HashMap()
        try:
            in_.skip(8)
            nConstants = in_.read() << 8 | in_.read()
            nConstants += 2
            i = 1
            while i < nConstants - 2:
                type_ = in_.read()
                if type_ == CONSTANT_Integer:
                    in_.skip(4)
                elif type_ == CONSTANT_Float:
                    in_.skip(4)
                elif type_ == CONSTANT_Long:
                    in_.skip(8)
                    i += 1
                elif type_ == CONSTANT_Double:
                    in_.skip(8)
                    i += 1
                elif type_ == CONSTANT_String:
                    in_.skip(2)
                elif type_ == CONSTANT_Fieldref:
                    in_.skip(4)
                elif type_ == CONSTANT_Methodref:
                    in_.skip(4)
                elif type_ == CONSTANT_InterfaceMethodref:
                    in_.skip(4)
                elif type_ == CONSTANT_NameAndType:
                    in_.skip(4)
                elif type_ == CONSTANT_Class:
                    offset = in_.read() << 8 | in_.read()
                    classTable.put(int(i), int(offset))
                elif type_ == CONSTANT_Utf8:
                    nChars = in_.read() << 8 | in_.read()
                    in_.skip(nChars)
                i += 1
            in_.skip(4)
            return classTable.get(int(in_.read() << 8 | in_.read())).intValue()
        except IOError as ex:
            raise ErrorException(ex)

    @classmethod
    def getConstantTypeName(cls, id):
        """ generated source for method getConstantTypeName """
        if id == CONSTANT_Utf8:
            return "Utf8"
        elif id == CONSTANT_Integer:
            return "Integer"
        elif id == CONSTANT_Float:
            return "Float"
        elif id == CONSTANT_Long:
            return "Long"
        elif id == CONSTANT_Double:
            return "Double"
        elif id == CONSTANT_Class:
            return "Class"
        elif id == CONSTANT_String:
            return "String"
        elif id == CONSTANT_Fieldref:
            return "Fieldref"
        elif id == CONSTANT_Methodref:
            return "Methodref"
        elif id == CONSTANT_InterfaceMethodref:
            return "InterfaceMethodref"
        elif id == CONSTANT_NameAndType:
            return "NameAndType"
        else:
            return "Type[" + id + "]"

    CONSTANT_Utf8 = 1
    CONSTANT_Integer = 3
    CONSTANT_Float = 4
    CONSTANT_Long = 5
    CONSTANT_Double = 6
    CONSTANT_Class = 7
    CONSTANT_String = 8
    CONSTANT_Fieldref = 9
    CONSTANT_Methodref = 10
    CONSTANT_InterfaceMethodref = 11
    CONSTANT_NameAndType = 12
    classTable = None
    realLoader = None
    targetName = None
    superclassOffset = int()

CommandLineProgram.#  * @usage CommandLineProgram.checkIfHeadless(className);


if __name__ == '__main__':
    import sys
    CommandLineProgram.main(sys.argv)

