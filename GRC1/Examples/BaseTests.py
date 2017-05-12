import random, os, sys, inspect
sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
from Library import GRCGraphics as GRC

interval = .5
win = GRC.GraphicsWindow("My Circle", 500, 500)

def main():

    p1 = 250
    p2 = 250
    size = 10
    
    c1 = GRC.Circle(GRC.Point(p1, p2), size)
    c2 = GRC.Circle(GRC.Point(p1, p2), size)
    c3 = GRC.Circle(GRC.Point(p1, p2), size)
    c4 = GRC.Circle(GRC.Point(p1, p2), size)


    c1.setFillColor("BLACK")
    c2.setFillColor("RED")
    c3.setFillColor("GREEN")
    c4.setFillColor("White")

    win.addItem(c1)
    win.addItem(c2)
    win.addItem(c3)
    win.addItem(c4)
    win.redraw()
    #pause(win)

    # win.redraw()
    # win.getMouse()

    c4.setFillColor("blue")
    for i in range(1,22):
        c1.move(-i,-i)
        c2.move(-i,i)
        c3.move(i,-i)
        c4.move(i,i)

        win.redraw()
        #win.getMouse()
        GRC.time.sleep(.05)

    myP1 = c1.getCenter()
    myP2 = c2.getCenter()
    myP3 = c3.getCenter()
    myP4 = c4.getCenter()

    drawLine (myP1, myP2)
    drawLine (myP2, myP4)
    drawLine (myP4, myP3)
    drawLine (myP3, myP1)
    drawLine (myP3, myP2)
    drawLine (myP4, myP1)
    
    # myLine1 = GRC.Line (myP1,myP2)
    # win.addItem(myLine1)
    # GRC.time.sleep(interval)
    # win.redraw()
    # print("myLine1")
    
    #myLine2 = GRC.Line(myP2, myP4)
    #win.addItem(myLine2)
    #GRC.time.sleep(interval)
    #win.redraw()
    #print("myLine2")


    # myLine3 = GRC.Line(myP4, myP3)
    # win.addItem(myLine3)
    # GRC.time.sleep(interval)
    # win.redraw()
    # print("myLine3")


    # myLine4 = GRC.Line(myP3, myP1)
    # win.addItem(myLine4)
    # GRC.time.sleep(interval)
    # win.redraw()
    # print("myLine4")


    # myLine5 = GRC.Line(myP3, myP2)
    # win.addItem(myLine5)
    # GRC.time.sleep(interval)
    # win.redraw()
    # print("myLine5")

    # myLine6 = GRC.Line(myP4, myP1)
    # win.addItem(myLine6)
    # GRC.time.sleep(interval)
    # win.redraw()
    # print("myLine6")


    #c.draw(win)
    #c1.draw(win)
    #c2.draw(win)

    win.waitForClick()

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

def drawLine (startPoint, endPoint):
    myLine = GRC.Line(startPoint, endPoint)
    win.addItem(myLine)
    GRC.time.sleep(interval)
    win.redraw()
    print(startPoint,endPoint)
    


def pause(win):
    win.redraw()
    win.waitForClick()


main()
