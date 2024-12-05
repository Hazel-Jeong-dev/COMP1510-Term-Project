import io
from unittest import TestCase
from unittest.mock import patch

import game


class TestShowIngredientsForCurrentLevel(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_for_current_level_when_level_1(self, mock_output):
        game_character = {"Name": "Chris", "Title": "Junior Chef", "Level": 1,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 15,
                          "Mastered Skills": ["Rinse"], "Items": []}
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        game.show_ingredients_for_current_level(game_character, jeyuk_ingredients)
        actual = mock_output.getvalue().strip()
        expected = ('You are currently Junior Chef.\n'
                    'You need to collect Carrots, Onions, and Garlic to level up.').strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_for_current_level_when_level_2(self, mock_output):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        game.show_ingredients_for_current_level(game_character, jeyuk_ingredients)
        actual = mock_output.getvalue().strip()
        expected = ('You are currently Sous Chef.\n'
                    'You need to collect Pork to level up.').strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_for_current_level_when_level_3(self, mock_output):
        game_character = {"Name": "Chris", "Title": "Head Chef", "Level": 3,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 30, "Max HP": 30,
                          "Mastered Skills": ["Rinse", "Cut", "Fire"], "Items": []}
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        game.show_ingredients_for_current_level(game_character, jeyuk_ingredients)
        actual = mock_output.getvalue().strip()
        expected = ('You are currently Head Chef.\n'
                    'You can now cook Jeyuk to win the game.').strip()
        self.assertEqual(actual, expected)
