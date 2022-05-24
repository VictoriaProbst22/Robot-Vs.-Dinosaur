from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    
    def __init__(self):
        self.robot = Robot('Robo')
        self.dinosaur = Dinosaur('Reptar', 20)


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    


    def display_welcome(self):
        print("Welcome to the Battle of Robot V Dinosaur. A Battle of Two Champions to Prove Whos Best! Whats Your Guess?")
    

    def battle_phase(self):
        while self.robot.health > 0 or self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

        #I know i want to include both "attack"fucnctions from Robot & Dinosaur
        # I want to use an 'if/else' statement for if Robot.attack _____ = Dinsaur.health decrease else dinosaur attacks and Robots.health decreases
        # #VOID FUNCTION
    def display_winner(self):
        if self.robot.health <=0:
         print('Dinosaur won!')
        else:
         print('RObot Won!')   