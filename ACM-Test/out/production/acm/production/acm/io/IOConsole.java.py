#!/usr/bin/env python
""" generated source for module IOConsole """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
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
#  * @(#)IOConsole.java   1.99.1 08/12/08
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
#  Bug fix 18-Feb-07 (ESR, JTFBug 2007-003, reported by Dale Skrien)
#    1. Fixed bug in ConsoleModel.clear.
# 
#  Bug fix 08-May-07 (ESR, JTFBug 2007-008)
#    1. Completely rewrote PrintConsole code which no longer worked in JDK 1.6.
# 
#  Code cleanup 21-May-08 (ESR)
#    1. Reimplemented menu bar code to correspond to overall redesign of
#       the ProgramMenuBar class.
# package: acm.io
#  Class: IOConsole 
# 
#  * The <code>IOConsole</code> class makes it easier to interact with
#  * the user using text-based input and output in the style of a
#  * traditional console.  Given a <code>IOConsole</code> object, you
#  * can write output to that console using the
#  * <a href="#print(String)"><code>print</code></a> and
#  * <a href="#println(String)"><code>println</code></a>
#  * methods, just as you would for the standard output stream.
#  * To request input from the user, the most common methods are
#  *
#  * <ul>
#  * <li><a href="#readInt()"><code>readInt</code></a>
#  * <li><a href="#readDouble()"><code>readDouble</code></a>
#  * <li><a href="#readBoolean()"><code>readBoolean</code></a>
#  * <li><a href="#readLine()"><code>readLine</code></a>
#  * </ul>
#  *
#  * <p>A <code>IOConsole</code> object is a lightweight component and must be
#  * added to an installed <code>Frame</code> or <code>JFrame</code> before it becomes
#  * visible on the screen.  The usual strategy for including a console in a frame is
#  * to use the <a href="../program/ConsoleProgram.html"><code>ConsoleProgram</code></a>
#  * mechanism in the <code>acm.program</code> package.
#  *
#  * The operation of the <code>IOConsole</code> class is illustrated by
#  * the following <code>test</code> method, which generates the session shown on
#  * the right.  The user input appears in <font color=blue>blue</font>,
#  * just as it does in the console window.
#  *
#  * <p><table><tr><td><pre><code>
#  * &nbsp;    public void test(IOConsole console) {
#  * &nbsp;       console.println("IOConsole class test");
#  * &nbsp;       int n = console.readInt("Enter an integer: ");
#  * &nbsp;       console.println("That integer was " + n);
#  * &nbsp;       double d = console.readDouble("Enter a real number: ");
#  * &nbsp;       console.println("That number was " + d);
#  * &nbsp;       boolean b = console.readBoolean("Enter a boolean value: ");
#  * &nbsp;       console.println("That value was " + b);
#  * &nbsp;       String line = console.readLine("Enter a line: ");
#  * &nbsp;       console.println("That line was \"" + line + "\"");
#  * &nbsp;    }
#  * </code></pre></td>
#  * <td width=260 align=right valign=top>
#  * <img src="../../../../images/ConsoleTest.gif">
#  * </td></tr></table>
#  
class IOConsole(Container, IOModel):
    """ generated source for class IOConsole """
    #  Constant: SYSTEM_CONSOLE 
    # 
    #  * This constant is an object that offers the functionality of the
    #  * <code>IOConsole</code> class, but which does so using the standard
    #  * I/O streams <code>System.in</code> and <code>System.out</code>.
    #  
    SYSTEM_CONSOLE = SystemConsole()

    #  Constructor: IOConsole() 
    # 
    #  * Creates a new <code>IOConsole</code> object.
    #  *
    #  * @usage IOConsole console = new IOConsole();
    #  
    def __init__(self):
        """ generated source for method __init__ """
        super(IOConsole, self).__init__()
        consoleModel = createConsoleModel()
        consoleModel.setConsole(self)
        setBackground(Color.WHITE)
        setInputColor(Color.BLUE)
        setInputStyle(Font.BOLD)
        setErrorColor(Color.RED)
        setErrorStyle(Font.BOLD)
        setFont(JTFTools.getStandardFont(DEFAULT_FONT))
        consolePane = consoleModel.getConsolePane()
        if consolePane != None:
            setLayout(BorderLayout())
            add(consolePane, BorderLayout.CENTER)
        reader = None
        writer = None
        exceptionOnError = False

    #  Method: clear() 
    # 
    #  * Clears the console display.
    #  *
    #  * @usage console.clear();
    #  
    def clear(self):
        """ generated source for method clear """
        consoleModel.clear()

    #  Method: print(value) 
    # 
    #  * Displays the argument value on the console, leaving the cursor at the end of
    #  * the output.  The <code>print</code> method is overloaded so that
    #  * <code>value</code> can be of any type.
    #  *
    #  * @usage console.print(value);
    #  * @param value The value to be displayed
    #  
    @overloaded
    def print_(self, value):
        """ generated source for method print_ """
        getWriter().print_(value)

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
    #  * @usage console.println();
    #  
    @overloaded
    def println(self):
        """ generated source for method println """
        getWriter().println()

    #  Method: println(value) 
    # 
    #  * Displays the argument value on the console and then advances the cursor
    #  * to the beginning of the next line.  The <code>println</code> method is
    #  * overloaded so that <code>value</code> can be of any type.
    #  *
    #  * @usage console.println(value);
    #  * @param value The value to be displayed
    #  
    @println.register(object, str)
    def println_0(self, value):
        """ generated source for method println_0 """
        getWriter().println(value)

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
    #  * Displays the error message on the console.
    #  *
    #  * @usage console.showErrorMessage(msg);
    #  * @param msg The error msg to be displayed
    #  
    def showErrorMessage(self, msg):
        """ generated source for method showErrorMessage """
        consoleModel.print_(msg, ConsoleModel.ERROR_STYLE)
        consoleModel.print_("\n", ConsoleModel.ERROR_STYLE)

    #  Method: readLine() 
    # 
    #  * Reads and returns a line of input from the console, without
    #  * including the end-of-line characters that terminate the input.
    #  *
    #  * @usage String str = console.readLine();
    #  * @return The next line of input as a <code>String</code>
    #  
    @overloaded
    def readLine(self):
        """ generated source for method readLine """
        return self.readLine(None)

    #  Method: readLine(prompt) 
    # 
    #  * Prompts the user to enter a line of text, which is then returned
    #  * as the value of this method.  The end-of-line characters that terminate
    #  * the input are not included in the returned string.
    #  *
    #  * @usage String str = console.readLine(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The next line of input as a <code>String</code>
    #  
    @readLine.register(object, str)
    def readLine_0(self, prompt):
        """ generated source for method readLine_0 """
        if prompt != None:
            self.print_(prompt)
        consoleModel.requestFocus()
        try:
            str_ = getReader().readLine()
            return str_
        except IOError as ex:
            raise ErrorException(ex)

    #  Method: readInt() 
    # 
    #  * Reads and returns an integer value from the user.  If the user types
    #  * a value that is not a legal integer, the method ordinarily offers the
    #  * user a chance to reenter the data, although this behavior can be
    #  * changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage int n = console.readInt();
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
    #  * @usage int n = console.readInt(low, high);
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
    #  * @usage int n = console.readInt(prompt);
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
        msg = None
        while True:
            line = self.readLine(prompt)
            try:
                n = Integer.parseInt(line)
                if n >= low and n <= high:
                    return n
                msg = "Value is outside the range [" + low + ":" + high + "]"
            except NumberFormatException as ex:
                msg = "Illegal numeric format"
            self.showErrorMessage(msg)
            if prompt == None:
                prompt = "Retry: "

    #  Method: readDouble() 
    # 
    #  * Reads and returns a double-precision value from the user.  If the user
    #  * types a value that is not a legal number, the method ordinarily offers
    #  * the user a chance to reenter the data, although this behavior can be
    #  * changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage double d = console.readDouble();
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
    #  * @usage double d = console.readDouble(low, high);
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
    #  * @usage double d = console.readDouble(prompt);
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
    #  * @usage d = console.readDouble(prompt, low, high);
    #  * @param prompt The prompt string to display to the user
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @readDouble.register(object, str, float, float)
    def readDouble_2(self, prompt, low, high):
        """ generated source for method readDouble_2 """
        msg = None
        while True:
            line = self.readLine(prompt)
            try:
                d = Double.valueOf(line).doubleValue()
                if d >= low and d <= high:
                    return d
                msg = "Value is outside the range [" + low + ":" + high + "]"
            except NumberFormatException as ex:
                msg = "Illegal numeric format"
            self.showErrorMessage(msg)
            if prompt == None:
                prompt = "Retry: "

    #  Method: readBoolean() 
    # 
    #  * Reads and returns a boolean value from the user, which must match
    #  * either <code>true</code> or <code>false</code>, ignoring case.
    #  * If the user types a value that is not one of these possibilities,
    #  * the method ordinarily offers the user a chance to reenter the data,
    #  * although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage boolean flag = console.readBoolean();
    #  * @return The value of the input interpreted as a boolean value
    #  
    @overloaded
    def readBoolean(self):
        """ generated source for method readBoolean """
        return self.readBoolean(None)

    #  Method: readBoolean(prompt) 
    # 
    #  * Prompts the user to enter a boolean value, which is then returned as
    #  * the value of this method.  If the user types a value that is not a
    #  * legal boolean value, the method ordinarily offers the user a chance
    #  * to reenter the data, although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage boolean flag = console.readBoolean(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The value of the input interpreted as a boolean value
    #  
    @readBoolean.register(object, str)
    def readBoolean_0(self, prompt):
        """ generated source for method readBoolean_0 """
        return self.readBoolean(prompt, "true", "false")

    #  Method: readBoolean(prompt, trueLabel, falseLabel) 
    # 
    #  * Prompts the user to enter a value, which is interpreted as a boolean value
    #  * by matching it against the <code>trueLabel</code> and <code>falseLabel</code>
    #  * parameters.  If the user types a value that is not one of the two choices,
    #  * <code>readBoolean</code> ordinarily offers the user a chance
    #  * to reenter the data, although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage boolean flag = console.readBoolean(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @param trueLabel The string used to indicate <code>true</code>
    #  * @param falseLabel The string used to indicate <code>false</code>
    #  * @return The value of the input interpreted as a boolean value
    #  
    @readBoolean.register(object, str, str, str)
    def readBoolean_1(self, prompt, trueLabel, falseLabel):
        """ generated source for method readBoolean_1 """
        while True:
            line = self.readLine(prompt)
            if line == None:
                raise ErrorException("End of file encountered")
            elif line.lower() == trueLabel.lower():
                return True
            elif line.lower() == falseLabel.lower():
                return False
            else:
                if exceptionOnError:
                    raise ErrorException("Illegal boolean format")
                self.showErrorMessage("Illegal boolean format")
                if prompt == None:
                    prompt = "Retry: "

    #  Method: getReader() 
    # 
    #  * Returns a <code>BufferedReader</code> object that can be used to read
    #  * from the console.
    #  *
    #  * @usage BufferedReader rd = console.getReader();
    #  * @return A <code>BufferedReader</code> that reads from this console
    #  
    def getReader(self):
        """ generated source for method getReader """
        if reader == None:
            reader = BufferedReader(ConsoleReader(consoleModel))
        return reader

    #  Method: getWriter() 
    # 
    #  * Returns a <code>PrintWriter</code> object that can be used to send
    #  * output to the console.
    #  *
    #  * @usage PrintWriter wr = console.getWriter();
    #  * @return A <code>PrintWriter</code> that writes to this console
    #  
    def getWriter(self):
        """ generated source for method getWriter """
        if writer == None:
            writer = PrintWriter(ConsoleWriter(consoleModel))
        return writer

    #  Method: setExceptionOnError(flag) 
    # 
    #  * Sets the error-handling mode of the console as specified by the <code>flag</code>
    #  * parameter.  If <code>flag</code> is <code>false</code> (which is the default), the
    #  * input methods give the user a chance to retry after erroneous input.  If this
    #  * value is set to <code>true</code>, illegal input raises an
    #  * <a href="../util/ErrorException.html"><code>ErrorException</code></a> instead.
    #  *
    #  * @usage console.setExceptionOnError(flag);
    #  * @param flag <code>false</code> to retry on errors; <code>true</code> to raise an exception
    #  
    def setExceptionOnError(self, flag):
        """ generated source for method setExceptionOnError """
        exceptionOnError = flag

    #  Method: getExceptionOnError() 
    # 
    #  * Returns the state of the error-handling flag.
    #  *
    #  * @usage boolean flag = console.getExceptionOnError();
    #  * @return The current setting of the error-handling mode (<code>false</code> to retry
    #  *         on errors; <code>true</code> to raise an exception)
    #  
    def getExceptionOnError(self):
        """ generated source for method getExceptionOnError """
        return exceptionOnError

    #  Method: setInputStyle(style) 
    # 
    #  * Sets the style parameters for console input.  The style parameter
    #  * is either <code>Font.PLAIN</code> or a sum of one or more of the attributes
    #  * <code>Font.BOLD</code> and <code>Font.ITALIC</code>.
    #  *
    #  * @usage console.setInputStyle(style);
    #  * @param style The style attributes to be used for console input
    #  * @noshow
    #  
    def setInputStyle(self, style):
        """ generated source for method setInputStyle """
        inputStyle = style
        consoleModel.setInputStyle(style)

    #  Method: getInputStyle() 
    # 
    #  * Returns the current style parameters for console input.
    #  *
    #  * @usage int style = console.getInputStyle();
    #  * @return The current input style
    #  * @noshow
    #  
    def getInputStyle(self):
        """ generated source for method getInputStyle """
        return inputStyle

    #  Method: setInputColor(color) 
    # 
    #  * Sets the color used for console input.
    #  *
    #  * @usage console.setInputColor(color);
    #  * @param color The color used for console input
    #  * @noshow
    #  
    def setInputColor(self, color):
        """ generated source for method setInputColor """
        inputColor = color
        consoleModel.setInputColor(color)

    #  Method: getInputColor() 
    # 
    #  * Returns the color currently in use for console input.
    #  *
    #  * @usage Color color = console.getInputColor();
    #  * @return The current input color
    #  * @noshow
    #  
    def getInputColor(self):
        """ generated source for method getInputColor """
        return inputColor

    #  Method: setErrorStyle(style) 
    # 
    #  * Sets the style parameters for console error messages.  The style parameter
    #  * is either <code>Font.PLAIN</code> or a sum of one or more of the attributes
    #  * <code>Font.BOLD</code> and <code>Font.ITALIC</code>.
    #  *
    #  * @usage console.setErrorStyle(style);
    #  * @param style The style attributes to be used for console error messages
    #  * @noshow
    #  
    def setErrorStyle(self, style):
        """ generated source for method setErrorStyle """
        errorStyle = style
        consoleModel.setErrorStyle(style)

    #  Method: getErrorStyle() 
    # 
    #  * Returns the current style parameters for console error messages.
    #  *
    #  * @usage int style = console.getErrorStyle();
    #  * @return The current error message style
    #  * @noshow
    #  
    def getErrorStyle(self):
        """ generated source for method getErrorStyle """
        return errorStyle

    #  Method: setErrorColor(color) 
    # 
    #  * Sets the color used for console error messages.
    #  *
    #  * @usage console.setErrorColor(color);
    #  * @param color The color used for console error messages
    #  * @noshow
    #  
    def setErrorColor(self, color):
        """ generated source for method setErrorColor """
        errorColor = color
        consoleModel.setErrorColor(color)

    #  Method: getErrorColor() 
    # 
    #  * Returns the color currently in use for console error messages.
    #  *
    #  * @usage Color color = console.getErrorColor();
    #  * @return The current error message color
    #  * @noshow
    #  
    def getErrorColor(self):
        """ generated source for method getErrorColor """
        return errorColor

    #  Method: setFont(str) 
    # 
    #  * Sets the font used for the console as specified by
    #  * the string <code>str</code>, which is interpreted in the style of
    #  * <code>Font.decode</code>.  The usual format of the font string is
    #  *
    #  * <p>   <i>family</i><code>-</code><i>style</i><code>-</code><i>size</i><p>
    #  *
    #  * where both <i>style</i> and <i>size</i> are optional.  If any of these parts
    #  * are specified as an asterisk, the existing value is retained.
    #  *
    #  * @usage console.setFont(str);
    #  * @param str A <code>String</code> specifying the new font
    #  
    @overloaded
    def setFont(self, str_):
        """ generated source for method setFont """
        self.setFont(JTFTools.decodeFont(str_, getFont()))

    #  Method: setInputScript(rd) 
    # 
    #  * Sets a new input script for the console, which will subsequently
    #  * take input from the specified reader.  When the input from the reader
    #  * has been exhausted, the console returns to its normal operation.  This
    #  * method is primarily useful for demonstrations and test suites, and is
    #  * not ordinarily invoked by students.
    #  *
    #  * @usage console.setInputScript(rd);
    #  * @param rd The reader from which console input is taken
    #  * @noshow
    #  
    def setInputScript(self, rd):
        """ generated source for method setInputScript """
        consoleModel.setInputScript(rd)

    #  Method: getInputScript() 
    # 
    #  * Retrieves the input script.  After the end of the input script has been
    #  * reached, this method will return <code>null</code>.
    #  *
    #  * @usage BufferedReader rd = console.getInputScript();
    #  * @return The reader representing the current input script
    #  
    def getInputScript(self):
        """ generated source for method getInputScript """
        return consoleModel.getInputScript()

    #  Method: cut() 
    # 
    #  * Implements the "Cut" menu operation.
    #  *
    #  * @usage console.cut();
    #  * @noshow
    #  
    def cut(self):
        """ generated source for method cut """
        consoleModel.cut()

    #  Method: copy() 
    # 
    #  * Implements the "Copy" menu operation.
    #  *
    #  * @usage console.copy();
    #  * @noshow
    #  
    def copy(self):
        """ generated source for method copy """
        consoleModel.copy()

    #  Method: paste() 
    # 
    #  * Implements the "Paste" menu operation.
    #  *
    #  * @usage console.paste();
    #  * @noshow
    #  
    def paste(self):
        """ generated source for method paste """
        consoleModel.paste()

    #  Method: selectAll() 
    # 
    #  * Implements the "Select All" menu operation.
    #  *
    #  * @usage console.selectAll();
    #  * @noshow
    #  
    def selectAll(self):
        """ generated source for method selectAll """
        consoleModel.selectAll()

    #  Method: save() 
    # 
    #  * Implements the "Save" menu operation.
    #  *
    #  * @usage console.save();
    #  * @noshow
    #  
    @overloaded
    def save(self):
        """ generated source for method save """
        wr = None
        while wr == None:
            try:
                if file_ == None:
                    frame_ = JTFTools.getEnclosingFrame(self)
                    if frame_ == None:
                        return
                    dir = System.getProperty("user.dir")
                    dialog = FileDialog(frame_, "Save Console As", FileDialog.SAVE)
                    dialog.setDirectory(dir)
                    dialog.setVisible(True)
                    filename = dialog.getFile()
                    if filename == None:
                        return
                    file_ = File(dialog.getDirectory(), filename)
                wr = FileWriter(file_)
                self.save(wr)
                wr.close()
                Platform.setFileTypeAndCreator(file_, "TEXT", "ttxt")
            except IOError as ex:
                dialog = IODialog(self)
                dialog.showErrorMessage(ex.getMessage())

    #  Method: saveAs() 
    # 
    #  * Implements the "Save As" menu operation.
    #  *
    #  * @usage console.saveAs();
    #  * @noshow
    #  
    def saveAs(self):
        """ generated source for method saveAs """
        file_ = None
        self.save()

    #  Method: save(wr) 
    # 
    #  * Copies the console output to the specified writer.
    #  *
    #  * @usage console.save(wr);
    #  * @param wr A <code>Writer</code> to which the console output is sent
    #  * @noshow
    #  
    @save.register(object, Writer)
    def save_0(self, wr):
        """ generated source for method save_0 """
        try:
            wr.write(consoleModel.getText())
        except IOError as ex:
            raise ErrorException(ex)

    #  Method: printConsole() 
    # 
    #  * Implements the "Print Console" menu operation.
    #  *
    #  * @usage console.printConsole();
    #  * @noshow
    #  
    @overloaded
    def printConsole(self):
        """ generated source for method printConsole """
        frame_ = JTFTools.getEnclosingFrame(self)
        if frame_ == None:
            return
        pj = getToolkit().getPrintJob(frame_, "Console", None)
        if pj == None:
            return
        self.printConsole(pj)
        pj.end()

    #  Method: printConsole(pj) 
    # 
    #  * Prints the console output using the specified <code>PrintJob</code> object.
    #  * This method is usually invoked from the <code>Print</code> menu item in
    #  * the <code>ProgramMenuBar</code> class and is not ordinarily called by clients.
    #  *
    #  * @usage console.printConsole(pj);
    #  * @param pj <code>PrintJob</code> object to which the output is sent
    #  * @noshow
    #  
    @printConsole.register(object, PrintJob)
    def printConsole_0(self, pj):
        """ generated source for method printConsole_0 """
        consoleModel.print_(pj)

    #  Method: script() 
    # 
    #  * Implements the "Script" menu operation.
    #  *
    #  * @usage console.script();
    #  * @noshow
    #  
    def script(self):
        """ generated source for method script """
        frame_ = JTFTools.getEnclosingFrame(self)
        dialog = FileDialog(frame_, "Input Script", FileDialog.LOAD)
        dialog.setDirectory(System.getProperty("user.dir"))
        dialog.setVisible(True)
        dirname = dialog.getDirectory()
        filename = dialog.getFile()
        if filename != None:
            try:
                rd = FileReader(File(File(dirname), filename))
                self.setInputScript(BufferedReader(rd))
            except IOError as ex:
                raise ErrorException(ex)

    #  Method: setMenuBar(mbar) 
    # 
    #  * Sets the menu bar that controls this console.
    #  *
    #  * @usage console.setMenuBar(mbar);
    #  * @param mbar The menu bar
    #  
    def setMenuBar(self, mbar):
        """ generated source for method setMenuBar """
        menuBar = mbar
        consoleModel.setMenuBar(mbar)

    #  Method: getMenuBar() 
    # 
    #  * Returns the menu bar that controls this console.
    #  *
    #  * @usage ProgramMenuBar mbar = console.getMenuBar();
    #  * @return The menu bar
    #  
    def getMenuBar(self):
        """ generated source for method getMenuBar """
        return menuBar

    #  Method: menuAction(e) 
    # 
    #  * Called whenever a relevant action is detected in the menu bar.
    #  * Subclasses can override this method to extend the set of menu
    #  * commands recognized by the console.
    #  
    def menuAction(self, e):
        """ generated source for method menuAction """
        cmd = e.getActionCommand()
        if cmd == "Cut":
            self.cut()
            return True
        elif cmd == "Copy":
            self.copy()
            return True
        elif cmd == "Paste":
            self.paste()
            return True
        elif cmd == "Select All":
            self.selectAll()
            return True
        elif cmd == "Save":
            self.save()
            return True
        elif cmd == "Save As":
            self.saveAs()
            return True
        elif cmd == "Script":
            self.script()
            return True
        elif cmd == "Print Console":
            self.printConsole()
            return True
        return False

    #  Method: isConsoleMenuItem(item) 
    # 
    #  * Returns <code>true</code> if the item is one that the console recognizes.
    #  
    def isConsoleMenuItem(self, item):
        """ generated source for method isConsoleMenuItem """
        cmd = item.getActionCommand()
        if cmd == None:
            return False
        i = 0
        while len(CONSOLE_MENU_ACTIONS):
            if cmd == CONSOLE_MENU_ACTIONS[i]:
                return True
            i += 1
        return False

    #  Method: updateMenuBar(mbar) 
    # 
    #  * Updates the menu bar to enable the appropriate menu items.
    #  
    def updateMenuBar(self, mbar):
        """ generated source for method updateMenuBar """
        iterator = mbar.iterator()
        while iterator.hasNext():
            item = iterator.next()
            if self.isConsoleMenuItem(item):
                item.setEnabled(True)
            else:
                item.setEnabled(not mbar.isFocusedItem(item))

    #  Override method: setBackground(color) 
    # 
    #  * Sets the background color used for the console.
    #  *
    #  * @usage console.setBackground(color);
    #  * @param color The new background color
    #  
    def setBackground(self, color):
        """ generated source for method setBackground """
        textPane = consoleModel.getTextPane()
        if textPane != None:
            textPane.setBackground(color)
        super(IOConsole, self).setBackground(color)

    #  Override method: setForeground(color) 
    # 
    #  * Sets the foreground color used for the output text.
    #  *
    #  * @usage console.setForeground(color);
    #  * @param color The color to use for the output text
    #  
    def setForeground(self, color):
        """ generated source for method setForeground """
        textPane = consoleModel.getTextPane()
        if textPane != None:
            textPane.setForeground(color)
        super(IOConsole, self).setForeground(color)

    #  Override method: setFont(font) 
    # 
    #  * Sets the font for the console.
    #  *
    #  * @usage console.setFont(font);
    #  * @param font The font to use for the console
    #  
    @setFont.register(object, Font)
    def setFont_0(self, font):
        """ generated source for method setFont_0 """
        font = JTFTools.getStandardFont(font)
        textPane = consoleModel.getTextPane()
        if textPane != None:
            textPane.setFont(font)
        super(IOConsole, self).setFont(font)

    #  Override method: requestFocus() 
    # 
    #  * Overrides the <code>requestFocus</code> method so that it forwards to the
    #  * console model.
    #  *
    #  * @usage console.requestFocus();
    #  * @noshow
    #  
    def requestFocus(self):
        """ generated source for method requestFocus """
        consoleModel.requestFocus()

    #  Override method: getPreferredSize() 
    # 
    #  * Overrides the <code>getPreferredSize</code> method to ensure that an
    #  * <code>IOConsole</code> is not too large.
    #  *
    #  * @usage Dimension size = console.getPreferredSize();
    #  * @noshow
    #  
    def getPreferredSize(self):
        """ generated source for method getPreferredSize """
        return getMinimumSize()

    #  Override method: getMinimumSize() 
    # 
    #  * Overrides the <code>getMinimumSize</code> method to ensure that an
    #  * <code>IOConsole</code> is not too large.
    #  *
    #  * @usage Dimension size = console.getMinimumSize();
    #  * @noshow
    #  
    def getMinimumSize(self):
        """ generated source for method getMinimumSize """
        return Dimension(MINIMUM_CONSOLE_WIDTH, MINIMUM_CONSOLE_HEIGHT)

    #  Protected method: createConsoleModel() 
    # 
    #  * Creates the console model used by this console.
    #  
    def createConsoleModel(self):
        """ generated source for method createConsoleModel """
        return StandardConsoleModel()

    #  Protected constant: DEFAULT_FONT 
    # 
    #  * The default font used by a new <code>IOConsole</code>.
    #  
    DEFAULT_FONT = Font("Monospaced", Font.PLAIN, 12)

    #  Protected constant: LINE_SEPARATOR 
    # 
    #  * The end-of-line separator for this platform.
    #  
    LINE_SEPARATOR = System.getProperty("line.separator")

    #  Protected constant: MINIMUM_CONSOLE_WIDTH 
    # 
    #  * The minimum width for a console.
    #  
    MINIMUM_CONSOLE_WIDTH = 50

    #  Protected constant: MINIMUM_CONSOLE_HEIGHT 
    # 
    #  * The minimum height for a console.
    #  
    MINIMUM_CONSOLE_HEIGHT = 40

    #  Private constants 
    CONSOLE_MENU_ACTIONS = ["Save", "Save As", "Print Console", "Script", "Cut", "Copy", "Paste", "Select All"]

    #  Private instance variables 
    consoleModel = None
    exceptionOnError = bool()
    inputColor = None
    inputStyle = int()
    errorColor = None
    errorStyle = int()
    reader = None
    writer = None
    file_ = None
    menuBar = None

