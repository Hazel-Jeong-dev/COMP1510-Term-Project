from unittest import TestCase

import game


class TestCharacterHasLeveled(TestCase):

    def test_character_has_leveled_return_a_boolean(self):
        game_character = {"Name": "Chris", "Title": "Junior Chef", "Level": 1,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 15,
                          "Mastered Skills": ["Rinse"], "Items": ["Carrots", "Onions", "Garlic"]}
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        self.assertIsInstance(game.character_has_leveled(game_character, jeyuk_ingredients), bool)

    def test_character_has_leveled_true_level_1(self):
        game_character = {"Name": "Chris", "Title": "Junior Chef", "Level": 1,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 15,
                          "Mastered Skills": ["Rinse"], "Items": ["Carrots", "Onions", "Garlic"]}
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        actual = game.character_has_leveled(game_character, jeyuk_ingredients)
        expected = True
        self.assertEqual(actual, expected)

    def test_character_has_leveled_false_level_1(self):
        game_character = {"Name": "Chris", "Title": "Junior Chef", "Level": 1,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 15,
                          "Mastered Skills": ["Rinse"], "Items": ["Carrots", "Garlic"]}
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        actual = game.character_has_leveled(game_character, jeyuk_ingredients)
        expected = False
        self.assertEqual(actual, expected)

    def test_character_has_leveled_true_level_2(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": ["Pork"]}
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        actual = game.character_has_leveled(game_character, jeyuk_ingredients)
        expected = True
        self.assertEqual(actual, expected)

    def test_character_has_leveled_false_level_2(self):
        game_character = {"Name": "Chris", "Title": "Sous Chef", "Level": 2,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 15, "Max HP": 20,
                          "Mastered Skills": ["Rinse", "Cut"], "Items": ["Beef"]}
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        actual = game.character_has_leveled(game_character, jeyuk_ingredients)
        expected = False
        self.assertEqual(actual, expected)

    def test_character_has_leveled_true_level_3(self):
        game_character = {"Name": "Chris", "Title": "Head Chef", "Level": 3,
                          "X-coordinate": 2, "Y-coordinate": 2, "Current HP": 30, "Max HP": 30,
                          "Mastered Skills": ["Rinse", "Cut", "Fire"], "Items": ["Jeyuk"]}
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        actual = game.character_has_leveled(game_character, jeyuk_ingredients)
        expected = True
        self.assertEqual(actual, expected)
