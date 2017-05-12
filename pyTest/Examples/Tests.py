from graphics import *
import time

def main():
    win = GraphicsWindow("My Circle", 500, 500)
    p1 = 250
    p2 = 250
    size = 10
    c1 = Circle(Point(p1, p2), size)
    c2 = Circle(Point(p1, p2), size)
    c3 = Circle(Point(p1, p2), size)
    c4 = Circle(Point(p1, p2), size)

    c1.setFill("BLACK")
    c2.setFill("RED")
    c3.setFill("GREEN")
    c4.setFill("White")

    win.addItem(c1)
    win.addItem(c2)
    win.addItem(c3)
    win.addItem(c4)
    win.redraw()
    pause(win)

    # win.redraw()
    # win.getMouse()

    c4.setFill("blue")
    for i in range(1,22):
        c1.move(-i,-i)
        c2.move(-i,i)
        c3.move(i,-i)
        c4.move(i,i)

        win.redraw()
        #win.getMouse()
        time.sleep(.05)

    myP1 = c1.getCenter()
    myP2 = c2.getCenter()

    myLine = Line (myP1,myP2)
    win.addItem(myLine)
    win.redraw()
    myP1 = c2.getCenter()
    myP2 = c4.getCenter()
    myLine2 = Line(myP1, myP2)
    win.addItem(myLine2)
    win.redraw()
    print("drawline")

    #c.draw(win)
    #c1.draw(win)
    #c2.draw(win)

    win.getMouse()

    c2.move(150,50)
    pause(win)

    c2.move(1,1)
    pause(win)

    c2.move(150,70)
    pause(win)

    c2.move(150,80)
    pause(win)

    c2.radius = 30
    pause(win)
    win.close()    # Close window when done


def pause(win):
    win.redraw()
    win.getMouse()


main()