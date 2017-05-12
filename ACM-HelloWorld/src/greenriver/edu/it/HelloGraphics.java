package greenriver.edu.it;

//public class HelloGraphics
//{
//
//    public static void main1(String[] args) {
//	    System.out.println("Starting Applications22");
//    }
//}

/*
 * File: HelloGraphics.java
 * ------------------------
 * This program displays the message "hello, world" and is inspired
 * by the first program "The C Programming Language" by Brian
 * Kernighan and Dennis Ritchie.  This version displays the message
 * graphically.
 */

import greenriver.edu.it.graphics.*;
import greenriver.edu.it.program.*;

public class HelloGraphics extends GraphicsProgram {

    public void run() {
        GLabel label = new GLabel("hello, world2");
        label.setFont("SansSerif-100");
        double x = (getWidth() - label.getWidth()) / 2;
        double y = (getHeight() + label.getAscent()) /2;
        add(label, x, y);
    }
}
