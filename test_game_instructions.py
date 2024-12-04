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
            "\nGood day, Chris. You are a junior chef who was travelling to a village known as a dream \n"
            "land for chefs. After a few days of travelling, you decided to take a nap in the shade of a big tree. \n"
            "But when you woke up, an old man was watching you curiously. You asked the man what he is up to, \n"
            "and he said he has been starving for a while, and he asked if you could get some food for him.\n"
            "Because you have such a kind heart, you decided to help him by getting some ingredients nearby and \n"
            "cooking some delicious dish using those. You will be using some basic culinary skills, which you will \n"
            "learn along the way, to get ingredients and cook some dish. \n\n"
            "As a junior chef, you will be getting some vegetables. Once you level up to a sous chef, you now \n"
            "can get some meat. Finally, once you become a head chef, you have all the power to cook some delicious \n"
            "dish using all ingredients you got so far. \n\n")
        self.assertEqual(actual, expected)
