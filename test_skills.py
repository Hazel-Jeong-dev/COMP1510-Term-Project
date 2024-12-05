from unittest import TestCase

import game


class TestSkills(TestCase):

    def test_skills_return_a_dictionary(self):
        self.assertIsInstance(game.skills(), dict)

    def test_skills_return_skills(self):
        actual = game.skills()
        expected = {"Rinse": {"Hit": 2, "Accuracy": 0.75},
                    "Cut": {"Hit": 5, "Accuracy": 0.5},
                    "Fire": {"Hit": 10, "Accuracy": 0.25}}
        self.assertEqual(actual, expected)
