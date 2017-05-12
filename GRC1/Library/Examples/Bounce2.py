import random, os, sys, inspect
sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
from Library import GRCGraphics as GRC

Colors =['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Pink', 'Purple', 'Gold', 'Silver', 'Gray', 'Maroon']
background1 = GRC.Image(GRC.Point(251, 134), "E:\\Data\\Github\\GRC1\\Content\\icecave.png")
reverseX = 1
reverseY = 1
x = 1
y = 1
heightmargin = 5
widethMargin = 5

reverse = 1


def main():

    wallBounce()


def wallBounce():
    windowWidth = 500
    windowHeight = 268

    Color = random.choice(Colors)
    gWindow = GRC.GraphicsWindow("Bounce", windowWidth, windowHeight)
    background1.draw(gWindow)
    p1 = 110
    p2 = 21
    size = 5
    margin = 15
    Ball = GRC.Circle(GRC.Point(p1, p2), size)

    Ball.setFillColor(Color)
    Ball.setBoarderColor("White")
    gWindow.addItem(Ball)
    gWindow.redraw()
    gWindow.update()
    GRC.time.sleep(1)
   # pause(gWindow)


    doBounce(gWindow, Ball, windowHeight, margin, windowWidth, size, Color)


def doBounce(gWindow, Ball, windowHeight, margin, windowWidth, size, Color):

    loopStatus = True
    while (loopStatus):
        global reverse
        global x
        global y
        Ball.move(x, y)
        GRC.time.sleep(.02)
        xx = int(Ball.getCenter().x)
        yy = int(Ball.getCenter().y)
        # print("xx=", xx,"yy=", yy, "x=",x, "y=",y)


        if any ([xx < Ball.radius, xx > windowWidth - Ball.radius]):
            #x=-x
            Color = getNewColor(Color)
            Ball.setFillColor(Color)
            Ball.setBoarderColor("White")
            calcBounceXAngle()
            Ball.move(4 - (x * reverseX), y)
            #Ball.moveTo()

        if any([yy < Ball.radius , yy > windowHeight - Ball.radius]):
            #y=-y
            Color = getNewColor(Color)
            Ball.setFillColor("White")
            Ball.setBoarderColor(Color)
            calcBounceYAngle()
            Ball.move(x, 4 + (y * reverseY))

        key = gWindow.checkForKeyPress()
        #print(key)
        if key == 'Escape':
            #gWindow.waitForKeyPress()
            gWindow.close()  # Close window when done


def calcBounceAngle():
    global reverse
    global x
    global y
    reverse = reverse * -1
    x = random.choice([1, 2, 3])
    y = random.choice([1, 2, 3])
    x = x * reverse
    y = y * reverse

def calcBounceXAngle():
    global reverseX
    global x
    reverseX = reverseX * -1
    x1 = x
    while (x1==x):
        x = random.choice([1, 2, 3,4])
    x = x * reverseX

def calcBounceYAngle():
    global reverseY
    global y
    reverseY = reverseY * -1
    y1 = y
    while (y1==y):
        y = random.choice([1, 2, 3,4])
    y = y * reverseY


def pause(win):
    win.redraw()
    win.waitForClick()
    win.waitForKeyPress()


def getNewColor(Color):
    newColor = Color
    while(Color == newColor):
        newColor = random.choice(Colors)
    return newColor


main()
