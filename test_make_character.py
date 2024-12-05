from unittest import TestCase

import game


class TestMakeCharacter(TestCase):

    def test_make_character_return_a_dictionary(self):
        self.assertIsInstance(game.make_character("Chris"), dict)

    def test_make_character_create_character(self):
        name = "Chris"
        actual = game.make_character(name)
        expected = {"Name": "Chris", "Title": "Junior Chef", "Level": 1, "X-coordinate": 2, "Y-coordinate": 2,
                    "Current HP": 15, "Max HP": 15, "Mastered Skills": ["Rinse"], "Items": []}
        self.assertEqual(actual, expected)
