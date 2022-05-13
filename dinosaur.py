class Dinosaur:

    def __init__(self):
        self.name = 'Reptar'
        self.attack_power = 10
        self.health = 100
        


    def dinosaur_attack(self, robot):
       robot.health = robot.health - self.attack_power
       if robot.health >= 0:
             print("Hit Landed! {robot.name} has been damaged!")
             robot.health = robot.health - 10
       else:
            print("Incoming!")






        #VOID FUNCTION
        #