#  Package interface: ConsoleModel 
# 
#  * This interface defines the operations that any console model must implement.
#  
class ConsoleModel(object):
    """ generated source for interface ConsoleModel """
    __metaclass__ = ABCMeta
    #  Constants for display types 
    OUTPUT_STYLE = 0
    INPUT_STYLE = 1
    ERROR_STYLE = 2

    #  Method signatures 
    @abstractmethod
    def setConsole(self, owner):
        """ generated source for method setConsole """

    @abstractmethod
    def getConsole(self):
        """ generated source for method getConsole """

    @abstractmethod
    @overloaded
    def print_(self, str_, style):
        """ generated source for method print_ """

    @abstractmethod
    def readLine(self):
        """ generated source for method readLine """

    @abstractmethod
    def setInputScript(self, rd):
        """ generated source for method setInputScript """

    @abstractmethod
    def getInputScript(self):
        """ generated source for method getInputScript """

    @abstractmethod
    def clear(self):
        """ generated source for method clear """

    @abstractmethod
    @overloaded
    def getText(self):
        """ generated source for method getText """

    @abstractmethod
    @getText.register(object, int, int)
    def getText_0(self, start, end):
        """ generated source for method getText_0 """

    @abstractmethod
    def getLength(self):
        """ generated source for method getLength """

    @abstractmethod
    def getConsolePane(self):
        """ generated source for method getConsolePane """

    @abstractmethod
    def getTextPane(self):
        """ generated source for method getTextPane """

    @abstractmethod
    def cut(self):
        """ generated source for method cut """

    @abstractmethod
    def copy(self):
        """ generated source for method copy """

    @abstractmethod
    def paste(self):
        """ generated source for method paste """

    @abstractmethod
    def selectAll(self):
        """ generated source for method selectAll """

    @abstractmethod
    def isPointSelection(self):
        """ generated source for method isPointSelection """

    @abstractmethod
    @print_.register(object, PrintJob)
    def print__0(self, pj):
        """ generated source for method print__0 """

    @abstractmethod
    def setInputStyle(self, style):
        """ generated source for method setInputStyle """

    @abstractmethod
    def setInputColor(self, color):
        """ generated source for method setInputColor """

    @abstractmethod
    def setErrorStyle(self, style):
        """ generated source for method setErrorStyle """

    @abstractmethod
    def setErrorColor(self, color):
        """ generated source for method setErrorColor """

    @abstractmethod
    def requestFocus(self):
        """ generated source for method requestFocus """

    @abstractmethod
    def setMenuBar(self, mbar):
        """ generated source for method setMenuBar """

