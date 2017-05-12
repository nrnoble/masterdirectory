from Library import GRCGraphics as GRC

# define size of graphics window
windowWidth = 300
windowHeight = 300

# Define the graphics window object
gWindow = GRC.GraphicsWindow("Title of window: Box", windowWidth, windowHeight)


def main():

     #drawPolygonBox()
     drawRectanglBox()


def drawPolygonBox():


    # set boarder Color of box object
    boarderColor = "Black"

    # set boarder Color of box object
    fillColor = "Yellow"

    # define a polygon object as a box
    box = GRC.Polygon(GRC.Point(10, 10), GRC.Point(25, 10), GRC.Point(25, 25), GRC.Point(10, 25))
    box.setBoarderColor(boarderColor)
    box.setFillColor(fillColor)
    p1 = GRC.Point(10,10)
    p2 = GRC.Point(20,20)

    mybox = GRC.BBox(p1,p2)
    mybox.draw(gWindow)

    # Pass graphic window object to the box object; call draw method.
    box.draw(gWindow)
    box.move(100,100)
    gWindow.waitForClick()
    # p1 = box.getCenter
    box.move(-90, -90)
    points = box.getPoints()

    # click on window to close\exit
    gWindow.waitForClick()


def drawRectanglBox():


    # set boarder Color of box object
    boarderColor = "Black"

    # set boarder Color of box object
    fillColor = "Yellow"

    # define a polygon object as a box
    box = GRC.Rectangle(GRC.Point(0, 0), GRC.Point(25, 25))
    box.setBoarderColor(boarderColor)
    box.setFillColor(fillColor)
    p1 = GRC.Point(10,10)
    p2 = GRC.Point(20,20)

    #mybox = GRC.BBox(p1,p2)
    #mybox.draw(gWindow)

    # Pass graphic window object to the box object; call draw method.
    box.draw(gWindow)
    box.jumpTo(GRC.Point(270,0))
    gWindow.waitForClick()


    status = True
    while status:
        mp = gWindow.checkForClick()
        if mp != None:
            box.jumpTo(mp)
            #print (mp)





    box.move(0, 50)
    #xx = box.getCenter().x
    #yy = box.getCenter().y
    p1 = box.p1
    p2 = box.p2

    xx = box.p1.x
    yy = box.p1.y

    #print (xx,yy,p1,p2)
    gWindow.waitForClick()

    #box.p2 = GRC.Point(p2.x+10,p2.y+10)
    print (box.p1.x, box.p1.y, box.p1, box.p2)

    box.jumpTo(GRC.Point(0,100))

    # click on window to close\exit
    gWindow.waitForClick()




# call main function

main()


