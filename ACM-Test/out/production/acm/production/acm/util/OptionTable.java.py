#!/usr/bin/env python
""" generated source for module OptionTable """
from __future__ import print_function
# 
#  * @(#)OptionTable.java   1.99.1 08/12/08
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
#    1. Eliminated relationship to HashTable superclass.
#    2. Added generic type tags.
# package: acm.util
#  Class: OptionTable 
# 
#  * This class implements a simple tool for parsing key/value pairs from
#  * a string.
#  
class OptionTable(object):
    """ generated source for class OptionTable """
    #  Constructor: OptionTable(str) 
    # 
    #  * Creates a new <code>OptionTable</code> and initializes it
    #  * from the specified string.  The options in <code>str</code>
    #  * are in two possible forms:
    #  *
    #  * <ol>
    #  * <li>key
    #  * <li>key=value
    #  * </ol>
    #  *
    #  * The first option sets the value associated with the key to
    #  * the empty string; the second supplies the value explicitly.
    #  *
    #  * @usage OptionTable options = new OptionTable(str);
    #  * @param str The option string that is parsed to initialize the table
    #  
    @overloaded
    def __init__(self, str_):
        """ generated source for method __init__ """
        self.__init__(str_, None)

    #  Constructor: OptionTable(str, keys) 
    # 
    #  * Creates a new <code>OptionTable</code> from the specified string,
    #  * checking to make sure that all keys exist in the string array
    #  * <code>keys</code>.  If <code>keys</code> is <code>null</code>,
    #  * checking is disabled.
    #  *
    #  * @usage OptionTable options = new OptionTable(str, keys);
    #  * @param str The option string that is parsed to initialize the table
    #  * @param keys An array of strings indicating the legal keys
    #  
    @__init__.register(object, str, str)
    def __init___0(self, str_, keys):
        """ generated source for method __init___0 """
        optionTable = HashMap()
        try:
            tokenizer = createTokenizer(str_)
            ttype = tokenizer.nextToken()
            while ttype != StreamTokenizer.TT_EOF:
                if ttype != StreamTokenizer.TT_WORD:
                    raise ErrorException("Illegal option string: " + str_)
                key = tokenizer.sval
                if keys != None and not keyExists(key, keys):
                    raise ErrorException("Unrecognized option: " + key)
                ttype = tokenizer.nextToken()
                if ttype == '=':
                    ttype = tokenizer.nextToken()
                    if ttype != StreamTokenizer.TT_WORD and ttype != '"' and ttype != '\'':
                        raise ErrorException("Illegal option string: " + str_)
                    optionTable.put(key, tokenizer.sval)
                    ttype = tokenizer.nextToken()
                else:
                    optionTable.put(key, "")
        except IOError as ex:
            raise ErrorException("Illegal option string: " + str_)

    #  Constructor: OptionTable(map) 
    # 
    #  * Creates a new <code>OptionTable</code> from an existing map.
    #  * Most clients will not need to use this method.
    #  *
    #  * @usage OptionTable options = new OptionTable(map);
    #  * @param map An existing key/value mapping
    #  
    @__init__.register(object, Map)
    def __init___1(self, map):
        """ generated source for method __init___1 """
        optionTable = HashMap()
        i = map.keySet().iterator()
        while i.hasNext():
            key = i.next()
            value = map.get(key)
            optionTable.put(key, value)


    #  Method: isSpecified(key) 
    # 
    #  * Returns true if the key has been specified in the option table.
    #  *
    #  * @usage if (options.isSpecified(key)) . . .
    #  * @param key The key being checked
    #  * @return <code>true</code> if <code>key</code> was specified in the option string
    #  
    def isSpecified(self, key):
        """ generated source for method isSpecified """
        return optionTable.containsKey(key)

    #  Method: getOption(key) 
    # 
    #  * Returns the value associated with <code>key</code> in the option
    #  * table, or <code>null</code> if no such value exists.
    #  *
    #  * @usage String value = options.getOption(key);
    #  * @param key The key
    #  * @return The corresponding option value
    #  
    @overloaded
    def getOption(self, key):
        """ generated source for method getOption """
        return self.getOption(key, None)

    #  Method: getOption(key, defValue) 
    # 
    #  * Returns the value associated with <code>key</code> in the option
    #  * table or the specified default value if no such binding exists.
    #  *
    #  * @usage String value = options.getOption(key, defValue);
    #  * @param key The key
    #  * @param defValue The default to use if the key is not found
    #  * @return The corresponding option value
    #  
    @getOption.register(object, str, str)
    def getOption_0(self, key, defValue):
        """ generated source for method getOption_0 """
        value = optionTable.get(key)
        return defValue if (value == None or value == "") else value

    #  Method: getIntOption(key) 
    # 
    #  * Returns the integer value associated with <code>key</code> in the option
    #  * table, or 0 if no such value exists.
    #  *
    #  * @usage int value = options.getIntOption(key);
    #  * @param key The key
    #  * @return The corresponding option value parsed as an integer
    #  
    @overloaded
    def getIntOption(self, key):
        """ generated source for method getIntOption """
        return self.getIntOption(key, 0)

    #  Method: getIntOption(key, defValue) 
    # 
    #  * Returns the integer value associated with <code>key</code> in the option
    #  * table or the specified default value if no such binding exists.
    #  *
    #  * @usage int value = options.getIntOption(key, defValue);
    #  * @param key The key
    #  * @param defValue The default to use if the key is not found
    #  * @return The corresponding option value
    #  
    @getIntOption.register(object, str, int)
    def getIntOption_0(self, key, defValue):
        """ generated source for method getIntOption_0 """
        binding = self.getOption(key, None)
        if binding == None or binding == "":
            return defValue
        return Integer.decode(binding).intValue()

    #  Method: getDoubleOption(key) 
    # 
    #  * Returns the <code>double</code> value associated with <code>key</code>
    #  * in the option table, or 0.0 if no such value exists.
    #  *
    #  * @usage double value = options.getDoubleOption(key);
    #  * @param key The key
    #  * @return The corresponding option value parsed as a <code>double</code>
    #  
    @overloaded
    def getDoubleOption(self, key):
        """ generated source for method getDoubleOption """
        return self.getDoubleOption(key, 0.0)

    #  Method: getDoubleOption(key, defValue) 
    # 
    #  * Returns the <code>double</code> value associated with <code>key</code>
    #  * in the option table or the specified default value if no such binding
    #  * exists.
    #  *
    #  * @usage double value = options.getDoubleOption(key, defValue);
    #  * @param key The key
    #  * @param defValue The default to use if the key is not found
    #  * @return The corresponding option value
    #  
    @getDoubleOption.register(object, str, float)
    def getDoubleOption_0(self, key, defValue):
        """ generated source for method getDoubleOption_0 """
        binding = self.getOption(key, None)
        if binding == None or binding == "":
            return defValue
        return Double.valueOf(binding).doubleValue()

    #  Method: getMap() 
    # 
    #  * Returns the <code>HashMap</code> used to associate keys and options.
    #  *
    #  * @usage HashMap<String,String> map = options.getMap();
    #  * @return The <code>HashMap</code> used to associate keys and options
    #  * @noshow
    #  
    def getMap(self):
        """ generated source for method getMap """
        return optionTable

    #  Private method: createTokenizer(str) 
    # 
    #  * Creates a tokenizer for the specified string.
    #  
    def createTokenizer(self, str_):
        """ generated source for method createTokenizer """
        t = StreamTokenizer(StringReader(str_))
        t.resetSyntax()
        t.wordChars(str(33), str(('=' - 1)))
        t.wordChars(str(('=' + 1)), str(126))
        t.quoteChar('"')
        t.quoteChar('\'')
        t.whitespaceChars(' ', ' ')
        t.whitespaceChars('\t', '\t')
        return t

    #  Private method: keyExists(key, keys) 
    # 
    #  * Checks to see whether the key exists in the array of keys.
    #  
    def keyExists(self, key, keys):
        """ generated source for method keyExists """
        i = 0
        while len(keys):
            if key == keys[i]:
                return True
            i += 1
        return False

    #  Private instance variables 
    optionTable = None

    #  Serial version UID 
    # 
    #  * The serialization code for this class.  This value should be incremented
    #  * whenever you change the structure of this class in an incompatible way,
    #  * typically by adding a new instance variable.
    #  
    serialVersionUID = 1

