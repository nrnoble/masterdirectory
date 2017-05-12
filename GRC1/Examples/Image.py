import random, os, sys, inspect, pickle
sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
import nrnoble as Util
from Library import GRCGraphics as GRC

windowWidth = 502
windowHeight = 268
interval = .1
Color = random.choice(Util.Colors)
gWindow1 = GRC.GraphicsWindow("Image Window-1", windowWidth, windowHeight)
gWindow2 = GRC.GraphicsWindow("Image Window-2", windowWidth, windowHeight)

background1 = GRC.Image(GRC.Point(251, 134), "..\\Content\\bwdock.png")
background2 = GRC.Image(GRC.Point(251, 134), "..\\Content\\blackbackground.png")

def main():

    background1.draw(gWindow1)
    background2.draw(gWindow2)
    gWindow1.redraw()
    gWindow2.redraw()



    for y in range(0,windowHeight -  5):
        for x in range (0,windowWidth - 5):
            red, green, blue = background1.getPixel(x,y)
            rgb = color_rgb(red, green, blue)
            background2.setPixel(x, y, rgb)

        gWindow2.update()




def color_rgb(r, g, b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color"""
    return "#%02x%02x%02x" % (r, g, b)


main()

Util.pause(gWindow2)
