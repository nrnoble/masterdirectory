import random, os, sys, inspect, pickle
sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
from Library import GRCGraphics as GRC


Colors =['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Pink', 'Purple', 'Gold', 'Silver', 'Gray', 'Maroon']

def main():
    windowWidth = 300
    windowHeight = 300

    Color = random.choice(Colors)
    gWindow = GRC.GraphicsWindow("Polygon", windowWidth, windowHeight)
    gWindow2 = GRC.GraphicsWindow("Polygon2", windowWidth, windowHeight)

    gWindow2.setCoords(0, 0, 10, 10)
    gWindow.setCoords(0, 0, 10, 10)
    t = GRC.Text(GRC.Point(5, 5), "Centered Text")
    t.draw(gWindow2)
    p = GRC.Polygon(GRC.Point(1, 1), GRC.Point(5, 3), GRC.Point(2, 7))
    p.draw(gWindow)
    pause(gWindow)

def pause(win):
    win.redraw()
    win.waitForClick()


main()
