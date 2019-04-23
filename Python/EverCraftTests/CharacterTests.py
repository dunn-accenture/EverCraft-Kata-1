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


    def test_ability_modifier_allows_high_strength_to_hit_on_lower_roll_than_armor_class_value(self):
        attacker = Character()
        attacker.str = 17
        defender = Character()
        defender.armor_class = 10

        roll = 7

        attacker.attack(defender, roll)

        self.assertEqual(1, defender.hit_points)

    def test_strength_modifier_applies_to_attack_damage(self):
        attacker = Character()
        attacker.str = 18
        defender = Character()
        defender.armor_class = 10

        roll = 7

        attacker.attack(defender, roll)

        self.assertEqual(0, defender.hit_points)

    def test_hit_always_deals_at_least_one_damage(self):
        attacker = Character()
        attacker.str = 1
        defender = Character()
        defender.armor_class = 10

        roll = 19

        attacker.attack(defender, roll)

        self.assertEqual(4, defender.hit_points)