#  Package class: StandardConsoleModel 
# 
#  * This class implements the console model using Swing.
#  
class StandardConsoleModel(KeyListener, FocusListener, ConsoleModel):
    """ generated source for class StandardConsoleModel """
    #  Constructor: StandardConsoleModel() 
    # 
    #  * Creates the framework for the standard console models.
    #  
    def __init__(self):
        """ generated source for method __init__ """
        super(StandardConsoleModel, self).__init__()
        outputMonitor = ConsoleOutputMonitor(self)
        inputMonitor = ConsoleInputMonitor(self)
        scrollPane = JScrollPane(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS)
        textPane = JTextPane()
        textPane.addKeyListener(self)
        textPane.addFocusListener(self)
        scrollPane.setViewportView(textPane)
        document = textPane.getDocument()
        lineSeparator = System.getProperty("line.separator")
        outputAttributes = SimpleAttributeSet()
        inputAttributes = SimpleAttributeSet()
        errorAttributes = SimpleAttributeSet()
        buffer_ = CharacterQueue()
        base = 0

    #  Method: setConsole(owner) 
    # 
    #  * Sets the identity of the owning console.  This method must be called after
    #  * creating the model object.
    #  
    def setConsole(self, owner):
        """ generated source for method setConsole """
        console = owner

    #  Method: getConsole(console) 
    # 
    #  * Returns the associated console.
    #  
    def getConsole(self):
        """ generated source for method getConsole """
        return console

    #  Method: print(str, style) 
    # 
    #  * Prints the string to the console.
    #  
    @overloaded
    def print_(self, str_, style):
        """ generated source for method print_ """
        outputMonitor.print_(str_, style)

    #  Method: readLine() 
    # 
    #  * Reads and returns the next line of text from the console.
    #  
    def readLine(self):
        """ generated source for method readLine """
        return inputMonitor.readLine()

    #  Method: setInputScript(rd) 
    # 
    #  * Sets a new input script for the console, which will subsequently
    #  * take input from the specified reader.
    #  
    def setInputScript(self, rd):
        """ generated source for method setInputScript """
        inputScript = rd
        if buffer_.isWaiting():
            try:
                line = inputScript.readLine()
                buffer_.enqueue(line + "\n")
            except IOError as ex:
                raise ErrorException(ex)

    #  Method: getInputScript() 
    # 
    #  * Retrieves the input script.  After the end of the input script has been
    #  * reached, this method will return <code>null</code>.
    #  
    def getInputScript(self):
        """ generated source for method getInputScript """
        return inputScript

    #  Method: clear() 
    # 
    #  * Clears the console pane.
    #  
    def clear(self):
        """ generated source for method clear """
        textPane.setText("")
        base = 0
        buffer_.clear()

    #  Method: getText() 
    # 
    #  * Returns the text stored in the console model.
    #  
    @overloaded
    def getText(self):
        """ generated source for method getText """
        return textPane.getText()

    #  Method: getText(start, end) 
    # 
    #  * Returns a substring from the text using endpoints defined as in
    #  * <code>substring</code> for strings.
    #  
    @getText.register(object, int, int)
    def getText_0(self, start, end):
        """ generated source for method getText_0 """
        try:
            return document.getText(start, end - start)
        except BadLocationException as ex:
            raise ErrorException(ex)

    #  Method: getLength() 
    # 
    #  * Returns the length of the text stored in the console model.
    #  
    def getLength(self):
        """ generated source for method getLength """
        return document.getLength()

    #  Method: getConsolePane() 
    # 
    #  * Returns the top-level component that represents the console.  This is the
    #  * pane that needs to be added to a parent.
    #  
    def getConsolePane(self):
        """ generated source for method getConsolePane """
        return scrollPane

    #  Method: getTextPane() 
    # 
    #  * Returns the component that holds the text.  This is the pane to which
    #  * messages like <code>setFont</code> and <code>requestFocus</code> should
    #  * be directed.
    #  
    def getTextPane(self):
        """ generated source for method getTextPane """
        return textPane

    #  Method: cut() 
    # 
    #  * Implements the "cut" menu operation.
    #  
    def cut(self):
        """ generated source for method cut """
        copy()
        deleteSelection()

    #  Method: copy() 
    # 
    #  * Implements the "copy" menu operation.
    #  
    def copy(self):
        """ generated source for method copy """
        textPane.copy()

    #  Method: paste() 
    # 
    #  * Implements the "paste" menu operation.
    #  
    def paste(self):
        """ generated source for method paste """
        if textPane.getSelectionEnd() != document.getLength():
            return
        start = deleteSelection()
        textPane.setSelectionStart(start)
        textPane.paste()
        textPane.select(document.getLength(), document.getLength())
        if isinstance(document, (DefaultStyledDocument, )):
            doc = document
            doc.setCharacterAttributes(start, textPane.getSelectionEnd() - start, inputAttributes, True)

    #  Method: selectAll() 
    # 
    #  * Implements the "select all" menu operation.
    #  
    def selectAll(self):
        """ generated source for method selectAll """
        textPane.selectAll()

    #  Method: isPointSelection() 
    def isPointSelection(self):
        """ generated source for method isPointSelection """
        return textPane.getSelectionStart() == textPane.getSelectionEnd()

    #  Method: print(pj) 
    # 
    #  * Prints the entire console using the specified <code>PrintJob</code> object.
    #  
    @print_.register(object, PrintJob)
    def print__0(self, pj):
        """ generated source for method print__0 """
        g = pj.getGraphics()
        pageSize = pj.getPageDimension()
        fm = textPane.getFontMetrics(textPane.getFont())
        fontHeight = fm.getHeight()
        fontAscent = fm.getAscent()
        x = PRINT_MARGIN
        y = PRINT_MARGIN + fontAscent
        linesPerPage = (pageSize.height - 2 * PRINT_MARGIN) / fontHeight
        linesRemaining = linesPerPage
        i = ElementIterator(document)
        while True:
            e = i.next()
            if e == None:
                break
            if e.isLeaf():
                try:
                    len = e.getEndOffset() - e.getStartOffset()
                    setStyleFromAttributes(g, e.getAttributes())
                    fm = g.getFontMetrics()
                    text = document.getText(e.getStartOffset(), len)
                    start = 0
                    while True:
                        last = False
                        delta = 1
                        eol = text.indexOf("\n", start)
                        if eol == -1:
                            eol = text.indexOf(lineSeparator, start)
                            if eol == -1:
                                eol = len(text)
                                last = True
                            else:
                                delta = len(lineSeparator)
                        if start < eol:
                            str_ = text.substring(start, eol)
                            g.drawString(str_, x, y)
                            x += fm.stringWidth(str_)
                        if last:
                            break
                        start = eol + delta
                        x = PRINT_MARGIN
                        y += fontHeight
                        linesRemaining -= 1
                        if linesRemaining <= 0:
                            g.dispose()
                            g = pj.getGraphics()
                            y = PRINT_MARGIN + fontAscent
                            linesRemaining = linesPerPage
                except BadLocationException as ex:
                    raise ErrorException(ex)
        pj.end()

    #  Method: setInputStyle(style) 
    # 
    #  * Sets the style parameters for console input.  The style parameter
    #  * is either <code>Font.PLAIN</code> or a sum of one or more of the attributes
    #  * <code>Font.BOLD</code> and <code>Font.ITALIC</code>.
    #  
    def setInputStyle(self, style):
        """ generated source for method setInputStyle """
        if self.getLength() != 0:
            raise ErrorException("Console styles and colors cannot be changed after I/O has started.")
        inputAttributes.addAttribute(StyleConstants.Bold, bool((style & Font.BOLD) != 0))
        inputAttributes.addAttribute(StyleConstants.Italic, bool((style & Font.ITALIC) != 0))

    #  Method: setInputColor(color) 
    # 
    #  * Sets the color used for console input.
    #  
    def setInputColor(self, color):
        """ generated source for method setInputColor """
        if self.getLength() != 0:
            raise ErrorException("Console styles and colors cannot be changed after I/O has started.")
        inputAttributes.addAttribute(StyleConstants.Foreground, color)

    #  Method: setErrorStyle(style) 
    # 
    #  * Sets the style parameters for console error messages.  The style parameter
    #  * is either <code>Font.PLAIN</code> or a sum of one or more of the attributes
    #  * <code>Font.BOLD</code> and <code>Font.ITALIC</code>.
    #  
    def setErrorStyle(self, style):
        """ generated source for method setErrorStyle """
        if self.getLength() != 0:
            raise ErrorException("Console styles and colors cannot be changed after I/O has started.")
        errorAttributes.addAttribute(StyleConstants.Bold, bool((style & Font.BOLD) != 0))
        errorAttributes.addAttribute(StyleConstants.Italic, bool((style & Font.ITALIC) != 0))

    #  Method: setErrorColor(color) 
    # 
    #  * Sets the color used for console error.
    #  
    def setErrorColor(self, color):
        """ generated source for method setErrorColor """
        if self.getLength() != 0:
            raise ErrorException("Console styles and colors cannot be changed after I/O has started.")
        errorAttributes.addAttribute(StyleConstants.Foreground, color)

    #  Method: requestFocus() 
    # 
    #  * Forwards the request focus to the text pane.
    #  * @noshow
    #  
    def requestFocus(self):
        """ generated source for method requestFocus """
        if textPane != None:
            textPane.requestFocus()

    #  Method: setMenuBar(mbar) 
    # 
    #  * Sets the menu bar that controls this console.
    #  * @noshow
    #  
    def setMenuBar(self, mbar):
        """ generated source for method setMenuBar """
        menuBar = mbar

    #  Implementation of the FocusListener interface 
    #  Method: focusGained 
    # 
    #  * Called when focus is gained by the console.
    #  
    def focusGained(self, e):
        """ generated source for method focusGained """
        hasFocus = True
        if menuBar != None:
            if actionListener == None:
                actionListener = ConsoleActionListener(console)
            menuBar.setFocusedListener(actionListener)
            console.updateMenuBar(menuBar)

    #  Method: focusLost 
    # 
    #  * Called when focus is lost by the console.
    #  
    def focusLost(self, e):
        """ generated source for method focusLost """
        hasFocus = False
        if menuBar != None:
            menuBar.setFocusedListener(None)

    #  Implementation of the KeyListener interface 
    #  Method: keyTyped(e) 
    # 
    #  * Responds to a key being typed in the console pane. Implements <code>KeyListener</code>.
    #  
    def keyTyped(self, e):
        """ generated source for method keyTyped """
        if not e.isMetaDown() and not e.isControlDown():
            buffer_.enqueue(e.getKeyChar())
            e.consume()

    #  Method: keyPressed(e) 
    # 
    #  * Responds to key presses that do not correspond to typed keys.
    #  * Implements <code>KeyListener</code>.
    #  
    def keyPressed(self, e):
        """ generated source for method keyPressed """
        if e.getKeyCode() == KeyEvent.VK_LEFT:
            buffer_.enqueue('\002')
        elif e.getKeyCode() == KeyEvent.VK_RIGHT:
            buffer_.enqueue('\006')
        if menuBar != None:
            menuBar.fireAccelerator(e)
        e.consume()

    #  Method: keyReleased(e) 
    # 
    #  * Responds to the release of a key.  Implements <code>KeyListener</code>.
    #  * @noshow
    #  
    def keyReleased(self, e):
        """ generated source for method keyReleased """
        e.consume()

    #  Protected method: printCallback(str, style) 
    # 
    #  * Prints the string to the console.  Synchronization is provided by
    #  * the <code>ConsoleOutputMonitor</code> class.
    #  
    def printCallback(self, str_, style):
        """ generated source for method printCallback """
        insert(str_, base, style)
        base += len(str_)
        setCaretPosition(base)

    #  Protected method: readLineCallback() 
    # 
    #  * Reads and returns the next line of text from the console.
    #  * Synchronization is provided by the <code>ConsoleInputMonitor</code> class.
    #  
    def readLineCallback(self):
        """ generated source for method readLineCallback """
        base = self.getLength()
        if inputScript != None:
            line = None
            try:
                line = inputScript.readLine()
            except IOError as ex:
                raise ErrorException(ex)
            if line != None:
                insert(line, base, INPUT_STYLE)
                insert("\n", base + len(line), OUTPUT_STYLE)
                base += 1 + len(line)
                return line
            try:
                inputScript.close()
            except IOError as ex:
                pass
                #  Empty 
            inputScript = None
        dot = int()
        ch = str()
        setCaretPosition(base)
        while (ch = buffer_.dequeue()) != '\n' and ch != '\r':
            if getCaretPosition() < base:
                setCaretPosition(self.getLength())
            dot = getSelectionStart()
            if ch == '\b':
                pass
            elif ch == '\177':
                if dot == getSelectionEnd():
                    if dot > base:
                        delete(dot - 1, dot)
                        dot -= 1
                else:
                    dot = deleteSelection()
            elif ch == 'A' - '@':
                self.selectAll()
                dot = -1
            elif ch == 'B' - '@':
                dot = max(getSelectionStart() - 1, base)
            elif ch == 'C' - '@':
                self.copy()
                dot = -1
            elif ch == 'F' - '@':
                dot = min(getSelectionEnd() + 1, self.getLength())
            elif ch == 'P' - '@':
                console.printConsole()
                dot = -1
            elif ch == 'S' - '@':
                console.save()
                dot = -1
            elif ch == 'V' - '@':
                self.paste()
                dot = -1
            elif ch == 'X' - '@':
                self.cut()
                dot = -1
            else:
                if dot != getSelectionEnd():
                    dot = deleteSelection()
                insert("" + ch, dot, INPUT_STYLE)
                dot += 1
            if dot != -1:
                select(dot, dot)
                setCaretPosition(dot)
        len = self.getLength() - base
        line = self.getText(base, base + len)
        insert("\n", base + len, OUTPUT_STYLE)
        base += len + 1
        return line

    #  Private method: isCommandEnabled(cmd) 
    # 
    #  * Returns true if the command should be enabled in the menu bar.
    #  
    def isCommandEnabled(self, cmd):
        """ generated source for method isCommandEnabled """
        if cmd == cmd:
            #  Avoid unused parameter warning 
        return hasFocus

    #  Private method: insert(str, dot, style) 
    # 
    #  * Inserts a string into the text pane at the position specified by <code>dot</code>,
    #  * using the specified style.
    #  
    def insert(self, str_, dot, style):
        """ generated source for method insert """
        try:
            attributes = outputAttributes
            if style == INPUT_STYLE:
                attributes = inputAttributes
            elif style == ERROR_STYLE:
                attributes = errorAttributes
            document.insertString(dot, str_, attributes)
        except BadLocationException as ex:
            pass
            #  Empty 

    #  Private method: delete(p1, p2) 
    # 
    #  * Deletes text from the text pane beginning at position <code>p1</code> and
    #  * continuing up to but not including <code>p2</code>.
    #  
    def delete(self, p1, p2):
        """ generated source for method delete """
        try:
            document.remove(p1, p2 - p1)
        except BadLocationException as ex:
            raise ErrorException(ex)

    #  Private method: setCaretPosition(pos) 
    # 
    #  * Sets the position of the input carat.
    #  
    def setCaretPosition(self, pos):
        """ generated source for method setCaretPosition """
        textPane.setCaretPosition(pos)

    #  Private method: getCaretPosition() 
    # 
    #  * Returns the position of the input carat.
    #  
    def getCaretPosition(self):
        """ generated source for method getCaretPosition """
        return textPane.getCaretPosition()

    #  Private method: select(p1, p2) 
    # 
    #  * Selects the characters in the range from p1 up to but not including p2.
    #  
    def select(self, p1, p2):
        """ generated source for method select """
        textPane.select(p1, p2)

    #  Private method: getSelectionStart() 
    # 
    #  * Returns the start of the selection.
    #  
    def getSelectionStart(self):
        """ generated source for method getSelectionStart """
        return textPane.getSelectionStart()

    #  Private method: getSelectionEnd() 
    # 
    #  * Returns the end of the selection.
    #  
    def getSelectionEnd(self):
        """ generated source for method getSelectionEnd """
        return textPane.getSelectionEnd()

    #  Private method: deleteSelection() 
    # 
    #  * Deletes the current selection and returns the index of the deletion point.
    #  
    def deleteSelection(self):
        """ generated source for method deleteSelection """
        start = max(base, self.getSelectionStart())
        end = self.getSelectionEnd()
        if end <= base:
            return self.getLength()
        self.delete(start, end)
        return start

    #  Private method: setStyleFromAttributes(g, attributes) 
    # 
    #  * Sets the relevant components of the graphics context from the attribute set.
    #  
    def setStyleFromAttributes(self, g, attributes):
        """ generated source for method setStyleFromAttributes """
        oldFont = textPane.getFont()
        style = 0
        if Boolean.TRUE == attributes.getAttribute(StyleConstants.Bold):
            style |= Font.BOLD
        if Boolean.TRUE == attributes.getAttribute(StyleConstants.Italic):
            style |= Font.ITALIC
        g.setFont(Font(oldFont.__name__, style, oldFont.getSize()))
        color = attributes.getAttribute(StyleConstants.Foreground)
        if color == None:
            color = textPane.getForeground()
        g.setColor(color)

    #  Private constants 
    PRINT_MARGIN = 36

    #  Private instance variables 
    actionListener = None
    outputMonitor = None
    inputMonitor = None
    inputScript = None
    buffer_ = None
    outputAttributes = None
    inputAttributes = None
    errorAttributes = None
    scrollPane = None
    textPane = None
    document = None
    lineSeparator = None
    base = int()
    hasFocus = bool()
    console = None
    menuBar = None

