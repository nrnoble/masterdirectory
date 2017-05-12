import random

from Library import GRCGraphics as GRC
from Library.Examples import nrnoble as Util

windowWidth = 300
windowHeight = 300
interval = 1
Color = random.choice(Util.Colors)
gWindow = GRC.GraphicsWindow("Text Demo", windowWidth, windowHeight)

def main():


    TextScroll()

def TextScroll():

    scrollText = GRC.Text(GRC.Point(500, 290), "Scroll Demo.... ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    scrollText.setTextColor("Blue")
    scrollText.setFontSize(12)
    gWindow.addItem(scrollText)
    gWindow.update()

    for moveX in range(1,700,1):
        scrollText.move(-1,0)
        gWindow.update()
        GRC.time.sleep(.01)

    Util.pause(gWindow)


main()
