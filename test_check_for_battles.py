from unittest import TestCase
from unittest.mock import patch

import game


class TestCheckForBattles(TestCase):

    @patch("random.choice", return_value="battle")
    def test_check_for_battles_return_a_boolean(self, _):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        self.assertIsInstance(game.check_for_battles(game_character), bool)

    @patch("random.choice", return_value="battle")
    def test_check_for_battles_there_is_a_battle(self, _):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        actual = game.check_for_battles(game_character)
        expected = True
        self.assertEqual(actual, expected)

    @patch("random.choice", return_value="safe")
    def test_check_for_battles_there_is_no_battle(self, _):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        actual = game.check_for_battles(game_character)
        expected = False
        self.assertEqual(actual, expected)
