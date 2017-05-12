#!/usr/bin/env python
""" generated source for module IODialog """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
# 
#  * @(#)IODialog.java   1.99.1 08/12/08
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
# package: acm.io
#  Class: IODialog 
# 
#  * The <code>IODialog</code> class provides a simple, dialog-based mechanism
#  * for interacting with the user.  It is therefore similar to the
#  * <code>JOptionPane</code> facility in Swing (which it uses in the implementation).
#  * The differences between the models are
#  *
#  * <ol>
#  * <li>The <code>IODialog</code> mechanism is considerably simpler, mostly
#  *     because it does not try to be as general.
#  * <li>The <code>IODialog</code> mechanism does not use static methods; clients
#  *     instantiate an <code>IODialog</code> object and make calls on that object,
#  *     thereby emphasizing the object-oriented idea.
#  * <li>The <code>IODialog</code> class works even if Swing is not available.
#  * </ol>
#  *
#  * The input methods available for <code>IODialog</code> are intentionally the
#  * same as those for the <a href="IOConsole.html"><code>IOConsole</code></a> class so
#  * that clients can substitute one model for another without making source changes.
#  * The input methods are therefore
#  *
#  * <ul>
#  * <li><a href="#readInt()"><code>readInt</code></a>
#  * <li><a href="#readDouble()"><code>readDouble</code></a>
#  * <li><a href="#readBoolean()"><code>readBoolean</code></a>
#  * <li><a href="#readLine()"><code>readLine</code></a>
#  * </ul>
#  *
#  * For example, the following code pops up a dialog box and
#  * allows the user to enter an integer:
#  *
#  * <p><pre><code>
#  * &nbsp;    IODialog dialog = new IODialog();
#  * &nbsp;    int n = dialog.readInt("Enter an integer: ");
#  * </code></pre>
#  
class IODialog(IOModel):
    """ generated source for class IODialog """
    #  Constructor: IODialog() 
    # 
    #  * Instantiates a new IODialog object that can then be used for dialog-based
    #  * input and output.
    #  *
    #  * @usage dialog = new IODialog();
    #  
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(IODialog, self).__init__()
        self.__init__(None)

    #  Constructor: IODialog(owner) 
    # 
    #  * Instantiates a new IODialog object that can then be used for dialog-based
    #  * input and output.
    #  *
    #  * @usage dialog = new IODialog(owner);
    #  * @param owner A <code>Component</code> used as the owner of created dialogs
    #  
    @__init__.register(object, Component)
    def __init___0(self, owner):
        """ generated source for method __init___0 """
        super(IODialog, self).__init__()
        myComponent = owner
        model = createModel()
        outputLine = ""
        exceptionOnError = False
        allowCancel = False

    #  Method: print(value) 
    # 
    #  * Displays the argument value, allowing for the possibility of more
    #  * output in the same dialog.  The <code>print</code> method is overloaded
    #  * so that <code>value</code> can be of any type.
    #  *
    #  * @usage dialog.print(value);
    #  * @param value The value to be displayed
    #  
    @overloaded
    def print_(self, value):
        """ generated source for method print_ """
        outputLine += value

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
    #  * Completes the output line and displays the dialog.
    #  *
    #  * @usage dialog.println();
    #  
    @overloaded
    def println(self):
        """ generated source for method println """
        model.popupMessage(outputLine)
        outputLine = ""

    #  Method: println(value) 
    # 
    #  * Adds the value to the current output line and then displays the dialog.
    #  * The <code>println</code> method is overloaded so that <code>value</code>
    #  * can be of any type.
    #  *
    #  * @usage dialog.println(value);
    #  * @param value The value to be displayed
    #  
    @println.register(object, str)
    def println_0(self, value):
        """ generated source for method println_0 """
        self.print_(value)
        self.println()

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
    #  * Displays the error message in an error dialog.
    #  *
    #  * @usage dialog.showErrorMessage(msg);
    #  * @param msg The error msg to be displayed
    #  
    def showErrorMessage(self, msg):
        """ generated source for method showErrorMessage """
        model.popupErrorMessage(msg)

    #  Method: readLine() 
    # 
    #  * Reads and returns a line of input from the dialog, without
    #  * including the end-of-line characters that terminate the input.
    #  *
    #  * @usage String str = dialog.readLine();
    #  * @return The next line of input as a <code>String</code>
    #  
    @overloaded
    def readLine(self):
        """ generated source for method readLine """
        return self.readLine(None)

    #  Method: readLine(prompt) 
    # 
    #  * Prompts the user to enter a single character, which is then returned
    #  * as the value of this method.  The end-of-line characters that terminate
    #  * the input are not included in the returned string.
    #  *
    #  * @usage String str = dialog.readLine(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The next line of input as a <code>String</code>
    #  
    @readLine.register(object, str)
    def readLine_0(self, prompt):
        """ generated source for method readLine_0 """
        if myConsole != None and myConsole.getInputScript() != None:
            return myConsole.readLine(prompt)
        prompt = outputLine if (prompt == None) else outputLine + prompt
        outputLine = ""
        line = None
        while (line = model.popupLineInputDialog(prompt, allowCancel)) == None:
            if allowCancel:
                raise CancelledException()
        return line

    #  Method: readInt() 
    # 
    #  * Reads and returns an integer value from the user.  If the user types
    #  * a value that is not a legal integer, the method ordinarily offers the
    #  * user a chance to reenter the data, although this behavior can be
    #  * changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage int n = dialog.readInt();
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
    #  * @usage int n = dialog.readInt(low, high);
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
    #  * @usage int n = dialog.readInt(prompt);
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
    #  * @usage int n = dialog.readInt(prompt, low, high);
    #  * @param prompt The prompt string to display to the user
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a decimal integer
    #  
    @readInt.register(object, str, int, int)
    def readInt_2(self, prompt, low, high):
        """ generated source for method readInt_2 """
        while True:
            line = self.readLine(prompt)
            try:
                n = Integer.parseInt(line)
                if n < low or n > high:
                    signalError("Value is outside the range [" + low + ":" + high + "]")
                return n
            except NumberFormatException as ex:
                signalError("Illegal integer format")

    #  Method: readDouble() 
    # 
    #  * Reads and returns a double-precision value from the user.  If the user
    #  * types a value that is not a legal number, the method ordinarily offers
    #  * the user a chance to reenter the data, although this behavior can be
    #  * changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage double d = dialog.readDouble();
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
    #  * @usage double d = dialog.readDouble(low, high);
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
    #  * @usage double d = dialog.readDouble(prompt);
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
    #  * @usage d = dialog.readDouble(prompt, low, high);
    #  * @param prompt The prompt string to display to the user
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @readDouble.register(object, str, float, float)
    def readDouble_2(self, prompt, low, high):
        """ generated source for method readDouble_2 """
        while True:
            line = self.readLine(prompt)
            try:
                d = Double.valueOf(line).doubleValue()
                if d < low or d > high:
                    signalError("Value is outside the range [" + low + ":" + high + "]")
                return d
            except NumberFormatException as ex:
                signalError("Illegal numeric format")

    #  Method: readBoolean() 
    # 
    #  * Reads and returns a boolean value from the user, which must match
    #  * either <code>true</code> or <code>false</code>, ignoring case.
    #  * If the user types a value that is not one of these possibilities,
    #  * the method ordinarily offers the user a chance to reenter the data,
    #  * although this behavior can be changed using the
    #  * <a href="#setExceptionOnError(boolean)"><code>setExceptionOnError</code></a> method.
    #  *
    #  * @usage boolean flag = dialog.readBoolean();
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
    #  * @usage boolean flag = dialog.readBoolean(prompt);
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
    #  * @usage boolean flag = dialog.readBoolean(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @param trueLabel The label for the button indicating <code>true</code>
    #  * @param falseLabel The label for the button indicating <code>false</code>
    #  * @return The value of the input interpreted as a boolean value
    #  
    @readBoolean.register(object, str, str, str)
    def readBoolean_1(self, prompt, trueLabel, falseLabel):
        """ generated source for method readBoolean_1 """
        if myConsole != None and myConsole.getInputScript() != None:
            return myConsole.readBoolean(prompt, trueLabel, falseLabel)
        prompt = outputLine if (prompt == None) else outputLine + prompt
        outputLine = ""
        choice = None
        while (choice = model.popupBooleanInputDialog(prompt, trueLabel, falseLabel, allowCancel)) == None:
            if allowCancel:
                raise CancelledException()
        return choice.booleanValue()

    #  Method: setExceptionOnError(flag) 
    # 
    #  * Sets the error-handling mode of the dialog as specified by the <code>flag</code>
    #  * parameter.  If <code>flag</code> is <code>false</code> (which is the default), the
    #  * input methods give the user a chance to retry after erroneous input.  If this
    #  * value is set to <code>true</code>, illegal input raises an
    #  * <a href="../util/ErrorException.html"><code>ErrorException</code></a> instead.
    #  *
    #  * @usage dialog.setExceptionOnError(flag);
    #  * @param flag <code>false</code> to retry on errors; <code>true</code> to raise an exception
    #  
    def setExceptionOnError(self, flag):
        """ generated source for method setExceptionOnError """
        exceptionOnError = flag

    #  Method: getExceptionOnError() 
    # 
    #  * Returns the state of the error-handling flag.
    #  *
    #  * @usage boolean flag = dialog.getExceptionOnError();
    #  * @return The current setting of the error-handling mode (<code>false</code> to retry
    #  *         on errors; <code>true</code> to raise an exception)
    #  
    def getExceptionOnError(self):
        """ generated source for method getExceptionOnError """
        return exceptionOnError

    #  Method: setAllowCancel(flag) 
    # 
    #  * Sets the cancellation mode of the dialog as specified by the <code>flag</code>
    #  * parameter.  If <code>flag</code> is <code>false</code> (which is the default),
    #  * the input methods do not include a "Cancel" button.  If this value is set to
    #  * to <code>true</code>, a "Cancel" button appears, which throws a
    #  * <a href="../util/CancelledException.html"><code>CancelledException</code></a>
    #  * if it is invoked.
    #  *
    #  * @usage dialog.setAllowCancel(flag);
    #  * @param flag <code>false</code> to remove "Cancel" button; <code>true</code> to enable it
    #  
    def setAllowCancel(self, flag):
        """ generated source for method setAllowCancel """
        allowCancel = flag

    #  Method: getAllowCancel() 
    # 
    #  * Returns the state of the cancellation mode.
    #  *
    #  * @usage boolean flag = dialog.getAllowCancel();
    #  * @return The current setting of the error-handling mode (<code>false</code> to retry
    #  *         on errors; <code>true</code> to raise an exception)
    #  
    def getAllowCancel(self):
        """ generated source for method getAllowCancel """
        return allowCancel

    #  Method: setAssociatedConsole(console) 
    # 
    #  * Establishes an associated console for the dialog. If the associated console
    #  * is non-<code>null</code> and the console is reading from an input stream,
    #  * then the dialog methods use the console for input instead of the dialog.
    #  *
    #  * @usage dialog.setAssociatedConsole(console);
    #  * @param console The associated console
    #  * @noshow
    #  
    def setAssociatedConsole(self, console):
        """ generated source for method setAssociatedConsole """
        myConsole = console

    #  Method: getAssociatedConsole() 
    # 
    #  * Returns the associated console for the dialog.
    #  *
    #  * @usage IOConsole console = dialog.getAssociatedConsole();
    #  * @return The associated console
    #  * @noshow
    #  
    def getAssociatedConsole(self):
        """ generated source for method getAssociatedConsole """
        return myConsole

    #  Factory method: createModel() 
    # 
    #  * Creates the input dialog model in Swing or AWT style, as appropriate.
    #  
    def createModel(self):
        """ generated source for method createModel """
        className = JPanel().__class__.__name__
        if className.startsWith("javax.swing.") and Platform.isSwingAvailable():
            try:
                swingDialogModelClass = Class.forName("acm.io.SwingDialogModel")
                types = [Class.forName("java.awt.Component")]
                args = [myComponent]
                con = swingDialogModelClass.getConstructor(types)
                return con.newInstance(args)
            except Exception as ex:
                return AWTDialogModel(myComponent)
        else:
            return AWTDialogModel(myComponent)

    def signalError(self, msg):
        """ generated source for method signalError """
        if exceptionOnError:
            raise ErrorException(msg)
        model.popupErrorMessage(msg)

    exceptionOnError = bool()
    allowCancel = bool()
    model = None
    myComponent = None
    myConsole = None
    outputLine = None


