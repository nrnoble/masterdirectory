from Library import GRCGraphics as GRC
from Library import nrnoble as Util


import random

windowWidth = 300
windowHeight = 300
interval = 1
Color = random.choice(Util.Colors)
gWindow = GRC.GraphicsWindow("Clock", windowWidth, windowHeight)
#lineStartPoint = []
#points = []

def main():

    circlePoints = pointsOnCircle(150,150,100)

    # angle = 0
    # for point in circlePoints:
    #     print ("Angle%: ",angle, point)
    #     angle += 1


    lineStartPoint = GRC.Point(150, 150)

    for tick in range (0,360,6):

        lineEndPoint = circlePoints[tick]
        line = GRC.Line(lineStartPoint, lineEndPoint)
        GRC.time.sleep(interval)
        gWindow.addItem(line)
        gWindow.redraw()






    #seconds(center, 150)

    # for tick in range (1,16):
    #     # line.move(GRC.Point(150,150),GRC.Point(10,1))
    #     gWindow.items.remove(line)
    #     gWindow.redraw()
    #     line = GRC.Line(GRC.Point(150, 150), GRC.Point(150+(tick*10), tick*10))
    #     GRC.time.sleep(interval)
    #     gWindow.addItem(line)
    #     gWindow.redraw()

    # # 16 - 30
    # lineStartPoint = GRC.Point(150, 150)
    # for tick in range (1,16,1):
    #     # line.move(GRC.Point(150,150),GRC.Point(10,1))
    #     gWindow.items.remove(line)
    #     gWindow.redraw()
    #
    #     lineEndPoint = GRC.Point(300 - (tick*10), 150 + tick*10 )
    #     line = GRC.Line(lineStartPoint, lineEndPoint)
    #     GRC.time.sleep(interval)
    #     gWindow.addItem(line)
    #     gWindow.redraw()
    #
    # # 31 - 45
    # lineStartPoint = GRC.Point(150, 150)
    # for tick in range (1,16,1):
    #     # line.move(GRC.Point(150,150),GRC.Point(10,1))
    #     gWindow.items.remove(line)
    #     gWindow.redraw()
    #
    #     lineEndPoint = GRC.Point(150 - (tick*10), 300 - tick*10 )
    #     line = GRC.Line(lineStartPoint, lineEndPoint)
    #     GRC.time.sleep(interval)
    #     gWindow.addItem(line)
    #     gWindow.redraw()
    #
    # # 46 - 60
    # for tick in range(1, 16, 1):
    #     # line.move(GRC.Point(150,150),GRC.Point(10,1))
    #     gWindow.items.remove(line)
    #     gWindow.redraw()
    #
    #     lineEndPoint = GRC.Point(0 + (tick * 10), 150 - tick * 10)
    #     line = GRC.Line(lineStartPoint, lineEndPoint)
    #     GRC.time.sleep(interval)
    #     gWindow.addItem(line)
    #     gWindow.redraw()

    Util.pause(gWindow)





def pointsOnCircle(x,y,radius):
    center = GRC.Point(x,y)
    center =[x,y]
    angles =[]
    for angle in range (0,360):
        px = point_on_circle (center,angle-90,radius)
      #  print (px)
        angles.append(px)
    # for angle in range(0, 360):
    #     print("Angle1: ", angle, angles[angle])
    return angles

def seconds(centerPoint, radius):


    xx = centerPoint.getX()
    yy = centerPoint.getY()

    for tick in range(1, 61, 1):

        if tick < 16:
            lineEndPoint = GRC.Point(radius + (tick * 10), tick * 10)

        if tick >=16 and tick < 31:
            lineEndPoint = GRC.Point(300 - ((tick-15) * 10), 150 + (tick-15) * 10)

        if tick >= 30 and tick < 46:
            lineEndPoint = GRC.Point(150 - ((tick-30) * 10), 300 - (tick-30) * 10)

        if tick >= 46 and tick < 61:
            lineEndPoint = GRC.Point(0 + ((tick-45) * 10), 150 - (tick-45) * 10)

        line = GRC.Line(centerPoint, lineEndPoint)
        GRC.time.sleep(interval)
        gWindow.addItem(line)
        gWindow.redraw()



def Clock():
    pass



def point_on_circle(center,Degree,radius):
    '''
        Finding the x,y coordinates on circle, based on given angle
    '''
    from math import cos, sin, pi
    #center of circle, angle in degree and radius of circle
    #center = [150,150]
    # angle = 90
    # radius = 15
    angle = (pi * 2) / 360
    #x = offsetX + radius * Cosine(Degree)
    #x = center[0] + (radius * cos(angle))
    #y = offsetY + radius * Sine(Degree)
    #y = center[1] + (radius * sin(angle))

    x = center[0] + (radius * cos(Degree * pi / 180))
    y = center[1] + (radius * sin(Degree * pi / 180))


    point = GRC.Point(int(x),int(y))
    return point

# def  DrawCirclePoints( points,  radius,  center):
#     slice = 2 * Math.PI / points;
#     for ( i = 0; i < points; i++)
#          angle = slice * i;
#          newX = (int)(center.X + radius * Math.Cos(angle))
#          newY = (int)(center.Y + radius * Math.Sin(angle))
#         Point p = new Point(newX, newY);
#         #Console.WriteLine(p);





main()