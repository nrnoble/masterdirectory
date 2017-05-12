import random, os, sys, inspect
sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
from Library import GRCGraphics as GRC

Colors =['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Pink', 'Purple', 'Gold', 'Gray', 'Maroon']

x = 0
y = 0
reverse = 1


def main():

    wallBounce()


def wallBounce():

    windowWidth = 300
    windowHeight = 300

    Color = random.choice(Colors)
    gWindow = GRC.GraphicsWindow("Move Ball", windowWidth, windowHeight)
    p1 = 10
    p2 = 10
    size = 10
    margin = 2
    Ball = GRC.Circle(GRC.Point(p1, p2), size)
    Ball.setFillColor(Color)
    Ball.setBoarderColor(Color)
    gWindow.addItem(Ball)
    gWindow.redraw()
    gWindow.update()
    GRC.time.sleep(1)
   #pause(gWindow)


    doBounce(gWindow, Ball, windowHeight, margin, windowWidth, size, Color)


def doBounce(gWindow, Ball, windowHeight, margin, windowWidth, size, Color):

    loopStatus = True
    Speed = 3
    while (loopStatus):
        global reverse
        global x
        global y
        #Ball.move(x, y)
        GRC.time.sleep(.02)
        xx = int(Ball.getCenter().x)
        yy = int(Ball.getCenter().y)

        # if (xx == (windowHeight - size - 2) or yy == (width - size - 2) or ((xx <= 2) or (yy <= 2))):
        #if any([xx >= (windowHeight - size - margin), yy >= (windowWidth - size - margin), xx <= margin, yy <= margin]):
        #   Color = getNewColor(Color)
        #   Ball.setFillColor(Color)
        #   Ball.setBoarderColor(Color)
        #   calcBounceAngle()

        key = gWindow.checkForKeyPress()
        #print(key)

        if key == 'Escape':
            #gWindow.waitForKeyPress()
            gWindow.close()  # Close window when done
            sys.exit(0)

        if key == "Left":
            if (windowWidth -(size/2) < Ball.getCenter().getX()):
                print ("X=", Ball.getCenter().getX())
                Ball.move(-(Speed), 0)

        if key == "Right":
            if (windowWidth -(size/2) > Ball.getCenter().getX()):
                print ("X=", Ball.getCenter().getX())
                Ball.move(Speed, 0)

        if key == "Down":
            Ball.move(0, Speed)

        if key == "Up":
            Ball.move(0, -(Speed))


def calcBounceAngle():
    global reverse
    global x
    global y
    reverse = reverse * -1
    x = random.choice([1, 2, 3, 4])
    y = random.choice([1, 2, 3, 4])
    x = x * reverse
    y = y * reverse



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