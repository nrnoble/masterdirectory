import random, os, sys, inspect, pickle
sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
import nrnoble as Util
from Library import GRCGraphics as GRC

windowWidth = 300
windowHeight = 25
interval = 1
Color = random.choice(GRC.COLORS)
gWindow = GRC.GraphicsWindow("Text Demo", windowWidth, windowHeight)

def main():

    TextScroll()

def TextScroll():

    scrollText = GRC.Text(GRC.Point(500, 15), "Scroll Demo.... ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    scrollText.setTextColor("Blue")
    scrollText.setFontSize(12)
    gWindow.addItem(scrollText)
    gWindow.update()

    for moveX in range(1,700,1):
        scrollText.move(-1,0)
        gWindow.redraw()
        GRC.time.sleep(.01)

    Util.pause(gWindow)


main()
