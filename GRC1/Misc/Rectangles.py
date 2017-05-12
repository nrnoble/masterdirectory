from Library import GRCGraphics as GRC

import random

Colors =['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Pink', 'Purple', 'Gold', 'Silver', 'Gray', 'Maroon']

def main(Colors):

    windowWidth = 300
    windowHeight = 300

    padding = 3

    Color = random.choice(Colors)
    gWindow = GRC.GraphicsWindow("Rectangles", windowWidth, windowHeight)

    sq = []
    rect = GRC.Rectangle(GRC.Point (10,10), GRC.Point(290,290))
    rect1 = GRC.Rectangle(GRC.Point (20,20), GRC.Point(280,280))
    for i in range (1,30):
        #rect = GRC.Rectangle(GRC.Point(padding * i, padding * i), GRC.Point(windowWidth - (padding * i),  + windowHeight - (padding * i)))
        gWindow.addItem(GRC.Rectangle(GRC.Point(padding * i, padding * i), GRC.Point(windowWidth - (padding * i),  + windowHeight - (padding * i))))
        gWindow.autoflush
        gWindow.update()

    gWindow.redraw()
    gWindow.waitForKeyPress()


main(Colors)