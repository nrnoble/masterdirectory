#!/usr/bin/env python
""" generated source for module Program_Test """
from __future__ import print_function
# package: greenriver.edu.acm.program
# 
#  * Created by Neal on 1/1/2017.
#  
class Program_Test(JApplet, IOModel, Runnable, MouseListener, MouseMotionListener, KeyListener, ActionListener):
    """ generated source for class Program_Test """
    #  Private constants 
    DEFAULT_X = 16
    DEFAULT_Y = 40
    DEFAULT_WIDTH = 754
    DEFAULT_HEIGHT = 492
    PRINT_MARGIN = 36

    #  Private instance variables 
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

    def getMyCaller(self):
        """ generated source for method getMyCaller """
        stack = Throwable().getStackTrace()
        return stack[2].getClassName() + "." + stack[2].getMethodName()

    def getWidth(self):
        """ generated source for method getWidth """
        caller = self.getMyCaller()
        if caller.startsWith("java.") or caller.startsWith("javax."):
            return super(Program_Test, self).getWidth()
        else:
            return getCentralRegionSize().width

    def getHeight(self):
        """ generated source for method getHeight """
        caller = self.getMyCaller()
        if caller.startsWith("java.") or caller.startsWith("javax."):
            return super(Program_Test, self).getHeight()
        else:
            return getCentralRegionSize().height

    def getCentralRegionSize(self):
        """ generated source for method getCentralRegionSize """
        if self.centerPanel == None:
            return super(Program_Test, self).getSize()
        if self.initFinished:
            return self.centerPanel.getSize()
        size = super(Program_Test, self).getSize() if (self.programFrame == None) else self.programFrame.getSize()
        insets = super(Program_Test, self).getInsets() if (self.programFrame == None) else self.programFrame.getInsets()
        size.width -= self.westPanel.getPreferredSize().width + self.eastPanel.getPreferredSize().width
        size.width -= insets.left + insets.right
        size.height -= self.northPanel.getPreferredSize().height + self.southPanel.getPreferredSize().height
        size.height -= insets.top + insets.bottom
        return size

