import time
import grovepi
from grove_rgb_lcd import *

light_sensor = 0

led = 4

threshold = 10

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

while True:
    try:
        sensor_value = grovepi.analogRead(light_sensor)
        print(sensor_value)
        
        resistance = (float)(1023 - sensor_value) * 10 / (sensor_value + 0.001)
        setRGB(255-10*sensor_value,255-10*sensor_value, 255-10*sensor_value)
        
        if sensor_value > threshold:
            groverpi.digitalWrite(led,0)
            setText_norefresh("Turn Off Smart Light")
        else:
            groverpi.digitalWrite(led,1)
            setText_norefresh("Turn On Smart Light")
            
        print("sensor_value = %d resistance = %.2f" %(sensor_value,resistance))
        time.sleep(.5)
        
    except:
        print("Error")