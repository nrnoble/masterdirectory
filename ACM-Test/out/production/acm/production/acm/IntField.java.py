#!/usr/bin/env python
""" generated source for module IntField """
from __future__ import print_function
# 
#  * @(#)IntField.java   1.99.1 08/12/08
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
#  Bug fix 2-Mar-07 (ESR, JTFBug 2007-004)
#    1. Fixed bug in the formatting code that allowed the display to
#       extend beyond the boundaries of the component.
# 
#  Bug fix 6-May-07 (ESR, JTFBug 2007-006)
#    1. Fixed various bugs in the localization of numbers.
# 
#  Feature enhancement 26-May-08 (ESR)
#    1. Added support for serialization.
# package: acm.gui
#  Class: IntField 
# 
#  * This class implements a simple interactor that accepts an integer value.
#  
class IntField(JTextField):
    """ generated source for class IntField """
    #  Constructor: IntField() 
    # 
    #  * Creates a new field object for entering a <code>int</code> value.
    #  * The contents of the field are initially blank.
    #  *
    #  * @usage IntField field = new IntField();
    #  
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(IntField, self).__init__()
        self.__init__("", Integer.MIN_VALUE, Integer.MAX_VALUE)

    #  Constructor: IntField(value) 
    # 
    #  * Creates a new field object for entering a <code>int</code> value.
    #  * The contents of the field initially contain the specified value.
    #  *
    #  * @usage IntField field = new IntField(value);
    #  * @param value The value to store in the field
    #  
    @__init__.register(object, int)
    def __init___0(self, value):
        """ generated source for method __init___0 """
        super(IntField, self).__init__()
        self.__init__("" + value, Integer.MIN_VALUE, Integer.MAX_VALUE)

    #  Constructor: IntField(low, high) 
    # 
    #  * Creates a new field object for entering a <code>int</code> value,
    #  * which is constrained to be within the specified range. The contents
    #  * of the field are initially blank.
    #  *
    #  * @usage IntField field = new IntField(low, high);
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  
    @__init__.register(object, int, int)
    def __init___1(self, low, high):
        """ generated source for method __init___1 """
        super(IntField, self).__init__()
        self.__init__("", low, high)

    #  Constructor: IntField(value, low, high) 
    # 
    #  * Creates a new field object for entering a <code>int</code> value,
    #  * which is constrained to be within the specified range. The contents
    #  * of the field initially contain the specified value.
    #  *
    #  * @usage IntField field = new IntField(value, low, high);
    #  * @param value The value to store in the field
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  
    @__init__.register(object, int, int, int)
    def __init___2(self, value, low, high):
        """ generated source for method __init___2 """
        super(IntField, self).__init__()
        self.__init__("" + value, low, high)

    #  Private constructor: IntField(str, low, high) 
    # 
    #  * Creates a new field object for entering a <code>int</code> value,
    #  * which is constrained to be within the specified range. The contents
    #  * of the field initially contain the specified string.
    #  
    @__init__.register(object, str, int, int)
    def __init___3(self, str_, low, high):
        """ generated source for method __init___3 """
        super(IntField, self).__init__()
        parser = NumberFormat.getNumberInstance(Locale.US)
        setBackground(Color.WHITE)
        setHorizontalAlignment(RIGHT)
        minValue = low
        maxValue = high
        setText(str_)
        exceptionOnError = False

    #  Method: getValue() 
    # 
    #  * Returns the value of this field as a <code>int</code>.  If this value is either
    #  * not a legal numeric value or is outside the specified range, this method will
    #  * either pop up a dialog allowing the user to reenter the value or throw an
    #  * <code>ErrorException</code> depending on the state of the <code>exceptionOnError</code>
    #  * flag.
    #  *
    #  * @usage int n = field.getValue();
    #  * @return The value stored in the field as a <code>int</code>
    #  
    def getValue(self):
        """ generated source for method getValue """
        text = getText().trim()
        if 0 == len(text):
            if minValue <= 0 and maxValue >= 0:
                return 0
            return minValue
        msg = None
        value = 0
        while True:
            try:
                value = parser.parse(text).intValue()
                if value >= minValue and value <= maxValue:
                    break
                msg = "Value is outside the specified range"
            except ParseException as ex:
                msg = "Illegal integer format"
            if exceptionOnError:
                raise ErrorException(msg)
            else:
                prompt = "Enter an integer"
                if minValue != Integer.MIN_VALUE:
                    if maxValue != Integer.MAX_VALUE:
                        prompt += " between " + minValue + " and " + maxValue
                    else:
                        prompt += " greater than " + minValue
                else:
                    if maxValue != Integer.MAX_VALUE:
                        prompt += " less than " + maxValue
                if dialog == None:
                    dialog = IODialog(self)
                value = dialog.readInt(prompt, minValue, maxValue)
                break
        setValue(value)
        return value

    #  Method: setValue(n) 
    # 
    #  * Sets the value of a field.
    #  *
    #  * @usage field.setValue(n);
    #  * @param n The value to be stored in the field
    #  
    def setValue(self, n):
        """ generated source for method setValue """
        setText(defaultFormat(n) if (formatter == None) else formatter.format(n))

    #  Method: getFormat() 
    # 
    #  * Returns the format currently in use for this field, or
    #  * <code>null</code> if no format has been set.
    #  *
    #  * @usage String format = field.getFormat();
    #  * @return The format for this field
    #  
    def getFormat(self):
        """ generated source for method getFormat """
        return formatString

    #  Method: setFormat(format) 
    # 
    #  * Sets the format used for the field.  The structure of the
    #  * format string is described in the comments for the DecimalFormat
    #  * class.
    #  *
    #  * @usage field.setFormat(format);
    #  * @param format The format to use for the field
    #  
    def setFormat(self, format):
        """ generated source for method setFormat """
        contents = getText().trim()
        value = 0
        if 0 != len(contents):
            try:
                value = parser.parse(contents).intValue()
            except ParseException as ex:
                raise ErrorException(ex)
        formatString = format
        if format == None:
            formatter = None
            parser = NumberFormat.getNumberInstance(Locale.US)
        else:
            formatter = DecimalFormat() if (0 == len(format)) else DecimalFormat(format)
            parser = formatter
        if 0 != len(contents):
            self.setValue(value)

    #  Method: setExceptionOnError(flag) 
    # 
    #  * Sets the error-handling mode of this interactor as specified by the <code>flag</code>
    #  * parameter.  If <code>flag</code> is <code>false</code> (which is the default),
    #  * calling <a href="#getValue()"><code>getValue</code></a> on this interactor displays
    #  * a dialog that gives the user a chance to retry after erroneous input.  If this
    #  * value is set to <code>true</code>, illegal input raises an
    #  * <a href="../util/ErrorException.html"><code>ErrorException</code></a> instead.
    #  *
    #  * @usage field.setExceptionOnError(flag);
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

    #  Override method: getPreferredSize() 
    # 
    #  * Overrides the standard definition to impose a target size.
    #  * @noshow
    #  
    def getPreferredSize(self):
        """ generated source for method getPreferredSize """
        size = super(IntField, self).getPreferredSize()
        return Dimension(max(MINIMUM_WIDTH, size.width), max(MINIMUM_HEIGHT, size.height))

    #  Private method: defaultFormat(n) 
    # 
    #  * This method formats the number if the formatter is <code>null</code>.
    #  * The only special case that applies occurs if the output is larger than
    #  * the field, in which case the entire display is replaced by number signs.
    #  
    def defaultFormat(self, n):
        """ generated source for method defaultFormat """
        str_ = "" + n
        availableSpace = getSize().width - 2 * PIXEL_MARGIN
        fm = getFontMetrics(getFont())
        if fm.stringWidth(str_) > availableSpace:
            str_ = ""
            while fm.stringWidth(str_ + "#") <= availableSpace:
                str_ += "#"
        return str_

    #  Private constants 
    MINIMUM_WIDTH = 60
    MINIMUM_HEIGHT = 22
    PIXEL_MARGIN = 2

    #  Private instance variables 
    exceptionOnError = bool()
    minValue = int()
    maxValue = int()
    formatString = None
    formatter = None
    parser = None
    dialog = None

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