#  Package class: ConsoleOutputMonitor 
# 
#  * This class implements synchronization for the output side of the console
#  * using method-level synchronization, thereby avoiding the compatibility
#  * problems of the <code>synchronized</code> statement.
#  
class ConsoleOutputMonitor(object):
    """ generated source for class ConsoleOutputMonitor """
    #  Constructor: new ConsoleOutputMonitor(model) 
    # 
    #  * Creates the new console output monitor, which calls back to the specified
    #  * model.
    #  
    def __init__(self, model):
        """ generated source for method __init__ """
        consoleModel = model

    #  Method: print(str, style) 
    # 
    #  * Prints the string to the console.
    #  
    @synchronized
    def print_(self, str_, style):
        """ generated source for method print_ """
        consoleModel.printCallback(str_, style)

    #  Private instance variables 
    consoleModel = None

#  Package class: ConsoleInputMonitor 
# 
#  * This class implements synchronization for the input side of the console
#  * using method-level synchronization, thereby avoiding the compatibility
#  * problems of the <code>synchronized</code> statement.
#  
class ConsoleInputMonitor(object):
    """ generated source for class ConsoleInputMonitor """
    #  Constructor: new ConsoleInputMonitor(model) 
    # 
    #  * Creates the new console input monitor, which calls back to the specified
    #  * model.
    #  
    def __init__(self, model):
        """ generated source for method __init__ """
        consoleModel = model

    #  Method: readLine() 
    # 
    #  * Reads and returns the next line of text from the console.
    #  
    @synchronized
    def readLine(self):
        """ generated source for method readLine """
        return consoleModel.readLineCallback()

    #  Private instance variables 
    consoleModel = None

