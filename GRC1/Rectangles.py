from Library import GRCGraphics as GRC

import random

Colors =['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Pink', 'Purple', 'Gold', 'Silver', 'Gray', 'Maroon']

def main(Colors):

    windowWidth = 300
    windowHeight = 300

    Color = random.choice(Colors)
    gWindow = GRC.GraphicsWindow("Rectangles", windowWidth, windowHeight)

    rect = GRC.Rectangle(GRC.Point (10,10), GRC.Point(10,20))
    gWindow.addItem(rect)
    gWindow.redraw()
    gWindow.waitForKeyPress()

