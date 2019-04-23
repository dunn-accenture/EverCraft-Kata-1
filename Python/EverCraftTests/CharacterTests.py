import unittest
from EverCraft.Character import Character

class CharacterTest(unittest.TestCase):

    def test_character_sets_name_to_value(self):
        character = Character("Aaron")

        self.assertEqual("Aaron", character.name)

    def test_character_sets_name_to_stranger_when_no_value_provided(self):
        character = Character()

        self.assertEqual("Stranger", character.name)