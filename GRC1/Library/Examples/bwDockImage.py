import inspect
import os
import pickle
import random
import sys

#sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

from Library.Examples import nrnoble as Util
from Library import GRCGraphics as GRC

windowWidth = 502
windowHeight = 268
interval = .1
Color = random.choice(Util.Colors)
gWindow1 = GRC.GraphicsWindow("Image Window-1", windowWidth, windowHeight)
#gWindow2 = GRC.GraphicsWindow("Image Window-2", windowWidth, windowHeight)

# background1 = GRC.Image(GRC.Point(251, 134), "E:\\Data\\Github\\GRC1\\Content\\bwdock.png")
# background2 = GRC.Image(GRC.Point(251, 134), ".\\Content\\blackbackground.png")
background2 = GRC.Image(GRC.Point(251, 134), ".\\Content\\randomPixelsbackground3.png")

def main():

    # background1.draw(gWindow1)
    background2.draw(gWindow1)
    # gWindow1.redraw()
    # gWindow2.redraw()
    pixels = []

    # for y in range(0,windowHeight -  3):
    #     for x in range (0,windowWidth):
    #         red, green, blue = background1.getPixel(x,y)
    #         rgb = color_rgb(red, green, blue)
    #         onePixel = pixel(x,y,rgb)
    #         pixels.append(onePixel)
    #         # print(onePixel.x,onePixel.y,onePixel.rgb)
    #         # Util.pause(gWindow2)
    #         # background2.setPixel(x, y, rgb)
    #         # print (y)


    # The first argument is a string containing the filename. The second argument is another string containing a few
    # characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w'
    # for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any
    # data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The

    # On Windows, 'b' appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and
    # 'r+b'. Python on Windows makes a distinction between text and binary files; the end-of-line characters in text
    # files are automatically altered slightly when data is read or written. This behind-the-scenes modification to
    # file data is fine for ASCII text files, but it’ll corrupt binary data like that in JPEG or EXE files. Be very
    # careful to use binary mode when reading and writing such files. On Unix, it doesn’t hurt to append a 'b' to the
    # mode, so you can use it platform-independently for all binary files.

    file = open('.\\Content\\bwDockImage.json', 'rb+')
    #json.dump(pixels, file)
    #pickle.dump(pixels, file)
    pixels2 = pickle.load(file)

    #pixels2 = json.dump(file)

    file.close()

    random.shuffle(pixels2)

    while len(pixels2) > 0:
        pix = pixels2.pop()
        background2.setPixel(pix.x, pix.y, pix.rgb)
        gWindow1.update()
    Util.pause(gWindow1)

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

Util.pause(gWindow1)