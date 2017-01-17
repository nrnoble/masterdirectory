from Library import GRCGraphics as GRC
from Library import nrnoble as Util


import random

windowWidth = 300
windowHeight = 300
interval = .1
Color = random.choice(Util.Colors)
gWindow = GRC.GraphicsWindow("Clock", windowWidth, windowHeight)

def main():

    line1 = GRC.Line(GRC.Point( 10, 10), GRC.Point(20, 10))
    gWindow.addItem(line1)
    gWindow.redraw()
    Util.sleep(5)
    line1.move(20,20)

    gWindow.redraw()



    Util.pause(gWindow)




def fifteenSeconds(centerPoint, radius):


    xx = centerPoint.getX()
    yy = centerPoint.getY()

    for tick in range(1, 16, 1):

        # line.move(GRC.Point(150,150),GRC.Point(10,1))
        #gWindow.items.remove(line)
        #gWindow.redraw()
        lineEndPoint = GRC.Point(radius + (tick * 10), tick * 10)
        line = GRC.Line(centerPoint, lineEndPoint)
        GRC.time.sleep(interval)
        gWindow.addItem(line)
        gWindow.redraw()




main()