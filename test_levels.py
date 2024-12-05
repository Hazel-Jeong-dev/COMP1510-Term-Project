from unittest import TestCase

import game


class TestLevels(TestCase):

    def test_levels_return_a_dictionary(self):
        self.assertIsInstance(game.levels(), dict)

    def test_levels_return_level_information(self):
        actual = game.levels()
        expected = {1: {"Title": "Junior Chef", "Max HP": 15, "Mastered Skills": ["Rinse"]},
                    2: {"Title": "Sous Chef", "Max HP": 20, "Mastered Skills": ["Rinse", "Cut"]},
                    3: {"Title": "Head Chef", "Max HP": 30, "Mastered Skills": ["Rinse", "Cut", "Fire"]}}
        self.assertEqual(actual, expected)
