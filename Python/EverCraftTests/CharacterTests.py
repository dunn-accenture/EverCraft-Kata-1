import unittest
from EverCraft.Character import Character

class CharacterTest(unittest.TestCase):

    def test_character_sets_name_to_value(self):
        character = Character("Aaron")

        self.assertEqual("Aaron", character.name)

    def test_character_sets_name_to_stranger_when_no_value_provided(self):
        character = Character()

        self.assertEqual("Stranger", character.name)

    def test_attack_roll_must_be_greater_than_or_equal_armor_to_hit(self):
        character1 = Character()
        character2 = Character()

        roll = 10

        character1.attack(character2, roll)

        self.assertEqual(4, character2.health)

    def test_attack_deals_double_damage_when_twenty_is_rolled(self):
        character1 = Character()
        character2 = Character()

        roll = 20

        character1.attack(character2, roll)

        self.assertEqual(3, character2.health)

    def test_character_is_dead_when_health_at_or_below_zero(self):
        character1 = Character()
        character2 = Character()

        self.assertTrue(character2.is_alive)

        self.kill_character(character1, character2)

        self.assertFalse(character2.is_alive)


    def kill_character(self, character1, character2):
        roll = character2.armor + 1

        for i in range(character2.health):
            character1.attack(character2, roll)

