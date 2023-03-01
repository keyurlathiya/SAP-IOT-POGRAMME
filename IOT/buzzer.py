import time
from grovepi import *

buzzer = 4

pinMode(buzzer,"OUTPUT")
time.sleep(1)

while True:
    try:
        digitalWrite(buzzer,1)
        time.sleep(.5)
        digitalWrite(buzzer,0)
        time.sleep(1)
        
    except:
        print("Error")
        