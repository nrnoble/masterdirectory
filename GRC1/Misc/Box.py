import random

from Library import GRCGraphics as GRC
from Library.Examples import nrnoble as Util

Colors =['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Pink', 'Purple', 'Gold', 'Silver', 'Gray', 'Maroon']

def main():
    windowWidth = 300
    windowHeight = 300

    Color = random.choice(Colors)
    gWindow = GRC.GraphicsWindow("Box", windowWidth, windowHeight)
    interval = .25
    #gWindow.setCoords(0, 0, 100, 100)
    # text = GRC.Text(GRC.Point(150, 50), "Centered Text")
    # text.setTextColor("Blue")
    # text.setSize(5)
    # gWindow.addItem(text)
    # for fontSize in range(5,25):
    #     text.setSize(fontSize)
    #     gWindow.redraw()
    #     GRC.time.sleep(interval)
    #
    # for fontSize in range(25, 8):
    #     text.setSize(fontSize)
    #     gWindow.redraw()
    #     GRC.time.sleep(interval)

    polygon1 = GRC.Polygon(GRC.Point(10, 10), GRC.Point(125, 10), GRC.Point(125,125), GRC.Point(10,125))
    polygon1.draw(gWindow)
    Util.pause(gWindow)




main()