class DialogModel(object):
    """ generated source for interface DialogModel """
    __metaclass__ = ABCMeta
    @abstractmethod
    def popupMessage(self, msg):
        """ generated source for method popupMessage """

    @abstractmethod
    def popupErrorMessage(self, msg):
        """ generated source for method popupErrorMessage """

    @abstractmethod
    def popupLineInputDialog(self, prompt, allowCancel):
        """ generated source for method popupLineInputDialog """

    @abstractmethod
    def popupBooleanInputDialog(self, prompt, trueLabel, falseLabel, allowCancel):
        """ generated source for method popupBooleanInputDialog """


class SwingDialogModel(DialogModel):
    """ generated source for class SwingDialogModel """
    def __init__(self, owner):
        """ generated source for method __init__ """
        super(SwingDialogModel, self).__init__()
        myComponent = owner
        if not iconTested:
            lf = UIManager.getLookAndFeel().__str__()
            if lf.indexOf("AquaLookAndFeel") == -1:
                inputIcon = None
            else:
                inputIcon = ImageIcon(MediaTools.createImage(AQUA_QUESTION_IMAGE))
            iconTested = True

    def popupMessage(self, msg):
        """ generated source for method popupMessage """
        JOptionPane.showMessageDialog(myComponent, msg)

    def popupErrorMessage(self, msg):
        """ generated source for method popupErrorMessage """
        JOptionPane.showMessageDialog(myComponent, msg, "Error", JOptionPane.ERROR_MESSAGE)

    def popupLineInputDialog(self, prompt, allowCancel):
        """ generated source for method popupLineInputDialog """
        pane = None
        if allowCancel:
            pane = JOptionPane(prompt, JOptionPane.QUESTION_MESSAGE, JOptionPane.OK_CANCEL_OPTION, inputIcon)
            pane.setWantsInput(True)
        else:
            choices = ["OK"]
            pane = JOptionPane(prompt, JOptionPane.QUESTION_MESSAGE, JOptionPane.OK_CANCEL_OPTION, inputIcon, choices, choices[0])
            pane.setWantsInput(True)
            pane.setInputValue("")
        dialog = pane.createDialog(myComponent, "Input")
        dialog.setVisible(True)
        value = pane.getInputValue()
        if value == JOptionPane.UNINITIALIZED_VALUE:
            return None
        return str(value)

    def popupBooleanInputDialog(self, prompt, trueLabel, falseLabel, allowCancel):
        """ generated source for method popupBooleanInputDialog """
        choices = []
        if allowCancel:
            choices = [None] * 3
            choices[2] = "Cancel"
        else:
            choices = [None] * 2
        choices[0] = trueLabel
        choices[1] = falseLabel
        label = trueLabel + "/" + falseLabel + " question"
        choice = JOptionPane.showOptionDialog(myComponent, prompt, label, JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE, inputIcon, choices, choices[0])
        if choice == 0:
            return Boolean.TRUE
        elif choice == 1:
            return Boolean.FALSE
        else:
            return None

    AQUA_QUESTION_IMAGE = ["4749463839613D003D00E60000FFFFFFE5E5E5FFCBFF8C8C8CA7A7A7ADADAD8D8D8D929292818181", "8585856F6F6F7373738888888B8B8B9A9A9A9D9D9D616161646464757575787878C2C2C295959597", "97976666666868687E7E7E808080565656575757E6E6E6E7E7E79F9F9FA0A0A05E5E5E5F5F5F6B6B", "6B6C6C6C6D6D6D6E6E6E7979797A7A7A7C7C7C7D7D7D5A5A5A5B5B5B5C5C5C5D5D5DE1E1E1E2E2E2", "E3E3E3E4E4E4AEAEAEAFAFAFB0B0B0B1B1B1E8E8E8E9E9E9EAEAEAEBEBEBECECECEDEDEDEEEEEEEF", "EFEFB2B2B2B3B3B3B4B4B4B5B5B5B6B6B6B7B7B7B8B8B8B9B9B9BABABABBBBBBBCBCBCBDBDBDBEBE", "BEBFBFBFC0C0C0C1C1C1F0F0F0F1F1F1F2F2F2F3F3F3F4F4F4F5F5F5F6F6F6F7F7F7F8F8F8F9F9F9", "FAFAFAFBFBFBFCFCFCFDFDFDFEFEFED1D1D1D2D2D2D3D3D3D4D4D4D5D5D5D6D6D6D7D7D7D8D8D8D9", "D9D9DADADADBDBDBDCDCDCDDDDDDDEDEDEDFDFDFE0E0E0C9C9C9CACACACBCBCBCCCCCCCDCDCDCECE", "CECFCFCFD0D0D0C5C5C5C6C6C6C7C7C7C8C8C8C3C3C3C4C4C4000000ED0000ED0000ED000021F904", "01000002002C000000003D003D004607FF800282838485868788898A8B863E1D6B53009293949596", "97925C1E6B8C853A3098A10825A1672DA72D6EA195566A863C655BB2B3B4B5B6B7B235A7273CB8BE", "B23B6D833D676256C7C8C9CACBC91A171ACCD1D25176378D1D5F446852DCDDDEDFDD0D21E3E303E0", "E7DE3D4B7B6B3B9D853C376D60784C4334457166393EFDFEFF007DBCA120E78C0C1D3EDE295C08CF", "8399396474309C28286180356B3AE0E011E50A972E5AA83CD18103869A36387A5044A4234D965597", "A2E80171E0C003253C6056D2C146118F345D820A1D4A746804542DD4142582CA41D1A742A3701A94", "234C96AB58B36ADDAAD5CB29025CC38AED41266145187AD85059CBB6ADDBB754FFF628E060620FDC", "BB709B8C91A828D89C2442D640194CB8B0E1C3880BEFB803C40E190F665726F2D183C70E1D9873E4", "B8C1A64E131B667888268343B2E9D3A853ABEEA4E3469A363E74AECAE2010D8C1CA86FA0A122BBF7", "2A193DDFE93073C537003C103298A1E466042A03BE63C448D40106D4EB68901A783A031583EB45B1", "94F154A6CAAF5F2F947CB97523C4A906E76FADB126E891D8FB628F9C4A3005FF7D2C60F0E5C11D57", "1468E081082688A0062D68A0E083105E71061A7CE910C31E6D54A1E1861C76E8E1872086E8A11365", "9446480E6CEC81C7142CB6E8E28B2F1A20C28C330E00E38D30DE3004181D28E21A1E407C11C59044", "1669E4901494B001FF094E1CE92491391881041831F0F50E0E318C71871133EC11C313608629E698", "6486D9C31840D4D0C41C6B7860256A385487461872DC410113491C7184117C1651001C3D042AA818", "55AE865A0E01988147113FB431460086462A000EB8496AE9A589E890830731BCC0C6A76CB4014300", "37BC8929213D04A0860C4F70E1DB1528B25169A439ACF14271C6ADB2031A32A0D6031B38E49AEB15", "6D52D4411A5808ABAC2439A8616A223BB864DC0D158880810A291C750A0A4DF896C30B8BE8B0466C", "BE7911820597DC60022A09F886067D8DA47105784551E182016028F5940AA87C40EF503298588819", "56FC4B540748B570465148B06BB0506DC05BDF0D5C546CF1FFC5185F0C042A1564CCC501A8D4E1F1", "C8158F37880E61C4A7B22D069CB280142BD312000C83ECA0861638E7ACF3CE3CF7AC4510A7480085", "CF44E73CC519837460867F4C5FE5850B2D80D0B458557CC1570E7360A1F5D65C77ED75D7206BF0F5", "D8646321C31966DD00870711B67D20830EBAEDB61B6DF0E5035AD2E4BD0C011710A0F7DFADD4F1A6", "07615020E2E18827CE610C4ED45D480E621CD1038E94B738060B34B63046E59517FE426484783086", "1160708EE304E48C7382E930F64004DDCF0EC2430C720C71C693B8CBC102392B7881BB933C30D1C4", "3EA023A25B1E41D8C1D1EFCC371F451B362CF145A10BC1F005053FE8D14199DC773FE6183F1CF1C6", "82BBC52BA443076AD4A14711F880814340F0C3FF850D3628E1C61830087C9A0FF1BC30861C7B6082", "118050001A0C01097BB0031EF6D0384139F00B6638884A3045120FC8A00D6A288318C0E0853A7810", "804220420744239A479D8A213C08C018ECD0981CEC8034279C486BD4400726FC600E908A21457C90", "0318C880073A0C222102010021FF0B4D414347436F6E2004031039000000015772697474656E2062", "7920474946436F6E76657274657220322E342E33206F66204D6F6E6461792C204D61792032352C20", "31393938003B"]
    iconTested = bool()
    inputIcon = None
    myComponent = None


