
class Character:

    def __init__(self):
        self.armor_class = 10
        self.hit_points = 5

    def attack(self, defender, roll):
        if roll <= defender.armor_class:
            return "MISSED ME!"
        else:
            defender.hit_points -= 1

            if roll == 20:
                defender.hit_points -= 1
            return "OUCH!"