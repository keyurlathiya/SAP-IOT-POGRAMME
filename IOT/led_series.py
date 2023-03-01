from grovepi import *

led = 4

pinMode(led, "OUTPUT")

ip = int(input())
if ip == 1:
    digitalWrite(led,1)
elif ip == 0:
    digitalWrite(led,0)
    