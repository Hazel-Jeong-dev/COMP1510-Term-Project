from unittest import TestCase

import game


class TestCheckIfGoalAttained(TestCase):

    def test_check_if_goal_attained_return_a_boolean(self):
        game_character = {"Name": "Chris", "Title": "Head Chef", "Level": 3,
                          "X-coordinate": 3, "Y-coordinate": 4, "Current HP": 7, "Max HP": 30,
                          "Mastered Skills": ["Rinse", "Cut", "Fire"], "Items": ["Jeyuk"]}
        dish = "Jeyuk"
        self.assertIsInstance(game.check_if_goal_attained(game_character, dish), bool)

    def test_check_if_goal_attained_true(self):
        game_character = {"Name": "Chris", "Title": "Head Chef", "Level": 3,
                          "X-coordinate": 3, "Y-coordinate": 4, "Current HP": 7, "Max HP": 30,
                          "Mastered Skills": ["Rinse", "Cut", "Fire"], "Items": ["Jeyuk"]}
        dish = "Jeyuk"
        actual = game.check_if_goal_attained(game_character, dish)
        expected = True
        self.assertEqual(actual, expected)
        
    def test_check_if_goal_attained_false(self):
        game_character = {"Name": "Chris", "Title": "Head Chef", "Level": 3,
                          "X-coordinate": 3, "Y-coordinate": 4, "Current HP": 7, "Max HP": 30,
                          "Mastered Skills": ["Rinse", "Cut", "Fire"], "Items": []}
        dish = "Jeyuk"
        actual = game.check_if_goal_attained(game_character, dish)
        expected = False
        self.assertEqual(actual, expected)