class AWTDialogModel(DialogModel):
    """ generated source for class AWTDialogModel """
    def __init__(self, owner):
        """ generated source for method __init__ """
        super(AWTDialogModel, self).__init__()
        myComponent = owner
        imagesReady = False

    def popupMessage(self, msg):
        """ generated source for method popupMessage """
        if not imagesReady:
            createImages()
        frame_ = JTFTools.getEnclosingFrame(myComponent)
        AWTMessageDialog(frame_, "Message", informImage, msg).setVisible(True)

    def popupErrorMessage(self, msg):
        """ generated source for method popupErrorMessage """
        if not imagesReady:
            createImages()
        frame_ = JTFTools.getEnclosingFrame(myComponent)
        AWTMessageDialog(frame_, "Error", errorImage, msg).setVisible(True)

    def popupLineInputDialog(self, prompt, allowCancel):
        """ generated source for method popupLineInputDialog """
        if not imagesReady:
            createImages()
        frame_ = JTFTools.getEnclosingFrame(myComponent)
        dialog = AWTLineInputDialog(frame_, prompt, questionImage, allowCancel)
        dialog.setVisible(True)
        return dialog.getInput()

    def popupBooleanInputDialog(self, prompt, trueLabel, falseLabel, allowCancel):
        """ generated source for method popupBooleanInputDialog """
        if not imagesReady:
            createImages()
        frame_ = JTFTools.getEnclosingFrame(myComponent)
        dialog = AWTBooleanInputDialog(frame_, prompt, questionImage, trueLabel, falseLabel, allowCancel)
        dialog.setVisible(True)
        return dialog.getInput()

    def createImages(self):
        """ generated source for method createImages """
        errorImage = MediaTools.createImage(ERROR_IMAGE)
        informImage = MediaTools.createImage(INFORM_IMAGE)
        questionImage = MediaTools.createImage(QUESTION_IMAGE)
        imagesReady = True

    errorImage = None
    informImage = None
    questionImage = None
    myComponent = None
    imagesReady = bool()
    ERROR_IMAGE = ["47494638396120002000F70000FFFFFF980098339999989800111111222222000054CBFFCB003298", "0033660033CC0033FE00323266330066660000659800989800CC9900FE99329800659800CC0099FE", "0098659898999999CC9900FE98009800329800659900CC9800FE3399CB3399FF9999339898659832", "0098650099339998659833CB9833FF9999CC0099FE00336699656698CC9898FF9999323200336600", "32003233006632009833339965009866339900663300983200666600986500CC3300FE3200CC6600", "FE65CCCC98CCFF99FFCC99FFFF993300CC3200FE6600CC6500FECC0033CC0066FE0032FE00653399", "33339966669933669865CC00CCCB00FEFE00CBFE00FE6699CC6598FF9898CC9999FFCB9833CC9966", "FF9933FF9865333333326532323265326565660033653232660066653265CC3300CC6600FE3200FE", "65000066CC0099CC0066FE0098FE00CCCC00FECB00CCFE00FEFE33CC0033FE0066CC0066FE00CB33", "98CC6699FF3399FF659866CC9965FF9898CC9899FF99CCCC00CCFE00FECB00FEFE00993333996633", "9933669865659833CB9966CC9933FF9865FF33CBCB33FFCC33CCFF33FFFF99CB3399FF3399CC6698", "FF65CC98CCCCCCCCCC99FFCBCBFFFF99CCFFCBCBFF99FFFFCBFF3333CB3366CB3333FF3366FF6533", "CB6666CC6633FF6565FFCB3333CB6533CB3365CC6666FF3333FF6633FF3366FF656533CB3333FF33", "33CB6633FF6666CB3366FF3366CC6665FF65CB33CBCC66CCCC33FFCC65FFFF33CCFF65CCFF33FFFF", "65FF66CCCC65FFCC65CCFF65FFFF98CCCC99FFCC99CCFF99FFFFCBCB33CCFF33CCCC66CCFF65FFCC", "33FFFF33FFCC65FFFF65444444656532DDDDDDCBFFFFFFFFCBEEEEEE100000980000001000660000", "000098000066777777888888AAAAAABBBBBB5555556666660000100000224400005400000000CC00", "00DC0000EE0000FE00003200004400880000980000AA0000BA0000CC0000DC0000EE0000FE00CC00", "00DC0000EE0000FE0000004400005400006600007600220000320000AA0000BA0000002200003200", "7600008800000000AA0000BA00007600008800000021F90401000096002C0000000020002000C7FF", "FFFF980098339999989800111111222222000054CBFFCB0032980033660033CC0033FE0032326633", "0066660000659800989800CC9900FE99329800659800CC0099FE0098659898999999CC9900FE9800", "9800329800659900CC9800FE3399CB3399FF99993398986598320098650099339998659833CB9833", "FF9999CC0099FE00336699656698CC9898FF99993232003366003200323300663200983333996500", "9866339900663300983200666600986500CC3300FE3200CC6600FE65CCCC98CCFF99FFCC99FFFF99", "3300CC3200FE6600CC6500FECC0033CC0066FE0032FE0065339933339966669933669865CC00CCCB", "00FEFE00CBFE00FE6699CC6598FF9898CC9999FFCB9833CC9966FF9933FF98653333333265323232", "65326565660033653232660066653265CC3300CC6600FE3200FE65000066CC0099CC0066FE0098FE", "00CCCC00FECB00CCFE00FEFE33CC0033FE0066CC0066FE00CB3398CC6699FF3399FF659866CC9965", "FF9898CC9899FF99CCCC00CCFE00FECB00FEFE009933339966339933669865659833CB9966CC9933", "FF9865FF33CBCB33FFCC33CCFF33FFFF99CB3399FF3399CC6698FF65CC98CCCCCCCCCC99FFCBCBFF", "FF99CCFFCBCBFF99FFFFCBFF3333CB3366CB3333FF3366FF6533CB6666CC6633FF6565FFCB3333CB", "6533CB3365CC6666FF3333FF6633FF3366FF656533CB3333FF3333CB6633FF6666CB3366FF3366CC", "6665FF65CB33CBCC66CCCC33FFCC65FFFF33CCFF65CCFF33FFFF65FF66CCCC65FFCC65CCFF65FFFF", "98CCCC99FFCC99CCFF99FFFFCBCB33CCFF33CCCC66CCFF65FFCC33FFFF33FFCC65FFFF6544444465", "6532DDDDDDCBFFFFFFFFCBEEEEEE100000980000001000660000000098000066777777888888AAAA", "AABBBBBB5555556666660000100000224400005400000000CC0000DC0000EE0000FE000032000044", "00880000980000AA0000BA0000CC0000DC0000EE0000FE00CC0000DC0000EE0000FE000000440000", "5400006600007600220000320000AA0000BA00000022000032007600008800000000AA0000BA0000", "7600008800000008E5002D091C28909DC1830813B22348D0202D85D5AA294C185121872EEC1E4E44", "18B1E34676EBD85DB48430E4C793074736CC88F22387861A377A3438F3A04991186352AC08916742", "950339B404F9B30BC3A30E87A63C5A90A55297057572F43955A2C59C2D3B529D78D1A94C9F350DDE", "EC2A95A6D58F5B71067DBA112853A11CE2CA9D4BD72853A41969E9DDCB77AFC8BB2BCBB67CC93429", "DB9F810F43F55A156D5AB236779E353B1921E4931EC35E657C53F260AC982B6A2ECAB2F341CDA30D", "5EF6FCB5324EC68A23ABB5243476D1A3B5893E5DE716B76CB16DED020EDAA5B8F1E3C8EF06040021", "FF0B4D414347436F6E2004031039000000015772697474656E20627920474946436F6E7665727465", "7220322E342E33206F66204D6F6E6461792C204D61792032352C2031393938003B"]
    INFORM_IMAGE = ["47494638396120002000F70000FFFFFF980098339999989800111111222222000054CBFFCB003298", "0033660033CC0033FE00323266330066660000659800989800CC9900FE99329800659800CC0099FE", "0098659898999999CC9900FE98009800329800659900CC9800FE3399CB3399FF9999339898659832", "0098650099339998659833CB9833FF9999CC0099FE00336699656698CC9898FF9999323200336600", "32003233006632009833339965009866339900663300983200666600986500CC3300FE3200CC6600", "FE65CCCC98CCFF99FFCC99FFFF993300CC3200FE6600CC6500FECC0033CC0066FE0032FE00653399", "33339966669933669865CC00CCCB00FEFE00CBFE00FE6699CC6598FF9898CC9999FFCB9833CC9966", "FF9933FF9865333333326532323265326565660033653232660066653265CC3300CC6600FE3200FE", "65000066CC0099CC0066FE0098FE00CCCC00FECB00CCFE00FEFE33CC0033FE0066CC0066FE00CB33", "98CC6699FF3399FF659866CC9965FF9898CC9899FF99CCCC00CCFE00FECB00FEFE00993333996633", "9933669865659833CB9966CC9933FF9865FF33CBCB33FFCC33CCFF33FFFF99CB3399FF3399CC6698", "FF65CC98CCCCCCCCCC99FFCBCBFFFF99CCFFCBCBFF99FFFFCBFF3333CB3366CB3333FF3366FF6533", "CB6666CC6633FF6565FFCB3333CB6533CB3365CC6666FF3333FF6633FF3366FF656533CB3333FF33", "33CB6633FF6666CB3366FF3366CC6665FF65CB33CBCC66CCCC33FFCC65FFFF33CCFF65CCFF33FFFF", "65FF66CCCC65FFCC65CCFF65FFFF98CCCC99FFCC99CCFF99FFFFCBCB33CCFF33CCCC66CCFF65FFCC", "33FFFF33FFCC65FFFF65444444656532DDDDDDCBFFFFFFFFCBEEEEEE100000980000001000660000", "000098000066777777888888AAAAAABBBBBB5555556666660000100000224400005400000000CC00", "00DC0000EE0000FE00003200004400880000980000AA0000BA0000CC0000DC0000EE0000FE00CC00", "00DC0000EE0000FE0000004400005400006600007600220000320000AA0000BA0000002200003200", "7600008800000000AA0000BA00007600008800000021F90401000096002C0000000020002000C7FF", "FFFF980098339999989800111111222222000054CBFFCB0032980033660033CC0033FE0032326633", "0066660000659800989800CC9900FE99329800659800CC0099FE0098659898999999CC9900FE9800", "9800329800659900CC9800FE3399CB3399FF99993398986598320098650099339998659833CB9833", "FF9999CC0099FE00336699656698CC9898FF99993232003366003200323300663200983333996500", "9866339900663300983200666600986500CC3300FE3200CC6600FE65CCCC98CCFF99FFCC99FFFF99", "3300CC3200FE6600CC6500FECC0033CC0066FE0032FE0065339933339966669933669865CC00CCCB", "00FEFE00CBFE00FE6699CC6598FF9898CC9999FFCB9833CC9966FF9933FF98653333333265323232", "65326565660033653232660066653265CC3300CC6600FE3200FE65000066CC0099CC0066FE0098FE", "00CCCC00FECB00CCFE00FEFE33CC0033FE0066CC0066FE00CB3398CC6699FF3399FF659866CC9965", "FF9898CC9899FF99CCCC00CCFE00FECB00FEFE009933339966339933669865659833CB9966CC9933", "FF9865FF33CBCB33FFCC33CCFF33FFFF99CB3399FF3399CC6698FF65CC98CCCCCCCCCC99FFCBCBFF", "FF99CCFFCBCBFF99FFFFCBFF3333CB3366CB3333FF3366FF6533CB6666CC6633FF6565FFCB3333CB", "6533CB3365CC6666FF3333FF6633FF3366FF656533CB3333FF3333CB6633FF6666CB3366FF3366CC", "6665FF65CB33CBCC66CCCC33FFCC65FFFF33CCFF65CCFF33FFFF65FF66CCCC65FFCC65CCFF65FFFF", "98CCCC99FFCC99CCFF99FFFFCBCB33CCFF33CCCC66CCFF65FFCC33FFFF33FFCC65FFFF6544444465", "6532DDDDDDCBFFFFFFFFCBEEEEEE100000980000001000660000000098000066777777888888AAAA", "AABBBBBB5555556666660000100000224400005400000000CC0000DC0000EE0000FE000032000044", "00880000980000AA0000BA0000CC0000DC0000EE0000FE00CC0000DC0000EE0000FE000000440000", "5400006600007600220000320000AA0000BA00000022000032007600008800000000AA0000BA0000", "7600008800000008A0002D091C48B0A0C1830809F659B8F09F43870C17268C4891E2C38A18FB4C8C", "F81062C484200536F418D260C691FF4E6A44A8F2E2C9920531C29CC9706648861D534AB46909634E", "992C55F671A932A650A22F830AADC8B3274A8F2B9B9ADC291564D4AA072962353A14EA568E1D3FF2", "ACF8536BC98C65992A450B3523D7966D933A3D1AD7AD42B83AE54EF559B7E659B27D9B8245FA15A5", "DFAD22C5228EC933200021FF0B4D414347436F6E2004031039000000015772697474656E20627920", "474946436F6E76657274657220322E342E33206F66204D6F6E6461792C204D61792032352C203139", "3938003B"]
    QUESTION_IMAGE = ["47494638396120002000F70000FFFFFF980098339999989800111111222222000054CBFFCB003298", "0033660033CC0033FE00323266330066660000659800989800CC9900FE99329800659800CC0099FE", "0098659898999999CC9900FE98009800329800659900CC9800FE3399CB3399FF9999339898659832", "0098650099339998659833CB9833FF9999CC0099FE00336699656698CC9898FF9999323200336600", "32003233006632009833339965009866339900663300983200666600986500CC3300FE3200CC6600", "FE65CCCC98CCFF99FFCC99FFFF993300CC3200FE6600CC6500FECC0033CC0066FE0032FE00653399", "33339966669933669865CC00CCCB00FEFE00CBFE00FE6699CC6598FF9898CC9999FFCB9833CC9966", "FF9933FF9865333333326532323265326565660033653232660066653265CC3300CC6600FE3200FE", "65000066CC0099CC0066FE0098FE00CCCC00FECB00CCFE00FEFE33CC0033FE0066CC0066FE00CB33", "98CC6699FF3399FF659866CC9965FF9898CC9899FF99CCCC00CCFE00FECB00FEFE00993333996633", "9933669865659833CB9966CC9933FF9865FF33CBCB33FFCC33CCFF33FFFF99CB3399FF3399CC6698", "FF65CC98CCCCCCCCCC99FFCBCBFFFF99CCFFCBCBFF99FFFFCBFF3333CB3366CB3333FF3366FF6533", "CB6666CC6633FF6565FFCB3333CB6533CB3365CC6666FF3333FF6633FF3366FF656533CB3333FF33", "33CB6633FF6666CB3366FF3366CC6665FF65CB33CBCC66CCCC33FFCC65FFFF33CCFF65CCFF33FFFF", "65FF66CCCC65FFCC65CCFF65FFFF98CCCC99FFCC99CCFF99FFFFCBCB33CCFF33CCCC66CCFF65FFCC", "33FFFF33FFCC65FFFF65444444656532DDDDDDCBFFFFFFFFCBEEEEEE100000980000001000660000", "000098000066777777888888AAAAAABBBBBB5555556666660000100000224400005400000000CC00", "00DC0000EE0000FE00003200004400880000980000AA0000BA0000CC0000DC0000EE0000FE00CC00", "00DC0000EE0000FE0000004400005400006600007600220000320000AA0000BA0000002200003200", "7600008800000000AA0000BA00007600008800000021F90401000096002C0000000020002000C7FF", "FFFF980098339999989800111111222222000054CBFFCB0032980033660033CC0033FE0032326633", "0066660000659800989800CC9900FE99329800659800CC0099FE0098659898999999CC9900FE9800", "9800329800659900CC9800FE3399CB3399FF99993398986598320098650099339998659833CB9833", "FF9999CC0099FE00336699656698CC9898FF99993232003366003200323300663200983333996500", "9866339900663300983200666600986500CC3300FE3200CC6600FE65CCCC98CCFF99FFCC99FFFF99", "3300CC3200FE6600CC6500FECC0033CC0066FE0032FE0065339933339966669933669865CC00CCCB", "00FEFE00CBFE00FE6699CC6598FF9898CC9999FFCB9833CC9966FF9933FF98653333333265323232", "65326565660033653232660066653265CC3300CC6600FE3200FE65000066CC0099CC0066FE0098FE", "00CCCC00FECB00CCFE00FEFE33CC0033FE0066CC0066FE00CB3398CC6699FF3399FF659866CC9965", "FF9898CC9899FF99CCCC00CCFE00FECB00FEFE009933339966339933669865659833CB9966CC9933", "FF9865FF33CBCB33FFCC33CCFF33FFFF99CB3399FF3399CC6698FF65CC98CCCCCCCCCC99FFCBCBFF", "FF99CCFFCBCBFF99FFFFCBFF3333CB3366CB3333FF3366FF6533CB6666CC6633FF6565FFCB3333CB", "6533CB3365CC6666FF3333FF6633FF3366FF656533CB3333FF3333CB6633FF6666CB3366FF3366CC", "6665FF65CB33CBCC66CCCC33FFCC65FFFF33CCFF65CCFF33FFFF65FF66CCCC65FFCC65CCFF65FFFF", "98CCCC99FFCC99CCFF99FFFFCBCB33CCFF33CCCC66CCFF65FFCC33FFFF33FFCC65FFFF6544444465", "6532DDDDDDCBFFFFFFFFCBEEEEEE100000980000001000660000000098000066777777888888AAAA", "AABBBBBB5555556666660000100000224400005400000000CC0000DC0000EE0000FE000032000044", "00880000980000AA0000BA0000CC0000DC0000EE0000FE00CC0000DC0000EE0000FE000000440000", "5400006600007600220000320000AA0000BA00000022000032007600008800000000AA0000BA0000", "7600008800000008A9002D091C485060AE83080F165C383021C27F1021268C28D1612E831633E6A2", "A8D121C68E1B2B82BCB8502345911E0982E478F024484B235BA27C593263C48E0C6BC64C98F3E3C4", "934033AAB4E952E64DA13B1FB24CDAF1E84E98319D8E2CD874A9D09E0D9F62659874EB50A608B112", "053A5321558B568B5ACC8A56ADDA9426DD5AE50936A4D4BA3FEFE2555A762F5FA65047EAD5C8D66F", "CAC26D07F3E43AB6AF59B175BD325EBB35200021FF0B4D414347436F6E2004031039000000015772", "697474656E20627920474946436F6E76657274657220322E342E33206F66204D6F6E6461792C204D", "61792032352C2031393938003B"]


