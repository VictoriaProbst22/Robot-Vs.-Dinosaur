from dinosaur import Dinosaur
from weapons import Weapons


class Robot:

  def __init__(self):
    self.name = 'Hugo'
    self.health = 100
    self.weapon = Weapons()

  def robot_attack(self, dinosaur):
    robot_attack = dinosaur.health - Weapons.attack_power
  if Dinosaur.health > 0:
    print(f"You Landed a Hit! {Dinosaur.name} is Wounded!")
  Dinosaur.health = Dinosaur.health - 35

    #i want the attack power to decrease the self.health of the oppenant
