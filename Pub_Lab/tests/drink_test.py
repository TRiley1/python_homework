import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Beer", 3.00,3,5)

    def test_drink_name(self):
        self.assertEqual("Beer", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(3.00, self.drink.price)