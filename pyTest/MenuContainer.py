#!/usr/bin/env python
""" generated source for module MENUCO~1 """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
# 
#  * Copyright (c) 1995, 2004, Oracle and/or its affiliates. All rights reserved.
#  * ORACLE PROPRIETARY/CONFIDENTIAL. Use is subject to license terms.
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  *
#  
# package: java.awt
# 
#  * The super class of all menu related containers.
#  *
#  * @author      Arthur van Hoff
#  
class MenuContainer(object):
    """ generated source for interface MenuContainer """
    __metaclass__ = ABCMeta
    @abstractmethod
    def getFont(self):
        """ generated source for method getFont """

    @abstractmethod
    def remove(self, comp):
        """ generated source for method remove """

    # 
    #      * @deprecated As of JDK version 1.1
    #      * replaced by dispatchEvent(AWTEvent).
    #      
    @abstractmethod
    def postEvent(self, evt):
        """ generated source for method postEvent """

