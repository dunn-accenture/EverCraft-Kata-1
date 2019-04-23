CRITICAL_HIT = 20

ability_mods = {
    1: -5,
    2: -4,
    3: -4,
    4: -3,
    5: -3,
    6: -2,
    7: -2,
    8: -1,
    9: -1,
    10: 0,
    11: 0,
    12: 1,
    13: 1,
    14: 2,
    15: 2,
    16: 3,
    17: 3,
    18: 4,
    19: 4,
    20: 5
}



class Character:

    def __init__(self):
        self.armor_class = 10
        self.hit_points = 5
        self.is_alive = True
        self.str = 10
        self.dex = 10
        self.con = 10
        self.wis = 10
        self.int = 10
        self.cha = 10

    def setCon(self, newCon):
        self.con = newCon
        self.hit_points += ability_mods[newCon]

    def attack(self, defender, roll):
        str_bonus = ability_mods[self.str]
        defender_dex_bonus = ability_mods[defender.dex]
        modified_roll = roll + str_bonus
        modified_defender_armor = defender.armor_class + defender_dex_bonus

        if modified_roll >= modified_defender_armor:
            defender.take_damage(self.is_crit(roll), str_bonus)

            return "OUCH!"

        else:
            return "MISSED ME!"

    def update_living_state(self):
        if self.hit_points <= 0:
            self.is_alive = False

    def take_damage(self, crit, bonus):
        if bonus < 0:
            bonus = 0
        if crit:
            bonus *= 2
            self.hit_points -= 1 + bonus

        self.hit_points -= 1 + bonus
        self.update_living_state()

    def is_crit(self, roll):
        if roll == CRITICAL_HIT:
            return True