class AWTDialog(Dialog, ActionListener):
    """ generated source for class AWTDialog """
    WIDTH = 260
    HEIGHT = 115

    def __init__(self, frame_, title, icon, allowCancel):
        """ generated source for method __init__ """
        super(AWTDialog, self).__init__(True)
        setLayout(BorderLayout())
        topPanel = Panel()
        buttonPanel = Panel()
        dataPanel = Panel()
        marginPanel = Panel()
        topPanel.setLayout(BorderLayout())
        buttonPanel.setLayout(FlowLayout())
        dataPanel.setLayout(BorderLayout())
        marginPanel.setLayout(BorderLayout())
        marginPanel.add(Label(" "))
        messageArea = AWTMessageCanvas()
        dataPanel.add(messageArea, BorderLayout.CENTER)
        initButtonPanel(buttonPanel, allowCancel)
        initDataPanel(dataPanel)
        topPanel.add(AWTIconCanvas(icon), BorderLayout.WEST)
        topPanel.add(dataPanel, BorderLayout.CENTER)
        add(topPanel, BorderLayout.CENTER)
        add(buttonPanel, BorderLayout.SOUTH)
        add(marginPanel, BorderLayout.EAST)
        bounds = frame_.getBounds()
        cx = bounds.x + bounds.width / 2
        cy = bounds.y + bounds.height / 2
        setBounds(cx - self.WIDTH / 2, cy - self.HEIGHT / 2, self.WIDTH, self.HEIGHT)
        validate()

    def initButtonPanel(self, buttonPanel, allowCancel):
        """ generated source for method initButtonPanel """

    def initDataPanel(self, dataPanel):
        """ generated source for method initDataPanel """

    def actionPerformed(self, e):
        """ generated source for method actionPerformed """

    def setMessage(self, msg):
        """ generated source for method setMessage """
        messageArea.setMessage(msg)

    messageArea = None


