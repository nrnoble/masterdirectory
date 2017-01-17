from GRC1.BaseGlobals import *

def update(rate=None):
    global update_lasttime
    if rate:
        now = time.time()
        pauseLength = 1 / rate - (now - update_lasttime)
        if pauseLength > 0:
            time.sleep(pauseLength)
            update_lasttime = now + pauseLength
        else:
            update_lasttime = now

    root.update()