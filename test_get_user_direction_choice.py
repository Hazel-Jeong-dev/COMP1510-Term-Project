from unittest import TestCase
from unittest.mock import patch

import game


class TestGetUserDirectionChoice(TestCase):

    @patch('builtins.input', return_value='1')
    def test_get_user_direction_choice_return_a_string(self, _):
        self.assertIsInstance(game.get_user_direction_choice(), str)

    @patch('builtins.input', return_value='1')
    def test_get_user_direction_choice_user_choose_1(self, _):
        actual = game.get_user_direction_choice()
        expected = "North"
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='2')
    def test_get_user_direction_choice_user_choose_2(self, _):
        actual = game.get_user_direction_choice()
        expected = "South"
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='3')
    def test_get_user_direction_choice_user_choose_3(self, _):
        actual = game.get_user_direction_choice()
        expected = "East"
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='4')
    def test_get_user_direction_choice_user_choose_4(self, _):
        actual = game.get_user_direction_choice()
        expected = "West"
        self.assertEqual(actual, expected)
