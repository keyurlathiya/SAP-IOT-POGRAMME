from grove_rgb_lcd import *
import time

a="Yash Kunj"
setRGB(0,190,0)

for i in a:
    setText(str(i))
    time.sleep(0.5)