class AWTMessageDialog(AWTDialog):
    """ generated source for class AWTMessageDialog """
    def __init__(self, frame_, title, icon, msg):
        """ generated source for method __init__ """
        super(AWTMessageDialog, self).__init__(False)
        setMessage(msg)

    def initButtonPanel(self, buttonPanel, allowCancel):
        """ generated source for method initButtonPanel """
        okButton = Button("OK")
        okButton.addActionListener(self)
        buttonPanel.add(okButton)

    def initDataPanel(self, dataPanel):
        """ generated source for method initDataPanel """

    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        if e.getSource() == okButton:
            setVisible(False)

    okButton = None


class AWTLineInputDialog(AWTDialog):
    """ generated source for class AWTLineInputDialog """
    def __init__(self, frame_, msg, icon, allowCancel):
        """ generated source for method __init__ """
        super(AWTLineInputDialog, self).__init__(allowCancel)
        setMessage(msg)

    def getInput(self):
        """ generated source for method getInput """
        return input

    def setVisible(self, flag):
        """ generated source for method setVisible """
        super(AWTLineInputDialog, self).setVisible(flag)
        if flag:
            textLine.requestFocus()

    def initButtonPanel(self, buttonPanel, allowCancel):
        """ generated source for method initButtonPanel """
        okButton = Button("OK")
        okButton.addActionListener(self)
        buttonPanel.add(okButton)
        if allowCancel:
            cancelButton = Button("Cancel")
            cancelButton.addActionListener(self)
            buttonPanel.add(cancelButton)

    def initDataPanel(self, dataPanel):
        """ generated source for method initDataPanel """
        textLine = TextField()
        textLine.addActionListener(self)
        dataPanel.add(textLine, BorderLayout.SOUTH)

    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        source = e.getSource()
        if source == okButton or source == textLine:
            input = textLine.getText()
            self.setVisible(False)
        elif source == cancelButton:
            input = None
            self.setVisible(False)

    cancelButton = None
    okButton = None
    textLine = None
    input = None


