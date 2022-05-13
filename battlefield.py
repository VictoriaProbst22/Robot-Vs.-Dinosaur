from dinosaur import Dinosaur

from robot import Robot

player_one = Robot()
player_two = Dinosaur()

class Battlefield:
    
    def __init__(self):
        self.name = 'Battlefield'



    def run_game(self):
        self.run_game = ''
    

    def display_welcome(self):
        print("Welcome to the Battle of Robot V Dinosaur. A Battle of Two Champions to Prove Whos Best! Whats Your Guess?")
        #VOID FUNCTION

    def battle_phase(self):
        if robot_attack and Dinosaur.health <= 50:
            print(f"Dinosaur Lost Health!")
        elif dinosaur_attack and Robot.health <= 50:
            print("Robots Health is Decreasing!")
        else:
            print('Incoming!')
       

        #I know i want to include both "attack"fucnctions from Robot & Dinosaur
        # I want to use an 'if/else' statement for if Robot.attack _____ = Dinsaur.health decrease else dinosaur attacks and Robots.health decreases
        # #VOID FUNCTION

    def display_winner(self):
        pass
        #VOID FUNCTION