'''
Two player game in continious while loop.
until one of the score is >= 30
'''
from sense_hat import SenseHat
import datetime
import csv
from time import sleep
from electronicDie import ElectronicDie

sense = SenseHat()

class Game(ElectronicDie):
    def __init__(self, csv_file, win_score):
        self.win_score = win_score
        self.csv_file = csv_file
        self.faces = 6
        sense.clear()

    def show_instruction(self):
        #msg = "Game is between two players P1 and P2. Player shakes board until display it shows tick in order to roll a die. Players to score more than {0} points first wins.".format(self.win_score)
        msg = "Instr..."
        sense.show_message(msg)
    
    def write_to_file(self, player, time, score):
        with open(self.csv_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([player, time, score])

    def play(self):
        self.show_instruction()
        is_player1 = True
        p1_score = 0
        p2_score = 0

        while p1_score <= self.win_score and p2_score <= self.win_score:
            sense.clear()
            sense.show_message('P1 turn') if is_player1 else sense.show_message('P2 turn')
            sleep(2)
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

        #winner = "P1" if p1_score > p2_score else "P2"
        #total_score = p1_score if winner == "P1" else p2_score

        if p1_score > p2_score:
            winner = "P1"
            total_score = p1_score
        else:
            winner = "P2"
            total_score = p2_score

        time = str(datetime.datetime.now())
        self.write_to_file(winner, time, total_score)
        sense.show_message(winner + " wins.")
        sense.clear()
  
game = Game("winner.csv", 30)
game.play()
