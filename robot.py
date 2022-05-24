from weapons import Weapons


class Robot:

  def __init__(self, name):
    self.name = name
    self.health = 100
    self.active_weapon = Weapons("Chainsaw", 20)

  def attack(self, dinosaur):
    dinosaur.health -= self.active_weapon.attack_power
    print(f"Hit!! {dinosaur.name} has {dinosaur.health} !")

    #i want the attack power to decrease the self.health of the oppenant
