import time
from grovepi import *

led = 7
button = 5

pinMode(led,"OUTPUT")
pinMode(button,"INPUT")

while True:
    try:
        v = digitalRead(button)
        if v==1:
            digitalWrite(led,1)
            print("LED on")
        else:
            digitalWrite(led,1)
            print("LED off")
    except:
           print("Error")