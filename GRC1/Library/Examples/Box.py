import random, os, sys, inspect
#sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
from Library import GRCGraphics as GRC

def main():

    # define size of graphics windows
    windowWidth = 300
    windowHeight = 300


    # Define the graphics window.
    gWindow = GRC.GraphicsWindow("Title of window: Box", windowWidth, windowHeight)

    # set boarder Color of box
    Color = "Black"

    #define a polygon as a box
    polygon = GRC.Polygon(GRC.Point(10, 10), GRC.Point(125, 10), GRC.Point(125,125), GRC.Point(10,125))

    #display box object on graphics windows
    polygon.draw(gWindow)

    #click to close window
    gWindow.waitForClick()


# call main function
main()