class AWTBooleanInputDialog(AWTDialog):
    """ generated source for class AWTBooleanInputDialog """
    def __init__(self, frame_, msg, icon, trueLabel, falseLabel, allowCancel):
        """ generated source for method __init__ """
        super(AWTBooleanInputDialog, self).__init__(allowCancel)
        setMessage(msg)
        trueButton.setLabel(trueLabel)
        falseButton.setLabel(falseLabel)

    def getInput(self):
        """ generated source for method getInput """
        return input

    def initButtonPanel(self, buttonPanel, allowCancel):
        """ generated source for method initButtonPanel """
        trueButton = Button("True")
        trueButton.addActionListener(self)
        buttonPanel.add(trueButton)
        falseButton = Button("False")
        falseButton.addActionListener(self)
        buttonPanel.add(falseButton)
        if allowCancel:
            cancelButton = Button("Cancel")
            cancelButton.addActionListener(self)
            buttonPanel.add(cancelButton)

    def initDataPanel(self, dataPanel):
        """ generated source for method initDataPanel """

    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        source = e.getSource()
        if source == trueButton:
            input = Boolean.TRUE
            setVisible(False)
        elif source == falseButton:
            input = Boolean.FALSE
            setVisible(False)
        elif source == cancelButton:
            input = None
            setVisible(False)

    trueButton = None
    falseButton = None
    cancelButton = None
    input = None