#  Package class: SystemConsole 
# 
#  * This class implements a version of <code>IOConsole</code> that responds to
#  * the methods of that class but that uses <code>System.in</code> and
#  * <code>System.out</code> for its input and output.  This class is not
#  * instantiated directly; clients gain access to this facility by using the
#  * <a href="IOConsole.html#SYSTEM_CONSOLE"><code>SYSTEM_CONSOLE</code></a>
#  * constant in the <a href="IOConsole.html"><code>IOConsole</code></a> class.
#  
class SystemConsole(IOConsole):
    """ generated source for class SystemConsole """
    #  Factory method: createConsoleModel() 
    # 
    #  * Creates the console model object used to implement this console.
    #  
    def createConsoleModel(self):
        """ generated source for method createConsoleModel """
        return SystemConsoleModel()

#  Package class: ConsoleWriter 
# 
#  * This class defines the underlying writer for the console.
#  * @noshow
#  
class ConsoleWriter(Writer):
    """ generated source for class ConsoleWriter """
    #  Constructor: ConsoleWriter(cp) 
    # 
    #  * Creates the basic writer object for the console.
    #  
    def __init__(self, cp):
        """ generated source for method __init__ """
        super(ConsoleWriter, self).__init__()
        consoleModel = cp

    #  Method: close() 
    # 
    #  * Closes the writer (does nothing in this case).
    #  
    def close(self):
        """ generated source for method close """
        #  Empty 

    #  Method: flush() 
    # 
    #  * Flushes any remaining output to the writer.
    #  
    def flush(self):
        """ generated source for method flush """
        #  Empty 

    #  Method: write(cbuf, off, len) 
    # 
    #  * Writes characters from <code>cbuf</code> starting at position <code>off</code>
    #  * up to a maximum of <code>len</code>.
    #  
    def write(self, cbuf, off, len):
        """ generated source for method write """
        str_ = str(cbuf, off, len)
        start = 0
        eol = int()
        while (eol = str_.indexOf(IOConsole.LINE_SEPARATOR, start)) != -1:
            consoleModel.print_(str_.substring(start, eol), ConsoleModel.OUTPUT_STYLE)
            consoleModel.print_("\n", ConsoleModel.OUTPUT_STYLE)
            start = eol + len(length)
        consoleModel.print_(str_.substring(start), ConsoleModel.OUTPUT_STYLE)

    #  Private instance variables 
    consoleModel = None

