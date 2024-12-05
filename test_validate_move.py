from unittest import TestCase

import game


class TestValidateMove(TestCase):

    def test_validate_move_return_a_boolean(self):
        board_rows = 5
        board_columns = 5
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "South"
        self.assertIsInstance(game.validate_move(board_rows, board_columns, game_character, move_direction), bool)

    def test_validate_move_travel_north_when_not_on_top_row(self):
        board_rows = 5
        board_columns = 5
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 3, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "North"
        actual = game.validate_move(board_rows, board_columns, game_character, move_direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_travel_north_when_on_top_row(self):
        board_rows = 5
        board_columns = 5
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "North"
        actual = game.validate_move(board_rows, board_columns, game_character, move_direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_travel_south_when_not_on_bottom_row(self):
        board_rows = 5
        board_columns = 5
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "South"
        actual = game.validate_move(board_rows, board_columns, game_character, move_direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_travel_south_when_on_bottom_row(self):
        board_rows = 5
        board_columns = 5
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 4, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "South"
        actual = game.validate_move(board_rows, board_columns, game_character, move_direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_travel_east_when_not_on_far_right_column(self):
        board_rows = 5
        board_columns = 5
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 1, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "East"
        actual = game.validate_move(board_rows, board_columns, game_character, move_direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_travel_east_when_on_far_right_column(self):
        board_rows = 5
        board_columns = 5
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 4, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "East"
        actual = game.validate_move(board_rows, board_columns, game_character, move_direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_travel_west_when_not_on_far_left_column(self):
        board_rows = 5
        board_columns = 5
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "West"
        actual = game.validate_move(board_rows, board_columns, game_character, move_direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_travel_west_when_on_far_left_column(self):
        board_rows = 5
        board_columns = 5
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 0, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "West"
        actual = game.validate_move(board_rows, board_columns, game_character, move_direction)
        expected = False
        self.assertEqual(actual, expected)
