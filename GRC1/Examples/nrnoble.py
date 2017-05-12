import random, time, sys

Colors =['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Pink', 'Purple', 'Gold', 'Silver', 'Gray', 'Maroon']
Colors2 =['Red', 'Green', 'Blue', 'White', 'Yellow', 'Orange', 'Pink', 'Purple', 'Gold', 'Silver', 'Gray', 'Maroon']



def pause(win):
    #win.redraw()
    win.update()
    win.waitForClick()

def getNewColor(Color):
    newColor = Color
    while (Color == newColor):
        newColor = random.choice(Colors)
    return newColor

def sleep(sec):
    time.sleep(sec)