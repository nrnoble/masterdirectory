#!/usr/bin/env python
""" generated source for module Platform """
from __future__ import print_function
# 
#  * @(#)Platform.java   1.99.1 08/12/08
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
#  REVISION HISTORY [NOTE: Remember to update JTF_VERSION on each release]
# 
#  -- V2.0 --
#  Feature enhancement 2-Mar-07 (ESR)
#    1. Added copyFileTypeAndCreator method.
#    2. Added getJTFVersion method.
# package: acm.util
#  Class: Platform 
# 
#  * This class contains methods to support platform-specific code.
#  
class Platform(object):
    """ generated source for class Platform """
    #  Constant: UNKNOWN 
    #  Indicates that the type of system cannot be determined. 
    UNKNOWN = 0

    #  Constant: MAC 
    #  Indicates that the system is some variety of Apple Macintosh. 
    MAC = 1

    #  Constant: UNIX 
    #  Indicates that the system is some variety of Unix or Linux. 
    UNIX = 2

    #  Constant: WINDOWS 
    #  Indicates that the system is some variety of Microsoft Windows. 
    WINDOWS = 3

    #  Private constructor: Platform 
    # 
    #  * Prevents anyone else from constructing this class.
    #  
    def __init__(self):
        """ generated source for method __init__ """
        #  Empty 

    #  Static method: getPlatform() 
    # 
    #  * Returns an enumeration constant specifying the type of platform
    #  * on which this applet is running, which is one of the supported
    #  * types defined at the beginning of this class.
    #  *
    #  * @return A constant specifying the platform type
    #  
    @classmethod
    def getPlatform(cls):
        """ generated source for method getPlatform """
        if platform != -1:
            return platform
        name = System.getProperty("os.name", "").lower()
        if name.startsWith("mac"):
            return platform = cls.MAC
        if name.startsWith("windows"):
            return platform = cls.WINDOWS
        if name.startsWith("microsoft"):
            return platform = cls.WINDOWS
        if name.startsWith("ms"):
            return platform = cls.WINDOWS
        if name.startsWith("unix"):
            return platform = cls.UNIX
        if name.startsWith("linux"):
            return platform = cls.UNIX
        return platform = cls.UNKNOWN

    #  Static method: isMac 
    # 
    #  * Checks whether the platform is a Macintosh.
    #  *
    #  * @return <code>true</code> if the platform is a Macintosh, <code>false</code> otherwise
    #  
    @classmethod
    def isMac(cls):
        """ generated source for method isMac """
        return cls.getPlatform() == cls.MAC

    #  Static method: isWindows() 
    # 
    #  * Checks whether the platform is a Windows machine.
    #  *
    #  * @return <code>true</code> if the platform is a Windows machine, <code>false</code> otherwise
    #  
    @classmethod
    def isWindows(cls):
        """ generated source for method isWindows """
        return cls.getPlatform() == cls.WINDOWS

    #  Static method: isUnix() 
    # 
    #  * Checks whether the platform is Unix.
    #  *
    #  * @return <code>true</code> if the platform is Unix, <code>false</code> otherwise
    #  
    @classmethod
    def isUnix(cls):
        """ generated source for method isUnix """
        return cls.getPlatform() == cls.UNIX

    #  Static method: setFileTypeAndCreator(filename, type, creator) 
    # 
    #  * Sets the Macintosh file type and creator.  This method is ignored on non-Mac
    #  * platforms.
    #  *
    #  * @param filename The name of the file
    #  * @param type A four-character string indicating the file type
    #  * @param creator A four-character string indicating the file type
    #  
    @classmethod
    @overloaded
    def setFileTypeAndCreator(cls, filename, type_, creator):
        """ generated source for method setFileTypeAndCreator """
        if not cls.isMac():
            return
        try:
            cls.setFileTypeAndCreator(File(filename), type_, creator)
        except Exception as ex:
            pass
            #  Empty 

    #  Static method: setFileTypeAndCreator(file, type, creator) 
    # 
    #  * Sets the Macintosh file type and creator.  This method is ignored on non-Mac
    #  * platforms.
    #  *
    #  * @param file The <code>File</code> object corresponding to the file
    #  * @param type A four-character string indicating the file type
    #  * @param creator A four-character string indicating the file type
    #  
    @classmethod
    @setFileTypeAndCreator.register(object, File, str, str)
    def setFileTypeAndCreator_0(cls, file_, type_, creator):
        """ generated source for method setFileTypeAndCreator_0 """
        if not cls.isMac():
            return
        try:
            mrjOSTypeClass = Class.forName("com.apple.mrj.MRJOSType")
            mrjFileUtilsClass = Class.forName("com.apple.mrj.MRJFileUtils")
            sig1 = [Class.forName("java.lang.String")]
            constructor = mrjOSTypeClass.getConstructor(sig1)
            sig2 = [Class.forName("java.io.File"), mrjOSTypeClass, mrjOSTypeClass]
            setFileTypeAndCreator = mrjFileUtilsClass.getMethod("setFileTypeAndCreator", sig2)
            args1 = [(type_ + "    ").substring(0, 4)]
            osType = constructor.newInstance(args1)
            args2 = [(creator + "    ").substring(0, 4)]
            creatorType = constructor.newInstance(args2)
            args3 = [file_, osType, creatorType]
            cls.setFileTypeAndCreator.invoke(None, args3)
        except Exception as ex:
            pass
            #  Empty 

    #  Static method: copyFileTypeAndCreator(newFile, oldFile) 
    # 
    #  * Sets the Macintosh file type and creator for the new file using the old file
    #  * as a model.  This method is ignored on non-Mac platforms.
    #  *
    #  * @param oldFile The <code>File</code> object corresponding to the existing file
    #  * @param newFile The <code>File</code> object corresponding to the new file
    #  
    @classmethod
    def copyFileTypeAndCreator(cls, oldFile, newFile):
        """ generated source for method copyFileTypeAndCreator """
        if not cls.isMac():
            return
        try:
            mrjOSTypeClass = Class.forName("com.apple.mrj.MRJOSType")
            mrjFileUtilsClass = Class.forName("com.apple.mrj.MRJFileUtils")
            sig1 = [Class.forName("java.io.File")]
            getFileType = mrjFileUtilsClass.getMethod("getFileType", sig1)
            getFileCreator = mrjFileUtilsClass.getMethod("getFileCreator", sig1)
            sig2 = [Class.forName("java.io.File"), mrjOSTypeClass, mrjOSTypeClass]
            setFileTypeAndCreator = mrjFileUtilsClass.getMethod("setFileTypeAndCreator", sig2)
            args1 = [oldFile]
            osType = getFileType.invoke(None, args1)
            creatorType = getFileCreator.invoke(None, args1)
            args2 = [newFile, osType, creatorType]
            cls.setFileTypeAndCreator.invoke(None, args2)
        except Exception as ex:
            pass
            #  Empty 

    #  Static method: getJTFVersion() 
    # 
    #  * Returns the version number of the JTF libraries as a string
    #  * suitable for use with the <code>compareVersion</code> method.  Note
    #  * that this returns the value of the version of the library that is
    #  * actually loaded.  Making this a constant would mean that the value
    #  * would be the one with which the code was compiled, which is less
    #  * likely to be useful.
    #  *
    #  * @usage String version = getJTFVersion();
    #  * @return The loaded version of the JTF libraries
    #  
    @classmethod
    def getJTFVersion(cls):
        """ generated source for method getJTFVersion """
        return JTF_VERSION

    #  Static method: compareVersion(version) 
    # 
    #  * This method compares the Java version given in the system properties
    #  * with the specified version and returns -1, 0, or +1 depending on whether
    #  * the system version is earlier than, equal to, or later than the specified
    #  * one.  Thus, to test whether the current version of the JDK was at least
    #  * 1.2.1, for example, you could write
    #  *
    #  * <p><pre><code>
    #  * </code></pre>
    #  *
    #  * @param version A string consisting of integers separated by periods
    #  * @return -1, 0, or +1 depending on whether the system version is earlier than,
    #  *         equal to, or later than the specified one
    #  
    @classmethod
    @overloaded
    def compareVersion(cls, version):
        """ generated source for method compareVersion """
        return cls.compareVersion(System.getProperty("java.version"), version)

    #  Static method: compareVersion(v1, v2) 
    # 
    #  * This method compares the version strings <code>v1</code> and <code>v2</code>
    #  * and returns -1, 0, or +1 depending on whether <code>v1</code> is earlier
    #  * than, equal to, or later than <code>v2</code>.
    #  *
    #  * @param v1 A string consisting of integers separated by periods
    #  * @param v2 A second version string in the same format
    #  * @return -1, 0, or +1 depending on whether <code>v1</code> is earlier than,
    #  *         equal to, or later than <code>v2</code>
    #  
    @classmethod
    @compareVersion.register(object, str, str)
    def compareVersion_0(cls, v1, v2):
        """ generated source for method compareVersion_0 """
        t1 = StringTokenizer(v1, ".")
        t2 = StringTokenizer(v2, ".")
        while t1.hasMoreTokens() and t2.hasMoreTokens():
            n1 = Integer.parseInt(t1.nextToken())
            n2 = Integer.parseInt(t2.nextToken())
            if n1 != n2:
                return -1 if (n1 < n2) else +1
        if t1.hasMoreTokens():
            return +1
        if t2.hasMoreTokens():
            return -1
        return 0

    #  Static method: isSwingAvailable() 
    # 
    #  * Checks whether Swing is available.  Unfortunately, some browsers seem to lie
    #  * about the JDK version and return a 1.2 number without actually having Swing.
    #  * This implementation tests the version first, but then confirms the result
    #  * by looking for the <code>JComponent</code> class.  Checking the version first
    #  * means that no <nobr><code>SecurityException</code>s</nobr> will be logged in
    #  * Windows machines, which always log <nobr><code>SecurityException</code>s</nobr>,
    #  * even if the exception is caught.
    #  *
    #  * @return <code>true</code> if Swing is available, <code>false</code> otherwise
    #  
    @classmethod
    def isSwingAvailable(cls):
        """ generated source for method isSwingAvailable """
        if not swingChecked:
            swingChecked = True
            cls.isSwingAvailable = False
            if cls.compareVersion("1.2") >= 0:
                try:
                    cls.isSwingAvailable = Class.forName("javax.swing.JComponent") != None
                except Exception as ex:
                    pass
                    #  Empty 
        return cls.isSwingAvailable

    #  Static method: isSunAudioAvailable() 
    # 
    #  * Checks whether the <code>sun.audio</code> package is available.
    #  *
    #  * @return <code>true</code> if the <code>sun.audio</code> package is available,
    #  *         <code>false</code> otherwise
    #  
    @classmethod
    def isSunAudioAvailable(cls):
        """ generated source for method isSunAudioAvailable """
        if not sunAudioChecked:
            sunAudioChecked = True
            try:
                cls.isSunAudioAvailable = Class.forName("sun.audio.AudioPlayer") != None
            except Exception as ex:
                cls.isSunAudioAvailable = False
        return cls.isSunAudioAvailable

    #  Static method: isJMFAvailable() 
    # 
    #  * Checks whether the Java Media Framework is available.
    #  *
    #  * @return <code>true</code> if the JMF package is available, <code>false</code> otherwise
    #  
    @classmethod
    def isJMFAvailable(cls):
        """ generated source for method isJMFAvailable """
        if not jmfChecked:
            jmfChecked = True
            try:
                cls.isJMFAvailable = Class.forName("javax.media.Player") != None
            except Exception as ex:
                cls.isJMFAvailable = False
        return cls.isJMFAvailable

    #  Static method: areCollectionsAvailable() 
    # 
    #  * Checks whether the JDK 1.2 collection classes are available.  Some browsers
    #  * return a version of the JDK that does not actually match what is supported.
    #  * This method actually checks whether the collection classes are there by
    #  * looking for the <code>ArrayList</code> class.
    #  *
    #  * @return <code>true</code> if collections are available, <code>false</code> otherwise
    #  
    @classmethod
    def areCollectionsAvailable(cls):
        """ generated source for method areCollectionsAvailable """
        if not collectionsChecked:
            collectionsChecked = True
            try:
                cls.areCollectionsAvailable = Class.forName("java.util.ArrayList") != None
            except Exception as ex:
                cls.areCollectionsAvailable = False
        return cls.areCollectionsAvailable

    #  Static method: areStandardFontFamiliesAvailable() 
    # 
    #  * Checks whether the JDK 1.2 standard font families (<code>Serif</code>,
    #  * <code>SansSerif</code>, and <code>Monospaced</code>) are available.
    #  *
    #  * @return <code>true</code> if the standard fonts are available, <code>false</code> otherwise
    #  
    @classmethod
    def areStandardFontFamiliesAvailable(cls):
        """ generated source for method areStandardFontFamiliesAvailable """
        if not fontsChecked:
            fontsChecked = True
            try:
                toolkitClass = Class.forName("java.awt.Toolkit")
                getFontList = toolkitClass.getMethod("getFontList", [None] * 0)
                fonts = str(getFontList.invoke(Toolkit.getDefaultToolkit(), [None] * 0))
                standardFontCount = 0
                i = 0
                while len(fonts):
                    if fonts[i] == "Serif" or fonts[i] == "SansSerif" or fonts[i] == "Monospaced":
                        standardFontCount += 1
                    i += 1
                cls.areStandardFontFamiliesAvailable = (standardFontCount == 3)
            except Exception as ex:
                cls.areStandardFontFamiliesAvailable = False
        return cls.areStandardFontFamiliesAvailable

    JTF_VERSION = "1.99.1"
    platform = -1
    areStandardFontFamiliesAvailable = bool()
    fontsChecked = bool()
    isSwingAvailable = bool()
    swingChecked = bool()
    areCollectionsAvailable = bool()
    collectionsChecked = bool()
    isSunAudioAvailable = bool()
    sunAudioChecked = bool()
    isJMFAvailable = bool()
    jmfChecked = bool()

Platform.#  * @usage int platform = Platform.getPlatform();

Platform.#  * @usage if (Platform.isMac()) . . .

Platform.#  * @usage if (Platform.isWindows()) . . .

Platform.#  * @usage if (Platform.isUnix()) . . .

Platform.#  * @usage Platform.setFileTypeAndCreator(filename, type, creator);

Platform.#  * @usage Platform.setFileTypeAndCreator(file, type, creator);

Platform.#  * @usage Platform.copyFileTypeAndCreator(oldFile, newFile);

Platform.#  * &nbsp;    if (Platform.compareVersion("1.2.1") &gt;= 0) . . .

Platform.#  * @usage int cmp = Platform.compareVersion(version);

Platform.#  * @usage int cmp = Platform.compareVersion(v1, v2);

Platform.#  * @usage if (Platform.isSwingAvailable()) . . .

Platform.#  * @usage if (Platform.isSunAudioAvailable()) . . .

Platform.#  * @usage if (Platform.isJMFAvailable()) . . .

Platform.#  * @usage if (Platform.areCollectionsAvailable()) . . .

Platform.#  * @usage if (Platform.areStandardFontFamiliesAvailable()) . . .

