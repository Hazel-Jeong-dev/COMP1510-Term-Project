from unittest import TestCase

import game


class TestGameInstructions(TestCase):

    def test_game_instructions_return_a_string(self):
        name = "Chris"
        self.assertIsInstance(game.game_instructions(name), str)

    def test_game_instructions_return_game_instructions(self):
        name = "Chris"
        actual = game.game_instructions(name)
        expected = (
            f"\nGood day, {name}. You are a junior chef who was travelling to a village known as a dream \n"
            f"land for chefs. After a few days of travelling, you decided to take a nap in the shade of a big tree. \n"
            f"But when you woke up, an old man was watching you curiously. You asked the man what he is up to, \n"
            f"and he said he has been starving for a while, and he asked if you could get some food for him.\n"
            f"Because you have such a kind heart, you decided to help him by getting some ingredients nearby and \n"
            f"cooking some delicious dish using those. You will be using some basic culinary skills, which you will \n"
            f"learn along the way, to get ingredients and cook some dish. \n\n"
            f"As a junior chef, you will be getting some vegetables. Once you level up to a sous chef, you now \n"
            f"can get some meat. Finally, once you become a head chef, you have all the power to cook some delicious \n"
            f"dish using all ingredients you got so far. \n\n")
        self.assertEqual(actual, expected)
