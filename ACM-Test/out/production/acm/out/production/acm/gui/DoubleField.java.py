#!/usr/bin/env python
""" generated source for module DoubleField """
from __future__ import print_function
# 
#  * @(#)DoubleField.java   1.99.1 08/12/08
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
#  Class: DoubleField 
# 
#  * This class implements a simple interactor that accepts a floating-point value.
#  
class DoubleField(JTextField):
    """ generated source for class DoubleField """
    #  Constructor: DoubleField() 
    # 
    #  * Creates a new field object for entering a <code>double</code> value.
    #  * The contents of the field are initially blank.
    #  *
    #  * @usage DoubleField field = new DoubleField();
    #  
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(DoubleField, self).__init__()
        self.__init__("", Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY)

    #  Constructor: DoubleField(value) 
    # 
    #  * Creates a new field object for entering a <code>double</code> value.
    #  * The contents of the field initially contain the specified value.
    #  *
    #  * @usage DoubleField field = new DoubleField(value);
    #  * @param value The value to store in the field
    #  
    @__init__.register(object, float)
    def __init___0(self, value):
        """ generated source for method __init___0 """
        super(DoubleField, self).__init__()
        self.__init__("" + value, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY)

    #  Constructor: DoubleField(low, high) 
    # 
    #  * Creates a new field object for entering a <code>double</code> value,
    #  * which is constrained to be within the specified range. The contents
    #  * of the field are initially blank.
    #  *
    #  * @usage DoubleField field = new DoubleField(low, high);
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  
    @__init__.register(object, float, float)
    def __init___1(self, low, high):
        """ generated source for method __init___1 """
        super(DoubleField, self).__init__()
        self.__init__("", low, high)

    #  Constructor: DoubleField(value, low, high) 
    # 
    #  * Creates a new field object for entering a <code>double</code> value,
    #  * which is constrained to be within the specified range. The contents
    #  * of the field initially contain the specified value.
    #  *
    #  * @usage DoubleField field = new DoubleField(value, low, high);
    #  * @param value The value to store in the field
    #  * @param low The lowest value in the permitted range
    #  * @param high The highest value in the permitted range
    #  
    @__init__.register(object, float, float, float)
    def __init___2(self, value, low, high):
        """ generated source for method __init___2 """
        super(DoubleField, self).__init__()
        self.__init__("" + value, low, high)

    #  Private constructor: DoubleField(str, low, high) 
    # 
    #  * Creates a new field object for entering a <code>double</code> value,
    #  * which is constrained to be within the specified range. The contents
    #  * of the field initially contain the specified string.
    #  
    @__init__.register(object, str, float, float)
    def __init___3(self, str_, low, high):
        """ generated source for method __init___3 """
        super(DoubleField, self).__init__()
        parser = NumberFormat.getNumberInstance(Locale.US)
        setBackground(Color.WHITE)
        setHorizontalAlignment(RIGHT)
        minValue = low
        maxValue = high
        setText(str_)
        exceptionOnError = False

    #  Method: getValue() 
    # 
    #  * Returns the value of this field as a <code>double</code>.  If this value is either
    #  * not a legal numeric value or is outside the specified range, this method will
    #  * either pop up a dialog allowing the user to reenter the value or throw an
    #  * <code>ErrorException</code> depending on the state of the <code>exceptionOnError</code>
    #  * flag.
    #  *
    #  * @usage double d = field.getValue();
    #  * @return The value stored in the field as a <code>double</code>
    #  
    def getValue(self):
        """ generated source for method getValue """
        text = getText().trim()
        if 0 == len(text):
            if minValue <= 0 and maxValue >= 0:
                return 0.0
            return minValue
        msg = None
        value = 0.0
        while True:
            try:
                value = parser.parse(text).doubleValue()
                if value >= minValue and value <= maxValue:
                    break
                msg = "Value is outside the specified range"
            except ParseException as ex:
                msg = "Illegal numeric format"
            if exceptionOnError:
                raise ErrorException(msg)
            else:
                prompt = "Enter a number"
                if minValue != Double.NEGATIVE_INFINITY:
                    if maxValue != Double.POSITIVE_INFINITY:
                        prompt += " between " + minValue + " and " + maxValue
                    else:
                        prompt += " greater than " + minValue
                else:
                    if maxValue != Double.POSITIVE_INFINITY:
                        prompt += " less than " + maxValue
                if dialog == None:
                    dialog = IODialog(self)
                value = dialog.readDouble(prompt, minValue, maxValue)
                break
        setValue(value)
        return value

    #  Method: setValue(d) 
    # 
    #  * Sets the value of a field.
    #  *
    #  * @usage field.setValue(d);
    #  * @param d The value to be stored in the field
    #  
    def setValue(self, d):
        """ generated source for method setValue """
        setText(defaultFormat(d) if (formatter == None) else formatter.format(d))

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
    #  * class.  If a format is set for the field, the format will also be
    #  * used to read the number to ensure that localization is correctly
    #  * handled.
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
                value = parser.parse(contents).doubleValue()
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
        size = super(DoubleField, self).getPreferredSize()
        return Dimension(max(MINIMUM_WIDTH, size.width), max(MINIMUM_HEIGHT, size.height))

    #  Private method: defaultFormat(d) 
    # 
    #  * This method formats the number if the formatter is <code>null</code>.
    #  * The code attempts to fit the value into the field.  All the work comes
    #  * from having to round off the digits that are shifted out of the field.
    #  
    def defaultFormat(self, d):
        """ generated source for method defaultFormat """
        str_ = "" + d
        availableSpace = getSize().width - 2 * PIXEL_MARGIN
        fm = getFontMetrics(getFont())
        if fm.stringWidth(str_) <= availableSpace:
            return str_
        eIndex = str_.indexOf("E")
        suffix = ""
        if eIndex != -1:
            suffix = str_.substring(eIndex)
            str_ = str_.substring(0, eIndex)
            try:
                d = parser.parse(str_).doubleValue()
            except ParseException as ex:
                raise ErrorException(ex)
        standard = NumberFormat.getNumberInstance(Locale.US)
        standard.setGroupingUsed(False)
        head = str_.substring(0, str_.indexOf('.') + 1)
        fractionSpace = availableSpace - fm.stringWidth(head + suffix)
        if fractionSpace > 0:
            fractionDigits = fractionSpace / fm.stringWidth("0")
            standard.setMaximumFractionDigits(fractionDigits)
            return standard.format(d) + suffix
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
    minValue = float()
    maxValue = float()
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

