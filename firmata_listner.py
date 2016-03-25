from sense_hat import SenseHat 
from random import randint 
from time import sleep 
import pyfirmata
from pyfirmata import Arduino, util

sense = SenseHat() 

board = Arduino('/dev/ttyACM1', baudrate=57600);

def setColor(r, g, b): 
    for x in range(0,8): 
        for y in range(0,8): 
            sense.set_pixel(x , y , r, g, b) 

thread = util.Iterator(board)
thread.start()

pin = board.get_pin('d:2:i');
pin.enable_reporting()

while True: 
    pinValue = pin.read()
    print pinValue
    if pinValue == 0:
        setColor(255, 0, 0)
    else:
        setColor(0, 255, 0)
    
    sleep(.5)
