from sense_hat import SenseHat
from time import sleep

class Emoji:    

    def smiley(self):
        x = (128, 128, 128) #white
        o = (0, 128, 0) # Green
        w = (0, 0, 128) # blue
        smiley_face = [            
            x, x, x, x, x, x, x, x,
            x, x, x, x, x, x, x, x,
            x, o, o, x, x, o, o, x,
            x, o, o, x, x, o, o, x,
            x, x, x, x, x, x, x, x,
            x, w, x, x, x, x, w, x,
            x, x, w, w, w, w, x, x,
            x, x, x, x, x, x, x, x
        ]
        return smiley_face
    
    def frowning(self):
        x = (128, 0, 0) #red
        o = (0, 0, 128) # blue
        w = (0, 0, 0) # black
        frowning_face = [            
            x, x, x, x, x, x, x, x,
            x, x, x, x, x, x, x, x,
            x, o, o, x, x, o, o, x,
            x, o, o, x, x, o, o, x,
            x, x, x, x, x, x, x, x,
            x, x, x, w, w, x, x, x,
            x, x, w, x, x, w, x, x,
            x, x, x, x, x, x, x, x
        ]
        return frowning_face

    def laughing(self):
        x = (100,100,0) #yellow
        o = (200, 100, 200)
        w = (225, 225, 225) # white
        laughing_face = [            
            x, x, x, x, x, x, x, x,
            x, x, x, x, x, x, x, x,
            x, o, o, x, x, o, o, x,
            x, o, o, x, x, o, o, x,
            x, x, x, x, x, x, x, x,
            x, w, w, w, w, w, w, x,
            x, x, w, w, w, w, x, x,
            x, x, x, x, x, x, x, x
        ]
        return laughing_face        


sense = SenseHat()
emoji = Emoji()

sense.set_pixels(emoji.smiley())
sleep(3)
sense.set_pixels(emoji.frowning())
sleep(3)
sense.set_pixels(emoji.laughing())
sleep(3)
sense.clear()