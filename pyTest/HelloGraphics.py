#!/usr/bin/env python
""" generated source for module HelloGraphics """
from __future__ import print_function
#
#  * File: HelloGraphics.java
#  * ------------------------
#  * This program displays the message "hello, world" and is inspired
#  * by the first program "The C Programming Language" by Brian
#  * Kernighan and Dennis Ritchie.  This version displays the message
#  * graphically.
#
class HelloGraphics(GraphicsProgram):
    """ generated source for class HelloGraphics """
    def run(self):
        """ generated source for method run """
        label = GLabel("hello, world2")
        label.setFont("SansSerif-100")
        x = (getWidth() - label.getWidth()) / 2
        y = (getHeight() + label.getAscent()) / 2
        add(label, x, y)

# Original Java code.

# /*
#  * File: HelloGraphics.java
#  * ------------------------
#  * This program displays the message "hello, world" and is inspired
#  * by the first program "The C Programming Language" by Brian
#  * Kernighan and Dennis Ritchie.  This version displays the message
#  * graphically.
#  */
#
# import acm.graphics.*;
# import acm.program.*;
#
# public class HelloGraphics extends GraphicsProgram {
#
# 	public void run() {
# 		GLabel label = new GLabel("hello, world2");
# 		label.setFont("SansSerif-100");
# 		double x = (getWidth() - label.getWidth()) / 2;
# 		double y = (getHeight() + label.getAscent()) / 2;
# 		add(label, x, y);
# 	}
#
#
# }
