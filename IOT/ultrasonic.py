from grovepi import *
from grove_rgb_lcd import *
import time

ultrasonic_ranger = 7

counter = 0
while True:
    distant = ultrasonicRead(ultrasonic_ranger)
    print(distant,'cm')
    setText_norefresh(str(distant)+'cm')
    counter+=1
    print(counter)
    time.sleep(0.5)