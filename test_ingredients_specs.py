from unittest import TestCase

import game


class TestIngredientsSpecs(TestCase):

    def test_ingredients_specs_return_a_dictionary(self):
        galbijjim_ingredients = {1: ("Carrots", "Potatoes", "Onions", "Garlic"), 2: "Beef", 3: "Galbijjim"}
        self.assertIsInstance(game.ingredients_specs(galbijjim_ingredients), dict)

    def test_ingredients_specs_galbijjim(self):
        galbijjim_ingredients = {1: ("Carrots", "Potatoes", "Onions", "Garlic"), 2: "Beef", 3: "Galbijjim"}
        actual = game.ingredients_specs(galbijjim_ingredients)
        expected = {"Carrots": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Potatoes": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Onions": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Garlic": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Beef": {"HP": 10, "Hit": 4, "Accuracy": 0.75},
                    "Galbijjim": {"HP": 20, "Hit": 5, "Accuracy": 0.75}}
        self.assertEqual(actual, expected)

    def test_ingredients_specs_jeyuk(self):
        jeyuk_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Pork", 3: "Jeyuk"}
        actual = game.ingredients_specs(jeyuk_ingredients)
        expected = {"Carrots": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Onions": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Garlic": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Pork": {"HP": 10, "Hit": 3, "Accuracy": 0.5},
                    "Jeyuk": {"HP": 20, "Hit": 5, "Accuracy": 0.75}}
        self.assertEqual(actual, expected)

    def test_ingredients_specs_dakgalbi(self):
        dakgalbi_ingredients = {1: ("Cabbages", "Potatoes", "Onions", "Garlic"), 2: "Chicken", 3: "Dakgalbi"}
        actual = game.ingredients_specs(dakgalbi_ingredients)
        expected = {"Cabbages": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Potatoes": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Onions": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Garlic": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Chicken": {"HP": 10, "Hit": 2, "Accuracy": 0.5},
                    "Dakgalbi": {"HP": 20, "Hit": 5, "Accuracy": 0.75}}
        self.assertEqual(actual, expected)

    def test_ingredients_specs_kongbul(self):
        kongbul_ingredients = {1: ("Bean Sprouts", "Onions", "Garlic"), 2: "Pork", 3: "Kongbul"}
        actual = game.ingredients_specs(kongbul_ingredients)
        expected = {"Bean Sprouts": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Onions": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Garlic": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Pork": {"HP": 10, "Hit": 3, "Accuracy": 0.5},
                    "Kongbul": {"HP": 20, "Hit": 5, "Accuracy": 0.75}}
        self.assertEqual(actual, expected)

    def test_ingredients_specs_jjimdak(self):
        jjimdak_ingredients = {1: ("Carrots", "Potatoes", "Onions", "Garlic"), 2: "Chicken", 3: "Jjimdak"}
        actual = game.ingredients_specs(jjimdak_ingredients)
        expected = {"Carrots": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Potatoes": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Onions": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Garlic": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Chicken": {"HP": 10, "Hit": 2, "Accuracy": 0.5},
                    "Jjimdak": {"HP": 20, "Hit": 5, "Accuracy": 0.75}}
        self.assertEqual(actual, expected)

    def test_ingredients_specs_samgyeopsal(self):
        samgyeopsal_ingredients = {1: ("Lettuce", "Garlic"), 2: "Pork", 3: "Samgyeopsal"}
        actual = game.ingredients_specs(samgyeopsal_ingredients)
        expected = {"Lettuce": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Garlic": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Pork": {"HP": 10, "Hit": 3, "Accuracy": 0.5},
                    "Samgyeopsal": {"HP": 20, "Hit": 5, "Accuracy": 0.75}}
        self.assertEqual(actual, expected)

    def test_ingredients_specs_bulgogi(self):
        bulgogi_ingredients = {1: ("Carrots", "Onions", "Garlic"), 2: "Beef", 3: "Bulgogi"}
        actual = game.ingredients_specs(bulgogi_ingredients)
        expected = {"Carrots": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Onions": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Garlic": {"HP": 5, "Hit": 1, "Accuracy": 0.5},
                    "Beef": {"HP": 10, "Hit": 4, "Accuracy": 0.75},
                    "Bulgogi": {"HP": 20, "Hit": 5, "Accuracy": 0.75}}
        self.assertEqual(actual, expected)
