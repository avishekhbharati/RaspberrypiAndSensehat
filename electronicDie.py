from sense_hat import SenseHat
from time import sleep
from random import randrange

class ElectronicDie:    

    def start(self):
        x = (0, 0, 0) # black
        b = (128, 128, 0) # yellow
        dice_array = [[            
            x, x, x, x, x, x, x, x,
            x, x, x, x, x, x, x, x,
            x, x, x, x, x, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, x, x, x, x, x,
            x, x, x, x, x, x, x, x,
            x, x, x, x, x, x, x, x
        ],[            
            x, x, x, x, x, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, x, x, x, x, x,
            x, x, x, x, x, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, x, x, x, x, x
        ],[            
            x, x, x, b, b, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, x, x, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, x, x, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, b, b, x, x, x
        ],[            
            x, x, x, x, x, x, x, x,
            x, b, b, x, x, b, b, x,
            x, b, b, x, x, b, b, x,
            x, x, x, x, x, x, x, x,
            x, x, x, x, x, x, x, x,
            x, b, b, x, x, b, b, x,
            x, b, b, x, x, b, b, x,
            x, x, x, x, x, x, x, x
        ],[            
            b, b, x, x, x, x, b, b,
            b, b, x, x, x, x, b, b,
            x, x, x, x, x, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, b, b, x, x, x,
            x, x, x, x, x, x, x, x,
            b, b, x, x, x, x, b, b,
            b, b, x, x, x, x, b, b
        ],[            
            b, b, x, b, b, x, b, b,
            b, b, x, b, b, x, b, b,
            x, x, x, x, x, x, x, x,
            b, b, x, b, b, x, b, b,
            b, b, x, b, b, x, b, b,
            x, x, x, x, x, x, x, x,
            b, b, x, b, b, x, b, b,
            b, b, x, b, b, x, b, b
        ]]
        sense = SenseHat()
        while True:
            x,y,z = [sense.get_accelerometer_raw()[key] for key in ['x','y','z']]
            if(abs(x) > 1 or abs(y) > 1 or abs(z) > 1):
                sense.set_pixels(dice_array[randrange(0, 6)])
                sleep(1)
                sense.clear()

electronicDie = ElectronicDie()
electronicDie.start()