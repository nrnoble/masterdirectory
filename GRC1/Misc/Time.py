import random
import time

from Library import GRCGraphics as GRC
from Library.Examples import nrnoble as Util

windowWidth = 300
windowHeight = 300
interval = .1
Color = random.choice(Util.Colors)
gWindow = GRC.GraphicsWindow("Text Demo", windowWidth, windowHeight)

def main():
    then = time.time()
    #Util.sleep(1)
    now = time.time()
    diff = now - then

    minutes, seconds = int(diff // 60), int(diff % 60)
    print('Next time you add blood is ' + str(minutes) + ':' + str(seconds))
    print('Next time you add blood is ' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))

    myTime1 = time.strptime("30 Nov 00", "%d %b %y")
    # myTime2 = time.strftime(%M,time.time())
    myTime3 = time.strftime("%a %d %b %Y %H:%M:%S +0000", time.gmtime())
    myTime3 = time.strftime("%S".zfill(3), time.gmtime())
    sec = int(myTime3)
    print(sec)



main()