class AWTIconCanvas(Canvas):
    """ generated source for class AWTIconCanvas """
    def __init__(self, icon):
        """ generated source for method __init__ """
        super(AWTIconCanvas, self).__init__()
        myIcon = icon

    def getMinimumSize(self):
        """ generated source for method getMinimumSize """
        return Dimension(48, 48)

    def getPreferredSize(self):
        """ generated source for method getPreferredSize """
        return self.getMinimumSize()

    def paint(self, g):
        """ generated source for method paint """
        g.drawImage(myIcon, 8, 8, self)

    myIcon = None


class AWTMessageCanvas(Canvas):
    """ generated source for class AWTMessageCanvas """
    MARGIN = 8
    MESSAGE_FONT = Font("Dialog", Font.PLAIN, 12)

    def __init__(self):
        """ generated source for method __init__ """
        super(AWTMessageCanvas, self).__init__()
        setFont(self.MESSAGE_FONT)

    def setMessage(self, msg):
        """ generated source for method setMessage """
        message = msg

    def paint(self, g):
        """ generated source for method paint """
        fm = g.getFontMetrics()
        x = self.MARGIN
        y = self.MARGIN + fm.getAscent()
        limit = getSize().width - self.MARGIN
        tokenizer = StringTokenizer(message, " ", True)
        while tokenizer.hasMoreTokens():
            token = tokenizer.nextToken()
            width = fm.stringWidth(token)
            if x + width > limit:
                x = self.MARGIN
                y += fm.getHeight()
                if token == " ":
                    continue 
            g.drawString(token, x, y)
            x += width

    message = None

