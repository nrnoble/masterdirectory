#!/usr/bin/env python
""" generated source for module PLATFO~1 """
from __future__ import print_function
from functools import wraps
from threading import RLock

def lock_for_object(obj, locks={}):
    return locks.setdefault(id(obj), RLock())

def synchronized(call):
    assert call.__code__.co_varnames[0] in ['self', 'cls']
    #@wraps(call)
    def inner(*args, **kwds):
        with lock_for_object(args[0]):
            return call(*args, **kwds)
    return inner

# 
#  Source code recreated from a .class file by IntelliJ IDEA
#  (powered by Fernflower decompiler)
# 
# package: sun.util.logging
class PlatformLogger(object):
    """ generated source for class PlatformLogger """
    OFF = 2147483647
    SEVERE = 1000
    WARNING = 900
    INFO = 800
    CONFIG = 700
    FINE = 500
    FINER = 400
    FINEST = 300
    ALL = -2147483648
    DEFAULT_LEVEL = None
    loggingEnabled = bool()
    loggers = None
    loggerProxy = None
    javaLoggerProxy = None

    #@classmethod
    #@synchronized
    def getLogger(cls, var0):
        """ generated source for method getLogger """
        pass
        # var1 = None
        # var2 = cls.loggers.get(var0)
        # if var2 != None:
        #     var1 = var2.get()
        # if var1 == None:
        #     var1 = PlatformLogger(var0)
        #     cls.loggers.put(var0, WeakReference(var1))
        # return var1

    #@classmethod
    #@synchronized
    def redirectPlatformLoggers(cls):
        """ generated source for method redirectPlatformLoggers """
        # if not cls.loggingEnabled and LoggingSupport.isAvailable():
        #     cls.loggingEnabled = True
        #     var0 = cls.loggers.entrySet().iterator()
        #     while var0.hasNext():
        #         var1 = var0.next()
        #         var2 = var1.getValue()
        #         var3 = var2.get()
        #         if var3 != None:
        #             var3.redirectToJavaLoggerProxy()

    def redirectToJavaLoggerProxy(self):
        """ generated source for method redirectToJavaLoggerProxy """
        var1 = PlatformLogger.DefaultLoggerProxy.__class__.cast(self.loggerProxy)
        var2 = PlatformLogger.JavaLoggerProxy(var1.name, var1.level)
        self.javaLoggerProxy = var2
        self.loggerProxy = var2

    def __init__(self, var1):
        """ generated source for method __init__ """
        if self.loggingEnabled:
            self.loggerProxy = self.javaLoggerProxy = PlatformLogger.JavaLoggerProxy(var1)
        else:
            self.loggerProxy = PlatformLogger.DefaultLoggerProxy(var1)

    def isEnabled(self):
        """ generated source for method isEnabled """
        return self.loggerProxy.isEnabled()

    def getName(self):
        """ generated source for method getName """
        return self.loggerProxy.name

    def isLoggable(self, var1):
        """ generated source for method isLoggable """
        if var1 == None:
            raise NullPointerException()
        else:
            var2 = self.javaLoggerProxy
            return var2.isLoggable(var1) if var2 != None else self.loggerProxy.isLoggable(var1)

    def level(self):
        """ generated source for method level """
        return self.loggerProxy.getLevel()

    def setLevel(self, var1):
        """ generated source for method setLevel """
        self.loggerProxy.setLevel(var1)

