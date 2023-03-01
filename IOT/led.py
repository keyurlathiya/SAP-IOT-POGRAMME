import time
from grovepi import *

led = 4

pinMode(led,"OUTPUT")


while True:
    digitalWrite(led,1)
    time.sleep(1)
    print("LED is on")
    
    digitalWrite(led,0)
    time.sleep(1)
    print("LED is off")