from grovepi import *
import sys
import os
import time
import urllib
from urllib import request

myAPI = "O342VTYJBPNNLZVK"
myDelay = 1

ultrasonic_ranger = 4


baseURL = 'https://api.thingspeak.com/update?api_key=%s' %myAPI

while True:
    try:
            distant = ultrasonicRead(ultrasonic_ranger)
            time.sleep(0.5)
            print(distant)
            
            distant=str(distant)
            
            f = urllib.request.urlopen(baseURL + "&field1=%s" %distant)
            
            f.close()
            
            time.sleep(int(myDelay))
            
            
    except TypeError:
        print("Error")
    except IOError:
        print("Error")