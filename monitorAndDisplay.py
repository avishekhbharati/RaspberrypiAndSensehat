from sense_hat import SenseHat
from time import sleep
import json


class TempreatureMonitor:
    
    RED_COLOR = [130, 0, 0]
    GREEN_COLOR = [0, 130, 0]
    BLUE_COLOR = [0, 0, 130]

    def __init__(self, filename):
        self.sense = SenseHat()
        data = self.read_from_file(filename)
        self.cold_max = data['cold_max']
        self.comfortable_min = data['comfortable_min']
        self.comfortable_max = data['comfortable_max']
        self.hot_min = data['hot_min']

    #reads from json file. If corrupted uses default values
    def read_from_file(self, filename):
        try:
            f = open(filename, 'r')
            return json.loads(f.read())
        except:
            self.sense.show_message("Error in reading json file: Using default values.")
            default_values = {
                "cold_max": 10,
                "comfortable_min": 10,
                "comfortable_max": 25,
                "hot_min": 25
            }
        return default_values

    #rounds up tempreature to two digits.
    def read_tempreature(self):
        return round(self.sense.get_temperature(), 2)

    
    #check the tempreature and set color
    def display_current_tempreature(self, temp):
        self.sense.clear()        
        str_format = str(temp) + "C"
        
        #here max value is inclusive
        if temp <= self.cold_max:
            self.sense.show_message(str_format, text_colour = self.BLUE_COLOR)
        elif temp > self.hot_min:
            self.sense.show_message(str_format, text_colour = self.RED_COLOR)
        else:
            self.sense.show_message(str_format, text_colour = self.GREEN_COLOR)


temp_monitor = TempreatureMonitor('config.json')
while True:
    curr_temp = temp_monitor.read_tempreature()
    temp_monitor.display_current_tempreature(curr_temp)
    sleep(10)