#  Package class: ConsoleReader 
# 
#  * This class defines the underlying reader for the console.
#  
class ConsoleReader(Reader):
    """ generated source for class ConsoleReader """
    #  Constructor: ConsoleReader(cp) 
    # 
    #  * Creates the basic reader object for the console.
    #  
    def __init__(self, cp):
        """ generated source for method __init__ """
        super(ConsoleReader, self).__init__()
        consoleModel = cp
        buffer_ = None

    #  Method: close() 
    # 
    #  * Closes the reader (does nothing in this case).
    #  
    def close(self):
        """ generated source for method close """
        #  Empty 

    #  Method: read(cbuf, off, len) 
    # 
    #  * Reads characters into <code>cbuf</code> starting at position <code>off</code>
    #  * up to a maximum of <code>len</code>.
    #  
    def read(self, cbuf, off, len):
        """ generated source for method read """
        if len == 0:
            return 0
        if buffer_ == None:
            buffer_ = consoleModel.readLine()
            if buffer_ == None:
                return -1
            buffer_ += "\n"
        if len < len(buffer_):
            buffer_.getChars(0, len, cbuf, off)
            buffer_ = buffer_.substring(len)
        else:
            len = len(buffer_)
            buffer_.getChars(0, len, cbuf, off)
            buffer_ = None
        return len

    #  Private instance variables 
    consoleModel = None
    buffer_ = None

