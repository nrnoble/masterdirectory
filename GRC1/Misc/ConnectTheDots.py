import random

from Library import GRCGraphics as GRC
from Library.Examples import nrnoble as Util

windowWidth = 300
windowHeight = 300
interval = .1
Color = random.choice(Util.Colors2)
gWindow = GRC.GraphicsWindow("Connect The Dots", windowWidth, windowHeight)
gWindow.setBackground("black")
pixels = []

def main():
    for i in range (0,50):
        x = random.randint(5, windowWidth - 5)
        y = random.randint(5, windowHeight - 5)
        rgb = color_rgb(255,255,0)
        pix = pixel (x,y,rgb)
        pixels.append(pix)
        gWindow.plotPixel(x,y,"Red")

    Util.sleep(1)
    pix1 = pixels.pop()
    pix2 = pixels.pop()
    line = GRC.Line(GRC.Point(pix1.x, pix1.y), GRC.Point(pix2.x, pix2.y))
    rndColor = random.choice(Util.Colors2)
    line.setFillColor(rndColor)
    gWindow.addItem(line)
    gWindow.redraw()
    gWindow.update()
    Util.sleep(interval)
    #print("paused")
    #Util.pause(gWindow)

    while len(pixels) > 0:
        pix1 = pix2
        pix2 = pixels.pop()
        line = GRC.Line(GRC.Point(pix1.x, pix1.y), GRC.Point(pix2.x, pix2.y))
        rndColor = random.choice(Util.Colors2)
        line.setFillColor(rndColor)
        gWindow.addItem(line)
        gWindow.redraw()
        gWindow.update()
        Util.sleep(interval)
        #print("Drawing to point " + str(pix2.x) + "," + str(pix2.y))
        #Util.pause(gWindow)

class pixel(object):
    def __init__(self, px, py, prgb):
        self.x = px
        self.y = py
        self.rgb = prgb




def color_rgb(r, g, b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color"""
    return "#%02x%02x%02x" % (r, g, b)
main()

print("paused")
Util.pause(gWindow)
print("Good bye!")
