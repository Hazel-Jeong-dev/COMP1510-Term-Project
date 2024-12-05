import io
from unittest import TestCase
from unittest.mock import patch

import game


class TestDescribeCurrentLocation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_when_at_center(self, mock_output):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        game.describe_current_location(game_character)
        actual = mock_output.getvalue().strip()
        expected = 'You are currently at (2, 2), and you have 20 HP left.'.strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_when_at_a_corner(self, mock_output):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 20, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        game.describe_current_location(game_character)
        actual = mock_output.getvalue().strip()
        expected = 'You are currently at (0, 0), and you have 20 HP left.'.strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_when_at_a_random_spot(self, mock_output):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 1, "Current HP": 20, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        game.describe_current_location(game_character)
        actual = mock_output.getvalue().strip()
        expected = 'You are currently at (3, 1), and you have 20 HP left.'.strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_when_full_HP(self, mock_output):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        game.describe_current_location(game_character)
        actual = mock_output.getvalue().strip()
        expected = 'You are currently at (3, 2), and you have 20 HP left.'.strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_when_not_full_HP(self, mock_output):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 2, "Current HP": 6, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        game.describe_current_location(game_character)
        actual = mock_output.getvalue().strip()
        expected = 'You are currently at (3, 2), and you have 6 HP left.'.strip()
        self.assertEqual(actual, expected)