#  Package class: SystemConsoleModel 
# 
#  * Implements the basic console operations for the system console.
#  
class SystemConsoleModel(ConsoleModel):
    """ generated source for class SystemConsoleModel """
    #  Constructor: SystemConsoleModel() 
    # 
    #  * Creates a new <code>SystemConsoleModel</code> object.
    #  
    def __init__(self):
        """ generated source for method __init__ """
        super(SystemConsoleModel, self).__init__()
        text = ""

    #  Method: setConsole(owner) 
    # 
    #  * Sets the identity of the owning console.  This method must be called after
    #  * creating the model object.
    #  
    def setConsole(self, owner):
        """ generated source for method setConsole """
        console = owner

    #  Method: getConsole(console) 
    # 
    #  * Returns the associated console.
    #  
    def getConsole(self):
        """ generated source for method getConsole """
        return console

    #  Method: clear() 
    # 
    #  * Clears the console pane.
    #  
    def clear(self):
        """ generated source for method clear """
        #  Empty 

    #  Method: print(str, style) 
    # 
    #  * Prints the string to the end of the console output.
    #  
    @overloaded
    def print_(self, str_, style):
        """ generated source for method print_ """
        print(str_, end="")
        text += str_

    #  Method: readLine() 
    # 
    #  * Reads and returns the next line of text from the console.
    #  
    def readLine(self):
        """ generated source for method readLine """
        System.out.flush()
        line = ""
        ch = int()
        try:
            while True:
                if inputScript == None:
                    ch = System.in_.read()
                else:
                    ch = inputScript.read()
                if ch == -1 and 0 == len(line):
                    try:
                        if inputScript != None:
                            inputScript.close()
                    except IOError as ex:
                        pass
                        #  Empty 
                    inputScript = None
                else:
                    if ch == -1 or ch == '\n':
                        break
                    line += str(ch)
        except IOError as ex:
            pass
            #  Empty 
        if inputScript != None:
            self.print_(line + "\n", INPUT_STYLE)
        return line

    #  Method: getText() 
    # 
    #  * Returns the text stored in the console pane.
    #  
    @overloaded
    def getText(self):
        """ generated source for method getText """
        return text

    #  Method: getText(start, end) 
    # 
    #  * Returns a substring from the text using endpoints defined as in
    #  * <code>substring</code> for strings.
    #  
    @getText.register(object, int, int)
    def getText_0(self, start, end):
        """ generated source for method getText_0 """
        return text.substring(start, end)

    #  Method: getLength() 
    # 
    #  * Returns the length of the text.
    #  
    def getLength(self):
        """ generated source for method getLength """
        return len(text)

    #  Method: getConsoleModel() 
    # 
    #  * Returns the top-level component that represents the console.  This is the
    #  * pane that needs to be added to a parent.
    #  
    def getConsoleModel(self):
        """ generated source for method getConsoleModel """
        return None

    #  Method: getTextPane() 
    # 
    #  * Returns the component that holds the text.  This is the model to which
    #  * messages like <code>setFont</code> and <code>requestFocus</code> should
    #  * be directed.
    #  
    def getTextPane(self):
        """ generated source for method getTextPane """
        return None

    #  Method: setFont(font) 
    # 
    #  * Sets the font for the console.
    #  *
    #  * @usage consoleModel.setFont(font);
    #  * @param font The new font for the console
    #  
    def setFont(self, font):
        """ generated source for method setFont """
        if font != font:
        #  Avoid unused parameter warning 
        #  Empty 

    #  Method: setInputStyle(style) 
    # 
    #  * Sets the style parameters for console input.  The style parameter
    #  * is either <code>Font.PLAIN</code> or a sum of one or more of the attributes
    #  * <code>Font.BOLD</code> and <code>Font.ITALIC</code>.
    #  
    def setInputStyle(self, style):
        """ generated source for method setInputStyle """
        #  Empty 

    #  Method: setInputColor(color) 
    # 
    #  * Sets the color used for console input.
    #  
    def setInputColor(self, color):
        """ generated source for method setInputColor """
        #  Empty 

    #  Method: setErrorStyle(style) 
    # 
    #  * Sets the style parameters for console error messages.  The style parameter
    #  * is either <code>Font.PLAIN</code> or a sum of one or more of the attributes
    #  * <code>Font.BOLD</code> and <code>Font.ITALIC</code>.
    #  
    def setErrorStyle(self, style):
        """ generated source for method setErrorStyle """
        #  Empty 

    #  Method: setErrorColor(color) 
    # 
    #  * Sets the color used for console error messages.
    #  
    def setErrorColor(self, color):
        """ generated source for method setErrorColor """
        #  Empty 

    #  Method: cut() 
    # 
    #  * Implements the "cut" menu operation.
    #  
    def cut(self):
        """ generated source for method cut """
        #  Empty 

    #  Method: copy() 
    # 
    #  * Implements the "copy" menu operation.
    #  
    def copy(self):
        """ generated source for method copy """
        #  Empty 

    #  Method: paste() 
    # 
    #  * Implements the "paste" menu operation.
    #  
    def paste(self):
        """ generated source for method paste """
        #  Empty 

    #  Method: selectAll() 
    # 
    #  * Implements the "select all" menu operation.
    #  
    def selectAll(self):
        """ generated source for method selectAll """
        #  Empty 

    #  Method: isPointSelection() 
    def isPointSelection(self):
        """ generated source for method isPointSelection """
        return True

    #  Method: print(pj) 
    # 
    #  * Prints the entire console using the specified <code>PrintJob</code> object.
    #  
    @print_.register(object, PrintJob)
    def print__0(self, pj):
        """ generated source for method print__0 """
        #  Empty 

    #  Method: setInputScript(rd) 
    # 
    #  * Sets a new input script for the console, which will subsequently
    #  * take input from the specified reader.
    #  
    def setInputScript(self, rd):
        """ generated source for method setInputScript """
        inputScript = rd

    #  Method: getInputScript() 
    # 
    #  * Retrieves the input script.  After the end of the input script has been
    #  * reached, this method will return <code>null</code>.
    #  
    def getInputScript(self):
        """ generated source for method getInputScript """
        return inputScript

    #  Method: getConsolePane() 
    # 
    #  * Returns the top-level component that represents the console.
    #  
    def getConsolePane(self):
        """ generated source for method getConsolePane """
        return None

    #  Method: requestFocus() 
    # 
    #  * Forwards the request focus to the text pane.
    #  * @noshow
    #  
    def requestFocus(self):
        """ generated source for method requestFocus """
        #  Empty 

    #  Method: setMenuBar(mbar) 
    # 
    #  * Sets the menu bar that controls this console.
    #  * @noshow
    #  
    def setMenuBar(self, mbar):
        """ generated source for method setMenuBar """
        #  Empty 

    #  Private instance variables 
    console = None
    inputScript = None
    text = None

