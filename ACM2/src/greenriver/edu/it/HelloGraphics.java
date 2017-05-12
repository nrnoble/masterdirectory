package greenriver.edu.it;


import acm.graphics.*;
import acm.program.*;

public class HelloGraphics extends GraphicsProgram {

    public void run() {
        GLabel label = new GLabel("hello, world2");
        label.setFont("SansSerif-100");
        double x = (getWidth() - label.getWidth()) / 2;
        double y = (getHeight() + label.getAscent()) / 2;
        add(label, x, y);
    }
}
