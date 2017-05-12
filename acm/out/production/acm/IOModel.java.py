#!/usr/bin/env python
""" generated source for module IOModel """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
# 
#  * @(#)IOModel.java   1.99.1 08/12/08
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
#  Interface: IOModel 
# 
#  * The <code>IOModel</code> interface defines the input and output methods
#  * supported by both the <a href="IOConsole.html"><code>IOConsole</code></a>
#  * and <a href="IODialog.html"><code>IODialog</code></a> classes.
#  
class IOModel(object):
    """ generated source for interface IOModel """
    __metaclass__ = ABCMeta
    #  Method: print(value) 
    # 
    #  * Displays the argument value, allowing for the possibility of more
    #  * output on the same line.  The <code>print</code> method is overloaded
    #  * so that <code>value</code> can be of any type.
    #  *
    #  * @usage model.print(value);
    #  * @param value The value to be displayed
    #  
    @abstractmethod
    @overloaded
    def print_(self, value):
        """ generated source for method print_ """

    # 
    #  * Makes sure that <code>print</code> can display a <code>boolean</code>.
    #  * @noshow
    #  
    @abstractmethod
    @print_.register(object, bool)
    def print__0(self, x):
        """ generated source for method print__0 """

    # 
    #  * Makes sure that <code>print</code> can display a <code>char</code>.
    #  * @noshow
    #  
    @abstractmethod
    @print_.register(object, str)
    def print__1(self, x):
        """ generated source for method print__1 """

    # 
    #  * Makes sure that <code>print</code> can display a <code>double</code>.
    #  * @noshow
    #  
    @abstractmethod
    @print_.register(object, float)
    def print__2(self, x):
        """ generated source for method print__2 """

    # 
    #  * Makes sure that <code>print</code> can display a <code>float</code>.
    #  * @noshow
    #  
    @abstractmethod
    @print_.register(object, float)
    def print__3(self, x):
        """ generated source for method print__3 """

    # 
    #  * Makes sure that <code>print</code> can display an <code>int</code>.
    #  * @noshow
    #  
    @abstractmethod
    @print_.register(object, int)
    def print__4(self, x):
        """ generated source for method print__4 """

    # 
    #  * Makes sure that <code>print</code> can display a <code>long</code>.
    #  * @noshow
    #  
    @abstractmethod
    @print_.register(object, long)
    def print__5(self, x):
        """ generated source for method print__5 """

    # 
    #  * Makes sure that <code>print</code> can display an <code>Object</code>.
    #  * @noshow
    #  
    @abstractmethod
    @print_.register(object, object)
    def print__6(self, x):
        """ generated source for method print__6 """

    #  Method: println() 
    # 
    #  * Completes the output line.
    #  *
    #  * @usage io.println();
    #  
    @abstractmethod
    @overloaded
    def println(self):
        """ generated source for method println """

    #  Method: println(value) 
    # 
    #  * Displays the value and then completes the line.  The <code>println</code>
    #  * method is overloaded so that <code>value</code> can be of any type.
    #  *
    #  * @usage io.println(value);
    #  * @param value The value to be displayed
    #  
    @abstractmethod
    @println.register(object, str)
    def println_0(self, value):
        """ generated source for method println_0 """

    # 
    #  * Makes sure that <code>println</code> can display a <code>boolean</code>.
    #  * @noshow
    #  
    @abstractmethod
    @println.register(object, bool)
    def println_1(self, x):
        """ generated source for method println_1 """

    # 
    #  * Makes sure that <code>println</code> can display a <code>char</code>.
    #  * @noshow
    #  
    @abstractmethod
    @println.register(object, str)
    def println_2(self, x):
        """ generated source for method println_2 """

    # 
    #  * Makes sure that <code>println</code> can display a <code>double</code>.
    #  * @noshow
    #  
    @abstractmethod
    @println.register(object, float)
    def println_3(self, x):
        """ generated source for method println_3 """

    # 
    #  * Makes sure that <code>println</code> can display a <code>float</code>.
    #  * @noshow
    #  
    @abstractmethod
    @println.register(object, float)
    def println_4(self, x):
        """ generated source for method println_4 """

    # 
    #  * Makes sure that <code>println</code> can display an <code>int</code>.
    #  * @noshow
    #  
    @abstractmethod
    @println.register(object, int)
    def println_5(self, x):
        """ generated source for method println_5 """

    # 
    #  * Makes sure that <code>println</code> can display a <code>long</code>.
    #  * @noshow
    #  
    @abstractmethod
    @println.register(object, long)
    def println_6(self, x):
        """ generated source for method println_6 """

    # 
    #  * Makes sure that <code>println</code> can display an <code>Object</code>.
    #  * @noshow
    #  
    @abstractmethod
    @println.register(object, object)
    def println_7(self, x):
        """ generated source for method println_7 """

    #  Method: showErrorMessage(msg) 
    # 
    #  * Displays the error message.
    #  *
    #  * @usage io.showErrorMessage(msg);
    #  * @param msg The error msg to be displayed
    #  
    @abstractmethod
    def showErrorMessage(self, msg):
        """ generated source for method showErrorMessage """

    #  Method: readLine() 
    # 
    #  * Reads and returns a line of input, without including the end-of-line
    #  * characters that terminate the input.
    #  *
    #  * @usage String str = io.readLine();
    #  * @return The next line of input as a <code>String</code>
    #  
    @abstractmethod
    @overloaded
    def readLine(self):
        """ generated source for method readLine """

    #  Method: readLine(prompt) 
    # 
    #  * Prompts the user to enter a line of text, which is then returned
    #  * as the value of this method.  The end-of-line characters that terminate
    #  * the input are not included in the returned string.
    #  *
    #  * @usage String str = io.readLine(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The next line of input as a <code>String</code>
    #  
    @abstractmethod
    @readLine.register(object, str)
    def readLine_0(self, prompt):
        """ generated source for method readLine_0 """

    #  Method: readInt() 
    # 
    #  * Reads and returns an integer value from the user.
    #  *
    #  * @usage int n = io.readInt();
    #  * @return The value of the input interpreted as a decimal integer
    #  
    @abstractmethod
    @overloaded
    def readInt(self):
        """ generated source for method readInt """

    #  Method: readInt(low, high) 
    # 
    #  * Reads and returns an integer value from the user, which is constrained to
    #  * be within the specified inclusive range.
    #  *
    #  * @usage int n = io.readInt(low, high);
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a decimal integer
    #  
    @abstractmethod
    @readInt.register(object, int, int)
    def readInt_0(self, low, high):
        """ generated source for method readInt_0 """

    #  Method: readInt(prompt) 
    # 
    #  * Prompts the user to enter an integer, which is then returned as the value
    #  * of this method.
    #  *
    #  * @usage int n = io.readInt(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The value of the input interpreted as a decimal integer
    #  
    @abstractmethod
    @readInt.register(object, str)
    def readInt_1(self, prompt):
        """ generated source for method readInt_1 """

    #  Method: readInt(prompt, low, high) 
    # 
    #  * Prompts the user to enter an integer, which is then returned as the value
    #  * of this method.  The value must be within the inclusive range between
    #  * <code>low</code> and <code>high</code>.
    #  *
    #  * @usage int n = io.readInt(prompt, low, high);
    #  * @param prompt The prompt string to display to the user
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a decimal integer
    #  
    @abstractmethod
    @readInt.register(object, str, int, int)
    def readInt_2(self, prompt, low, high):
        """ generated source for method readInt_2 """

    #  Method: readDouble() 
    # 
    #  * Reads and returns a double-precision value from the user.
    #  *
    #  * @usage double d = io.readDouble();
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @abstractmethod
    @overloaded
    def readDouble(self):
        """ generated source for method readDouble """

    #  Method: readDouble(low, high) 
    # 
    #  * Reads and returns a double-precision value from the user, which is
    #  * constrained to be within the specified inclusive range.
    #  *
    #  * @usage double d = io.readDouble(low, high);
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @abstractmethod
    @readDouble.register(object, float, float)
    def readDouble_0(self, low, high):
        """ generated source for method readDouble_0 """

    #  Method: readDouble(prompt) 
    # 
    #  * Prompts the user to enter an double-precision number, which is then
    #  * returned as the value of this method.
    #  *
    #  * @usage double d = io.readDouble(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @abstractmethod
    @readDouble.register(object, str)
    def readDouble_1(self, prompt):
        """ generated source for method readDouble_1 """

    #  Method: readDouble(prompt, low, high) 
    # 
    #  * Prompts the user to enter an double-precision number, which is then returned
    #  * as the value of this method.  The value must be within the inclusive range
    #  * between <code>low</code> and <code>high</code>.
    #  *
    #  * @usage d = io.readDouble(prompt, low, high);
    #  * @param prompt The prompt string to display to the user
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  * @return The value of the input interpreted as a <code>double</code>
    #  
    @abstractmethod
    @readDouble.register(object, str, float, float)
    def readDouble_2(self, prompt, low, high):
        """ generated source for method readDouble_2 """

    #  Method: readBoolean() 
    # 
    #  * Reads and returns a boolean value from the user, which must match
    #  * either <code>true</code> or <code>false</code>, ignoring case.
    #  *
    #  * @usage boolean flag = io.readBoolean();
    #  * @return The value of the input interpreted as a boolean value
    #  
    @abstractmethod
    @overloaded
    def readBoolean(self):
        """ generated source for method readBoolean """

    #  Method: readBoolean(prompt) 
    # 
    #  * Prompts the user to enter a boolean value, which is then returned as
    #  * the value of this method.
    #  *
    #  * @usage boolean flag = io.readBoolean(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @return The value of the input interpreted as a boolean value
    #  
    @abstractmethod
    @readBoolean.register(object, str)
    def readBoolean_0(self, prompt):
        """ generated source for method readBoolean_0 """

    #  Method: readBoolean(prompt, trueLabel, falseLabel) 
    # 
    #  * Prompts the user to enter a value, which is interpreted as a boolean value
    #  * by matching it against the <code>trueLabel</code> and <code>falseLabel</code>
    #  * parameters.
    #  *
    #  * @usage boolean flag = dialog.readBoolean(prompt);
    #  * @param prompt The prompt string to display to the user
    #  * @param trueLabel The string used to indicate <code>true</code>
    #  * @param falseLabel The string used to indicate <code>false</code>
    #  * @return The value of the input interpreted as a boolean value
    #  
    @abstractmethod
    @readBoolean.register(object, str, str, str)
    def readBoolean_1(self, prompt, trueLabel, falseLabel):
        """ generated source for method readBoolean_1 """

