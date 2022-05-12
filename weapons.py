class Weapons:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.set_weapon_name()
    
    def set_weapon_name(self):
        weapon_name = input('Choose Your Weapon: ')
        self.name = weapon_name

    def set_attack_power(self):
        attack_power = 15
        attack_power = self.attack_power




