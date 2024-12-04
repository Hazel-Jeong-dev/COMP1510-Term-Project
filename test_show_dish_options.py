import io
from unittest import TestCase
from unittest.mock import patch

import game


class TestShowDishOptions(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_dish_options_print_dish_options(self, mock_output):
        dish_options = {
            "Galbijjim": {"Difficulty": 5, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Beef"},
            "Jeyuk": {"Difficulty": 3, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Pork"},
            "Dakgalbi": {"Difficulty": 2, "Vegetables": ("Cabbages", "Potatoes", "Onions", "Garlic"),
                         "Meat": "Chicken"},
            "Kongbul": {"Difficulty": 3, "Vegetables": ("Bean Sprouts", "Onions", "Garlic"), "Meat": "Pork"},
            "Jjimdak": {"Difficulty": 2, "Vegetables": ("Carrots", "Potatoes", "Onions", "Garlic"), "Meat": "Chicken"},
            "Samgyeopsal": {"Difficulty": 1, "Vegetables": ("Lettuce", "Garlic"), "Meat": "Pork"},
            "Bulgogi": {"Difficulty": 4, "Vegetables": ("Carrots", "Onions", "Garlic"), "Meat": "Beef"}}
        game.show_dish_options(dish_options)
        actual = mock_output.getvalue()
        expected = ('Here are some dish options you can choose from:\n\n'
                    '1.	Galbijjim, Difficulty: 5\n'
                    '2.	Jeyuk, Difficulty: 3\n'
                    '3.	Dakgalbi, Difficulty: 2\n'
                    '4.	Kongbul, Difficulty: 3\n'
                    '5.	Jjimdak, Difficulty: 2\n'
                    '6.	Samgyeopsal, Difficulty: 1\n'
                    '7.	Bulgogi, Difficulty: 4\n')
        self.assertEqual(actual, expected)
