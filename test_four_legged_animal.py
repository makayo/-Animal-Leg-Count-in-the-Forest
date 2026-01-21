import unittest
from four_legged_animal import count_four_legged_animals

class TestAnimalLegCount(unittest.TestCase):

    def test_example_one(self):
        animals = ['lion', 'monkey', 'deer', 'snake', 'elephant']
        self.assertEqual(count_four_legged_animals(animals), 3)

    def test_example_two(self):
        animals = ['frog', 'horse', 'spider', 'ant']
        self.assertEqual(count_four_legged_animals(animals), 1)

    def test_all_four_legged(self):
        animals = ['dog', 'cat', 'horse']
        self.assertEqual(count_four_legged_animals(animals), 3)

    def test_empty_list(self):
        self.assertEqual(count_four_legged_animals([]), 0)

    def test_unknown_animals(self):
        animals = ['dragon', 'unicorn']
        self.assertEqual(count_four_legged_animals(animals), 0)

    def test_mixed_known_unknown(self):
        animals = ['lion', 'unknown', 'cat']
        self.assertEqual(count_four_legged_animals(animals), 2)

if __name__ == "__main__":
    unittest.main()
