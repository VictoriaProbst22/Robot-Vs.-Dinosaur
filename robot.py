from weapons import Weapons

from dinosaur import Dinosaur

class Robot:

  def __init__(self):
    self.name = 'Hugo'
    self.health = 100
    self.weapon = Weapons()

  def robot_attack(self, Dinosaur):
    robot_attack = Dinosaur.health - Weapons.attack_power
  

    #i want the attack power to decrease the self.health of the oppenant
