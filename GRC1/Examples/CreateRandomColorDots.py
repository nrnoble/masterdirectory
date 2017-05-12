import random, os, sys, inspect
sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

import nrnoble as Util
from Library import GRCGraphics as GRC

windowWidth = 502
windowHeight = 268
interval = .1
Color = random.choice(Util.Colors)
gWindow1 = GRC.GraphicsWindow("Image Window-1", windowWidth, windowHeight)
gWindow2 = GRC.GraphicsWindow("Image Window-2", windowWidth, windowHeight)

# background1 = GRC.Image(GRC.Point(251, 134), "E:\\Data\\Github\\GRC1\\Content\\bwdock.png")
# background1 = GRC.Image(GRC.Point(251, 134), "E:\\Data\\Github\\GRC1\\Content\\icecave.png")
background2 = GRC.Image(GRC.Point(251, 134), "..\\Content\\blackbackground.png")

def main():

    filepath = '.\\Content\\randomColors.pkle'
    background2.draw(gWindow2)

    pixels = []

    for y in range(0,windowHeight - 3):
        for x in range (0,windowWidth):
            # red, green, blue = background1.getPixel(x,y)
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)

            rgb = color_rgb(red, green, blue)
            onePixel = pixel(x,y,rgb)
            pixels.append(onePixel)
            # print(onePixel.x,onePixel.y,onePixel.rgb)

            
            background2.setPixel(x, y, rgb)
            gWindow2.update()
            
            # print (y)
    print("pausing")
    Util.pause(gWindow2)
    print("saving")
    background2.save(".\\Content\\randomPixelsbackground3.png")

    # The first argument is a string containing the filename. The second argument is another string containing a few
    # characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w'
    # for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any
    # data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The
    # mode argument is optional; 'r' will be assumed if it’s omitted.

    # On Windows, 'b' appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and
    # 'r+b'. Python on Windows makes a distinction between text and binary files; the end-of-line characters in text
    # files are automatically altered slightly when data is read or written. This behind-the-scenes modification to
    # file data is fine for ASCII text files, but it’ll corrupt binary data like that in JPEG or EXE files. Be very
    # careful to use binary mode when reading and writing such files. On Unix, it doesn’t hurt to append a 'b' to the
    # mode, so you can use it platform-independently for all binary files.


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


