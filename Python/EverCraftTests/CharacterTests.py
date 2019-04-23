import unittest
from EverCraft.Character import Character

class CharacterTest(unittest.TestCase):

    def test_if_roll_is_lower_than_armor_character_misses_attack(self):
        attacker = Character()
        defender = Character()

        roll = 1

        self.assertEqual("MISSED ME!", attacker.attack(defender, roll))

    def test_if_roll_is_higher_than_armor_character_hits(self):
        attacker = Character()
        defender = Character()

        roll = defender.armor_class + 1

        self.assertEqual("OUCH!", attacker.attack(defender, roll))

    def test_if_attacker_hits_defender_loses_one_hit_point(self):
        attacker = Character()
        defender = Character()

        roll = defender.armor_class + 1

        attacker.attack(defender, roll)

        self.assertEqual(4, defender.hit_points)

    def test_if_attacker_critical_hits_defender_loses_two_hit_points(self):
        attacker = Character()
        defender = Character()

        roll = 20

        attacker.attack(defender, roll)

        self.assertEqual(3, defender.hit_points)

    def test_if_defender_hit_points_less_or_equal_to_zero_defender_dies(self):
        attacker = Character()
        defender = Character()

        roll = defender.armor_class + 1

        for i in range(defender.hit_points):
            attacker.attack(defender, roll)

        self.assertFalse(defender.is_alive)