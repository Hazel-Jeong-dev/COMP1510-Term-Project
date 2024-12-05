from unittest import TestCase

import game


class TestIsAlive(TestCase):

    def test_is_alive_return_a_boolean(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        self.assertIsInstance(game.is_alive(game_character), bool)

    def test_is_alive_when_alive(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        actual = game.is_alive(game_character)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_when_dead(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 0, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        actual = game.is_alive(game_character)
        expected = False
        self.assertEqual(actual, expected)
