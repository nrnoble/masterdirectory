from Library import GRCGraphics as GRC
from Library import nrnoble as Util


import random

windowWidth = 300
windowHeight = 300
interval = .1
Color = random.choice(Util.Colors)
gWindow = GRC.GraphicsWindow("Text Demo", windowWidth, windowHeight)

def main():

    #TextResizeDemo()
    TextScroll()

def TextResizeDemo():

    # gWindow.setCoords(0, 0, 300, 300)
    demoText = GRC.Text(GRC.Point(150, 10), "Text Demo")
    text = GRC.Text(GRC.Point(150, 100), "Centered Text")
    text.setTextColor("Blue")
    text.setFontSize(5)
    gWindow.addItem(demoText)
    gWindow.addItem(text)

    fontColor = "blue"
    while (True):

        fontColor = Util.getNewColor(fontColor)

        for fontSize in range(5,25,2):
            text.setFontSize(fontSize)
            text.setTextColor(fontColor)
            gWindow.redraw()
            GRC.time.sleep(interval)

        for fontSize2 in range(25,5,-2):
            text.setFontSize(fontSize2)
            gWindow.redraw()
            GRC.time.sleep(interval)

def TextScroll():

    scrollText = GRC.Text(GRC.Point(434, 290), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    scrollText.setTextColor("Blue")
    scrollText.setFontSize(12)
    gWindow.addItem(scrollText)
    gWindow.redraw()

    for moveX in range(1,575,1):
        scrollText.move(-1,0)
        gWindow.redraw()
        GRC.time.sleep(.01)

    Util.pause(gWindow)


main()
