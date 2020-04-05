from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
x = (128, 128, 0) 
o = (0, 0, 0) 

class ElectronicDie:
   def one(self):
      return [
         o, o, o, o, o, o, o, o,
         o, o, o, o, o, o, o, o,
         o, o, o, o, o, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, o, o, o, o, o,
         o, o, o, o, o, o, o, o,
         o, o, o, o, o, o, o, o
      ]

   def two(self):
      return [
         o, o, o, o, o, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, o, o, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, o, o, o, o, o,
         o, o, o, o, o, o, o, o
      ]

   def three(self):
      return [
         o, o, o, x, x, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, o, o, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, o, o, o, o, o,
         o, o, o, x, x, o, o, o,
         o, o, o, x, x, o, o, o
      ]

   def four(self):
      return [
         o, o, o, o, o, o, o, o,
         o, o, x, x, o, x, x, o,
         o, o, x, x, o, x, x, o,
         o, o, o, o, o, o, o, o,
         o, o, x, x, o, x, x, o,
         o, o, x, x, o, x, x, o,
         o, o, o, o, o, o, o, o,
         o, o, o, o, o, o, o, o
      ]

   def five(self):
      return [
         o, o, o, o, o, o, o, o,
         x, x, o, o, o, o, x, x,
         x, x, o, o, o, o, x, x,
         o, o, o, x, x, o, o, o,
         o, o, o, x, x, o, o, o,
         x, x, o, o, o, o, x, x,
         x, x, o, o, o, o, x, x,
         o, o, o, o, o, o, o, o
      ]

   def six(self):
      return [
         o, o, x, x, o, x, x, o,
         o, o, x, x, o, x, x, o,
         o, o, o, o, o, o, o, o,
         o, o, x, x, o, x, x, o,
         o, o, x, x, o, x, x, o,
         o, o, o, o, o, o, o, o,
         o, o, x, x, o, x, x, o,
         o, o, x, x, o, x, x, o
      ]
   
   def tick(self):
      x = (0, 255, 0)
      o = (0, 0, 0)
      return [
         o, o, o, o, o, o, o, o,
         o, o, o, o, o, o, o, x,
         o, o, o, o, o, o, x, o,
         o, o, o, o, o, x, o, o,
         x, o, o, o, x, o, o, o,
         o, x, o, x, o, o, o, o,
         o, o, x, o, o, o, o, o,
         o, o, o, o, o, o, o, o
      ]

   def get_die_faces(self, number):
      if number == 1:
         return self.one()
      elif number == 2:
         return self.two()
      elif number == 3:
         return self.three()
      elif number == 4:
         return self.four()
      elif number == 5:
         return self.five()
      else:
         return self.six()

   def detect_motion(self):
      while True:
         acceleration = sense.get_accelerometer_raw()
         x = abs(acceleration['x'])
         y = abs(acceleration['y'])
         z = abs(acceleration['z'])

         if x > 2 or y > 2 or z > 2:
            print("x={0}, y={1}, z={2}".format(x,y,z))
            sense.set_pixels(self.tick())
            sleep(2)
            break
         else:
            sense.show_letter("?", (255, 0, 0))


   def generate_randomnumber(self, faces):
      #last number is exclusive. so add 1.
      return random.randrange(1, faces + 1)
   

   def display_die(self, number):
      try:
         sense.set_pixels(self.get_die_faces(number))
      except:
         print("Die number is not in the range. Input Number: {0}".format(number))
