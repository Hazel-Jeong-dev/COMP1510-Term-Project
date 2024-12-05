from unittest import TestCase

import game


class TestLevelUpProtocol(TestCase):

    def test_level_up_protocol_level_1_to_level_2(self):
        game_character = {"Name": "Chris", "Title": "Junior Chef", "Level": 1,
                          "X-coordinate": 3, "Y-coordinate": 0, "Current HP": 3, "Max HP": 15,
                          "Mastered Skills": ["Rinse"], "Items": ["Carrots", "Onions", "Garlic"]}
        level_info = {1: {"Title": "Junior Chef", "Max HP": 15, "Mastered Skills": ["Rinse"]},
                      2: {"Title": "Sous Chef", "Max HP": 20, "Mastered Skills": ["Rinse", "Cut"]},
                      3: {"Title": "Head Chef", "Max HP": 30, "Mastered Skills": ["Rinse", "Cut", "Fire"]}}
        game.level_up_protocol(game_character, level_info)
        expected = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                    "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 20, "Max HP": 20,
                    "Mastered Skills": ["Rinse", "Cut"], "Items": []}
        self.assertEqual(game_character, expected)

    def test_level_up_protocol_level_2_to_level_3(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 1, "Y-coordinate": 2, "Current HP": 5, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": ["Pork"]}
        level_info = {1: {"Title": "Junior Chef", "Max HP": 15, "Mastered Skills": ["Rinse"]},
                      2: {"Title": "Sous Chef", "Max HP": 20, "Mastered Skills": ["Rinse", "Cut"]},
                      3: {"Title": "Head Chef", "Max HP": 30, "Mastered Skills": ["Rinse", "Cut", "Fire"]}}
        game.level_up_protocol(game_character, level_info)
        expected = {"Name": "Chris", "Title": "Head Chef", "Level": 3,
                    "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 30, "Max HP": 30,
                    "Mastered Skills": ["Rinse", "Cut", "Fire"], "Items": []}
        self.assertEqual(game_character, expected)
