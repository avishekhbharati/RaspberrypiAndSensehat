from sense_hat import SenseHat
import datetime
import csv
from time import sleep
from electronicDie import ElectronicDie

sense = SenseHat()

class Game(ElectronicDie):
    #supply csv file name, number of die faces, and score to win
    def __init__(self, csv_file, faces, win_score):
        self.win_score = win_score
        self.csv_file = csv_file
        #hardcoded as 6 for now.
        self.faces = faces 
        sense.clear()

    #displays instructions for the game
    def show_instruction(self):
        msg = "Game is between P1 and P2. Player shakes board until it shows tick in order to roll a die. Players to score more than {0} points first wins.".format(self.win_score)
        sense.show_message(msg)
    
    #writes the winners detail in file
    def write_to_file(self, player, time, score):
        try:
            with open(self.csv_file, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([player, time, score])
        except:
            sense.show_message("Failed to write result to a file.")

    #method for game play. 
    def play(self):
        self.show_instruction()
        is_player1 = True
        p1_score = 0
        p2_score = 0

        #loop until one of the players reaches passes the winning score
        while p1_score <= self.win_score and p2_score <= self.win_score:
            sense.clear()
            sense.show_message('P1 turn') if is_player1 else sense.show_message('P2 turn')
            sleep(1)
            self.detect_motion()
            random_number = self.generate_randomnumber(self.faces)
            self.display_die(random_number)
            sleep(2)

            if is_player1:
                p1_score = p1_score + random_number
                sense.show_message("P1 : {0}".format(p1_score))
                is_player1 = False
            else:
                p2_score = p2_score + random_number
                sense.show_message("P2 : {0}".format(p2_score))
                is_player1 = True

        if p1_score > p2_score:
            winner = "P1"
            total_score = p1_score
        else:
            winner = "P2"
            total_score = p2_score

        time = str(datetime.datetime.now())
        self.write_to_file(winner, time, total_score)
        #displays winning message
        sense.show_message(winner + " wins.")
        sense.clear()
  
game = Game("winner.csv", 6, 30)
game.play()
