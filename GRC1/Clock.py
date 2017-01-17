from Library import GRCGraphics as GRC
from Library import nrnoble as Util


import random, time, sys

windowWidth = 300
windowHeight = 300
interval = 1
Color = random.choice(Util.Colors)
gWindow = GRC.GraphicsWindow("Clock", windowWidth, windowHeight)
#lineStartPoint = []
#points = []

def main():



    circlePoints = pointsOnCircle(150,150,100)
    HourHandcirclePoints = pointsOnCircle(150, 150, 90)
    minuteHandcirclePoints = pointsOnCircle(150, 150, 95)
    secondHandEndPoint = circlePoints[0]
    clockCenter = GRC.Point(150, 150)
    secondHand = GRC.Line(secondHandEndPoint, clockCenter)
    gWindow.addItem(secondHand)
    gWindow.setBackground("Black")

    for tick in range (0,360,6):
        gWindow.plotPixel(circlePoints[tick].getX(), circlePoints[tick].getY(), "Yellow")

    while(True):
        sec = int (time.strftime("%S".zfill(3), time.localtime()))
        minute = int(time.strftime("%M".zfill(3), time.localtime()))
        hour = int(time.strftime("%I".zfill(3), time.localtime()))

        #print (hour, minute, sec)

        hourHandEndPoint = HourHandcirclePoints[hour * 30]
        minuteHandEndPoint = minuteHandcirclePoints[minute * 6]
        secondHandEndPoint = circlePoints[sec * 6]

        hourHand = clockHand(hourHandEndPoint, 3, "red", clockCenter)
        # hourHand = GRC.Line(hourHandEndPoint, clockCenter)
        # hourHand.setWidth(3)
        # hourHand.setFill("red")
        # hourHand.setArrow("first")

        MinuteHand = clockHand(minuteHandEndPoint, 2, "Blue", clockCenter)
        # MinuteHand = GRC.Line(minuteHandEndPoint, clockCenter)
        # MinuteHand.setWidth(2)
        # MinuteHand.setFill("Blue")
        # MinuteHand.setArrow("first")

        secondHand = clockHand(secondHandEndPoint, 1, "White", clockCenter)

        # secondHand = GRC.Line(secondHandEndPoint, clockCenter)
        # secondHand.setWidth(1)
        # secondHand.setFill("white")
        # secondHand.setArrow("first")


        hourHand.draw(gWindow)
        secondHand.draw(gWindow)
        MinuteHand.draw(gWindow)

        message = GRC.Text(GRC.Point(150, 290), str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(sec).zfill(2))
        message.setFill("Green")
        message.draw(gWindow)
        GRC.time.sleep(interval)

        message.undraw()
        hourHand.undraw()
        secondHand.undraw()
        MinuteHand.undraw()


Util.pause(gWindow)


def clockHand (endPoint, handWidth, handColor, clockCenter):
    hourHand = GRC.Line(endPoint, clockCenter)
    hourHand.setWidth(handWidth)
    hourHand.setFill(handColor)
    hourHand.setArrow("first")
    return hourHand


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

    angle = (pi * 2) / 360


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