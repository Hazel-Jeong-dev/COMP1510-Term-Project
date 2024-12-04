import io
from unittest import TestCase
from unittest.mock import patch

import game


class TestShowIngredientsToGet(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_to_get_galbijjim(self, mock_output):
        dishes = {
            "Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
        dish = "Galbijjim"
        game.show_ingredients_to_get(dishes, dish)
        actual = mock_output.getvalue().strip()
        expected = ('\nYou have chosen Galbijjim.'
                    '\nYou will need to get Carrots, Potatoes, Onions, Garlic, and Beef to cook Galbijjim.').strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_to_get_jeyuk(self, mock_output):
        dishes = {
            "Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
        dish = "Jeyuk"
        game.show_ingredients_to_get(dishes, dish)
        actual = mock_output.getvalue().strip()
        expected = ('\nYou have chosen Jeyuk.'
                    '\nYou will need to get Carrots, Onions, Garlic, and Pork to cook Jeyuk.').strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_to_get_dakgalbi(self, mock_output):
        dishes = {
            "Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
        dish = "Dakgalbi"
        game.show_ingredients_to_get(dishes, dish)
        actual = mock_output.getvalue().strip()
        expected = ('\nYou have chosen Dakgalbi.'
                    '\nYou will need to get Cabbages, Potatoes, Onions, Garlic, and Chicken to cook Dakgalbi.').strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_to_get_kongbul(self, mock_output):
        dishes = {
            "Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
        dish = "Kongbul"
        game.show_ingredients_to_get(dishes, dish)
        actual = mock_output.getvalue().strip()
        expected = ('\nYou have chosen Kongbul.'
                    '\nYou will need to get Bean Sprouts, Onions, Garlic, and Pork to cook Kongbul.').strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_to_get_jjimdak(self, mock_output):
        dishes = {
            "Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
        dish = "Jjimdak"
        game.show_ingredients_to_get(dishes, dish)
        actual = mock_output.getvalue().strip()
        expected = ('\nYou have chosen Jjimdak.'
                    '\nYou will need to get Carrots, Potatoes, Onions, Garlic, and Chicken to cook Jjimdak.').strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_to_get_samgyeopsal(self, mock_output):
        dishes = {
            "Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
        dish = "Samgyeopsal"
        game.show_ingredients_to_get(dishes, dish)
        actual = mock_output.getvalue().strip()
        expected = ('\nYou have chosen Samgyeopsal.'
                    '\nYou will need to get Lettuce, Garlic, and Pork to cook Samgyeopsal.').strip()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_ingredients_to_get_bulgogi(self, mock_output):
        dishes = {
            "Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
        dish = "Bulgogi"
        game.show_ingredients_to_get(dishes, dish)
        actual = mock_output.getvalue().strip()
        expected = ('\nYou have chosen Bulgogi.'
                    '\nYou will need to get Carrots, Onions, Garlic, and Beef to cook Bulgogi.').strip()
        self.assertEqual(actual, expected)
