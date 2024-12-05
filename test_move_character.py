from unittest import TestCase

import game


class TestMoveCharacter(TestCase):

    def test_move_character_travel_north(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "North"
        game.move_character(game_character, move_direction)
        expected = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                    "X-coordinate": 3, "Y-coordinate": 1, "Current HP": 15, "Max HP": 20,
                    "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        self.assertEqual(game_character, expected)

    def test_move_character_travel_south(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "South"
        game.move_character(game_character, move_direction)
        expected = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                    "X-coordinate": 3, "Y-coordinate": 3, "Current HP": 15, "Max HP": 20,
                    "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        self.assertEqual(game_character, expected)

    def test_move_character_travel_east(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "East"
        game.move_character(game_character, move_direction)
        expected = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                    "X-coordinate": 4, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                    "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        self.assertEqual(game_character, expected)

    def test_move_character_travel_west(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 3, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        move_direction = "West"
        game.move_character(game_character, move_direction)
        expected = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                    "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                    "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        self.assertEqual(game_character, expected)
