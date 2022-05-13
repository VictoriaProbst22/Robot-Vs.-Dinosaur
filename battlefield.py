from dinosaur import Dinosaur

from robot import Robot


class Battlefield:
    
    def __init__(self):
        self.name = 'Battlefield'
        self.robot = Robot()
        self.dinosaur = Dinosaur()



    def run_game(self):
        self.run_game = ''
    

    def display_welcome(self):
        print("Welcome to the Battle of Robot V Dinosaur. A Battle of Two Champions to Prove Whos Best! Whats Your Guess?")
        #VOID FUNCTION

    def battle_phase(self):
        if self.robot.robot_attack and Dinosaur.health <= 50:
            print(f"Dinosaur Lost Health!")
        elif Dinosaur.dinosaur_attack and Robot.health <= 50:
            print("Robots Health is Decreasing!")
        else:
            print('Incoming!')
       

        #I know i want to include both "attack"fucnctions from Robot & Dinosaur
        # I want to use an 'if/else' statement for if Robot.attack _____ = Dinsaur.health decrease else dinosaur attacks and Robots.health decreases
        # #VOID FUNCTION

    def display_winner(self):
        pass
        #VOID FUNCTION