#    #@overloaded
    def severe(self, var1):
        """ generated source for method severe """
        self.loggerProxy.doLog(PlatformLogger.Level.SEVERE, var1)

    ##@severe.register(object, str, Throwable)
    def severe_0(self, var1, var2):
        """ generated source for method severe_0 """
        self.loggerProxy.doLog(PlatformLogger.Level.SEVERE, var1, var2)

    ##@severe.register(object, str, A)
    def severe_1(self, var1, *var2):
        """ generated source for method severe_1 """
        self.loggerProxy.doLog(PlatformLogger.Level.SEVERE, var1, var2)

    ##@overloaded
    def warning(self, var1):
        """ generated source for method warning """
        self.loggerProxy.doLog(PlatformLogger.Level.WARNING, var1)

    ##@warning.register(object, str, Throwable)
    def warning_0(self, var1, var2):
        """ generated source for method warning_0 """
        self.loggerProxy.doLog(PlatformLogger.Level.WARNING, var1, var2)

    ##@warning.register(object, str, A)
    def warning_1(self, var1, *var2):
        """ generated source for method warning_1 """
        self.loggerProxy.doLog(PlatformLogger.Level.WARNING, var1, var2)

    ##@overloaded
    def info(self, var1):
        """ generated source for method info """
        self.loggerProxy.doLog(PlatformLogger.Level.INFO, var1)

    ##@info.register(object, str, Throwable)
    def info_0(self, var1, var2):
        """ generated source for method info_0 """
        self.loggerProxy.doLog(PlatformLogger.Level.INFO, var1, var2)

    ##@info.register(object, str, A)
    def info_1(self, var1, *var2):
        """ generated source for method info_1 """
        self.loggerProxy.doLog(PlatformLogger.Level.INFO, var1, var2)

    ##@overloaded
    def config(self, var1):
        """ generated source for method config """
        self.loggerProxy.doLog(PlatformLogger.Level.CONFIG, var1)

    ##@config.register(object, str, Throwable)
    def config_0(self, var1, var2):
        """ generated source for method config_0 """
        self.loggerProxy.doLog(PlatformLogger.Level.CONFIG, var1, var2)

    #@config.register(object, str, A)
    def config_1(self, var1, *var2):
        """ generated source for method config_1 """
        self.loggerProxy.doLog(PlatformLogger.Level.CONFIG, var1, var2)

    #@overloaded
    def fine(self, var1):
        """ generated source for method fine """
        self.loggerProxy.doLog(PlatformLogger.Level.FINE, var1)

    #@fine.register(object, str, Throwable)
    def fine_0(self, var1, var2):
        """ generated source for method fine_0 """
        self.loggerProxy.doLog(PlatformLogger.Level.FINE, var1, var2)

    #@fine.register(object, str, A)
    def fine_1(self, var1, *var2):
        """ generated source for method fine_1 """
        self.loggerProxy.doLog(PlatformLogger.Level.FINE, var1, var2)

    #@overloaded
    def finer(self, var1):
        """ generated source for method finer """
        self.loggerProxy.doLog(PlatformLogger.Level.FINER, var1)

    #@finer.register(object, str, Throwable)
    def finer_0(self, var1, var2):
        """ generated source for method finer_0 """
        self.loggerProxy.doLog(PlatformLogger.Level.FINER, var1, var2)

    #@finer.register(object, str, A)
    def finer_1(self, var1, *var2):
        """ generated source for method finer_1 """
        self.loggerProxy.doLog(PlatformLogger.Level.FINER, var1, var2)

    #@overloaded
    def finest(self, var1):
        """ generated source for method finest """
        self.loggerProxy.doLog(PlatformLogger.Level.FINEST, var1)

    #@finest.register(object, str, Throwable)
    def finest_0(self, var1, var2):
        """ generated source for method finest_0 """
        self.loggerProxy.doLog(PlatformLogger.Level.FINEST, var1, var2)

    #@finest.register(object, str, A)
    def finest_1(self, var1, *var2):
        """ generated source for method finest_1 """
        self.loggerProxy.doLog(PlatformLogger.Level.FINEST, var1, var2)

    def run(self):
        """ generated source for method run """
        var1 = System.getProperty("java.util.logging.config.class")
        var2 = System.getProperty("java.util.logging.config.file")
        return Boolean.valueOf(var1 != None or var2 != None)

    class DefaultLoggerProxy(object):
        # """ generated source for class DefaultLoggerProxy """
        # effectiveLevel = self.deriveEffectiveLevel(None)
        # level = None
        # formatString = LoggingSupport.getSimpleFormat(False)
        # date = Date()

        #@classmethod
        def outputStream(cls):
            """ generated source for method outputStream """
            return System.err

        def __init__(self, var1):
            """ generated source for method __init__ """
            #super(DefaultLoggerProxy, self).__init__(var1)

        def isEnabled(self):
            """ generated source for method isEnabled """
            return self.effectiveLevel != PlatformLogger.Level.OFF

        def getLevel(self):
            """ generated source for method getLevel """
            return self.level

        def setLevel(self, var1):
            """ generated source for method setLevel """
            var2 = self.level
            if var2 != var1:
                self.level = var1
                self.effectiveLevel = self.deriveEffectiveLevel(var1)

        #@overloaded
        def doLog(self, var1, var2):
            """ generated source for method doLog """
            if self.isLoggable(var1):
                self.outputStream().print_(self.format(var1, var2, None))

        #@doLog.register(object, PlatformLogger.Level, str, Throwable)
        def doLog_0(self, var1, var2, var3):
            """ generated source for method doLog_0 """
            if self.isLoggable(var1):
                self.outputStream().print_(self.format(var1, var2, var3))

        #@doLog.register(object, PlatformLogger.Level, str, A)
        def doLog_1(self, var1, var2, *var3):
            """ generated source for method doLog_1 """
            if self.isLoggable(var1):
                var4 = self.formatMessage(var2, var3)
                self.outputStream().print_(self.format(var1, var4, None))

        def isLoggable(self, var1):
            """ generated source for method isLoggable """
            var2 = self.effectiveLevel
            return var1.intValue() >= var2.intValue() and var2 != PlatformLogger.Level.OFF

        def deriveEffectiveLevel(self, var1):
            """ generated source for method deriveEffectiveLevel """
            return PlatformLogger.DEFAULT_LEVEL if var1 == None else var1

        def formatMessage(self, var1, *var2):
            """ generated source for method formatMessage """
            try:
                return (var1 if var1.indexOf("{0") < 0 and var1.indexOf("{1") < 0 and var1.indexOf("{2") < 0 and var1.indexOf("{3") < 0 else MessageFormat.format(var1, var2)) if var2 != None and len(var2) else var1
            except Exception as var4:
                return var1

        #@synchronized
        def format(self, var1, var2, var3):
            """ generated source for method format """
            self.date.setTime(System.currentTimeMillis())
            var4 = ""
            if var3 != None:
                var5 = StringWriter()
                var6 = PrintWriter(var5)
                var6.println()
                var3.printStackTrace(var6)
                var6.close()
                var4 = var5.__str__()

            return self.formatString.format([None]  )

        def getCallerInfo(self):
            """ generated source for method getCallerInfo """
            var1 = None
            var2 = None
            var3 = SharedSecrets.getJavaLangAccess()
            var4 = Throwable()
            var5 = var3.getStackTraceDepth(var4)
            var6 = "sun.util.logging.PlatformLogger"
            var7 = True
            var8 = 0
            while var8 < var5:
                var9 = var3.getStackTraceElement(var4, var8)
                var10 = var9.getClassName()
                if var7:
                    if var10 == var6:
                        var7 = False
                elif not var10 == var6:
                    var1 = var10
                    var2 = var9.getMethodName()
                    break
                var8 += 1
            return var1 + " " + var2 if var1 != None else self.name

    class JavaLoggerProxy(PlatformLogger, LoggerProxy):
        """ generated source for class JavaLoggerProxy """
        javaLogger = None

        #@overloaded
        def __init__(self, var1):
            """ generated source for method __init__ """
            super(JavaLoggerProxy, self).__init__()
            self.__init__(var1, None)

        #@__init__.register(object, str, PlatformLogger.Level)
        def __init___0(self, var1, var2):
            """ generated source for method __init___0 """
            super(JavaLoggerProxy, self).__init__(var1)
            self.javaLogger = LoggingSupport.getLogger(var1)
            if var2 != None:
                LoggingSupport.setLevel(self.javaLogger, var2.javaLevel)

        #@overloaded
        def doLog(self, var1, var2):
            """ generated source for method doLog """
            LoggingSupport.log(self.javaLogger, var1.javaLevel, var2)

        #@doLog.register(object, PlatformLogger.Level, str, Throwable)
        def doLog_0(self, var1, var2, var3):
            """ generated source for method doLog_0 """
            LoggingSupport.log(self.javaLogger, var1.javaLevel, var2, var3)

        #@doLog.register(object, PlatformLogger.Level, str, A)
        def doLog_1(self, var1, var2, *var3):
            """ generated source for method doLog_1 """
            if self.isLoggable(var1):
                var4 = len(var3)
                var5 = [None] * var4
                var6 = 0
                while var6 < var4:
                    var5[var6] = str(var3[var6])
                    var6 += 1
                LoggingSupport.log(self.javaLogger, var1.javaLevel, var2, var5)

        def isEnabled(self):
            """ generated source for method isEnabled """
            return LoggingSupport.isLoggable(self.javaLogger, PlatformLogger.Level.OFF.javaLevel)

        def getLevel(self):
            """ generated source for method getLevel """
            var1 = LoggingSupport.getLevel(self.javaLogger)
            if var1 == None:
                return None
            else:
                try:
                    return PlatformLogger.Level.valueOf(LoggingSupport.getLevelName(var1))
                except IllegalArgumentException as var3:
                    return PlatformLogger.Level.valueOf(LoggingSupport.getLevelValue(var1))

        def setLevel(self, var1):
            """ generated source for method setLevel """
            LoggingSupport.setLevel(self.javaLogger, None if var1 == None else var1.javaLevel)

        def isLoggable(self, var1):
            """ generated source for method isLoggable """
            return LoggingSupport.isLoggable(self.javaLogger, var1.javaLevel)

        var0 = PlatformLogger.Level.values()
        var1 = int()
        var2 = 0
        var3 = var0[var2]

    class Level:
        """ generated source for enum Level """
        ALL = u'ALL'
        FINEST = u'FINEST'
        FINER = u'FINER'
        FINE = u'FINE'
        CONFIG = u'CONFIG'
        INFO = u'INFO'
        WARNING = u'WARNING'
        SEVERE = u'SEVERE'
        OFF = u'OFF'
        javaLevel = None
        LEVEL_VALUES = []

        def __init__(self):
            """ generated source for method __init__ """

        def intValue(self):
            """ generated source for method intValue """
            return self.LEVEL_VALUES[self.ordinal()]

        #@classmethod
        def valueOf(cls, var0):
            """ generated source for method valueOf """
            if var0 == -2147483648:
                return cls.ALL
            elif var0 == 300:
                return cls.FINEST
            elif var0 == 400:
                return cls.FINER
            elif var0 == 500:
                return cls.FINE
            elif var0 == 700:
                return cls.CONFIG
            elif var0 == 800:
                return cls.INFO
            elif var0 == 900:
                return cls.WARNING
            elif var0 == 1000:
                return cls.SEVERE
            elif var0 == 2147483647:
                return cls.OFF
            else:
                var1 = Arrays.binarySearch(cls.LEVEL_VALUES, 0, len(LEVEL_VALUES), var0)
                return values()[var1 if var1 >= 0 else -var1 - 1]

    class LoggerProxy(object):
        """ generated source for class LoggerProxy """
        name = None

        def __init__(self, var1):
            """ generated source for method __init__ """
            self.name = var1

        def isEnabled(self):
            """ generated source for method isEnabled """

        def getLevel(self):
            """ generated source for method getLevel """

        def setLevel(self, var1):
            """ generated source for method setLevel """

        #@overloaded
        def doLog(self, var1, var2):
            """ generated source for method doLog """

        #@doLog.register(object, PlatformLogger.self.Level, str, Throwable)
        def doLog_0(self, var1, var2, var3):
            """ generated source for method doLog_0 """

        #@doLog.register(object, PlatformLogger.self.Level, str, A)
        def doLog_1(self, var1, var2, *var3):
            """ generated source for method doLog_1 """

        def isLoggable(self, var1):
            """ generated source for method isLoggable """

