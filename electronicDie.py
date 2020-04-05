from sense_hat import SenseHat
from time import sleep
from random import randrange

class ElectronicDie:
    
    def roll_die(self):
        sense = SenseHat()
        x,y,z = [sense.get_accelerometer_raw()[key] for key in ['x','y','z']]
        while True:
            if(abs(x) > 1 or abs(y) > 1 or abs(z) > 1):
                return self.display_die()

    def display_die(self):
        number = randrange(1, 7)
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
        sense.set_pixels(dice_array[number-1])
        sleep(1.5)
        sense.clear()
        return number

electronicDie = ElectronicDie()
electronicDie.roll_die()