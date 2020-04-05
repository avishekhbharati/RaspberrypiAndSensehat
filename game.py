from sense_hat import SenseHat
from time import sleep
from electronicDie import ElectronicDie


class Game:    

    def start(self):
        player_points = [0, 0]
        electronicDie = ElectronicDie()
        while(player_points[0]<30 and player_points[1]<=30)
            for player in range(0, 2):
                player_points[player] = player_points[player] + electronicDie.roll_die()
                if(player_points[player]>=30):
                    display_text("text")

    def display_text(self, string):
        print(string)
        
game = Game()
game.start()