#  Package class: CharacterQueue 
# 
#  * This class defines a simple character queue.
#  
class CharacterQueue(object):
    """ generated source for class CharacterQueue """
    #  Constructor: CharacterQueue() 
    # 
    #  * Creates an empty character queue.
    #  
    def __init__(self):
        """ generated source for method __init__ """
        buffer_ = ""

    #  Method: enqueue(ch) 
    # 
    #  * Adds a character to the end of the queue.
    #  
    @overloaded
    @synchronized
    def enqueue(self, ch):
        """ generated source for method enqueue """
        buffer_ += ch
        notifyAll()

    #  Method: enqueue(str) 
    # 
    #  * Adds a string to the end of the queue.
    #  
    @enqueue.register(object, str)
    @synchronized
    def enqueue_0(self, str_):
        """ generated source for method enqueue_0 """
        buffer_ += str_
        notifyAll()

    #  Method: dequeue() 
    # 
    #  * Removes and returns the first character in the queue.  If the queue
    #  * is empty, this method waits for data.
    #  
    @synchronized
    def dequeue(self):
        """ generated source for method dequeue """
        while 0 == len(buffer_):
            try:
                isWaiting = True
                wait()
                isWaiting = False
            except InterruptedException as ex:
                pass
                #  Empty 
        ch = buffer_.charAt(0)
        buffer_ = buffer_.substring(1)
        return ch

    #  Method: clear() 
    # 
    #  * Clears the character queue.
    #  
    @synchronized
    def clear(self):
        """ generated source for method clear """
        buffer_ = ""
        notifyAll()

    #  Method: isWaiting() 
    # 
    #  * Returns <code>true</code> if the buffer is in a waiting state.
    #  
    def isWaiting(self):
        """ generated source for method isWaiting """
        return self.isWaiting

    #  Private instance variables 
    buffer_ = None
    isWaiting = bool()

#  Package class: ConsoleActionListener 
# 
#  * This class listens for menu bar actions directed toward the console.
#  
class ConsoleActionListener(ActionListener):
    """ generated source for class ConsoleActionListener """
    #  Constructor: ConsoleActionListener(owner) 
    # 
    #  * Creates a new action listener for the specified console.
    #  
    def __init__(self, owner):
        """ generated source for method __init__ """
        super(ConsoleActionListener, self).__init__()
        console = owner

    #  Method: actionPerformed(e) 
    # 
    #  * Responds to the specified action event.
    #  
    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        console.menuAction(e)

    #  Private instance variables 
    console = None

